export async function onRequestGet({ params, env }) {
  const key = (params.key || []).join("/");
  const obj = await env.PHOTOS.get(key);
  if (!obj) return new Response("not found", { status: 404 });
  return new Response(obj.body, {
    headers: {
      "content-type": obj.httpMetadata?.contentType || "image/jpeg",
      "cache-control": "public, max-age=31536000, immutable",
    },
  });
}
