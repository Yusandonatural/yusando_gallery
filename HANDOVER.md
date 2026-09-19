# 引き継ぎ書 — 悠三堂古美術ギャラリー

2026年9月11日時点。茶道具ポータル（4言語）と在庫システム（Cloudflare）の全体像、
運用手順、ハマりどころ、残っている作業をまとめる。

---

## 0. 一枚で

| | 何 | どこ |
|---|---|---|
| 表側 | 静的サイト。Pythonで生成した `docs/` を GitHub Pages が配信 | https://gallery.yusando.com |
| 裏側 | Cloudflare Worker。在庫API・写真配信・登録画面 | https://yusando-gallery.isozaki-f67.workers.dev |
| データ | D1 `gallery-db`（在庫）／R2 `gallery-photos`（写真） | Cloudflare |
| AI | Claude API（`claude-sonnet-5`）で写真から銘・説明・等級を生成 | Worker から呼ぶ |
| 問い合わせ | Jotform（日英併記） | https://form.jotform.com/262528014622047 |
| リポジトリ | `Yusandonatural/yusando_gallery`、`main` ブランチ | Google Drive 内で作業（後述の注意あり） |

**更新の流れ**：`python3 build.py` → `docs/` が更新される → GitHub Desktop でコミット＆プッシュ → 数分で反映。
Worker（`src/index.js`）を触ったときは、加えて Cloudflare 側の再デプロイ。

---

## 1. リポジトリの構成

```
yusando_gallery/
├── build.py            ← これ1本で全言語を生成する入口
├── gen.py              日本語版。ページ本体・site.js・CSSのコピー・CNAME
├── gen_en.py           英語版（gen.py から FONTS/ROOT を借りる）
├── gen_fr.py           仏語版（コア5＋道具詳細8。記事は英語へ誘導）
├── gen_zh.py           繁体字版（同上。台湾寄りの語彙、Noto TC フォント）
├── l10n.py             言語横断の後処理：切替UI・hreflang・OG・約物・キャッシュ番号・sitemap
├── icons.py            24×24 の線画アイコン22点＋地球儀。<symbol>/<use> スプライト
├── sekki_data.py       二十四節気のデータ（日本語）
├── sekki_ko.py         七十二候
├── types_articles.py   「○○の種類」記事のデータ
├── evolution.py        「茶道具の変遷」記事
├── make_ogp.py         OGP画像を Playwright で描く（assets/ogp.png, ogp-en.png）
├── css/style.css       原本。build で docs/css/ にコピーされる
├── assets/             favicon・OGP。docs/assets/ にコピー
├── src/index.js        Cloudflare Worker 本体
├── wrangler.toml       Worker 設定（D1/R2 binding、価格帯、モデル名）
├── schema.sql          items テーブルの原型
├── schema-additions.sql 後から足した列（適用済み。再作成用の記録）
├── PLAN-sencha.md      煎茶道具サイトの実装プラン
└── docs/               ★ 生成物。GitHub Pages と Worker の assets の両方がここを配信
    ├── index.html tools.html setup.html guide.html articles/ tools/   日本語 21ページ
    ├── en/  fr/  zh/                                                  各言語
    ├── item.html stock.html upload.html bulk.html drafts.html        Worker 用画面（生成物ではない・手書き）
    ├── js/site.js  在庫連携（gen.py が生成）／ js/lang.js  言語切替（l10n.py が生成）
    ├── js/bulk.js  js/drafts.js                                       一括登録・下書き（手書き）
    ├── style.css   Worker用画面の共通CSS（docs/css/style.css とは別物）
    ├── css/ assets/ sitemap.xml robots.txt CNAME
```

**生成物と手書きの区別が大事。** `docs/` の中で `item.html / stock.html / upload.html / bulk.html / drafts.html / style.css / js/bulk.js / js/drafts.js / js/edit.js` は手書きで、`build.py` は触らない。それ以外は `build.py` が毎回上書きする。手書きの側を直すときは直接編集する。

---

## 2. ページ生成

