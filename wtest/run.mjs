import { makeEnv, AI_OK, req, photoForm } from './harness.mjs';
let pass = 0, fail = 0;
const ok = (c, m) => { c ? pass++ : (fail++, console.log('  ✗ ' + m)); };

const W = (await import('../worker-pages/index.js')).default;

// ---- 1. 下書きを作る（AIは呼ばれない） -----------------------------------
{
  const { env, calls } = makeEnv({ aiReply: AI_OK });
  const r = await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(4, { batch: 'B1', cover_hash: 'h1' }) }), env);
  const j = await r.json();
  ok(r.status === 200, 'draft: 200');
  ok(j.id && j.photos === 4, 'draft: id と枚数が返る');
  ok(calls.anthropic === 0, 'draft: AIを呼んでいない');
  const row = env.DB._db.prepare('SELECT * FROM items').get();
  ok(row.status === 'draft', 'draft: status=draft');
  ok(row.analysis_status === 'pending', 'draft: analysis_status=pending');
  ok(row.batch_id === 'B1', 'draft: batch_id が入る');
  ok(row.price === 5000, 'draft: 既定の等級2で価格が入る');
  ok(JSON.parse(row.photos).length === 4, 'draft: 写真キー4件');
  ok(env.PHOTOS._store.size === 4, 'draft: R2に4枚');

  // 公開一覧に draft は出ない
  const pub = await (await W.fetch(req('/api/items', { token: null }), env)).json();
  ok(pub.length === 0, 'draft: 公開一覧に出ない');
  // 認証ありなら batch で絞れる
  const mine = await (await W.fetch(req('/api/items?batch=B1'), env)).json();
  ok(mine.length === 1, 'draft: 認証ありなら batch で引ける');
}

// ---- 2. 重複した写真をはじく ---------------------------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  const a = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'same' }) }), env)).json();
  const b = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'same' }) }), env)).json();
  ok(b.duplicate_of === a.id, '重複: 既存のidを返す');
  ok(env.DB._db.prepare('SELECT count(*) c FROM items').get().c === 1, '重複: 二重登録しない');
}

// ---- 3. 解析する ----------------------------------------------------------
{
  const { env, calls } = makeEnv({ aiReply: AI_OK });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(4) }), env)).json();
  const r = await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  const j = await r.json();
  ok(r.status === 200, '解析: 200');
  ok(calls.anthropic === 1, '解析: AIを1回呼ぶ');
  ok(calls.lastImages === 4, '解析: R2から4枚読み直して渡している');
  const row = env.DB._db.prepare('SELECT * FROM items WHERE id=?').get(id);
  ok(row.analysis_status === 'done', '解析: done');
  ok(row.mei === '初霜' && row.mei_romaji === 'Hatsushimo', '解析: 銘が入る');
  ok(row.description_en === 'A description.', '解析: 英文が入る');
  ok(row.tier === 3 && row.price === 7000, '解析: 等級と価格');
  ok(row.same_object === 1, '解析: same_object=1');
  ok(row.status === 'draft', '解析後もまだ下書きのまま');
}

// ---- 3b. 人が等級を指定したときは AI より優先される ----------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });          // AI は tier 3 を返す
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { tier: '1' }) }), env)).json();
  await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  const row = env.DB._db.prepare('SELECT * FROM items WHERE id=?').get(id);
  ok(row.tier === 1 && row.price === 3000, '等級: 人の指定(1)がAIの見立て(3)に勝つ');
}

// ---- 4. 写真の取り違えを拾う ---------------------------------------------
{
  const { env } = makeEnv({ aiReply: { ...AI_OK, same_object: false, group_warning: '2枚目だけ別の碗' } });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(4) }), env)).json();
  const j = await (await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env)).json();
  ok(j.same_object === false, '警告: same_object=false が返る');
  const row = env.DB._db.prepare('SELECT * FROM items WHERE id=?').get(id);
  ok(row.same_object === 0 && row.group_warning === '2枚目だけ別の碗', '警告: DBに残る');
}

// ---- 5. 解析が失敗しても行は残り、再試行できる ---------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK, aiStatus: 429 });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(3) }), env)).json();
  const r = await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  const j = await r.json();
  ok(r.status === 502, '失敗: 502');
  ok(j.retryable === true, '失敗: 429は再試行可と伝える');
  const row = env.DB._db.prepare('SELECT * FROM items WHERE id=?').get(id);
  ok(row.analysis_status === 'failed', '失敗: failed として残る');
  ok(row.analysis_error, '失敗: 理由が残る');
  ok(JSON.parse(row.photos).length === 3, '失敗: 写真は保持される');
}

