# -*- coding: utf-8 -*-
"""煎茶の道具 — 道具一覧ページの「抹茶／煎茶」切り替え（A案）

tools.html の中で、抹茶の札と煎茶の札を出し分ける。ページは増やさない。
本文の元は sencha_ja.py（日本語の原稿データ）。ここでは札に必要な
名前・ローマ字・一行説明だけを4言語で持ち、HTMLの組み立て関数を置く。

出し分けの仕組みは CSS 2行（style.css）と site.js の 30 行：
  <html data-tea="matcha"> のとき [data-tea="sencha"] を消す。逆も同じ。
  属性が無ければ全部見える（JSが無い環境の保険）。

守ること
  - 道具名は訳さない。漢字＋ローマ字。
  - 価格は出さない。「今買える」は使わない。
  - 抹茶側の文章・順序は動かさない。
"""
from icons import icon as ico

# ─────────────────────────────────────────── スイッチと見出しの文言 ──
UI = {
    "ja": dict(matcha="抹茶", matcha_sub="MATCHA", sencha="煎茶", sencha_sub="SENCHA",
               aria="抹茶と煎茶の切り替え",
               lv_kicker="揃えかた — THREE STAGES", lv_title="三つの段階で考える",
               lv_lede="煎茶の道具も、いちどに揃える必要はありません。急須ひとつで淹れるところから始めて、客を迎え、席を整える。段階ごとに道具が増えていきます。",
               main_h="煎茶の道具", main_sub="UTENSILS OF SENCHA — 詳細ページは準備中",
               other_h="そのほかの道具", other_sub="FURTHER UTENSILS — 概説",
               soon="くわしい紹介は準備中"),
    "en": dict(matcha="Matcha", matcha_sub="", sencha="Sencha", sencha_sub="",
               aria="Switch between matcha and sencha utensils",
               lv_kicker="HOW TO BUILD A SET — THREE STAGES", lv_title="Three stages to think in",
               lv_lede="Sencha utensils need not be gathered all at once either. Begin with a single kyūsu, then welcome guests, then compose the table. Each stage adds a few pieces.",
               main_h="Utensils of Sencha", main_sub="DETAIL PAGES COMING",
               other_h="Further Utensils", other_sub="OVERVIEW",
               soon="Detail page in preparation"),
    "fr": dict(matcha="Matcha", matcha_sub="", sencha="Sencha", sencha_sub="",
               aria="Basculer entre les ustensiles du matcha et du sencha",
               lv_kicker="COMPOSER SON SERVICE — TROIS ÉTAPES", lv_title="Trois étapes pour y penser",
               lv_lede="Les ustensiles du sencha, eux non plus, ne se réunissent pas d’un coup. On commence avec un seul kyūsu, puis on reçoit, puis on compose la table. Chaque étape ajoute quelques pièces.",
               main_h="Ustensiles du sencha", main_sub="PAGES DÉTAILLÉES À VENIR",
               other_h="Autres ustensiles", other_sub="APERÇU",
               soon="Page détaillée en préparation"),
    "zh": dict(matcha="抹茶", matcha_sub="MATCHA", sencha="煎茶", sencha_sub="SENCHA",
               aria="切換抹茶與煎茶的道具",
               lv_kicker="如何備齊 — 三個階段", lv_title="分三個階段來想",
               lv_lede="煎茶的道具也不必一次備齊。先從一把急須開始泡茶，再迎客，再佈置茶席。每個階段多添幾件。",
               main_h="煎茶的道具", main_sub="UTENSILS OF SENCHA — 詳細頁面籌備中",
               other_h="其他道具", other_sub="FURTHER UTENSILS — 概說",
               soon="詳細介紹籌備中"),
}

