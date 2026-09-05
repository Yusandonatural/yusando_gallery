# 悠三堂古美術ギャラリー — 中古茶道具ポータル

均一価格の中古茶道具ポータル(静的HTML)。日本語+英語併記。

> ときめきやワクワクでお茶道具を選びたい。<br>
> 初心者でも楽しみやすい、均一価格の中古お茶道具ポータルです。

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

フォルダごとサーバーに置くだけで動きます(ビルド不要)。
Netlify / GitHub Pages / さくらのレンタルサーバ等にそのままアップロードできます。

## 将来のEC連携について

各道具詳細ページに `<div class="shop-stub" data-ec-category="chawan">` という
「在庫枠」を用意してあります。`js/site.js` の `CHADOGU_EC` オブジェクトが連携ポイントです。

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
