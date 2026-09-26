'use strict';
// npm start の前に、起動できない典型的な原因を調べて直す（直せないものは対処法を表示する）

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const root = path.join(__dirname, '..');
const fail = (msg) => {
  console.error('\n[Shizuka Browser] 起動できません: ' + msg + '\n');
  process.exit(1);
};

const [major, minor] = process.versions.node.split('.').map(Number);
if (major < 22 || (major === 22 && minor < 12)) {
  fail(`Node.js ${process.versions.node} は古すぎます。22.12 以上が必要です。\n` +
    '  https://nodejs.org/ から LTS 版を入れ直してから、もう一度 npm install → npm start してください。');
}

const electronDir = path.join(root, 'node_modules', 'electron');
if (!fs.existsSync(electronDir)) {
  fail('部品がまだ入っていません。このフォルダ（browser）で先に npm install を実行してください。');
}

// npm install 時の Electron 本体のダウンロードは、失敗しても黙って終わることがある
const pathFile = path.join(electronDir, 'path.txt');
const binary = fs.existsSync(pathFile) && path.join(electronDir, 'dist', fs.readFileSync(pathFile, 'utf8').trim());
if (!binary || !fs.existsSync(binary)) {
  console.log('[Shizuka Browser] Electron 本体をダウンロードしています（初回のみ・約100MB）…');
  const r = spawnSync(process.execPath, [path.join(electronDir, 'install.js')], { cwd: electronDir, stdio: 'inherit' });
  const ok = r.status === 0 && fs.existsSync(pathFile) &&
    fs.existsSync(path.join(electronDir, 'dist', fs.readFileSync(pathFile, 'utf8').trim()));
  if (!ok) {
    fail('Electron 本体をダウンロードできませんでした。ネットワーク（社内プロキシ・セキュリティソフト）を確認し、\n' +
      '  node_modules フォルダを削除してから npm install をやり直してください。');
  }
}

// Linux: chrome-sandbox の権限が正しくないと起動直後に落ちる
if (process.platform === 'linux') {
  const sandbox = path.join(electronDir, 'dist', 'chrome-sandbox');
  try {
    const st = fs.statSync(sandbox);
    const userns = (() => {
      try { return fs.readFileSync('/proc/sys/kernel/unprivileged_userns_clone', 'utf8').trim() === '1'; } catch { return true; }
    })();
    if (!(st.uid === 0 && (st.mode & 0o4000)) && !userns) {
      fail('Linux のサンドボックス設定が必要です。次の2行を実行してから npm start してください:\n' +
        `  sudo chown root ${sandbox}\n  sudo chmod 4755 ${sandbox}`);
    }
  } catch {}
}