# ─────────────────────────────────────────── 三つの段階 ──
# 抹茶側の LV_JA と同じ形（タグ, 短い名, 副題）
STAGE_LABEL = {
    "ja": {1: ("LV.1", "急須で淹れる", "一杯の味を決める道具"),
           2: ("LV.2", "客をもてなす", "淹れた茶を客の前へ"),
           3: ("LV.3", "席を整える", "湯を沸かし、卓上をしつらえる")},
    "en": {1: ("LV.1", "Brew with a kyūsu", "The pieces that decide one cup"),
           2: ("LV.2", "Serve a guest", "Carry the tea to the guest"),
           3: ("LV.3", "Compose the table", "Boil the water, set the scene")},
    "fr": {1: ("LV.1", "Infuser au kyūsu", "Les pièces qui décident d’une tasse"),
           2: ("LV.2", "Servir un invité", "Porter le thé devant l’invité"),
           3: ("LV.3", "Composer la table", "Chauffer l’eau, dresser la scène")},
    "zh": {1: ("LV.1", "用急須泡茶", "決定一杯滋味的道具"),
           2: ("LV.2", "款待客人", "把茶端到客人面前"),
           3: ("LV.3", "佈置茶席", "燒水、擺設桌上的景致")},
}

STAGES = [
    # (level, slugs, {lang: (title, lede, note)})
    (1, ["chashinko", "chago", "kyusu", "hohin", "yuzamashi"], {
        "ja": ("急須で淹れる",
               "葉を量り、湯を冷まし、急須で淹れる。一杯の味を決める道具。台所の湯とこの数点で、今日から始められます。",
               "急須か宝瓶のどちらか一つで十分です。湯冷ましは、なければ湯呑で代用できます。"),
        "en": ("Brew with a kyūsu",
               "Measure the leaf, cool the water, brew in the pot. These decide the taste of one cup — and with kitchen hot water they are all you need to begin today.",
               "One pot is enough — a kyūsu or a hōhin. A plain cup can stand in for the yuzamashi at first."),
        "fr": ("Infuser au kyūsu",
               "Doser les feuilles, laisser tiédir l’eau, infuser dans la théière. Ces pièces décident du goût d’une tasse ; avec l’eau chaude de la cuisine, elles suffisent pour commencer aujourd’hui.",
               "Une seule théière suffit, kyūsu ou hōhin. Au début, une simple tasse peut remplacer le yuzamashi."),
        "zh": ("用急須泡茶",
               "量葉、涼水、用急須泡。這幾件決定一杯茶的滋味。有廚房的熱水和這幾樣，今天就能開始。",
               "急須或寶瓶擇一即可。沒有湯冷，先用茶杯代替也行。"),
    }),
    (2, ["senchawan", "chataku", "bon", "kensui"], {
        "ja": ("客をもてなす",
               "淹れた茶を客の前へ運ぶ道具。小さな碗の白で茶の色を見せ、茶托に載せて差し出します。",
               "煎茶碗は五客か六客の揃いが基本。茶托は錫が好まれますが、木や竹でも構いません。"),
        "en": ("Serve a guest",
               "The pieces that carry the tea to the guest: a small white-lined cup to show the colour, set on a saucer and offered.",
               "Cups usually come in sets of five or six. Tin is the classic saucer, but wood or bamboo serve just as well."),
        "fr": ("Servir un invité",
               "Les pièces qui portent le thé devant l’invité : une petite tasse au fond blanc pour montrer la couleur, posée sur une soucoupe.",
               "Les tasses vont par cinq ou six. L’étain est la soucoupe classique, mais le bois ou le bambou conviennent aussi."),
        "zh": ("款待客人",
               "把泡好的茶端到客人面前的道具。小碗內的白，襯出茶色；放在茶托上奉出。",
               "煎茶碗以五客或六客成套為基本。茶托以錫為佳，木或竹亦可。"),
    }),
    (3, ["ryoro", "suichu", "kinto", "binshiki", "teiran", "chabitsu", "robyo", "kikyoku", "koro"], {
        "ja": ("席を整える",
               "湯を沸かし、道具を並べ、席をしつらえる。文人の卓上の景色を、ひと組の道具でつくる段階です。",
               "涼炉とボーフラは、卓上で湯を沸かすための一対。提籃や茶櫃は道具を納めて運ぶ器で、席の格を静かに決めます。"),
        "en": ("Compose the table",
               "Boil the water, lay out the pieces, set the scene: the literati tabletop, made from one set of utensils.",
               "The ryōro and bōfura are a pair for boiling water on the table. Baskets and chests hold and carry the set, and quietly set the tone of the room."),
        "fr": ("Composer la table",
               "Chauffer l’eau, disposer les pièces, dresser la scène : la table des lettrés, composée d’un seul service.",
               "Le ryōro et le bōfura forment la paire qui chauffe l’eau sur la table. Paniers et coffres rangent et transportent le service, et donnent discrètement le ton."),
        "zh": ("佈置茶席",
               "燒水、擺道具、佈置茶席。用一組道具，做出文人桌上的景致。",
               "涼爐與保夫良是桌上燒水的一對。提籃、茶櫃用來收納與搬運，靜靜地決定茶席的格調。"),
    }),
]

