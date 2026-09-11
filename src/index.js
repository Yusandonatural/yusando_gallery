// gallery.yusando.com — 茶器ギャラリー Worker
const ALLOWED = ["https://gallery.yusando.com", "https://yusandonatural.github.io"];
const cors = (request) => {
  const o = request?.headers.get("origin") || "";
  const ok = ALLOWED.includes(o) || o.endsWith(".workers.dev");
  return {
    "access-control-allow-origin": ok ? o : ALLOWED[0],
    "access-control-allow-methods": "GET,POST,PATCH,DELETE,OPTIONS",
    "access-control-allow-headers": "content-type,x-upload-token",
    "access-control-max-age": "86400",
    "vary": "origin",
  };
};
// リクエストごとに json() を作る。モジュール全体で1個の変数に現在のリクエストを
// 入れておくと、await の間に別のリクエストがそれを上書きしてしまい、
// 応答が他人の origin 用の CORS ヘッダを持つことがあるため。
const jsonWith = (request) => (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", ...cors(request) } });
const authed = (request, env) => {
  const t = request.headers.get("x-upload-token") || new URL(request.url).searchParams.get("token");
  return !!env.UPLOAD_TOKEN && t === env.UPLOAD_TOKEN;
};
const CATEGORIES = ["茶碗","茶入","棗","水指","建水","蓋置","茶杓","花入","香合",
  "釜・風炉","急須・宝瓶","湯冷まし","湯呑・茶托","菓子器","掛物","その他"];
const tiers = (env) => (env.PRICE_TIERS || "3000,5000,7000,10000").split(",").map((n) => parseInt(n.trim(), 10));
const publicItem = (row) => ({ ...row, photos: JSON.parse(row.photos || "[]"), has_box: !!row.has_box, raw_json: undefined });

const SYSTEM = `あなたは日本の茶道具商の目利きです。茶器の写真を観察し、事実に基づいて記述します。
作家名・窯・時代は断定せず「〜と思われる」「〜風」と書きます。写っていないことは書きません。
出力は必ずJSONのみ。前置き・コードフェンス不要。`;

const prompt = (n, forcedCategory) => `写真${n}枚の茶器について、次のJSONを返してください。
日本語と英語の両方を書きます。英語は日本語の直訳ではなく、海外の茶道具愛好家に向けた自然な英文にしてください。
${forcedCategory ? `この茶器の種別は「${forcedCategory}」です。category はこの値をそのまま返してください。` : ""}
{
 "category": "種別。次のいずれか: ${CATEGORIES.join("／")}",
 "technique": "成形・技法（例: 轆轤成形、手捏ね、粉引、刷毛目）",
 "technique_en": "同上を英語で（例: wheel-thrown, hand-built, kohiki slip）",
 "glaze": "釉薬・土味の観察",
 "glaze_en": "同上を英語で",
 "kiln": "推定産地・窯（不明なら「不詳」）",
 "kiln_en": "同上を英語で（不明なら \"Unknown\"）",
 "era": "推定時代（例: 現代／昭和／江戸後期。不明なら「不詳」）",
 "era_en": "同上を英語で（例: Contemporary / Shōwa / late Edo。不明なら \"Unknown\"）",
 "condition": "状態（ニュウ・ホツ・直し・貫入・使用感の有無を具体的に）",
 "condition_en": "同上を英語で",
 "has_box": true/false（共箱・箱書きが写っているか）,
 "mei": "銘（漢字2〜4字。季節・景色・茶趣にちなむ）",
 "mei_yomi": "銘の読み（ひらがな）",
 "mei_romaji": "銘のローマ字（例: Hatsushimo）",
 "mei_en": "銘の英訳（例: First Frost）。詩的な短い語で",
 "mei_reason": "銘の由来（40字以内）",
 "mei_reason_en": "銘の由来を英語で（1文）",
 "description": "茶道具商の文体で150〜220字。観察できた特徴→見どころ→取り合わせの提案。断定を避ける。",
 "description_en": "同じ内容を英語で80〜130語。日本語の直訳ではなく、英語として自然な茶道具の解説に。",
 "tier": 1〜4の整数,
 "tier_reason": "等級の理由（40字以内）",
 "same_object": 渡された写真がすべて同一の器かどうか true/false,
 "group_warning": same_object が false のとき、何が違って見えるかを20字以内で。true なら空文字
}
等級の基準：
1 = 小物・量産的・目立つキズや直しがある
2 = 標準的な茶器。健全で普段使いに良い
3 = 作行き・釉調が良い、作家物と思われる、見どころが明確
4 = 共箱や箱書きあり、作家サインが確認できる、特に上質
`;
// ---------------------------------------------------------------- 解析 --
// 写真から所見を得るところだけを切り出してある。1点ずつ登録する従来の導線と、
// 下書きを後からまとめて解析する一括登録の導線が、同じ処理を共有するため。
async function analyse(images, count, forcedCategory, env) {
  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
    body: JSON.stringify({
      model: env.CLAUDE_MODEL || "claude-sonnet-5", max_tokens: 2600, system: SYSTEM,
      messages: [{ role: "user", content: [...images, { type: "text", text: prompt(count, forcedCategory) }] }],
    }),
  });
  if (!res.ok) {
    const detail = await res.text();
    // 429 と 5xx は時間をおけば通ることがある。呼び出し側が再試行を判断できるよう伝える。
    throw Object.assign(new Error("AI解析に失敗しました"), {
      detail, status: 502, retryable: res.status === 429 || res.status >= 500,
    });
  }
  const data = await res.json();
  const text = data.content.filter((c) => c.type === "text").map((c) => c.text).join("");
  let ai;
  try { ai = JSON.parse(text.replace(/```json|```/g, "").trim()); }
  catch { throw Object.assign(new Error("AIの出力を読めませんでした"), { detail: text, status: 502 }); }
  return { ai, text };
}

