'use strict';

const path = require('path');
const { app, BrowserWindow, WebContentsView, Menu, ipcMain, session, shell } = require('electron');
const { Shield } = require('./shield');
const { toNavigableUrl } = require('./privacy');

// 広告・計測用のChromium機能と、先読み（アクセスしていないサイトへの通信）を止める
app.commandLine.appendSwitch('disable-features', [
  'BrowsingTopics', 'InterestGroupStorage', 'Fledge', 'PrivacySandboxAdsAPIs',
  'AttributionReportingCrossAppWeb', 'ConversionMeasurement', 'FencedFrames',
  'SpeculationRulesPrefetchProxy', 'NetworkPrediction', 'UserAgentClientHint',
].join(','));
app.commandLine.appendSwitch('dns-prefetch-disable');
app.commandLine.appendSwitch('force-webrtc-ip-handling-policy', 'disable_non_proxied_udp');

const TOOLBAR_HEIGHT = 84;
const HOME_URL = 'file://' + path.join(__dirname, 'ui', 'start.html');
// "persist:" を付けないパーティション＝履歴・Cookie・キャッシュはメモリ上だけで、終了時にすべて消える
const PARTITION = 'shizuka-private';

let win = null;
let browsingSession = null;
const tabs = new Map(); // id -> { view, blocked }
let activeTabId = null;
let nextTabId = 1;

// Electron名やアプリ名を含まない、一般的なChromeのUser-Agentにそろえる
function genericUserAgent() {
  const chrome = process.versions.chrome.split('.')[0];
  const platform = {
    darwin: 'Macintosh; Intel Mac OS X 10_15_7',
    win32: 'Windows NT 10.0; Win64; x64',
  }[process.platform] || 'X11; Linux x86_64';
  return `Mozilla/5.0 (${platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${chrome}.0.0.0 Safari/537.36`;
}

function tabState(id) {
  const tab = tabs.get(id);
  const wc = tab.view.webContents;
  const url = wc.getURL();
  return {
    id,
    title: wc.getTitle() || 'New Tab',
    url: url === HOME_URL ? '' : url,
    loading: wc.isLoading(),
    canGoBack: wc.navigationHistory.canGoBack(),
    canGoForward: wc.navigationHistory.canGoForward(),
    blocked: tab.blocked,
    active: id === activeTabId,
  };
}

function sendState() {
  if (!win || win.isDestroyed()) return;
  win.webContents.send('tabs:state', [...tabs.keys()].map(tabState));
}

function layoutActiveView() {
  const tab = tabs.get(activeTabId);
  if (!tab) return;
  const [width, height] = win.getContentSize();
  tab.view.setBounds({ x: 0, y: TOOLBAR_HEIGHT, width, height: Math.max(0, height - TOOLBAR_HEIGHT) });
}

function createTab(url = HOME_URL) {
  const id = nextTabId++;
  const view = new WebContentsView({
    webPreferences: {
      session: browsingSession,
      sandbox: true,
      contextIsolation: true,
      nodeIntegration: false,
      spellcheck: false,
      safeDialogs: true,
    },
  });
  const wc = view.webContents;
  wc.setWebRTCIPHandlingPolicy('disable_non_proxied_udp');
  tabs.set(id, { view, blocked: 0 });

  // target=_blank などは新しいタブで開き、勝手なポップアップウィンドウは作らせない
  wc.setWindowOpenHandler(({ url: target, disposition }) => {
    if (/^https?:/.test(target) && disposition !== 'other') createTab(target);
    return { action: 'deny' };
  });
  wc.on('did-start-navigation', (_e, _url, isInPlace, isMainFrame) => {
    if (isMainFrame && !isInPlace) tabs.get(id).blocked = 0;
    sendState();
  });
  for (const ev of ['did-navigate', 'did-navigate-in-page', 'page-title-updated', 'did-start-loading', 'did-stop-loading']) {
    wc.on(ev, sendState);
  }
  wc.on('before-input-event', (event, input) => handleShortcut(event, input));

  win.contentView.addChildView(view);
  switchTab(id);
  wc.loadURL(url);
  return id;
}

function switchTab(id) {
  if (!tabs.has(id)) return;
  activeTabId = id;
  for (const [tid, tab] of tabs) tab.view.setVisible(tid === id);
  layoutActiveView();
  tabs.get(id).view.webContents.focus();
  sendState();
}