# ─────────────────────────────────────────── 煎茶の道具 8点（札） ──
# name は訳さない。sub は各言語で「読み／ローマ字 — 英名」に相当する副題。
TOOLS = [
    dict(no="01", slug="kyusu", level=1, name="急須", romaji="Kyūsu",
         sub={"ja": "きゅうす / Kyūsu — Side-handle Teapot", "en": "急須 — Side-handle Teapot",
              "fr": "急須 — Théière à poignée latérale", "zh": "急須 — Kyūsu"},
         lede={"ja": "茶葉に湯を注ぎ、茶を淹れて注ぐ小さな土瓶。煎茶の道具はこの一つから始まります。",
               "en": "A small clay pot for steeping and pouring. Every sencha set begins with this one piece.",
               "fr": "Une petite théière de terre pour infuser et verser. Tout service de sencha commence par cette pièce.",
               "zh": "把熱水注入茶葉、泡好再倒出的小土瓶。煎茶的道具，從這一件開始。"}),
    dict(no="02", slug="hohin", level=1, name="宝瓶", romaji="Hōhin",
         sub={"ja": "ほうひん / Hōhin — Handleless Pot", "en": "宝瓶 — Handleless Pot",
              "fr": "宝瓶 — Théière sans anse", "zh": "寶瓶 — Hōhin"},
         lede={"ja": "取っ手のない平たい急須。ぬるめの湯で、玉露や上級の煎茶をゆっくり淹れます。",
               "en": "A flat pot with no handle, held in the palm. For gyokuro and fine sencha, brewed slowly in cooler water.",
               "fr": "Une théière plate sans anse, tenue dans la paume. Pour le gyokuro et les senchas fins, infusés lentement à l’eau tiède.",
               "zh": "沒有把手的扁平急須。用溫一點的水，慢慢泡玉露或上等煎茶。"}),
    dict(no="03", slug="yuzamashi", level=1, name="湯冷まし", romaji="Yuzamashi",
         sub={"ja": "ゆざまし / Yuzamashi — Water Cooler", "en": "湯冷まし — Water Cooler",
              "fr": "湯冷まし — Refroidisseur d’eau", "zh": "湯冷 — Yuzamashi"},
         lede={"ja": "沸いた湯を一度移して、茶に合う温度まで下げる器。煎茶のおいしさの要です。",
               "en": "A lipped bowl into which boiled water is poured to cool to the right temperature — the key to good sencha.",
               "fr": "Un bol à bec où l’on verse l’eau bouillie pour la laisser tiédir à la bonne température, la clé d’un bon sencha.",
               "zh": "把燒開的水先倒進來，降到適合茶的溫度。煎茶好喝的關鍵。"}),
    dict(no="04", slug="senchawan", level=2, name="煎茶碗", romaji="Senchawan",
         sub={"ja": "せんちゃわん / Senchawan — Sencha Cup", "en": "煎茶碗 — Sencha Cup",
              "fr": "煎茶碗 — Tasse à sencha", "zh": "煎茶碗 — Senchawan"},
         lede={"ja": "掌に収まる小さな茶碗。内側の白で、茶の色を見ます。五客・六客の揃いで使います。",
               "en": "A cup small enough to sit in the palm. Its white interior shows the colour of the tea. Used in sets of five or six.",
               "fr": "Une tasse qui tient dans la paume. Son intérieur blanc révèle la couleur du thé. Par services de cinq ou six.",
               "zh": "一手可握的小茶碗。以內側的白，看茶的顏色。五客、六客成套使用。"}),
    dict(no="05", slug="chataku", level=2, name="茶托", romaji="Chataku",
         sub={"ja": "ちゃたく / Chataku — Saucer", "en": "茶托 — Saucer",
              "fr": "茶托 — Soucoupe", "zh": "茶托 — Chataku"},
         lede={"ja": "煎茶碗をのせて客に出す台。錫、木、銀、竹と、素材で表情が変わります。",
               "en": "The saucer on which the cup is offered. Tin, wood, silver or bamboo — each material changes the mood.",
               "fr": "La soucoupe sur laquelle on présente la tasse. Étain, bois, argent ou bambou : chaque matière change l’expression.",
               "zh": "放煎茶碗奉給客人的托。錫、木、銀、竹，材質不同，表情各異。"}),
    dict(no="06", slug="chashinko", level=1, name="茶心壺", romaji="Chashinko",
         sub={"ja": "ちゃしんこ / Chashinko — Tea Caddy", "en": "茶心壺 — Tea Caddy",
              "fr": "茶心壺 — Boîte à thé", "zh": "茶心壺 — Chashinko"},
         lede={"ja": "茶葉をしまっておく錫の壺。煎茶の席では、ここから葉を取り出します。",
               "en": "A tin caddy for the leaf. At a sencha gathering, the leaves are taken from here.",
               "fr": "Une boîte d’étain pour les feuilles. Lors d’une réunion de sencha, c’est d’ici que l’on prend le thé.",
               "zh": "收放茶葉的錫壺。煎茶席上，從這裡取葉。"}),
    dict(no="07", slug="chago", level=1, name="茶合・茶則", romaji="Chagō / Chasoku",
         sub={"ja": "ちゃごう・ちゃそく / Chagō — Leaf Scoop", "en": "茶合・茶則 — Leaf Scoop",
              "fr": "茶合・茶則 — Cuillère à thé", "zh": "茶合・茶則 — Chagō"},
         lede={"ja": "茶葉を量り、急須へ移す道具。竹を割って作ったものが多く、銘を持つこともあります。",
               "en": "Measures the leaf and carries it to the pot. Usually a split length of bamboo; some bear poetic names.",
               "fr": "Dose les feuilles et les porte à la théière. Le plus souvent un bambou fendu ; certains portent un nom poétique.",
               "zh": "量取茶葉、移入急須的道具。多以剖竹製成，有的還有銘。"}),
    dict(no="08", slug="ryoro", level=3, name="涼炉・ボーフラ", romaji="Ryōro / Bōfura",
         sub={"ja": "りょうろ・ぼーふら / Ryōro — Brazier & Kettle", "en": "涼炉・ボーフラ — Brazier & Kettle",
              "fr": "涼炉・ボーフラ — Réchaud et bouilloire", "zh": "涼爐・保夫良 — Ryōro"},
         lede={"ja": "炭火をおこす小さな炉と、その上で湯を沸かす土瓶。文人の卓上の景色です。",
               "en": "A small clay brazier and the earthenware kettle that sits on it — the literati tabletop in miniature.",
               "fr": "Un petit réchaud de terre et la bouilloire qui s’y pose : la table des lettrés en miniature.",
               "zh": "起炭火的小爐，與架在上面燒水的土瓶。文人桌上的景致。"}),
]