### 動かし方
```
python3 build.py
```
`gen.py → gen_en.py → gen_fr.py → gen_zh.py` の順に書き、最後に `l10n.finish()` が全68ページに後処理をかける。所要数秒。依存は Python 3 のみ（Playwright は OGP を描き直すときだけ）。

### 言語の構成
| 言語 | prefix | ページ数 | 範囲 |
|---|---|---|---|
| 日本語 | `/` | 21 | 全部 |
| English | `/en/` | 21 | 全部 |
| Français | `/fr/` | 13 | コア5＋道具詳細8 |
| 繁體中文 | `/zh/` | 13 | 同上 |

仏・中は記事8本が未訳。それらへのリンクは英語版へ飛ばし、小さく「EN」のバッジを付けている（`EN_TAG`）。どの言語にどのページがあるかは `l10n.py` の `CORE` が唯一の真実。ページを訳し終えたら `CORE` に足すと、切替・hreflang・sitemap が全部ついてくる。

### 用語の方針
- 茶道用語は日本語を主、訳語を添える（Chawan (bol à thé)／茶碗（chawan））。
- **銘は訳さない。** ローマ字（`mei_romaji`）を併記する。`mei_en` 列はあるが表示には使っていない。
- 繁体字は台湾寄り。日本語フォントに無い字（價・們など）が混ざって字面が崩れるため、`zh` だけ Noto Serif TC / Noto Sans TC を読み込む（`html[lang="zh-Hant"]` で `--serif/--sans` を差し替え）。
- 仏語は約物を自動で整える（`«  »`、`;:!?` の前の細い空白）。`l10n.smarten()`。

### 言語切替
`<details class="lang-sw">`。開閉とキーボードはブラウザ任せ。`js/lang.js` は Escape と外側クリックで閉じるだけ。狭い画面ではハンバーガーの中で全幅の1行になる。

### 抹茶／煎茶の切り替え（道具一覧）
`tools.html` の見出し下に二択のスイッチ。ページは増やしていない（`CORE` はそのまま）。

- 状態は `<html data-tea="matcha|sencha">`。出し分けは `style.css` の2行（`html[data-tea=matcha] [data-tea=sencha]{display:none}` とその逆）。属性が無ければ全部見える＝JSが無くても壊れない。
- URL の `#sencha` / `#matcha` が最優先、次に `localStorage.yusando_tea`、無ければ抹茶。`#sencha` という **id は置かない**（置くとそこへ跳ぶ）。
- 煎茶側のデータと組み立ては **`sencha.py`** の1か所（4言語の札・段階3枚・スイッチ文言）。各 `gen_*.py` の `tools_body` は `_sencha.switch(lang)` と `_sencha.block(lang)` を呼ぶだけ。日本語の本文原稿は `sencha_ja.py`（詳細ページを作る段階2の材料）。
- 抹茶側の札は `<div data-tea="matcha">` で包んであるだけで、中身は変えていない。
- 煎茶の詳細ページはまだ無い。札は `<div class="tool-card plain">` で「準備中」。作るときは `sencha_ja.py` の `TOOLS[].sections` を `detail()` の型に流し込み、`CORE` に `tools/kyusu.html` 等を足す。
- 煎茶碗は「煎茶碗」の札だけ。抹茶側の「茶碗」は煎茶側には出さない（決定 2026-09-14）。

### ロゴ
ヘッダーの「C」は **`assets/cerendipity-symbol-gold.svg`** を `<img class="brand__c">` で貼る（ポータル4言語・`stock.html`・`item.html` とも）。続く「erendipity」は文字（Optima 系）。ロゴ一式は `assets/`（symbol-ink／gold／reverse、favicon-16／32、favicon.ico、OG）。C を差し替えるときは SVG ファイルを置き換えるだけ。ページ側は `.brand__c` の高さ（.88em）だけ持つ。

### アイコン
`icons.py` に線だけを書く。煎茶側の17点（急須・宝瓶・湯冷まし・煎茶碗・茶托・茶心壺・茶合・涼炉・水注・巾筒・瓶敷・盆・提籃・茶櫃・炉屏・器局・香炉）もここ。太さ・色は CSS（`.ico`, `.ico--sm`, `.ico--hero`, `.ico--plate`）が決める。部位図の番号は `parts_icon(slug, dots)`。座標は `gen_en.py` の `TOOLS_EN[...]["parts_dots"]` が原本で、仏・中はそれを import している。