// 解析結果を items の1行に流し込む。INSERT と UPDATE で同じ並びを使う。
function analysisFields(ai, text, forcedTier, forcedCategory, env) {
  const tier = Math.min(4, Math.max(1, forcedTier || ai.tier || 2));
  return {
    mei: ai.mei, mei_yomi: ai.mei_yomi, mei_reason: ai.mei_reason,
    category: forcedCategory || (CATEGORIES.includes(ai.category) ? ai.category : "その他"),
    technique: ai.technique, glaze: ai.glaze, kiln: ai.kiln, era: ai.era, condition: ai.condition,
    has_box: ai.has_box ? 1 : 0, description: ai.description,
    tier, price: tiers(env)[tier - 1], tier_reason: ai.tier_reason, raw_json: text,
    mei_en: ai.mei_en || null, mei_romaji: ai.mei_romaji || null, mei_reason_en: ai.mei_reason_en || null,
    technique_en: ai.technique_en || null, glaze_en: ai.glaze_en || null, kiln_en: ai.kiln_en || null,
    era_en: ai.era_en || null, condition_en: ai.condition_en || null, description_en: ai.description_en || null,
    // 写真の取り違えは記述の誤りと違って後から気づきにくいので、解析のついでに
    // 「4枚は同じ器か」も答えさせ、怪しい行に印を残す。追加の呼び出しは要らない。
    same_object: ai.same_object === false ? 0 : 1,
    group_warning: ai.same_object === false ? (ai.group_warning || "写真が同一の器に見えません") : null,
    analysis_status: "done", analysis_error: null,
  };
}

async function updateRow(id, fields, env) {
  const keys = Object.keys(fields);
  await env.DB.prepare(`UPDATE items SET ${keys.map((k) => `${k}=?`).join(",")} WHERE id=?`)
    .bind(...keys.map((k) => fields[k]), id).run();
}

async function readPhotos(row, env) {
  const keys = JSON.parse(row.photos || "[]");
  const images = [];
  for (const key of keys) {
    const obj = await env.PHOTOS.get(key);
    if (!obj) continue;
    const buf = await obj.arrayBuffer();
    images.push({ type: "image", source: {
      type: "base64", media_type: obj.httpMetadata?.contentType || "image/jpeg", data: toBase64(buf) } });
  }
  return images;
}