# ─────────────────────────────────────────── そのほかの道具 10点 ──
OTHERS = [
    dict(slug="suichu", level=3, name="水注", romaji="Suichū",
         sub={"ja": "すいちゅう / Suichū — Water Pitcher", "en": "水注 — Water Pitcher", "fr": "水注 — Pichet à eau", "zh": "水注 — Suichū"},
         desc={"ja": "水を入れておき、ボーフラに差す器。", "en": "Holds fresh water to top up the kettle.",
               "fr": "Contient l’eau fraîche pour remplir la bouilloire.", "zh": "盛水備用、添入保夫良的器皿。"}),
    dict(slug="kensui", level=2, name="建水", romaji="Kensui",
         sub={"ja": "けんすい / Kensui — Waste-water Bowl", "en": "建水 — Waste-water Bowl", "fr": "建水 — Bol à eaux usées", "zh": "建水 — Kensui"},
         desc={"ja": "器を温めた湯や、残った茶を捨てる器。「こぼし」とも。", "en": "Receives the water used to warm the cups and any tea left over. Also called koboshi.",
               "fr": "Reçoit l’eau qui a chauffé les tasses et le thé restant. Dit aussi koboshi.", "zh": "倒掉溫杯的水和剩茶的器皿。也叫「こぼし」。"}),
    dict(slug="kinto", level=3, name="茶巾・巾筒", romaji="Chakin / Kintō",
         sub={"ja": "ちゃきん・きんとう / Kintō — Cloth & Holder", "en": "茶巾・巾筒 — Cloth & Holder", "fr": "茶巾・巾筒 — Linge et étui", "zh": "茶巾・巾筒 — Kintō"},
         desc={"ja": "器を拭く布と、それを納める筒。", "en": "The cloth for wiping the cups, and the small tube that holds it.",
               "fr": "Le linge qui essuie les tasses, et le petit étui qui le range.", "zh": "擦拭器皿的布，和收納它的筒。"}),
    dict(slug="binshiki", level=3, name="瓶敷", romaji="Binshiki",
         sub={"ja": "びんしき / Binshiki — Pot Stand", "en": "瓶敷 — Pot Stand", "fr": "瓶敷 — Dessous de théière", "zh": "瓶敷 — Binshiki"},
         desc={"ja": "沸いたボーフラや急須を下ろす敷物。", "en": "A mat or stand on which the hot kettle or pot is set down.",
               "fr": "Un support sur lequel on pose la bouilloire ou la théière chaude.", "zh": "放置燒開的保夫良或急須的墊子。"}),
    dict(slug="bon", level=2, name="盆", romaji="Bon",
         sub={"ja": "ぼん / Bon — Tray", "en": "盆 — Tray", "fr": "盆 — Plateau", "zh": "盆 — Bon"},
         desc={"ja": "煎茶碗と茶托を客の前へ運ぶ。", "en": "Carries the cups and saucers to the guests.",
               "fr": "Porte les tasses et les soucoupes devant les invités.", "zh": "把煎茶碗和茶托端到客人面前。"}),
    dict(slug="teiran", level=3, name="提籃", romaji="Teiran",
         sub={"ja": "ていらん / Teiran — Carrying Basket", "en": "提籃 — Carrying Basket", "fr": "提籃 — Panier de transport", "zh": "提籃 — Teiran"},
         desc={"ja": "道具一式を納めて持ち運ぶ籠。野外で茶を楽しむための道具。", "en": "A basket that holds the whole set for carrying — made for tea out of doors.",
               "fr": "Un panier qui range tout le service pour le transporter : fait pour le thé en plein air.", "zh": "收納整套道具、提著走的籃子。為了在戶外喝茶而生。"}),
    dict(slug="chabitsu", level=3, name="茶櫃", romaji="Chabitsu",
         sub={"ja": "ちゃびつ / Chabitsu — Tea Chest", "en": "茶櫃 — Tea Chest", "fr": "茶櫃 — Coffre à thé", "zh": "茶櫃 — Chabitsu"},
         desc={"ja": "急須や碗をしまっておく櫃。家の茶の間の道具。", "en": "A chest for keeping the pot and cups — the tea-room furniture of the home.",
               "fr": "Un coffre où l’on range théière et tasses : le meuble à thé de la maison.", "zh": "收放急須和茶碗的櫃子。家中茶間的道具。"}),
    dict(slug="robyo", level=3, name="炉屏", romaji="Robyō",
         sub={"ja": "ろびょう / Robyō — Small Screen", "en": "炉屏 — Small Screen", "fr": "炉屏 — Petit paravent", "zh": "爐屏 — Robyō"},
         desc={"ja": "涼炉の後ろに立てる小さな屏風。", "en": "A small folding screen stood behind the brazier.",
               "fr": "Un petit paravent dressé derrière le réchaud.", "zh": "立在涼爐後面的小屏風。"}),
    dict(slug="kikyoku", level=3, name="器局", romaji="Kikyoku",
         sub={"ja": "ききょく / Kikyoku — Utensil Cabinet", "en": "器局 — Utensil Cabinet", "fr": "器局 — Cabinet à ustensiles", "zh": "器局 — Kikyoku"},
         desc={"ja": "道具を納め、席に据える棚や箱。", "en": "A shelf or cabinet that holds the utensils and stands in the room.",
               "fr": "Une étagère ou un cabinet qui range les ustensiles et prend place dans la pièce.", "zh": "收納道具、安置在席上的架或箱。"}),
    dict(slug="koro", level=3, name="香炉・花器", romaji="Kōro / Kaki",
         sub={"ja": "こうろ・かき / Kōro — Incense & Flowers", "en": "香炉・花器 — Incense & Flowers", "fr": "香炉・花器 — Encens et fleurs", "zh": "香爐・花器 — Kōro"},
         desc={"ja": "席を整える。煎茶の席では文人画や盆栽も飾られました。", "en": "Dress the room. Literati paintings and bonsai were also displayed at sencha gatherings.",
               "fr": "Habillent la pièce. Aux réunions de sencha, on exposait aussi peintures de lettrés et bonsaï.", "zh": "佈置茶席。煎茶席上也會擺文人畫和盆栽。"}),
]

