'use strict';
// すべてのページ（フレーム）で、ページ自身のスクリプトより先に実行される追跡防止処理

const { contextBridge, webFrame } = require('electron');

function hardenPage() {
  const define = (obj, prop, value) => {
    try {
      Object.defineProperty(obj, prop, { get: () => value, configurable: true });
    } catch {}
  };

  // 離脱時などに解析データを送る sendBeacon は「送ったふり」だけする
  if (navigator.sendBeacon) {
    navigator.sendBeacon = function sendBeacon() { return true; };
  }

  // 追跡を拒否する意思表示（Do Not Track / Global Privacy Control）
  define(Navigator.prototype, 'doNotTrack', '1');
  define(Navigator.prototype, 'globalPrivacyControl', true);

  // 端末の識別に使われやすいAPIを隠す
  define(Navigator.prototype, 'getBattery', undefined);
  define(Navigator.prototype, 'getInstalledRelatedApps', undefined);

  // 広告用のブラウザAPI（Topics / Protected Audience / Attribution Reporting）を無効化
  define(Document.prototype, 'browsingTopics', undefined);
  define(Navigator.prototype, 'joinAdInterestGroup', undefined);
  define(Navigator.prototype, 'runAdAuction', undefined);
  define(Document.prototype, 'interestCohort', undefined);
}

if (contextBridge.executeInMainWorld) {
  contextBridge.executeInMainWorld({ func: hardenPage });
} else {
  webFrame.executeJavaScript(`(${hardenPage.toString()})()`);
}

// 広告枠の非表示：最初にサイト別ルールを、DOMができたら出現したclass/idに合うルールを要求する
if (window === window.top && location.protocol.startsWith('http')) {
  const { ipcRenderer } = require('electron');
  const request = (dom) => ipcRenderer.invoke('shield:cosmetics', location.href, dom).catch(() => {});
  request();

  const seenClasses = new Set();
  const seenIds = new Set();
  const seenHrefs = new Set();
  let pending = null;

  const collect = (root) => {
    const dom = { classes: [], ids: [], hrefs: [] };
    const elements = root.querySelectorAll ? [root, ...root.querySelectorAll('[class],[id],a[href]')] : [];
    for (const el of elements) {
      if (!el.getAttribute) continue;
      for (const c of el.classList || []) if (!seenClasses.has(c)) { seenClasses.add(c); dom.classes.push(c); }
      if (el.id && !seenIds.has(el.id)) { seenIds.add(el.id); dom.ids.push(el.id); }
      if (el.tagName === 'A' && el.href && !seenHrefs.has(el.href)) { seenHrefs.add(el.href); dom.hrefs.push(el.href); }
    }
    return dom;
  };
  const flush = () => {
    pending = null;
    const dom = collect(document.documentElement);
    if (dom.classes.length || dom.ids.length || dom.hrefs.length) request(dom);
  };

  window.addEventListener('DOMContentLoaded', () => {
    flush();
    new MutationObserver(() => { if (!pending) pending = setTimeout(flush, 100); })
      .observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ['class', 'id'] });
  }, { once: true });
}
