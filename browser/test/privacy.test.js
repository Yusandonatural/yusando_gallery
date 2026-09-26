'use strict';
const test = require('node:test');
const assert = require('node:assert');
const p = require('../src/privacy');

test('追跡パラメータを除去し、通常のパラメータは残す', () => {
  assert.strictEqual(
    p.stripTrackingParams('https://shop.example.jp/item?id=42&utm_source=x&utm_medium=y&fbclid=abc#top'),
    'https://shop.example.jp/item?id=42#top');
  assert.strictEqual(p.stripTrackingParams('https://example.com/?GCLID=1'), 'https://example.com/');
  assert.strictEqual(p.stripTrackingParams('https://example.com/?q=tea&page=2'), null);
  assert.strictEqual(p.stripTrackingParams('file:///tmp/a?utm_source=x'), null);
  assert.strictEqual(p.stripTrackingParams('not a url'), null);
});

test('第三者判定は登録ドメイン単位', () => {
  assert.strictEqual(p.isThirdParty('https://cdn.example.co.jp/a.js', 'https://www.example.co.jp/'), false);
  assert.strictEqual(p.isThirdParty('https://tracker.com/p.gif', 'https://www.example.co.jp/'), true);
  assert.strictEqual(p.isThirdParty('https://a.github.io/x', 'https://b.github.io/'), true);
  assert.strictEqual(p.isThirdParty('http://127.0.0.1:3000/a', 'http://127.0.0.1:3000/'), false);
  assert.strictEqual(p.isThirdParty('https://x.com/', null), false);
});

test('送信ヘッダー: DNT/GPC付与、第三者Cookie削除、リファラー縮小', () => {
  const h = { cookie: 'id=1', Referer: 'https://news.example.jp/article/123?user=me', 'X-Client-Data': 'abc' };
  const { thirdParty } = p.sanitizeRequestHeaders(h, 'https://ads.tracker.com/px', 'https://news.example.jp/article/123');
  assert.strictEqual(thirdParty, true);
  assert.strictEqual(h.DNT, '1');
  assert.strictEqual(h['Sec-GPC'], '1');
  assert.strictEqual(h.cookie, undefined);
  assert.strictEqual(h['X-Client-Data'], undefined);
  assert.strictEqual(h.Referer, 'https://news.example.jp/');
});

test('送信ヘッダー: 同一サイトならCookieとリファラーは維持', () => {
  const h = { Cookie: 'session=1', Referer: 'https://www.example.jp/a/b' };
  p.sanitizeRequestHeaders(h, 'https://api.example.jp/data', 'https://www.example.jp/a/b');
  assert.strictEqual(h.Cookie, 'session=1');
  assert.strictEqual(h.Referer, 'https://www.example.jp/a/b');
});

test('受信ヘッダー: 第三者のSet-Cookieだけ捨てる', () => {
  const third = { 'set-cookie': ['uid=1'], 'content-type': ['image/gif'] };
  assert.strictEqual(p.sanitizeResponseHeaders(third, 'https://tracker.com/p', 'https://example.jp/'), true);
  assert.deepStrictEqual(Object.keys(third), ['content-type']);
  const first = { 'Set-Cookie': ['s=1'] };
  assert.strictEqual(p.sanitizeResponseHeaders(first, 'https://example.jp/login', 'https://example.jp/'), false);
  assert.ok(first['Set-Cookie']);
});

test('内蔵の最小遮断リストはサブドメインも対象', () => {
  assert.ok(p.isFallbackBlocked('https://securepubads.g.doubleclick.net/tag/js/gpt.js'));
  assert.ok(p.isFallbackBlocked('https://www.google-analytics.com/collect'));
  assert.ok(!p.isFallbackBlocked('https://www.google.com/'));
  assert.ok(!p.isFallbackBlocked('https://notdoubleclick.net/'));
});

test('アドレスバー入力のURL化', () => {
  assert.strictEqual(p.toNavigableUrl('yusando.com'), 'https://yusando.com');
  assert.strictEqual(p.toNavigableUrl('gallery.yusando.com/item.html?id=1'), 'https://gallery.yusando.com/item.html?id=1');
  assert.strictEqual(p.toNavigableUrl('http://localhost:8080'), 'http://localhost:8080');
  assert.strictEqual(p.toNavigableUrl('localhost:8080'), 'https://localhost:8080');
  assert.strictEqual(p.toNavigableUrl('奈良 お茶'), 'https://duckduckgo.com/?q=%E5%A5%88%E8%89%AF%20%E3%81%8A%E8%8C%B6');
  assert.strictEqual(p.toNavigableUrl('   '), null);
});