---

## 3. 在庫システム（Cloudflare）

### 構成
- Worker `yusando-gallery`（`src/index.js`、ESM 1ファイル）
- D1 `gallery-db`　id `6aee87a8-e748-4515-859b-5285a03bc4a1`
- R2 `gallery-photos`
- `[assets] directory = "docs"` → 静的ファイルは Worker からも配信される（workers.dev 側）
- Secrets：`ANTHROPIC_API_KEY`、`UPLOAD_TOKEN`（登録画面の合言葉）。ダッシュボードで設定。**値は読み出せない**。
- Vars：`PRICE_TIERS = "3000,5000,7000,10000"`、`CLAUDE_MODEL = "claude-sonnet-5"`

### API
| Method | Path | 認証 | 何 |
|---|---|---|---|
| GET | `/api/health` | 任意 | 設定の有無。合言葉ありなら鍵の書式チェックも返す。**鍵の中身は返さない** |
| GET | `/api/items` | 任意 | 匿名：published/sold のみ。認証：全部。`?batch=` `?status=`（認証）、`?category=` `?color=` `?shape=`（誰でも）で絞れる |
| GET | `/api/items/:id` | 不要 | id **または品番**（`Y-0042`／`y-42`／`42`）で1件 |
| PATCH | `/api/items/:id` | 要 | 許可された列だけ更新（status, mei, category, tier, sekki, 各 `_en` …）。`{cover: <key>}` でその写真を表紙に（`photos` の直書きは不可） |
| POST | `/api/upload` | 要 | 1点登録。写真→AI→**draft**。画面で直して公開 |
| POST | `/api/draft` | 要 | 一括登録用。写真だけ預かり `status='draft'`。AIは呼ばない |
| POST | `/api/items/:id/analyze` | 要 | 下書き1点をAIで読む。失敗は `analysis_status='failed'` で残る |
| POST | `/api/items/:id/classify` | 要 | **色・形だけ**を付け直す（写真3枚まで。文章は触らない）。同時に**正面の写真を1枚目（表紙）に動かす**。下書き画面の「色・形を付ける」 |
| POST | `/api/items/bulk` | 要 | `{ids, action}`。publish（解析済みのみ）／hide／delete（R2の写真も消す） |
| GET | `/photos/:key` | 不要 | R2 の写真。1年キャッシュ |

認証は `x-upload-token` ヘッダまたは `?token=`。

### D1 `items` テーブル
```
id            TEXT PK   8桁ランダム。URL用
sku, sku_seq            品番 Y-0042 と連番。一意索引。下書き作成時に採番、以後変えない
created_at, status      status: published / sold / hidden / draft
mei, mei_yomi, mei_reason, mei_romaji, mei_en, mei_reason_en
category                固定16種のいずれか（src/index.js の CATEGORIES）
technique, glaze, kiln, era, condition（＋各 _en）
has_box, description, description_en
tier (1-4), price, forced_tier   forced_tier は人が指定したときだけ。AIの見立てを打ち消さないため
tier_reason, raw_json   raw_json はAIの生出力
photos                  R2キーのJSON配列
sekki, sekki_reason     節気（JSON配列）。一覧のチップに出る
batch_id                一括登録の単位
analysis_status         pending / done / failed
analysis_error
same_object, group_warning   AIが「写真は同じ器か」を答えた結果。0なら下書き画面で警告
cover_hash              表紙写真のSHA-256。二重登録よけ
color, shape            検索用の固定語彙（src/index.js の COLORS / SHAPES）。語彙の外の値は入らない。
                        color は器物全般、shape は茶碗だけ。stock.html で絞り込み、item.html で表示、edit.js で修正
```
現在7件、全部 `茶碗`・`published`。品番 Y-0001〜0007。