// ---- 6. まとめて公開 ------------------------------------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  const ids = [];
  for (let i = 0; i < 3; i++) {
    const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'c' + i }) }), env)).json();
    ids.push(id);
  }
  await W.fetch(req(`/api/items/${ids[0]}/analyze`, { method: 'POST' }), env);
  await W.fetch(req(`/api/items/${ids[1]}/analyze`, { method: 'POST' }), env);
  // ids[2] は未解析のまま
  const j = await (await W.fetch(req('/api/items/bulk', { method: 'POST', json: { ids, action: 'publish' } }), env)).json();
  ok(j.changed === 2, '一括公開: 解析済みの2件だけ公開される');
  const pub = await (await W.fetch(req('/api/items', { token: null }), env)).json();
  ok(pub.length === 2, '一括公開: 公開一覧に2件');
  ok(env.DB._db.prepare("SELECT status FROM items WHERE id=?").get(ids[2]).status === 'draft', '一括公開: 未解析は draft のまま');
}

// ---- 7. まとめて削除すると R2 の写真も消える -----------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(4) }), env)).json();
  ok(env.PHOTOS._store.size === 4, '削除前: R2に4枚');
  await W.fetch(req('/api/items/bulk', { method: 'POST', json: { ids: [id], action: 'delete' } }), env);
  ok(env.PHOTOS._store.size === 0, '削除: R2の写真も消える');
  ok(env.DB._db.prepare('SELECT count(*) c FROM items').get().c === 0, '削除: 行も消える');
}

// ---- 8. 合言葉なしでは通らない -------------------------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  for (const [path, opt] of [
    ['/api/draft', { method: 'POST', token: null, form: photoForm(1) }],
    ['/api/items/xx/analyze', { method: 'POST', token: null }],
    ['/api/items/bulk', { method: 'POST', token: null, json: { ids: ['a'], action: 'delete' } }],
  ]) ok((await W.fetch(req(path, opt), env)).status === 401, `認証: ${path} は401`);
  // 鍵の中身は匿名に返さない
  const h = await (await W.fetch(req('/api/health', { token: null }), env)).json();
  ok(h.anthropic_key === '設定済み' && h.key_length === undefined, '/api/health: 匿名には鍵の情報を返さない');
  const h2 = await (await W.fetch(req('/api/health'), env)).json();
  ok(h2.key_length === 7, '/api/health: 合言葉ありなら書式チェックを返す');
}

// ---- 9. 1点登録は下書きとして入り、人が直してから公開する -----------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  const r = await W.fetch(req('/api/upload', { method: 'POST', form: photoForm(4, { category: '茶碗' }) }), env);
  const j = await r.json();
  ok(r.status === 200 && j.id, '1点登録: 200');
  ok(j.status === 'draft', '1点登録: 返事に status=draft が入る（画面はこれで編集に進む）');
  const row = env.DB._db.prepare('SELECT * FROM items').get();
  ok(row.status === 'draft', '1点登録: いきなり公開しない（人が確かめてから）');
  // 公開側の一覧に draft が漏れないこと
  const pub = await (await W.fetch(new Request('https://w/api/items'), env)).json();
  ok(pub.length === 0, '1点登録: 公開一覧にはまだ出ない');
  // 人が直して公開するところまで
  const pr = await W.fetch(req(`/api/items/${j.id}`, { method: 'PATCH', json: { mei: '直した銘', status: 'published' } }), env);
  ok(pr.status === 200, '1点登録: 直して公開できる');
  const row2 = env.DB._db.prepare('SELECT * FROM items').get();
  ok(row2.status === 'published' && row2.mei === '直した銘', '1点登録: 直した銘のまま公開される');
  ok(row.mei === '初霜' && row.price === 7000, '従来の登録: 中身も従来どおり');
}


