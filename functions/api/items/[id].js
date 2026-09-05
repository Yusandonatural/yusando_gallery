import { json, authed, tiers, publicItem } from "../../_lib.js";

export async function onRequestGet({ params, env }) {
  const row = await env.DB.prepare("SELECT * FROM items WHERE id=?").bind(params.id).first();
  if (!row || row.status === "hidden") return json({ error: "not found" }, 404);
  return json(publicItem(row));
}

// 修正・売却済・非公開の切り替え（合言葉必須）
export async function onRequestPatch({ request, params, env }) {
  if (!authed(request, env)) return json({ error: "unauthorized" }, 401);
  const body = await request.json();
  const allowed = ["status", "mei", "mei_yomi", "mei_reason", "description", "tier", "category", "kiln", "era", "condition"];
  const sets = [], vals = [];
  for (const k of allowed) if (k in body) { sets.push(`${k}=?`); vals.push(body[k]); }
  if ("tier" in body) { sets.push("price=?"); vals.push(tiers(env)[Math.min(4, Math.max(1, body.tier)) - 1]); }
  if (!sets.length) return json({ error: "nothing to update" }, 400);
  vals.push(params.id);
  await env.DB.prepare(`UPDATE items SET ${sets.join(",")} WHERE id=?`).bind(...vals).run();
  return json({ ok: true });
}
