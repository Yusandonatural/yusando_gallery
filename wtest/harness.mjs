// Worker を本物の SQLite と偽の R2 / Anthropic で動かす試験台。
import { DatabaseSync } from 'node:sqlite';

export function makeEnv({ aiReply, aiStatus = 200 } = {}) {
  const db = new DatabaseSync(':memory:');
  db.exec(`CREATE TABLE items (
    id TEXT PRIMARY KEY, created_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'published',
    mei TEXT, mei_yomi TEXT, mei_reason TEXT, category TEXT, technique TEXT,
    glaze TEXT, kiln TEXT, era TEXT, condition TEXT, has_box INTEGER DEFAULT 0,
    description TEXT, tier INTEGER NOT NULL DEFAULT 2, price INTEGER NOT NULL,
    tier_reason TEXT, photos TEXT NOT NULL, raw_json TEXT,
    sekki TEXT, sekki_reason TEXT, mei_en TEXT, mei_romaji TEXT, mei_reason_en TEXT,
    description_en TEXT, technique_en TEXT, glaze_en TEXT, kiln_en TEXT, era_en TEXT,
    condition_en TEXT, batch_id TEXT, analysis_status TEXT NOT NULL DEFAULT 'done',
    analysis_error TEXT, same_object INTEGER, group_warning TEXT, cover_hash TEXT, forced_tier INTEGER, sku TEXT UNIQUE, sku_seq INTEGER UNIQUE)`);

  const DB = {
    prepare(sql) {
      let bound = [];
      const api = {
        bind(...a) { bound = a.map(v => v === undefined ? null : (typeof v === 'boolean' ? +v : v)); return api; },
        async all() { return { results: db.prepare(sql).all(...bound) }; },
        async first() { return db.prepare(sql).get(...bound) ?? null; },
        async run() { const r = db.prepare(sql).run(...bound); return { meta: { changes: Number(r.changes) } }; },
      };
      return api;
    },
    _db: db,
  };

  const store = new Map();
  const PHOTOS = {
    async put(k, buf, o) { store.set(k, { buf, type: o?.httpMetadata?.contentType }); },
    async get(k) { const v = store.get(k); return v ? {
      body: v.buf, httpMetadata: { contentType: v.type },
      async arrayBuffer() { return v.buf; } } : null; },
    async delete(k) { store.delete(k); },
    _store: store,
  };

  const calls = { anthropic: 0 };
  globalThis.fetch = async (url, init) => {
    if (String(url).includes('api.anthropic.com')) {
      calls.anthropic++;
      const body = JSON.parse(init.body);
      calls.lastImages = body.messages[0].content.filter(c => c.type === 'image').length;
      if (aiStatus !== 200) return new Response('rate limited', { status: aiStatus });
      return new Response(JSON.stringify({
        content: [{ type: 'text', text: JSON.stringify(aiReply) }],
      }), { status: 200 });
    }
    throw new Error('unexpected fetch ' + url);
  };

  return { env: { DB, PHOTOS, ANTHROPIC_API_KEY: 'sk-test', UPLOAD_TOKEN: 'aiotoko',
                  PRICE_TIERS: '3000,5000,7000,10000' }, calls, db };
}

export const AI_OK = {
  category: '茶碗', technique: '轆轤成形', technique_en: 'wheel-thrown',
  glaze: '長石釉', glaze_en: 'feldspar glaze', kiln: '不詳', kiln_en: 'Unknown',
  era: '現代', era_en: 'Contemporary', condition: '良好', condition_en: 'Good',
  has_box: true, mei: '初霜', mei_yomi: 'はつしも', mei_romaji: 'Hatsushimo',
  mei_en: 'First Frost', mei_reason: '白い釉に因む', mei_reason_en: 'For its white glaze',
  description: '説明です。', description_en: 'A description.',
  tier: 3, tier_reason: '作行きが良い', same_object: true, group_warning: '',
};

export function req(path, { method = 'GET', token = 'aiotoko', form, json } = {}) {
  const h = { origin: 'https://gallery.yusando.com' };
  if (token) h['x-upload-token'] = token;
  let body;
  if (form) { body = form; }
  else if (json) { body = JSON.stringify(json); h['content-type'] = 'application/json'; }
  return new Request('https://w.example.com' + path, { method, headers: h, body });
}

export function photoForm(n, extra = {}) {
  const fd = new FormData();
  for (let i = 0; i < n; i++)
    fd.append('photos', new File([new Uint8Array([137, 80, 78, 71, i])], `p${i}.jpg`, { type: 'image/jpeg' }));
  for (const [k, v] of Object.entries(extra)) fd.append(k, v);
  return fd;
}