// ---- 10. 品番 ----------------------------------------------------------
{
  const { env } = makeEnv({ aiReply: AI_OK });
  const a = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'x1' }) }), env)).json();
  const b = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'x2' }) }), env)).json();
  ok(a.sku === 'Y-0001' && b.sku === 'Y-0002', '品番: 下書き作成時に連番で振られる');
  const row = env.DB._db.prepare('SELECT * FROM items WHERE id=?').get(a.id);
  ok(row.sku_seq === 1, '品番: sku_seq も入る');

  // 解析しても品番は変わらない
  const an = await (await W.fetch(req(`/api/items/${a.id}/analyze`, { method: 'POST' }), env)).json();
  ok(an.sku === 'Y-0001', '品番: 解析の応答にも載る');
  ok(env.DB._db.prepare('SELECT sku FROM items WHERE id=?').get(a.id).sku === 'Y-0001',
     '品番: 解析後も変わらない');

  // 種別を直しても品番は変わらない（札と結びつくため）
  await W.fetch(req(`/api/items/${a.id}`, { method: 'PATCH', json: { category: '棗' } }), env);
  ok(env.DB._db.prepare('SELECT sku FROM items WHERE id=?').get(a.id).sku === 'Y-0001',
     '品番: 種別を直しても変わらない');

  // 品番で引ける
  for (const key of ['Y-0001', 'y-0001', '1']) {
    const r = await (await W.fetch(req(`/api/items/${key}`, { token: null }), env)).json();
    ok(r.id === a.id, `品番: ${key} で引ける`);
  }
  // 重複したときも品番を返す
  const dup = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2, { cover_hash: 'x1' }) }), env)).json();
  ok(dup.duplicate_of === a.id && dup.sku === 'Y-0001', '品番: 重複の知らせにも品番が載る');

  // 従来の1点登録でも振られる
  const up = await (await W.fetch(req('/api/upload', { method: 'POST', form: photoForm(2) }), env)).json();
  ok(up.sku === 'Y-0003', '品番: 従来の1点登録でも続きの番号が振られる');
  // 通し番号に穴や重複がない
  const skus = env.DB._db.prepare('SELECT sku FROM items ORDER BY sku_seq').all().map(r => r.sku);
  ok(JSON.stringify(skus) === '["Y-0001","Y-0002","Y-0003"]', '品番: 連番に穴も重複もない');
}


// ---- 11. あとから写真を足す --------------------------------------------
{
  const { env, calls } = makeEnv({ aiReply: AI_OK });
  // 正面1枚だけで登録
  const { id, sku } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(1) }), env)).json();
  await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  ok(calls.lastImages === 1, '後付け: まず1枚で解析される');
  ok(JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos).length === 1,
     '後付け: 写真1枚で登録されている');

  // 上面・下面をあとから足す
  const r = await W.fetch(req(`/api/items/${id}/photos`, { method: 'POST', form: photoForm(2) }), env);
  const j = await r.json();
  ok(r.status === 200 && j.added === 2 && j.photos === 3, '後付け: 2枚足せて合計3枚');
  const keys = JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos);
  ok(keys.length === 3, '後付け: DBの写真も3枚');
  ok(new Set(keys).size === 3, '後付け: キーが重複しない（続きの番号になる）');
  ok(keys[0].endsWith('/1.jpeg') && keys[2].endsWith('/3.jpeg'), '後付け: 1→3 の連番');
  ok(env.PHOTOS._store.size === 3, '後付け: R2にも3枚');
  ok(env.DB._db.prepare('SELECT sku FROM items WHERE id=?').get(id).sku === sku,
     '後付け: 品番は変わらない');

  // 足しただけでは読み直さない
  const before = calls.anthropic;
  ok(calls.anthropic === before, '後付け: 足すだけではAIを呼ばない');
  // 明示的に読み直すと3枚で解析される
  await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  ok(calls.lastImages === 3, '後付け: 読み直すと3枚すべてが渡る');

  // 品番でも足せる
  const r2 = await W.fetch(req(`/api/items/${sku}/photos`, { method: 'POST', form: photoForm(1) }), env);
  ok((await r2.json()).photos === 4, '後付け: 品番を指定しても足せる');

  // 上限を超えたら断る
  const over = await W.fetch(req(`/api/items/${id}/photos`, { method: 'POST', form: photoForm(3) }), env);
  ok(over.status === 400, '後付け: 5枚を超えると断る');
  ok(JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos).length === 4,
     '後付け: 断ったときは何も足さない');

  // 合言葉なしは通らない
  ok((await W.fetch(req(`/api/items/${id}/photos`, { method: 'POST', token: null, form: photoForm(1) }), env)).status === 401,
     '後付け: 合言葉なしは401');
  ok((await W.fetch(req('/api/items/zzzz/photos', { method: 'POST', form: photoForm(1) }), env)).status === 404,
     '後付け: 無い茶器は404');
}

