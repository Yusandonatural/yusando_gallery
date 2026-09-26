'use strict';
// Electronを使わずに Shield のリクエスト処理を検証する（electronモジュールを差し替え）
const test = require('node:test');
const assert = require('node:assert');
const Module = require('node:module');
const os = require('node:os');
const path = require('node:path');

const tabUrl = 'https://news.example.jp/article/1';
const fakeElectron = {
  app: { getPath: () => os.tmpdir() },
  webContents: { fromId: () => ({ isDestroyed: () => false, getURL: () => tabUrl }) },
  ipcMain: { handle() {}, removeHandler() {} },
};
const origLoad = Module._load;
Module._load = function (request, ...rest) {
  if (request === 'electron') return fakeElectron;
  return origLoad.call(this, request, ...rest);
};
const { Shield } = require('../src/shield');

function fakeSession() {
  const handlers = {};
  return {
    handlers,
    setSpellCheckerEnabled() {},
    setPermissionRequestHandler(fn) { handlers.permission = fn; },
    setPermissionCheckHandler(fn) { handlers.permissionCheck = fn; },
    registerPreloadScript() { return 'id'; },
    unregisterPreloadScript() {},
    webRequest: {
      onBeforeRequest(_f, fn) { handlers.beforeRequest = fn; },
      onBeforeSendHeaders(_f, fn) { handlers.beforeSendHeaders = fn; },
      onHeadersReceived(_f, fn) { handlers.headersReceived = fn; },
    },
  };
}

const call = (fn, details) => new Promise((resolve) => fn({ webContentsId: 1, ...details }, resolve));

test('Shield: 広告・トラッカーを遮断し、通常の通信は通す', async (t) => {
  const ses = fakeSession();
  const blocked = [];
  const shield = new Shield(ses, (_id, url, reason) => blocked.push([url, reason]));
  await shield.enable();
  if (!shield.blocker) t.diagnostic('フィルターリスト未取得のため内蔵リストで検証');
  const h = ses.handlers;

  for (const url of [
    'https://www.googletagmanager.com/gtag/js?id=G-XXXX',
    'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js',
    'https://securepubads.g.doubleclick.net/tag/js/gpt.js',
  ]) {
    // 遮断（cancel）か、通信しない無害な代替スクリプト（data: URL）への差し替えのどちらか
    const res = await call(h.beforeRequest, { url, resourceType: 'script', referrer: tabUrl });
    assert.ok(res.cancel === true || /^data:/.test(res.redirectURL || ''), url);
  }
  assert.deepStrictEqual(await call(h.beforeRequest, { url: 'https://news.example.jp/app.js', resourceType: 'script' }), {});
  assert.deepStrictEqual(await call(h.beforeRequest, { url: 'https://news.example.jp/log', resourceType: 'ping' }), { cancel: true });

  const nav = await call(h.beforeRequest, { url: 'https://news.example.jp/?id=5&utm_source=tw&fbclid=z', resourceType: 'mainFrame' });
  assert.deepStrictEqual(nav, { redirectURL: 'https://news.example.jp/?id=5' });
  assert.ok(blocked.length >= 5);

  // 位置情報などの権限は拒否
  const perm = await new Promise((r) => h.permission(null, 'geolocation', r));
  assert.strictEqual(perm, false);

  const sent = await call(h.beforeSendHeaders, {
    url: 'https://cdn.other.com/img.png', resourceType: 'image',
    requestHeaders: { Cookie: 'a=1', Referer: tabUrl },
  });
  assert.strictEqual(sent.requestHeaders.Cookie, undefined);
  assert.strictEqual(sent.requestHeaders.Referer, 'https://news.example.jp/');
  assert.strictEqual(sent.requestHeaders.DNT, '1');

  const recv = await call(h.headersReceived, {
    url: 'https://cdn.other.com/img.png', resourceType: 'image',
    responseHeaders: { 'Set-Cookie': ['t=1'], 'Content-Type': ['image/png'] },
  });
  assert.deepStrictEqual(recv.responseHeaders, { 'Content-Type': ['image/png'] });

  const same = await call(h.headersReceived, {
    url: 'https://news.example.jp/style.css', resourceType: 'stylesheet',
    responseHeaders: { 'Set-Cookie': ['s=1'] },
  });
  assert.deepStrictEqual(same, {});
});
