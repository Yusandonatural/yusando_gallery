'use strict';

const $ = (id) => document.getElementById(id);
const address = $('address');
let editingAddress = false;
let loading = false;

// タブ要素はidごとに使い回す。作り直すとクリックの途中で×ボタンが入れ替わり、押しても閉じなくなる
const tabElements = new Map();

function createTabElement(id) {
  const el = document.createElement('div');
  el.className = 'tab';
  const title = document.createElement('span');
  title.className = 'title';
  const close = document.createElement('button');
  close.className = 'close';
  close.textContent = '×';
  close.title = 'タブを閉じる (Ctrl+W)';
  close.addEventListener('mousedown', (e) => e.stopPropagation());
  close.addEventListener('click', (e) => { e.stopPropagation(); window.browser.closeTab(id); });
  el.addEventListener('mousedown', (e) => {
    if (e.button === 1) window.browser.closeTab(id);
    else if (e.button === 0) window.browser.switchTab(id);
  });
  el.append(title, close);
  return el;
}

function render(tabs) {
  const container = $('tabs');
  const ids = new Set(tabs.map((t) => t.id));
  for (const [id, el] of tabElements) {
    if (!ids.has(id)) { el.remove(); tabElements.delete(id); }
  }
  tabs.forEach((tab, i) => {
    let el = tabElements.get(tab.id);
    if (!el) { el = createTabElement(tab.id); tabElements.set(tab.id, el); }
    el.className = 'tab' + (tab.active ? ' active' : '') + (tab.loading ? ' loading' : '');
    el.title = tab.title;
    el.querySelector('.title').textContent = tab.title;
    if (container.children[i] !== el) container.insertBefore(el, container.children[i] || null);
  });

  const active = tabs.find((t) => t.active);
  if (!active) return;
  $('back').disabled = !active.canGoBack;
  $('forward').disabled = !active.canGoForward;
  loading = active.loading;
  $('reload').textContent = loading ? '×' : '↻';
  $('reload').title = loading ? '読み込みを中止' : '再読み込み (Ctrl+R)';
  $('blocked-count').textContent = active.blocked;
  if (!editingAddress) address.value = active.url;
  document.title = active.title;
}

$('new-tab').addEventListener('click', () => window.browser.newTab());
$('back').addEventListener('click', () => window.browser.back());
$('forward').addEventListener('click', () => window.browser.forward());
$('reload').addEventListener('click', () => (loading ? window.browser.stop() : window.browser.reload()));
$('home').addEventListener('click', () => window.browser.home());
$('address-form').addEventListener('submit', (e) => {
  e.preventDefault();
  editingAddress = false;
  window.browser.go(address.value);
});
address.addEventListener('focus', () => { editingAddress = true; address.select(); });
address.addEventListener('blur', () => { editingAddress = false; });
address.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') { editingAddress = false; address.blur(); window.browser.ready(); }
});

// ツールバーにフォーカスがあるときもショートカットを効かせる
document.addEventListener('keydown', (e) => {
  const mod = navigator.platform.startsWith('Mac') ? e.metaKey : e.ctrlKey;
  if ((mod && ['t', 'w', 'l', 'r', 'Tab'].includes(e.key)) || e.key === 'F5' ||
      (e.altKey && ['ArrowLeft', 'ArrowRight'].includes(e.key))) {
    e.preventDefault();
    window.browser.shortcut({
      type: 'keyDown', key: e.key, control: e.ctrlKey, meta: e.metaKey, alt: e.altKey, shift: e.shiftKey,
    });
  }
});

window.browser.onState(render);
window.browser.onFocusAddress(() => address.focus());
window.browser.ready();