// ---- 10. 色と形（検索用の固定語彙） ---------------------------------------
{
  const { env } = makeEnv({ aiReply: { ...AI_OK, color: '白', shape: '井戸形' } });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2) }), env)).json();
  await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  let row = env.DB._db.prepare('SELECT color, shape FROM items WHERE id=?').get(id);
  ok(row.color === '白' && row.shape === '井戸形', '色形: AIの答えが入る');
  // 語彙の外の値は捨てる
  const { env: e2 } = makeEnv({ aiReply: { ...AI_OK, color: '紫', shape: 'まる' } });
  const { id: id2 } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2) }), e2)).json();
  await W.fetch(req(`/api/items/${id2}/analyze`, { method: 'POST' }), e2);
  row = e2.DB._db.prepare('SELECT color, shape FROM items WHERE id=?').get(id2);
  ok(row.color === null && row.shape === null, '色形: 語彙に無い値は null');
  // 茶碗以外なら形は持たない
  const { env: e3 } = makeEnv({ aiReply: { ...AI_OK, category: '棗', color: '黒', shape: '筒形' } });
  const { id: id3 } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(2) }), e3)).json();
  await W.fetch(req(`/api/items/${id3}/analyze`, { method: 'POST' }), e3);
  row = e3.DB._db.prepare('SELECT color, shape FROM items WHERE id=?').get(id3);
  ok(row.color === '黒' && row.shape === null, '色形: 茶碗以外は形を持たない');
  // 人が直せる／絞り込める
  await W.fetch(req(`/api/items/${id}`, { method: 'PATCH', json: { shape: '筒形', status: 'published' } }), env);
  const hit = await (await W.fetch(new Request('https://w/api/items?category=茶碗&shape=筒形'), env)).json();
  const miss = await (await W.fetch(new Request('https://w/api/items?shape=平形'), env)).json();
  ok(hit.length === 1 && miss.length === 0, '色形: ?shape= で公開一覧を絞れる');
  const bad = await (await W.fetch(new Request('https://w/api/items?color=紫'), env)).json();
  ok(bad.length === 1, '色形: 語彙に無い絞り込みは無視される（全部返る）');
}

// ---- 11. 色・形だけ付け直す（/classify） ---------------------------------
{
  const { env, calls } = makeEnv({ aiReply: AI_OK });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(3) }), env)).json();
  await W.fetch(req(`/api/items/${id}/analyze`, { method: 'POST' }), env);
  await W.fetch(req(`/api/items/${id}`, { method: 'PATCH', json: { mei: '人が直した銘', shape: '平形' } }), env);
  const before = calls.anthropic;
  const r = await W.fetch(req(`/api/items/${id}/classify`, { method: 'POST' }), env);
  const j = await r.json();
  ok(r.status === 200 && j.color === '白' && j.shape === '井戸形', 'classify: 色形が返る');
  ok(calls.anthropic === before + 1 && calls.lastImages === 3, 'classify: AIを1回、写真は3枚まで');
  const row = env.DB._db.prepare('SELECT mei, color, shape FROM items WHERE id=?').get(id);
  ok(row.mei === '人が直した銘' && row.shape === '井戸形', 'classify: 文章は触らず色形だけ更新');
}

// ---- 12. 表紙は正面に ------------------------------------------------------
{
  // classify が「3枚目が正面」と答えたら photos の順が入れ替わる
  const { env, calls } = makeEnv({ aiReply: { ...AI_OK, front: 3 } });
  const { id } = await (await W.fetch(req('/api/draft', { method: 'POST', form: photoForm(3) }), env)).json();
  const before = JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos);
  const j = await (await W.fetch(req(`/api/items/${id}/classify`, { method: 'POST' }), env)).json();
  const after = JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos);
  ok(calls.lastImages === 3, '表紙: classify は写真3枚まで見る');
  ok(after[0] === before[2] && after.length === 3 && j.cover_changed === true, '表紙: 正面が1枚目に動く');
  // 人が PATCH {cover} で選べる
  const r = await W.fetch(req(`/api/items/${id}`, { method: 'PATCH', json: { cover: before[1] } }), env);
  const after2 = JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos);
  ok(r.status === 200 && after2[0] === before[1] && after2.length === 3, '表紙: PATCH cover で選べる');
  const bad = await W.fetch(req(`/api/items/${id}`, { method: 'PATCH', json: { cover: 'nope/9.jpg' } }), env);
  ok(bad.status === 400, '表紙: 無い写真は拒む');
  // photos を直接書き換えることはできない
  await W.fetch(req(`/api/items/${id}`, { method: 'PATCH', json: { photos: '["x"]', mei: 'a' } }), env);
  const after3 = JSON.parse(env.DB._db.prepare('SELECT photos FROM items WHERE id=?').get(id).photos);
  ok(after3.length === 3, '表紙: photos の直書きは無視される');
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
