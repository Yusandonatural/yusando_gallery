# Shizuka Browser（静）

広告を除去し、閲覧の追跡（トラッキング）を遮断するプライバシー重視のWebブラウザ。Electron（Chromium）製。

## 起動

必要なもの: **Node.js 22.12 以上**（https://nodejs.org/ の LTS 版）

```
git fetch origin
git checkout claude/dazzling-mayer-cfmss5   # browser フォルダはこのブランチにある
cd browser
npm install
npm start
```

リポジトリの一番上のフォルダからなら `npm run browser` だけで同じことをする。

`npm start` は起動前に自動で点検し、Electron本体のダウンロード漏れは自動で取り直す。
直せない原因（Node.jsが古い、Linuxのサンドボックス設定など）は、対処法を日本語で表示して止まる。

配布用パッケージ（Windows .exe / macOS .dmg / Linux AppImage）: `npm run dist`

## 広告の除去

- **通信の遮断**: EasyList・EasyPrivacy・uBlock Origin系のフィルターリスト（Ghostery adblocker）で、広告・トラッカーへの通信を送信前に止める。一部は通信しない無害な代替スクリプトに差し替え、サイトが壊れないようにする
- **広告枠の非表示**: 通信を止めた後に残る広告枠やCookieバナーを、要素隠しルールで消す
- リストは起動時に更新し、取得できないときは前回分（`adblock-engine.bin`）、それもなければ内蔵の最小リストで遮断する

## 追跡の遮断

| 対象 | 対策 |
|---|---|
| URLの追跡パラメータ | `utm_*`・`fbclid`・`gclid`・`msclkid` などを開く前に除去 |
| 第三者Cookie | 他サイトへのCookie送信と、他サイトからのCookie設定を両方捨てる |
| リファラー | 他サイトへは閲覧中ページのURLを送らず、オリジン（ドメイン）だけにする |
| 解析ビーコン | `sendBeacon`・`<a ping>`・CSPレポートを送らない |
| 追跡拒否の意思表示 | `DNT: 1` と `Sec-GPC: 1`（Global Privacy Control）を全リクエストに付ける |
| 広告用ブラウザ機能 | Topics API・Protected Audience・Attribution Reporting を無効化 |
| 端末の識別 | User-Agentを一般的なChromeと同じにし、Client Hints・Battery APIを止める |
| IPアドレス漏えい | WebRTCでのローカルIP漏えいを防ぐ |
| 先読み通信 | DNS先読み・投機的プリフェッチを止め、開いていないサイトへ通信しない |
| 権限 | 位置情報・通知・カメラ・マイク等の要求はすべて自動で拒否 |
| 閲覧の痕跡 | 履歴・Cookie・キャッシュはメモリ上だけ。ウィンドウを閉じると消える |
| 検索 | 検索エンジンは利用者を追跡しない DuckDuckGo |

ツールバー右の 🛡 の数字は、今のページで遮断した広告・追跡の件数。

## 限界

- サイト自身のサーバーが受け取るアクセス記録（IPアドレス・閲覧ページ）は、ブラウザ側では消せない。IPを隠すにはVPNやTorが必要
- プロバイダ（回線事業者）からは接続先のドメインが見える
- フィルターリストにない新しい広告・トラッカーは素通りすることがある

## ショートカット

| 操作 | キー |
|---|---|
| 新しいタブ / タブを閉じる | Ctrl+T / Ctrl+W（macは⌘） |
| アドレスバーへ | Ctrl+L |
| 再読み込み | Ctrl+R / F5 |
| 戻る / 進む | Alt+← / Alt+→ |
| タブ切り替え | Ctrl+Tab / Ctrl+Shift+Tab |

## 構成

- `src/main.js` — ウィンドウとタブ管理、Chromiumの機能停止
- `src/shield.js` — セッションへの広告ブロック・追跡防止の組み込み
- `src/privacy.js` — 追跡パラメータ除去・第三者判定・ヘッダー整形（Electron非依存）
- `src/page-preload.js` — 各ページで先に動くスクリプト（ビーコン無効化・広告枠の非表示要求）
- `src/ui/` — ツールバー画面と新しいタブのページ
- `test/` — `npm test` で実行