async function upload(request, env) {
  const json = jsonWith(request);
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  const form = await request.formData();
  const files = form.getAll("photos").filter((f) => f && f.size > 0).slice(0, 5);
  if (!files.length) return json({ error: "写真が1枚もありません" }, 400);
  const forcedTier = parseInt(form.get("tier") || "", 10);
  const rawCat = (form.get("category") || "").trim();
  const forcedCategory = CATEGORIES.includes(rawCat) ? rawCat : "";
  if (!env.ANTHROPIC_API_KEY) return json({ error: "ANTHROPIC_API_KEY が未設定です（Settings → Variables and Secrets）" }, 500);
  const tooBig = files.find((f) => f.size > 4.5 * 1024 * 1024);
  if (tooBig) return json({ error: `写真が大きすぎます（${(tooBig.size/1048576).toFixed(1)}MB）。縮小して再送してください` }, 413);

  const id = crypto.randomUUID().slice(0, 8);
  const { keys, images } = await storePhotos(id, files, env);

  let ai, text;
  try { ({ ai, text } = await analyse(images, files.length, forcedCategory, env)); }
  catch (e) { return json({ error: e.message, detail: e.detail }, e.status || 502); }

  const f = analysisFields(ai, text, forcedTier, forcedCategory, env);
  const cols = ["id", "created_at", "status", "photos", ...Object.keys(f)];
  const vals = [id, new Date().toISOString(), "published", JSON.stringify(keys), ...Object.keys(f).map((k) => f[k])];
  await env.DB.prepare(`INSERT INTO items (${cols.join(",")}) VALUES (${cols.map(() => "?").join(",")})`)
    .bind(...vals).run();
  return json({ id, mei: ai.mei, price: f.price, tier: f.tier, url: `/item.html?id=${id}` });
}

// 写真を R2 に置き、同時に解析用の base64 も作る。
async function storePhotos(id, files, env) {
  const keys = [], images = [];
  for (const [i, f] of files.entries()) {
    const buf = await f.arrayBuffer();
    const type = f.type || "image/jpeg";
    const key = `${id}/${i + 1}.${type.split("/")[1] || "jpg"}`;
    await env.PHOTOS.put(key, buf, { httpMetadata: { contentType: type } });
    keys.push(key);
    images.push({ type: "image", source: { type: "base64", media_type: type, data: toBase64(buf) } });
  }
  return { keys, images };
}

// ------------------------------------------------------------ 一括登録 --
// 一括登録では、写真の保存と AI 解析を別のリクエストに分ける。1リクエストで
// 両方やると、100点なら十数分の長い処理が1本になり、途中で切れたときに
// 何点目まで通ったのか分からなくなるため。写真だけ先に確実に預かって
// status='draft' の行を作り、解析は後から1点ずつ流して結果を書き足す。
async function createDraft(request, env) {
  const json = jsonWith(request);
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  const form = await request.formData();
  const files = form.getAll("photos").filter((f) => f && f.size > 0).slice(0, 5);
  if (!files.length) return json({ error: "写真が1枚もありません" }, 400);
  const tooBig = files.find((f) => f.size > 4.5 * 1024 * 1024);
  if (tooBig) return json({ error: `写真が大きすぎます（${(tooBig.size/1048576).toFixed(1)}MB）` }, 413);

  // 同じ写真を二度上げてしまったときに、黙って二重登録にならないようにする。
  const coverHash = (form.get("cover_hash") || "").trim() || null;
  if (coverHash) {
    const dup = await env.DB.prepare("SELECT id, mei, status FROM items WHERE cover_hash=?").bind(coverHash).first();
    if (dup) return json({ duplicate_of: dup.id, mei: dup.mei, status: dup.status }, 200);
  }

  const rawCat = (form.get("category") || "").trim();
  const category = CATEGORIES.includes(rawCat) ? rawCat : null;
  // tier は NOT NULL なので下書きにも仮の値が要る。ただし「仮の2」と「人が2を
  // 選んだ」を取り違えると、解析のときに AI の見立てを黙って打ち消してしまう。
  // 人が指定したときだけ forced_tier に残し、仮の値と区別する。
  const t = parseInt(form.get("tier") || "", 10);
  const forcedTier = t >= 1 && t <= 4 ? t : null;

  const id = crypto.randomUUID().slice(0, 8);
  const { keys } = await storePhotos(id, files, env);
  await env.DB.prepare(`INSERT INTO items
    (id, created_at, status, photos, tier, price, forced_tier, category, batch_id, cover_hash, analysis_status)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)`)
    .bind(id, new Date().toISOString(), "draft", JSON.stringify(keys),
      forcedTier || 2, tiers(env)[(forcedTier || 2) - 1], forcedTier,
      category, (form.get("batch") || "").trim() || null, coverHash, "pending").run();
  return json({ id, photos: keys.length });
}