BY_SLUG = {t["slug"]: t for t in TOOLS + OTHERS}


# ─────────────────────────────────────────── HTML ──
def switch(lang):
    """「抹茶｜煎茶」の二択。href は #matcha / #sencha。
    JS が無くてもページ内リンクとして害が無く、URL で状態を共有できる。"""
    u = UI[lang]
    def a(key, cur):
        sub = f' <span>{u[key + "_sub"]}</span>' if u[key + "_sub"] else ""
        return (f'<a href="#{key}" data-tea-pick="{key}"'
                + (' aria-current="true"' if cur else "") + f'>{u[key]}{sub}</a>')
    return (f'<nav class="tea-sw reveal" aria-label="{u["aria"]}">'
            + a("matcha", True) + a("sencha", False) + '</nav>')


def _badge(lang, level):
    tag, short, _ = STAGE_LABEL[lang][level]
    return f'<span class="lv-badge lv{level}"><b>{tag}</b>{short}</span>'


def _stages(lang):
    blocks = ""
    for level, slugs, texts in STAGES:
        tag, _short, sub = STAGE_LABEL[lang][level]
        title, lede, note = texts[lang]
        chips = "".join(f'<span class="lv-chip plain">{BY_SLUG[s]["name"]}</span>' for s in slugs)
        blocks += (f'<div class="lv-card lv{level} reveal">'
                   f'<div class="lv-head"><span class="lv-tag">{tag}</span>'
                   f'<div><h3>{title}</h3><p class="lv-sub">{sub}</p></div></div>'
                   f'<p class="lv-lede">{lede}</p>'
                   f'<div class="lv-chips">{chips}</div>'
                   f'<p class="lv-note">{note}</p></div>')
    return f'<div class="lv-grid">{blocks}</div>'


