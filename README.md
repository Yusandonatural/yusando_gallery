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

---

# 静的ポータル(悠三堂古美術ギャラリー)

`docs/` には、在庫システムに加えて **日本語21ページ + 英語21ページの静的ポータル**が入っています。
`gen.py` / `gen_en.py` で生成され、出力先は `docs/`。

| パス | 中身 |
|---|---|
| `docs/index.html` | ポータルのトップ(旧・在庫一覧は `docs/stock.html` に移動) |
| `docs/stock.html` | 在庫一覧(以前の `docs/index.html`。中身は変えていません) |
| `docs/item.html` / `docs/upload.html` | 在庫の詳細 / 登録(戻り先を `/stock.html` に変更) |
| `docs/style.css` | 在庫システム側のスタイル(ポータルは `docs/css/style.css`) |

## 構成(日本語21ページ + 英語21ページ)

| ファイル | 内容 |
|---|---|
| `index.html` | トップ(コンセプト・このサイトについて・EC連携予告) |
| `tools.html` | 日本の茶道具一覧(詳細8点+概説14点=計22道具)。LV.1〜3の揃えかた別に分類 |
| `setup.html` | 炉と風炉のしつらえ(配置図・比較表)+点前で必要な道具チェックリスト |
| `guide.html` | 使い方・薄茶点前のながれ・はじめてのひと揃え |
| `tools/chawan.html` ほか8点 | 道具別詳細:名前と種類/歴史/部位の名称(図解)/使い方/中古で選ぶポイント/在庫枠 |
| `css/style.css` | 共通スタイル |
| `articles/` | 読みもの8本(茶碗/釜/茶入/棗/茶筅の種類・茶道の歴史・茶道具の進化・二十四節気と七十二候) |
| `js/site.js` | ナビ・スクロール演出・**EC連携フック** |
| `en/` | 英語版(全21ページ・日本語版と1対1で対応) |
| `assets/` | favicon・OGP画像(SNSシェア用 1200×630) |
| `sitemap.xml` / `robots.txt` | 検索エンジン向け(生成時に自動出力) |

詳細ページ: 茶碗 / 茶筅 / 茶杓 / 棗 / 茶釜 / 柄杓 / 帛紗 / 水指

## 公開方法

生成物はすべて `docs/` に出ます。GitHub Pages の公開元を **main / `/docs`** にすれば、
そのまま https://gallery.yusando.com で公開されます(`docs/CNAME` は生成時に自動作成)。
Cloudflare Worker 側も `wrangler.toml` の `assets = docs` で同じフォルダを配信します。

## 在庫連携(Yusando Gallery Worker API)

各道具詳細ページの「在庫枠」に、Worker が返す在庫を表示します。
`docs/js/site.js` の `CHADOGU_EC` が連携ポイント(生成元は `gen.py` の末尾)。

```js
window.CHADOGU_EC = {
  enabled: true,
  endpoint: "https://yusando-gallery.isozaki-f67.workers.dev",
  categories: { chawan:"茶碗", chaire:"茶入", natsume:"棗", ... },
};
```

- `categories` はポータルのスラッグ → API の固定16種への対応表。
  ここに無い道具(茶筅・帛紗・柄杓など)は「準備中」の文面のまま出ます
- 在庫が0件のとき・APIに繋がらないときも「準備中」のまま。壊れて見えることはありません
- カードから `item.html?id=…` へ飛びます(Worker側の詳細ページ)
- **別ドメインから読む場合**は Worker の `src/index.js` の `ALLOWED` に
  そのドメインを足して再デプロイすること

```js
window.CHADOGU_EC = {
  enabled: false,   // ← trueにすると全詳細ページで在庫表示が有効に
  endpoint: "",     // Shopify Storefront API などのエンドポイント
  fetchListings: async (category) => [...], // 商品取得を実装
};
```

- **Shopify連携の場合**: 商品に道具スラッグ(`chawan`, `natsume` など)のタグを付け、
  Storefront API で `tag:カテゴリ` 検索した結果を返すだけで、各ページの在庫枠に表示されます。
- カート・決済はShopify側(Buy Button / チェックアウトリンク)に委ねる構成が最小工数です。

## 編集方法

ページは `gen.py`(日本語)/ `gen_en.py`(英語)から生成しています。
`python3 gen.py && python3 gen_en.py` で全ページが再生成されます。

| ファイル | 中身 |
|---|---|
| `gen.py` | 日本語サイト全体。`TOOLS` / `MINOR` に道具データ |
| `icons.py` | **道具アイコン22点(24×24 ラインアイコン)**。`<symbol>` スプライト+`<use>`で全ページに配置。色は `currentColor`、線幅はCSSの `.ico` で制御 |
| `gen_en.py` | 英語サイト(`en/`)。`TOOLS_EN` / `MINOR_EN` |
| `sekki_data.py` | 二十四節気ごとの茶花・茶杓の銘・茶碗・棗の図柄(日英) |
| `sekki_art.py` | 節気ごとの季節の絵柄SVG(24点) |
| `sekki_ko.py` | 七十二候(全72候・日英) |
| `evolution.py` | 「茶道具の進化」記事の内容(日英) |
| `types_articles.py` | 釜・茶入・棗の「種類」記事の内容(日英) |
| `cards/gen_cards.py` | A5展示カード。`python3 gen_cards.py && python3 render_pdf.py` でPDF出力 |
| `make_ogp.py` | OGP画像(`assets/ogp.png` / `ogp-en.png`)を再生成 |

### `gen_en.py` の後処理でやっていること

英語版の生成後、日英あわせて42ページに対して次を自動で流し込みます。

- 言語切替リンク(EN ⇄ 日本語)
- `canonical` / `hreflang`(ja / en / x-default)
- OGP・Twitterカード(タイトル・説明・画像)
- favicon / apple-touch-icon / theme-color
- 引用符の自動整形(`"..."` → `“...”`、`'` → `’`)と裸の `&` のエスケープ
- `sitemap.xml`(42URL・言語間リンク付き)と `robots.txt`

HTMLを直接編集しても構いませんが、次回の生成で上書きされます。

