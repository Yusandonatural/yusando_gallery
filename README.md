# 悠三堂古美術ギャラリー — 中古茶道具ポータル

中古茶道具のためのポータルサイト(静的HTML)。日本語+英語併記。

## 構成(12ページ)

| ファイル | 内容 |
|---|---|
| `index.html` | トップ(コンセプト・このサイトについて・EC連携予告) |
| `tools.html` | 日本の茶道具一覧(詳細8点+概説8点=計16道具) |
| `setup.html` | 炉と風炉のしつらえ(配置図・比較表)+点前で必要な道具チェックリスト |
| `guide.html` | 使い方・薄茶点前のながれ・はじめてのひと揃え |
| `tools/chawan.html` ほか8点 | 道具別詳細:名前と種類/歴史/部位の名称(図解)/使い方/中古で選ぶポイント/在庫枠 |
| `css/style.css` | 共通スタイル |
| `js/site.js` | ナビ・スクロール演出・**EC連携フック** |

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
- 

## 編集方法

ページは `gen.py`(Python)から生成しています。文言や道具の追加は
`gen.py` 内の `TOOLS` / `MINOR` データを編集して `python3 gen.py` を実行すると
全ページに反映されます。HTMLを直接編集しても構いません。
