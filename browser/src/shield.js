'use strict';
// ブラウジング用セッションに広告ブロックと追跡防止を組み込む

const fs = require('fs');
const path = require('path');
const { app, webContents, ipcMain } = require('electron');
const { ElectronBlocker } = require('@ghostery/adblocker-electron');
const { parse } = require('tldts');
const privacy = require('./privacy');

// 許可するのは全画面表示とクリップボードへの書き込みだけ（位置情報・通知・カメラ等はすべて拒否）
const ALLOWED_PERMISSIONS = new Set(['fullscreen', 'clipboard-sanitized-write']);

async function loadBlocker() {
  const cachePath = path.join(app.getPath('userData'), 'adblock-engine.bin');
  // 広告＋トラッカー＋迷惑要素（Cookieバナー等）の全リスト。取得できないときは前回のキャッシュを使う
  return ElectronBlocker.fromPrebuiltFull(fetch, {
    path: cachePath,
    read: fs.promises.readFile,
    write: fs.promises.writeFile,
  });
}

// ページを開いているタブのトップレベルURL（第三者かどうかの判定基準）
function firstPartyUrlOf(details) {
  if (details.resourceType === 'mainFrame') return details.url;
  const wc = details.webContentsId ? webContents.fromId(details.webContentsId) : null;
  return (wc && !wc.isDestroyed() && wc.getURL()) || details.referrer || null;
}

class Shield {
  constructor(session, onBlocked) {
    this.session = session;
    this.onBlocked = onBlocked; // (webContentsId, url, reason) => void
    this.blocker = null;
  }

  async enable() {
    const ses = this.session;

    // スペルチェック辞書の外部取得も止める
    ses.setSpellCheckerEnabled(false);
    ses.setPermissionRequestHandler((_wc, permission, callback) => callback(ALLOWED_PERMISSIONS.has(permission)));
    ses.setPermissionCheckHandler((_wc, permission) => ALLOWED_PERMISSIONS.has(permission));

    // 追跡防止のページ内スクリプト（sendBeacon無効化など）
    ses.registerPreloadScript({ type: 'frame', filePath: path.join(__dirname, 'page-preload.js') });

    try {
      this.blocker = await loadBlocker();
      // 広告枠などの要素隠し（コスメティックフィルター）は page-preload.js から要求される
      ipcMain.handle('shield:cosmetics', (event, url, dom) => this.injectCosmetics(event, url, dom));
    } catch (err) {
      console.error('[shield] フィルターリストを読み込めませんでした。内蔵の最小リストで遮断します:', err.message);
    }

    // webRequestはイベントごとにリスナーが1つだけなので、広告ブロックの処理もここでまとめて呼ぶ
    ses.webRequest.onBeforeRequest({ urls: ['<all_urls>'] }, (details, callback) => this.handleBeforeRequest(details, callback));
    ses.webRequest.onBeforeSendHeaders({ urls: ['<all_urls>'] }, (details, callback) => this.handleBeforeSendHeaders(details, callback));
    ses.webRequest.onHeadersReceived({ urls: ['<all_urls>'] }, (details, callback) => this.handleHeadersReceived(details, callback));
  }

  // ページのURLとDOM内のclass/idに合う非表示ルールと広告対策スクリプトを注入する
  injectCosmetics(event, url, dom) {
    if (!this.blocker || event.sender.session !== this.session) return;
    const { hostname, domain } = parse(url);
    const initial = dom === undefined;
    const { active, styles, scripts } = this.blocker.getCosmeticsFilters({
      url,
      hostname: hostname || '',
      domain: domain || '',
      classes: dom?.classes,
      ids: dom?.ids,
      hrefs: dom?.hrefs,
      getBaseRules: initial,
      getInjectionRules: initial,
      getExtendedRules: false,
      getRulesFromHostname: initial,
      getRulesFromDOM: !initial,
      callerContext: { frameId: event.frameId, processId: event.processId },
    });
    if (active === false) return;
    if (styles.length > 0) event.sender.insertCSS(styles, { cssOrigin: 'user' });
    for (const script of scripts) {
      event.sender.executeJavaScript(script, true).catch(() => {});
    }
  }

  report(details, reason) {
    if (this.onBlocked) this.onBlocked(details.webContentsId, details.url, reason);
  }

  handleBeforeRequest(details, callback) {
    const { url, resourceType } = details;

    if (resourceType === 'mainFrame' || resourceType === 'subFrame') {
      const cleaned = privacy.stripTrackingParams(url);
      if (cleaned) {
        this.report(details, 'tracking-params');
        callback({ redirectURL: cleaned });
        return;
      }
      if (resourceType === 'mainFrame') {
        callback({});
        return;
      }
    }

    if (privacy.ALWAYS_BLOCKED_TYPES.has(resourceType)) {
      this.report(details, 'beacon');
      callback({ cancel: true });
      return;
    }

    if (!this.blocker) {
      if (privacy.isFallbackBlocked(url)) {
        this.report(details, 'ad');
        callback({ cancel: true });
      } else {
        callback({});
      }
      return;
    }

    this.blocker.onBeforeRequest(details, (response) => {
      if (response.cancel || response.redirectURL) this.report(details, 'ad');
      callback(response);
    });
  }

  handleBeforeSendHeaders(details, callback) {
    const headers = { ...details.requestHeaders };
    privacy.sanitizeRequestHeaders(headers, details.url, firstPartyUrlOf(details));
    callback({ requestHeaders: headers });
  }

  handleHeadersReceived(details, callback) {
    const headers = { ...(details.responseHeaders || {}) };
    const changed = privacy.sanitizeResponseHeaders(headers, details.url, firstPartyUrlOf(details));
    const finish = (response) => {
      if (response.responseHeaders) callback(response);
      else if (changed) callback({ responseHeaders: headers });
      else callback({});
    };
    if (this.blocker) {
      this.blocker.onHeadersReceived({ ...details, responseHeaders: headers }, finish);
    } else {
      finish({});
    }
  }
}

module.exports = { Shield };