### 登録の流れ
**1点ずつ**（`upload.html`）：写真1〜5枚を選ぶ → 端末で長辺1600pxに縮小 → `/api/upload` → **下書き**として登録 → その場で編集欄が開く → 直して「公開する」で published。即公開はしない。押さずに離れても下書きは残り、`drafts.html` から続けられる。

**まとめて**（`bulk.html` → `drafts.html`）：組の分け方は3通り。既定は**ファイル名**（`1.jpg`＝正面、`1_top.jpg`＝上面、`1_bottom.jpg`＝裏面、`1_box.jpg`＝共箱。同じ番号を1組にし、正面→上面→裏面→箱の順。正面の無い組には印）。ほかに「決まった枚数」「撮影した間隔（EXIF）」。

1. 写真を全部選ぶ。ファイル名の番号で組に分ける（名前を付けていなければ、撮影時刻の間隔か枚数で）
2. 画面で組を直す（←／分／×／→、前の組と合わせる）。組ごとに種別・等級を指定可
3. 「登録する」→ 組ごとに `/api/draft`（写真だけ）→ 続けて `/api/items/:id/analyze` を同時3本で
4. 下書き画面で確認。`same_object=0` は金茶の印。種別・等級はその場で直せる
5. チェックして「まとめて公開」

途中でタブを閉じても下書きはD1に残る。`bulk.html` を開き直すと「続きから読み取る」が出る（`localStorage` の `yusando_last_batch`）。

### AIが書いたものを人が直す
`docs/js/edit.js`（`window.YSD_EDIT.render(container, item, opts)`）が編集フォームの唯一の定義。`upload.html`（登録直後）と `drafts.html`（「内容を直す」）の両方がこれを呼ぶ。画面ごとに欄を書くと必ず食い違うので、欄を増やすときは `edit.js` の `FIELDS` に1行足す（`patchItem` の allowlist にも同じ名前を足すこと）。

- 銘／説明／所見／英語（折りたたみ）／分類（種別・等級・二十四節気）
- **変えた欄だけ** PATCH する。触っていない欄まで送ると、別画面での編集を古い値で上書きしてしまう。
- 直した欄は枠が金色になり、操作列に「N 箇所を直しました」と出る。

### 道具ページのギャラリー
各道具の詳細ページ（4言語）の末尾「この道具のギャラリー」は、`docs/js/site.js` の stock ブロックが `/api/items?category=<種別>` を読んで描く。件数入り見出し → 絞り込みチップ（色は全種別、形は茶碗だけ。語彙は Worker の `COLORS`/`SHAPES` と同じで、site.js 側に4言語の表示名を持つ）→ 12件ずつ「もっと見る」→ `stock.html?category=<種別>` へのリンク（在庫一覧側がタブを合わせて開く）。静的ページの変更だけで動くので Worker の再デプロイは要らない。価格や販売の語は出さない（制約 §7）。

### 卸・業者様へ（WHOLESALE）
トップページの最後に `id="wholesale"` の節がある（4言語）。フッターの並びからも飛べる。中身は取り合わせの提案・状態の案内・海外発送・お取引についての4枠と、問い合わせフォーム（Jotform、`form.jotform.com/262528014622047`）へのボタン。**価格は書かない。オンラインでの取り扱いは準備中と明記する**（制約 §7）。文面は各 `gen*.py` の `index_body` の末尾にあるので、直すときは4つとも直す。アンカーで飛んだときに見出しがヘッダーに隠れないよう、`css/style.css` に `section[id]{scroll-margin-top:96px}` を置いた。

### 費用の目安
1点＝写真4枚で入力約11,000トークン・出力約1,200トークン → **約5円**。100点で500円強。写真を1024pxにすると約3割減。

---

## 4. 問い合わせ

Jotform `262528014622047`。項目：お名前／メール／種別（この茶道具について・見学・その他）／茶器ID（非表示）／銘（非表示）／内容／連絡方法／電話。
`item.html` から `?item=<品番>&mei=<銘>` を付けて飛ぶので、どの器物の問い合わせかが記録に残る。`stock.html` の下部にも導線あり。

---

