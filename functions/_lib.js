export const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8" } });

export const authed = (request, env) => {
  const t = request.headers.get("x-upload-token") || new URL(request.url).searchParams.get("token");
  return env.UPLOAD_TOKEN && t === env.UPLOAD_TOKEN;
};

export const tiers = (env) => (env.PRICE_TIERS || "3000,5000,7000,10000").split(",").map((n) => parseInt(n.trim(), 10));

export const publicItem = (row) => ({
  ...row,
  photos: JSON.parse(row.photos || "[]"),
  has_box: !!row.has_box,
  raw_json: undefined,
});
