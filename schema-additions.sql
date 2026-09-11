-- 一括登録のために追加した列。gallery-db には適用済み。
-- status には従来の published / sold / hidden に加えて draft が入る。
-- draft は公開側の一覧（status IN ('published','sold')）に出ないので、
-- 解析前の行がポータルに漏れることはない。
ALTER TABLE items ADD COLUMN batch_id TEXT;                            -- まとめて登録した単位
ALTER TABLE items ADD COLUMN analysis_status TEXT NOT NULL DEFAULT 'done';  -- pending / done / failed
ALTER TABLE items ADD COLUMN analysis_error TEXT;
ALTER TABLE items ADD COLUMN same_object INTEGER;                      -- 写真がすべて同じ器か
ALTER TABLE items ADD COLUMN group_warning TEXT;                       -- 違って見える点
ALTER TABLE items ADD COLUMN cover_hash TEXT;                          -- 表紙写真のSHA-256（二重登録よけ）
ALTER TABLE items ADD COLUMN forced_tier INTEGER;                      -- 人が等級を指定したときだけ入る

CREATE INDEX IF NOT EXISTS idx_items_batch ON items(batch_id, created_at);
CREATE INDEX IF NOT EXISTS idx_items_analysis ON items(analysis_status);
CREATE INDEX IF NOT EXISTS idx_items_cover_hash ON items(cover_hash);
