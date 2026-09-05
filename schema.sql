-- 既に gallery-db に適用済み。再作成用に保管。
CREATE TABLE IF NOT EXISTS items (
  id TEXT PRIMARY KEY,
  created_at TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'published',   -- published / sold / hidden
  mei TEXT, mei_yomi TEXT, mei_reason TEXT,
  category TEXT, technique TEXT, glaze TEXT, kiln TEXT, era TEXT, condition TEXT,
  has_box INTEGER DEFAULT 0,
  description TEXT,
  tier INTEGER NOT NULL DEFAULT 2,             -- 1..4
  price INTEGER NOT NULL,
  tier_reason TEXT,
  photos TEXT NOT NULL,                        -- JSON array of R2 keys
  raw_json TEXT
);
CREATE INDEX IF NOT EXISTS idx_items_status_created ON items(status, created_at DESC);