def _card(lang, t):
    # 詳細ページはまだ無いので <a> ではなく <div>。番号と副題は抹茶側と同じ位置。
    return (f'<div class="tool-card plain reveal" data-slug="{t["slug"]}">'
            f'<span class="tool-num">{t["no"]}</span>{_badge(lang, t["level"])}'
            f'<div class="tool-art">{ico(t["slug"])}</div>'
            f'<h3 class="tool-name">{t["name"]}</h3>'
            f'<p class="tool-yomi">{t["sub"][lang]}</p>'
            f'<p class="tool-desc">{t["lede"][lang]}</p>'
            f'<p class="tool-more soon">{UI[lang]["soon"]}</p></div>')


def _minor(lang, m):
    return (f'<div class="tool-card plain reveal" data-slug="{m["slug"]}">'
            f'{_badge(lang, m["level"])}'
            f'<div class="tool-art">{ico(m["slug"])}</div>'
            f'<h3 class="tool-name">{m["name"]}</h3>'
            f'<p class="tool-yomi">{m["sub"][lang]}</p>'
            f'<p class="tool-desc">{m["desc"][lang]}</p></div>')


def block(lang):
    """煎茶側の全部（段階3枚＋道具8点＋そのほか10点）。data-tea="sencha" で包む。"""
    u = UI[lang]
    return (f'<div data-tea="sencha">'
            f'<div class="section-head reveal" style="margin-top:8px">'
            f'<p class="section-kicker">{u["lv_kicker"]}</p>'
            f'<h2 class="section-title">{u["lv_title"]}</h2><div class="rule"></div>'
            f'<p class="section-lede">{u["lv_lede"]}</p></div>'
            + _stages(lang)
            + f'<div class="cat-head reveal"><h2>{u["main_h"]}</h2><span class="en-sub">{u["main_sub"]}</span></div>'
            f'<div class="tools-grid">{"".join(_card(lang, t) for t in TOOLS)}</div>'
            f'<div class="cat-head reveal"><h2>{u["other_h"]}</h2><span class="en-sub">{u["other_sub"]}</span></div>'
            f'<div class="tools-grid">{"".join(_minor(lang, m) for m in OTHERS)}</div>'
            '</div>')