function closeTab(id) {
  const tab = tabs.get(id);
  if (!tab) return;
  const ids = [...tabs.keys()];
  const index = ids.indexOf(id);
  win.contentView.removeChildView(tab.view);
  tab.view.webContents.close();
  tabs.delete(id);
  if (tabs.size === 0) {
    createTab();
    return;
  }
  if (activeTabId === id) switchTab(ids[index + 1] ?? ids[index - 1]);
  else sendState();
}

function activeWebContents() {
  const tab = tabs.get(activeTabId);
  return tab ? tab.view.webContents : null;
}

function onBlocked(webContentsId) {
  for (const [id, tab] of tabs) {
    if (tab.view.webContents.id === webContentsId) {
      tab.blocked++;
      if (id === activeTabId) sendState();
      return;
    }
  }
}

function handleShortcut(event, input) {
  if (input.type !== 'keyDown') return;
  const mod = process.platform === 'darwin' ? input.meta : input.control;
  const key = input.key.toLowerCase();
  const wc = activeWebContents();
  let handled = true;
  if (mod && key === 't') createTab();
  else if (mod && key === 'w') closeTab(activeTabId);
  else if (mod && key === 'l') { win.webContents.focus(); win.webContents.send('ui:focus-address'); }
  else if ((mod && key === 'r') || key === 'f5') wc && wc.reload();
  else if (input.alt && key === 'arrowleft') wc && wc.navigationHistory.goBack();
  else if (input.alt && key === 'arrowright') wc && wc.navigationHistory.goForward();
  else if (mod && key === 'tab') {
    const ids = [...tabs.keys()];
    const step = input.shift ? -1 : 1;
    switchTab(ids[(ids.indexOf(activeTabId) + step + ids.length) % ids.length]);
  } else handled = false;
  if (handled) event.preventDefault();
}

function registerIpc() {
  ipcMain.on('tab:new', () => createTab());
  ipcMain.on('tab:close', (_e, id) => closeTab(id));
  ipcMain.on('tab:switch', (_e, id) => switchTab(id));
  ipcMain.on('nav:go', (_e, input) => {
    const url = toNavigableUrl(String(input));
    const wc = activeWebContents();
    if (url && wc) { wc.loadURL(url); wc.focus(); }
  });
  ipcMain.on('nav:back', () => activeWebContents()?.navigationHistory.goBack());
  ipcMain.on('nav:forward', () => activeWebContents()?.navigationHistory.goForward());
  ipcMain.on('nav:reload', () => activeWebContents()?.reload());
  ipcMain.on('nav:stop', () => activeWebContents()?.stop());
  ipcMain.on('nav:home', () => activeWebContents()?.loadURL(HOME_URL));
  ipcMain.on('ui:ready', sendState);
  ipcMain.on('ui:shortcut', (event, input) => handleShortcut({ preventDefault() {} }, input));
}

async function createWindow() {
  session.defaultSession.setSpellCheckerEnabled(false);
  browsingSession = session.fromPartition(PARTITION, { cache: false });
  browsingSession.setUserAgent(genericUserAgent());
  const shield = new Shield(browsingSession, onBlocked);
  await shield.enable();

  win = new BrowserWindow({
    width: 1280,
    height: 860,
    title: 'Shizuka Browser',
    backgroundColor: '#f7f6f2',
    webPreferences: {
      preload: path.join(__dirname, 'ui', 'preload.js'),
      sandbox: true,
      contextIsolation: true,
      spellcheck: false,
    },
  });
  win.loadFile(path.join(__dirname, 'ui', 'index.html'));
  // ツールバー画面から外部サイトへ遷移させない
  win.webContents.on('will-navigate', (e) => e.preventDefault());
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https?:/.test(url)) createTab(url);
    return { action: 'deny' };
  });
  win.on('resize', layoutActiveView);
  win.on('closed', () => { win = null; tabs.clear(); });

  createTab();
}

Menu.setApplicationMenu(process.platform === 'darwin' ? Menu.buildFromTemplate([
  { role: 'appMenu' }, { role: 'editMenu' }, { role: 'windowMenu' },
]) : null);

registerIpc();
app.whenReady().then(createWindow);
app.on('window-all-closed', () => app.quit());
app.on('web-contents-created', (_e, contents) => {
  // ページから任意のアプリ（mailto: 等）を黙って起動させない。http(s)以外は外部に渡さない
  contents.on('will-navigate', (event, url) => {
    if (!/^(https?|file|about|data):/.test(url)) {
      event.preventDefault();
      if (/^mailto:/.test(url)) shell.openExternal(url);
    }
  });
});
