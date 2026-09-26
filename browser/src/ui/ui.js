'use strict';

const $ = (id) => document.getElementById(id);
const address = $('address');
let editingAddress = false;
let loading = false;

function render(tabs) {
  const container = $('tabs');
  container.replaceChildren();
  for (const tab of tabs) {
    const el = document.createElement('div');
    el.className = 'tab' + (tab.active ? ' active' : '') + (tab.loading ? ' loading' : '');
    el.title = tab.title;
    const title = document.createElement('span');
    title.className = 'title';
    title.textContent = tab.title;
    const close = document.createElement('button');
    close.className = 'close';
    close.textContent = '×';
    close.title = 'タブを閉じる (Ctrl+W)';
    close.addEventListener('click', (e) => { e.stopPropagation(); window.browser.closeTab(tab.id); });
    el.addEventListener('mousedown', (e) => {
      if (e.button === 1) window.browser.closeTab(tab.id);
      else if (e.button === 0) window.browser.switchTab(tab.id);
    });
    el.append(title, close);
    container.append(el);
  }

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
