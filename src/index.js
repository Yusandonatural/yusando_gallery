// gallery.yusando.com — 茶器ギャラリー Worker
const ALLOWED = ["https://gallery.yusando.com", "https://yusandonatural.github.io"];
const cors = (request) => {
  const o = request?.headers.get("origin") || "";
  const ok = ALLOWED.includes(o) || o.endsWith(".workers.dev");
  return {
    "access-control-allow-origin": ok ? o : ALLOWED[0],
    "access-control-allow-methods": "GET,POST,PATCH,OPTIONS",
    "access-control-allow-headers": "content-type,x-upload-token",
    "access-control-max-age": "86400",
    "vary": "origin",
  };
};
let CUR = null; // 現在のリクエスト（CORSヘッダ用）
const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", ...cors(CUR) } });
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
 "tier_reason": "等級の理由（40字以内）"
}
等級の基準：
1 = 小物・量産的・目立つキズや直しがある
2 = 標準的な茶器。健全で普段使いに良い
3 = 作行き・釉調が良い、作家物と思われる、見どころが明確
4 = 共箱や箱書きあり、作家サインが確認できる、特に上質
`;
async function upload(request, env) {
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  const form = await request.formData();
  const files = form.getAll("photos").filter((f) => f && f.size > 0).slice(0, 5);
  if (!files.length) return json({ error: "写真が1枚もありません" }, 400);
  const forcedTier = parseInt(form.get("tier") || "", 10);
  const rawCat = (form.get("category") || "").trim();
  const forcedCategory = CATEGORIES.includes(rawCat) ? rawCat : "";
  if (!env.ANTHROPIC_API_KEY) return json({ error: "ANTHROPIC_API_KEY が未設定です（Settings → Variables and Secrets）" }, 500);
  for (const f of files) if (f.size > 4.5 * 1024 * 1024) return json({ error: `写真が大きすぎます（${(f.size/1048576).toFixed(1)}MB）。縮小して再送してください` }, 413);

  const id = crypto.randomUUID().slice(0, 8);
  const keys = [], images = [];
  for (const [i, f] of files.entries()) {
    const buf = await f.arrayBuffer();
    const type = f.type || "image/jpeg";
    const key = `${id}/${i + 1}.${type.split("/")[1] || "jpg"}`;
    await env.PHOTOS.put(key, buf, { httpMetadata: { contentType: type } });
    keys.push(key);
    images.push({ type: "image", source: { type: "base64", media_type: type, data: toBase64(buf) } });
  }

  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
    body: JSON.stringify({
      model: env.CLAUDE_MODEL || "claude-sonnet-5", max_tokens: 2600, system: SYSTEM,
      messages: [{ role: "user", content: [...images, { type: "text", text: prompt(files.length, forcedCategory) }] }],
    }),
  });
  if (!res.ok) return json({ error: "AI解析に失敗しました", detail: await res.text() }, 502);
  const data = await res.json();
  const text = data.content.filter((c) => c.type === "text").map((c) => c.text).join("");
  let ai;
  try { ai = JSON.parse(text.replace(/```json|```/g, "").trim()); }
  catch { return json({ error: "AIの出力を読めませんでした", detail: text }, 502); }

  const tier = Math.min(4, Math.max(1, forcedTier || ai.tier || 2));
  const price = tiers(env)[tier - 1];
  const category = forcedCategory || (CATEGORIES.includes(ai.category) ? ai.category : "その他");
  await env.DB.prepare(`INSERT INTO items
    (id, created_at, status, mei, mei_yomi, mei_reason, category, technique, glaze, kiln, era, condition, has_box, description, tier, price, tier_reason, photos, raw_json,
     mei_en, mei_romaji, mei_reason_en, technique_en, glaze_en, kiln_en, era_en, condition_en, description_en)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?)`)
    .bind(id, new Date().toISOString(), "published", ai.mei, ai.mei_yomi, ai.mei_reason, category, ai.technique, ai.glaze, ai.kiln, ai.era, ai.condition,
      ai.has_box ? 1 : 0, ai.description, tier, price, ai.tier_reason, JSON.stringify(keys), text,
      ai.mei_en || null, ai.mei_romaji || null, ai.mei_reason_en || null, ai.technique_en || null,
      ai.glaze_en || null, ai.kiln_en || null, ai.era_en || null, ai.condition_en || null,
      ai.description_en || null).run();
  return json({ id, mei: ai.mei, price, tier, url: `/item.html?id=${id}` });
}

async function listItems(request, env) {
  const sql = authed(request, env)
    ? "SELECT * FROM items ORDER BY created_at DESC"
    : "SELECT * FROM items WHERE status IN ('published','sold') ORDER BY created_at DESC";
  const { results } = await env.DB.prepare(sql).all();
  return json(results.map(publicItem));
}

async function getItem(id, env) {
  const row = await env.DB.prepare("SELECT * FROM items WHERE id=?").bind(id).first();
  if (!row || row.status === "hidden") return json({ error: "not found" }, 404);
  return json(publicItem(row));
}

async function patchItem(request, id, env) {
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

async function photo(key, env) {
  const obj = await env.PHOTOS.get(key);
  if (!obj) return new Response("not found", { status: 404 });
  return new Response(obj.body, { headers: {
    "content-type": obj.httpMetadata?.contentType || "image/jpeg",
    "cache-control": "public, max-age=31536000, immutable", ...cors(CUR) } });
}

function toBase64(buf) {
  let s = ""; const b = new Uint8Array(buf);
  for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
  return btoa(s);
}

export default {
  async fetch(request, env) {
    CUR = request;
    const { pathname } = new URL(request.url);
    const m = request.method;
    if (m === "OPTIONS") return new Response(null, { status: 204, headers: cors(request) });
    if (pathname === "/api/health" && m === "GET") {
      const k = env.ANTHROPIC_API_KEY || "";
      return json({
        anthropic_key: k ? `${k.slice(0, 16)}…${k.slice(-4)} (${k.length}文字${/\s/.test(k) ? "・空白あり!" : ""}${/["']/.test(k) ? "・引用符あり!" : ""})` : "未設定",
        upload_token: env.UPLOAD_TOKEN ? "設定済み" : "未設定",
        db: !!env.DB, photos: !!env.PHOTOS,
      });
    }
    if (pathname === "/api/upload" && m === "POST") return upload(request, env);
    if (pathname === "/api/items" && m === "GET") return listItems(request, env);
    const item = pathname.match(/^\/api\/items\/([\w-]+)$/);
    if (item && m === "GET") return getItem(item[1], env);
    if (item && m === "PATCH") return patchItem(request, item[1], env);
    if (pathname.startsWith("/photos/") && m === "GET") return photo(decodeURIComponent(pathname.slice(8)), env);
    return env.ASSETS.fetch(request); // docs/ の静的ファイル
  },
};
