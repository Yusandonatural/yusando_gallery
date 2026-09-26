'use strict';
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('browser', {
  newTab: () => ipcRenderer.send('tab:new'),
  closeTab: (id) => ipcRenderer.send('tab:close', id),
  switchTab: (id) => ipcRenderer.send('tab:switch', id),
  go: (input) => ipcRenderer.send('nav:go', input),
  back: () => ipcRenderer.send('nav:back'),
  forward: () => ipcRenderer.send('nav:forward'),
  reload: () => ipcRenderer.send('nav:reload'),
  stop: () => ipcRenderer.send('nav:stop'),
  home: () => ipcRenderer.send('nav:home'),
  ready: () => ipcRenderer.send('ui:ready'),
  shortcut: (input) => ipcRenderer.send('ui:shortcut', input),
  onState: (fn) => ipcRenderer.on('tabs:state', (_e, tabs) => fn(tabs)),
  onFocusAddress: (fn) => ipcRenderer.on('ui:focus-address', fn),
});
