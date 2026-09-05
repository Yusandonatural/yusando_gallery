import { json, authed, tiers } from "../_lib.js";

const SYSTEM = `あなたは日本の茶道具商の目利きです。茶器の写真を観察し、事実に基づいて記述します。
作家名・窯・時代は断定せず「〜と思われる」「〜風」と書きます。写っていないことは書きません。
出力は必ずJSONのみ。前置き・コードフェンス不要。`;

const prompt = (n) => `写真${n}枚の茶器について、次のJSONを返してください。
{
 "category": "種別（例: 茶碗／茶入／水指／建水／蓋置／茶杓／花入）",
 "technique": "成形・技法（例: 轆轤成形、手捏ね、粉引、刷毛目）",
 "glaze": "釉薬・土味の観察",
 "kiln": "推定産地・窯（不明なら「不詳」）",
 "era": "推定時代（例: 現代／昭和／江戸後期 など。不明なら「不詳」）",
 "condition": "状態（ニュウ・ホツ・直し・貫入・使用感の有無を具体的に）",
 "has_box": true/false（共箱・箱書きが写っているか）,
 "mei": "銘（漢字2〜4字。季節・景色・茶趣にちなむ）",
 "mei_yomi": "銘の読み（ひらがな）",
 "mei_reason": "銘の由来（40字以内）",
 "description": "茶道具商の文体で150〜220字。観察できた特徴→見どころ→取り合わせの提案。断定を避ける。",
 "tier": 1〜4の整数,
 "tier_reason": "等級の理由（40字以内）"
}
等級の基準：
1 = 小物・量産的・目立つキズや直しがある
2 = 標準的な茶器。健全で普段使いに良い
3 = 作行き・釉調が良い、作家物と思われる、見どころが明確
4 = 共箱や箱書きあり、作家サインが確認できる、特に上質
`;

export async function onRequestPost({ request, env }) {
  if (!authed(request, env)) return json({ error: "合言葉が違います" }, 401);
  const form = await request.formData();
  const files = form.getAll("photos").filter((f) => f && f.size > 0).slice(0, 5);
  if (!files.length) return json({ error: "写真が1枚もありません" }, 400);
  const forcedTier = parseInt(form.get("tier") || "", 10);

  const id = crypto.randomUUID().slice(0, 8);
  const keys = [];
  const images = [];
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
      model: env.CLAUDE_MODEL || "claude-sonnet-5",
      max_tokens: 1200,
      system: SYSTEM,
      messages: [{ role: "user", content: [...images, { type: "text", text: prompt(files.length) }] }],
    }),
  });
  if (!res.ok) return json({ error: "AI解析に失敗しました", detail: await res.text() }, 502);
  const data = await res.json();
  const text = data.content.filter((c) => c.type === "text").map((c) => c.text).join("");
  let ai;
  try { ai = JSON.parse(text.replace(/```json|```/g, "").trim()); }
  catch { return json({ error: "AIの出力を読めませんでした", detail: text }, 502); }

  const T = tiers(env);
  const tier = Math.min(4, Math.max(1, forcedTier || ai.tier || 2));
  const price = T[tier - 1];
  const now = new Date().toISOString();

  await env.DB.prepare(`INSERT INTO items
    (id, created_at, status, mei, mei_yomi, mei_reason, category, technique, glaze, kiln, era, condition, has_box, description, tier, price, tier_reason, photos, raw_json)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`)
    .bind(id, now, "published", ai.mei, ai.mei_yomi, ai.mei_reason, ai.category, ai.technique, ai.glaze, ai.kiln, ai.era, ai.condition,
      ai.has_box ? 1 : 0, ai.description, tier, price, ai.tier_reason, JSON.stringify(keys), text)
    .run();

  return json({ id, mei: ai.mei, price, tier, url: `/item.html?id=${id}` });
}

function toBase64(buf) {
  let s = ""; const b = new Uint8Array(buf);
  for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
  return btoa(s);
}