async function analyzeItem(request, id, env) {
  const json = jsonWith(request);
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  if (!env.ANTHROPIC_API_KEY) return json({ error: "ANTHROPIC_API_KEY が未設定です" }, 500);
  const row = await env.DB.prepare("SELECT * FROM items WHERE id=?").bind(id).first();
  if (!row) return json({ error: "not found" }, 404);

  const images = await readPhotos(row, env);
  if (!images.length) return json({ error: "写真を読み出せませんでした" }, 500);

  try {
    const { ai, text } = await analyse(images, images.length, row.category || "", env);
    const f = analysisFields(ai, text, row.forced_tier, row.category || "", env);
    await updateRow(id, f, env);
    return json({ id, mei: f.mei, category: f.category, tier: f.tier,
      same_object: !!f.same_object, group_warning: f.group_warning });
  } catch (e) {
    await updateRow(id, { analysis_status: "failed", analysis_error: String(e.message || e).slice(0, 300) }, env);
    return json({ id, error: e.message, detail: e.detail, retryable: !!e.retryable }, e.status || 502);
  }
}

// まとめて公開・非公開・削除。解析の済んでいない行は公開しない。
async function bulkItems(request, env) {
  const json = jsonWith(request);
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  const { ids, action } = await request.json();
  if (!Array.isArray(ids) || !ids.length) return json({ error: "対象がありません" }, 400);
  if (ids.length > 200) return json({ error: "一度に処理できるのは200件までです" }, 400);
  const marks = ids.map(() => "?").join(",");

  if (action === "publish") {
    const { meta } = await env.DB.prepare(
      `UPDATE items SET status='published' WHERE id IN (${marks}) AND analysis_status='done'`)
      .bind(...ids).run();
    return json({ ok: true, changed: meta.changes });
  }
  if (action === "hide") {
    const { meta } = await env.DB.prepare(`UPDATE items SET status='hidden' WHERE id IN (${marks})`)
      .bind(...ids).run();
    return json({ ok: true, changed: meta.changes });
  }
  if (action === "delete") {
    // 行を消す前に R2 の写真も片付ける。残すと参照されない画像が溜まり続ける。
    const { results } = await env.DB.prepare(`SELECT photos FROM items WHERE id IN (${marks})`).bind(...ids).all();
    for (const r of results) {
      for (const key of JSON.parse(r.photos || "[]")) {
        try { await env.PHOTOS.delete(key); } catch (e) { console.warn("R2 delete failed", key, e); }
      }
    }
    const { meta } = await env.DB.prepare(`DELETE FROM items WHERE id IN (${marks})`).bind(...ids).run();
    return json({ ok: true, changed: meta.changes });
  }
  return json({ error: "action は publish / hide / delete のいずれかです" }, 400);
}

async function listItems(request, env) {
  const json = jsonWith(request);
  // 公開側は published / sold のみ。draft はここに載らないので、解析前の
  // 行がポータルに漏れることはない。
  if (!authed(request, env)) {
    const { results } = await env.DB.prepare(
      "SELECT * FROM items WHERE status IN ('published','sold') ORDER BY created_at DESC").all();
    return json(results.map(publicItem));
  }
  const q = new URL(request.url).searchParams;
  const where = [], binds = [];
  if (q.get("batch")) { where.push("batch_id=?"); binds.push(q.get("batch")); }
  if (q.get("status")) { where.push("status=?"); binds.push(q.get("status")); }
  const sql = "SELECT * FROM items"
    + (where.length ? ` WHERE ${where.join(" AND ")}` : "")
    + " ORDER BY created_at DESC";
  const { results } = await env.DB.prepare(sql).bind(...binds).all();
  return json(results.map(publicItem));
}

