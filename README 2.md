# gallery.yusando.com — 茶器ギャラリー

写真を送る → AIが銘・説明・等級を作る → そのまま掲載。在庫はD1、写真はR2。

## 価格（4等級・均一）
`wrangler.toml` の `PRICE_TIERS = "3000,5000,7000,10000"` を変えるだけ。

## 公開手順（初回のみ）
1. GitHubに `gallery-yusando` リポジトリを作り、このフォルダをpush
2. Cloudflare ダッシュボード → Workers & Pages → Create → Pages → Connect to Git
   - Build command: なし　／ Output directory: `public`
3. Pages プロジェクト → Settings → Bindings で確認（wrangler.tomlから自動）
   - D1 `DB` = gallery-db（作成済み ID: 6aee87a8-e748-4515-859b-5285a03bc4a1）
   - R2 `PHOTOS` = gallery-photos（作成済み）
4. Settings → Variables and Secrets に **Secret** を2つ
   - `ANTHROPIC_API_KEY`
   - `UPLOAD_TOKEN`（登録画面の合言葉。長めの文字列に）
5. Custom domains → `gallery.yusando.com` を追加
6. Route 53 に CNAME を追加（AWS CLI）
   ```
   gallery.yusando.com  CNAME  gallery-yusando.pages.dev
   ```
   Cloudflareが所有権確認のTXTを求める場合はその1本も追加。

## 使い方
- `https://gallery.yusando.com/upload` で写真を選び、合言葉を入れて「登録して掲載する」
- 一覧: `/`　詳細: `/item.html?id=xxxx`
- 売却済にする／非公開／銘の修正（合言葉付きで PATCH）:
  ```
  curl -X PATCH https://gallery.yusando.com/api/items/xxxx \
    -H "x-upload-token: 合言葉" -H "content-type: application/json" \
    -d '{"status":"sold"}'            # sold / hidden / published
  -d '{"mei":"初霜","mei_yomi":"はつしも"}'
  -d '{"tier":3}'                      # 等級変更 → 価格も連動
  ```
- 問い合わせ先は `public/item.html` の `INQUIRY` を変更

## 構成
```
functions/api/upload.js      写真→R2保存→Claude解析→D1登録
functions/api/items.js       一覧（公開分）
functions/api/items/[id].js  詳細 / PATCH更新
functions/photos/[[key]].js  R2画像配信
public/                      index.html / item.html / upload.html / style.css
```