HOME_LEDE = {
    "ja": "煎茶の道具の代表八点。急須ひとつから始まります。くわしい紹介は、順に整えていきます。",
    "en": "The eight principal utensils of sencha. It all begins with a single kyūsu; detail pages will follow.",
    "fr": "Les huit pièces principales du sencha. Tout commence par un seul kyūsu ; les fiches détaillées suivront.",
    "zh": "煎茶的八件主要道具。從一把急須開始。詳細介紹陸續整理中。",
}


def home_lede(lang):
    """トップ「まずは、八つの道具から」の説明文（煎茶側）。抹茶側の文は data-tea="matcha" で包む。"""
    return f'<p class="section-lede" data-tea="sencha">{HOME_LEDE[lang]}</p>'


def home_grid(lang):
    """トップ用：煎茶の道具8点の札だけ。段階札や「そのほか」は出さない。"""
    return (f'<div class="tools-grid" data-tea="sencha">'
            f'{"".join(_card(lang, t) for t in TOOLS)}</div>')


if __name__ == "__main__":
    for lang in UI:
        html = block(lang)
        assert html.count('class="tool-card') == len(TOOLS) + len(OTHERS)
    for s in sum((st[1] for st in STAGES), []):
        assert s in BY_SLUG, s
    print("ok:", len(TOOLS), "tools,", len(OTHERS), "others, 4 langs")