async function getItem(request, id, env) {
  const json = jsonWith(request);
  const row = await env.DB.prepare("SELECT * FROM items WHERE id=?").bind(id).first();
  if (!row || row.status === "hidden") return json({ error: "not found" }, 404);
  return json(publicItem(row));
}

async function patchItem(request, id, env) {
  const json = jsonWith(request);
  if (!authed(request, env)) return json({ error: "unauthorized" }, 401);
  const body = await request.json();
  const allowed = ["status", "mei", "mei_yomi", "mei_reason", "description", "tier", "category",
    "kiln", "era", "condition", "technique", "glaze", "sekki", "sekki_reason",
    "mei_en", "mei_romaji", "mei_reason_en", "description_en",
    "technique_en", "glaze_en", "kiln_en", "era_en", "condition_en"];
  if (Array.isArray(body.sekki)) body.sekki = JSON.stringify(body.sekki);
  const sets = [], vals = [];
  for (const k of allowed) if (k in body) { sets.push(`${k}=?`); vals.push(body[k]); }
  if ("tier" in body) { sets.push("price=?"); vals.push(tiers(env)[Math.min(4, Math.max(1, body.tier)) - 1]); }
  if (!sets.length) return json({ error: "nothing to update" }, 400);
  vals.push(id);
  await env.DB.prepare(`UPDATE items SET ${sets.join(",")} WHERE id=?`).bind(...vals).run();
  return json({ ok: true });
}

async function photo(request, key, env) {
  const obj = await env.PHOTOS.get(key);
  if (!obj) return new Response("not found", { status: 404 });
  return new Response(obj.body, { headers: {
    "content-type": obj.httpMetadata?.contentType || "image/jpeg",
    "cache-control": "public, max-age=31536000, immutable", ...cors(request) } });
}

function toBase64(buf) {
  let s = ""; const b = new Uint8Array(buf);
  for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
  return btoa(s);
}

export default {
  async fetch(request, env) {
    const json = jsonWith(request);
    const { pathname } = new URL(request.url);
    const m = request.method;
    if (m === "OPTIONS") return new Response(null, { status: 204, headers: cors(request) });
    if (pathname === "/api/health" && m === "GET") {
      // このエンドポイントは誰でも叩けるので、鍵の中身は一切返さない。
      // 書式チェック（長さ・空白・引用符の混入）は合言葉を持つ人にだけ返す。
      const k = env.ANTHROPIC_API_KEY || "";
      return json({
        anthropic_key: k ? "設定済み" : "未設定",
        upload_token: env.UPLOAD_TOKEN ? "設定済み" : "未設定",
        db: !!env.DB, photos: !!env.PHOTOS,
        ...(authed(request, env) ? {
          key_length: k.length,
          key_has_space: /\s/.test(k),
          key_has_quote: /["']/.test(k),
        } : {}),
      });
    }
    if (pathname === "/api/upload" && m === "POST") return upload(request, env);
    if (pathname === "/api/draft" && m === "POST") return createDraft(request, env);
    if (pathname === "/api/items/bulk" && m === "POST") return bulkItems(request, env);
    if (pathname === "/api/items" && m === "GET") return listItems(request, env);
    const analyze = pathname.match(/^\/api\/items\/([\w-]+)\/analyze$/);
    if (analyze && m === "POST") return analyzeItem(request, analyze[1], env);
    const item = pathname.match(/^\/api\/items\/([\w-]+)$/);
    if (item && m === "GET") return getItem(request, item[1], env);
    if (item && m === "PATCH") return patchItem(request, item[1], env);
    if (pathname.startsWith("/photos/") && m === "GET") return photo(request, decodeURIComponent(pathname.slice(8)), env);
    return env.ASSETS.fetch(request); // docs/ の静的ファイル
  },
};
