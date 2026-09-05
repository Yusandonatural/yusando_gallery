import { json, authed, publicItem } from "../_lib.js";

export async function onRequestGet({ request, env }) {
  const sql = authed(request, env)
    ? "SELECT * FROM items ORDER BY created_at DESC"
    : "SELECT * FROM items WHERE status IN ('published','sold') ORDER BY created_at DESC";
  const { results } = await env.DB.prepare(sql).all();
  return json(results.map(publicItem));
}
