# yusando_gallery — 茶器ギャラリー

写真を送る → AIが銘・説明・等級を作る → そのまま掲載。

- 表側（画面）: GitHub Pages → https://gallery.yusando.com （`docs/`）
- 裏側（API・写真・在庫）: Cloudflare Worker → https://yusando-gallery.isozaki-f67.workers.dev

## 公開手順
### Worker（Cloudflare）— 済
Git連携で `npx wrangler deploy`。D1 `DB`・R2 `PHOTOS` は wrangler.toml から自動。
Secrets: `ANTHROPIC_API_KEY`, `UPLOAD_TOKEN`（Settings → Variables and Secrets）

### GitHub Pages
1. GitHubリポジトリ → Settings → Pages
   - Source: **Deploy from a branch**
   - Branch: `main` ／ Folder: **/docs** → Save
2. Custom domain に `gallery.yusando.com` を入れて Save（`docs/CNAME` があるので自動でも入る）
3. Route 53 に CNAME を追加（AWS CLI）
   ```
   gallery.yusando.com  CNAME  yusandonatural.github.io
   ```
4. DNSが通ったら GitHub Pages 設定で **Enforce HTTPS** にチェック

## 価格（4等級）
`wrangler.toml` の `PRICE_TIERS = "3000,5000,7000,10000"`

## 使い方
- 登録: https://gallery.yusando.com/upload.html （合言葉＝UPLOAD_TOKEN）
- 一覧: https://gallery.yusando.com/　　詳細: /item.html?id=xxxx
- 売却済・非公開・銘の修正:
  ```
  curl -X PATCH https://yusando-gallery.isozaki-f67.workers.dev/api/items/xxxx \
    -H "x-upload-token: 合言葉" -H "content-type: application/json" \
    -d '{"status":"sold"}'      # sold / hidden / published
  ```
- 問い合わせ先は `docs/item.html` の `INQUIRY` を変更

## 構成
```
wrangler.toml   Worker設定（assets=docs, D1, R2）
src/index.js    API（/api/upload, /api/items, /photos/*）+ CORS
docs/           index.html / item.html / upload.html / style.css / CNAME
schema.sql      D1スキーマ（適用済み）
```