## 5. ハマりどころ（実際に起きたこと）

**Google Drive が原因のもの**
- リポジトリが Google Drive の中にある。Drive がファイルを「クラウドのみ」に脱水化すると、`git` や Python が `Resource deadlock avoided (errno 35)` で読めなくなる。**対処**：Finder でファイルを開く、または「オフラインで使用可能」にする。Claude 側からは `device_stage_files` で復元できる。
- 上書きは `<path>.new` に書いてから `os.replace()` で差し替えると通る。直接開いて書くと落ちることがある。
- **根本対処**：リポジトリを Drive の外（`~/github/` など）へ移すこと。推奨。

**git**
- `git status` を裏で走らせると `.git/index.lock` が残り、GitHub Desktop が「ブロックしているファイルがある」と言う。Claude 側は `git --no-optional-locks` を使う。残ったら `.git/index.lock` を消す（`_to_delete/` に移す）。
- 別の作業から force push されて履歴が巻き戻ったことが一度ある。プッシュ前に `git fetch` で origin を見る。

**Cloudflare**
- 以前、デプロイ済みの Worker に CORS ヘッダが無く、ポータルの在庫カードが一切出なかった。サーバ間の fetch は Origin を送らないので気づきにくい。**ブラウザから見えないときは、まず本番の Worker のコードを読む。**
- `/api/health` は誰でも叩ける。鍵の中身を返さないよう直してある（2026-09-11）。
- `let CUR = null` にリクエストを入れて使い回す作りは、`await` 中に別のリクエストで上書きされる競合があった。リクエストごとに `jsonWith(request)` を作る形に直してある。

**GitHub Pages**
- Source は `main` / `/docs`。ルートにすると `docs/CNAME` が見えず 404 になる（実際になった）。

**Claude 側の制約**
- GitHub へのプッシュはできない（資格情報がない）。コミット＆プッシュは GitHub Desktop で。
- Worker のデプロイもできない（Cloudflare MCP は Workers に対して読み取りのみ）。D1 は読み書きできる。
- Secrets の値は読めない（UPLOAD_TOKEN を忘れたら Cloudflare で再設定）。
- `device_bash` はファイルを削除できない。`_to_delete/` に移す運用。中身は時々手で捨てる。

---

## 6. 残っている作業

| 優先 | 内容 | 状態 |
|---|---|---|
| ★ | **コミット＆プッシュ、Worker 再デプロイ**（品番対応・Worker の修正） | 未 |
| 高 | 抹茶側の記事8本の仏語・繁体字化（節気17,000字が大物） | 未着手 |
| 高 | 煎茶道具サイト（`PLAN-sencha.md`）。名称・流派・自社茶リンクの3点を決めてから | 待ち |
| 中 | 一括登録を実際に使って、区切り30秒と写真1600pxの妥当性を見る | 未 |
| 中 | `stock.html` に抹茶／煎茶の大区分タブ（煎茶側と同時） | 未 |
| 低 | A5 の展示カードPDF（22道具＋段階バッジ）の再生成 | 未 |
| 低 | 背景削除（本番登録時）。以前の質問。案は出していない | 未 |
| 低 | `_to_delete/` の中身を捨てる | 随時 |

---

## 7. 前提と制約（変えないこと）

- **通販の許可はまだ無い。** 価格は表に出さない。「お問い合わせください」で止める。文言の「今買える」は使わない。
- 品番は一度振ったら変えない。種別や銘を直しても番号はそのまま。
- `docs/` の手書きファイル（§1）を `build.py` で上書きしない。
- 銘は訳さない。

---

## 8. 検証の道具

- Worker：`wtest/run.mjs`（Node 22 の `node:sqlite` と偽R2で本物の SQL を通す。55項目）
- 画面：Playwright（`/opt/pw-browsers/chromium`）。API は `ctx.route()` で偽装。EXIF付きの試験用写真は `piexif` で作る
- リンク切れ：`docs/` 全体を走査して相対リンクの存在を確認（1,882本・切れ0が現状）
- 横あふれ：1280px と 390px で `scrollWidth > clientWidth` を見る
