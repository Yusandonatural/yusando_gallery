# -*- coding: utf-8 -*-
"""繁體中文版——五個主要頁面。

各項道具的細部頁面與長篇文章目前僅有日文版與英文版，因此相關連結皆指向英文版，
並以「EN」標記。用語依日文原名為主：漢字直接沿用，必要時補上說明，
純日語的讀音則附上羅馬字。
"""
import os
from gen import ROOT
from icons import sprite as ico_sprite, icon as ico, parts_icon


def w(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)
    print("wrote", path)


def en(path, depth=1):
    return "../" * depth + "en/" + path



# The Japanese faces used elsewhere lack a number of Traditional-Chinese
# glyphs (價, 們, 灣 …), so the browser was substituting them one character at
# a time and the line went visibly uneven. These pages load Noto TC instead.
FONTS_ZH = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600&family=Noto+Sans+TC:wght@300;400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">'''

EN_TAG = '<span class="en-only" title="此頁目前提供英文版">EN</span>'


# ------------------------------------------------------------------ shell --
def shell_zh(title, desc, body, root="../", current=""):
    def nav(href, label, key):
        cls = ' class="current"' if current == key else ''
        return f'<a href="{root}zh/{href}"{cls}>{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS_ZH}
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body>
{ico_sprite()}
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{root}zh/index.html" aria-label="Cerendipity — 悠三堂古美術藝廊">
      <span class="brand-word"><img class="brand__c" src="{root}assets/cerendipity-symbol-gold.svg" alt="C" width="100" height="100"><span>erendipity</span></span>
      <span class="brand-ja">悠三堂古美術藝廊</span>
    </a>
    <button class="nav-toggle" aria-label="選單" onclick="document.querySelector('.nav-links').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links">
      {nav("index.html","首頁","home")}
      {nav("tools.html","茶道具一覽","tools")}
      {nav("setup.html","爐與風爐","setup")}
      {nav("guide.html","點前的流程","guide")}
      {nav("articles/index.html","專文","articles")}
      {nav("index.html#about","關於本站","about")}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="f-inner">
    <div>
      <p class="f-mark">悠三堂古美術藝廊 <span class="en-sub">YUSANDO ANTIQUE GALLERY</span></p>
      <p class="f-note">均一價的二手日本茶道具。<br>讓您憑心動選擇，而非憑價格。</p>
    </div>
    <nav class="f-nav">
      <a href="{root}zh/index.html">首頁</a>
      <a href="{root}zh/tools.html">茶道具一覽</a>
      <a href="{root}zh/setup.html">爐與風爐</a>
      <a href="{root}zh/guide.html">點前的流程</a>
      <a href="{root}zh/articles/index.html">專文</a>
      <a href="{root}zh/index.html#about">關於本站</a>
    </nav>
  </div>
  <p class="f-copy">© 2026 YUSANDO ANTIQUE GALLERY — 本站為展示用草稿，目前尚未開放線上販售。</p>
</footer>
<script src="{root}js/site.js"></script>
</body>
</html>'''


# ------------------------------------------------------------------- data --
TOOLS_ZH = [
 dict(slug="chawan", level=1, name="茶碗", yomi="chawan", zh="抹茶碗", num="01",
   lede="點茶與飲茶所用的碗。最能透露主人品味的一件道具，每逢節令便重新挑選。"),
 dict(slug="chasen", level=1, name="茶筅", yomi="chasen", zh="竹製打茶器", num="02",
   lede="以一整支竹子削成八十至一百二十支細穗。屬於消耗品，需要定期更換——茶湯的細泡由它決定。"),
 dict(slug="chashaku", level=1, name="茶杓", yomi="chashaku", zh="舀抹茶的竹匙", num="03",
   lede="一片薄竹，以蒸氣彎出弧度。茶人親手削製並為它取「銘」，是所有道具中最私密的一件。"),
 dict(slug="natsume", level=1, name="棗", yomi="natsume", zh="薄茶用漆製茶器", num="04",
   lede="盛裝薄茶抹茶的漆器，因形似棗子的果實而得名。"),
 dict(slug="kama", level=2, name="釜", yomi="kama", zh="鐵製燒水釜", num="05",
   lede="煮水的鐵釜。釜中水聲被稱作「松風」，為一室的靜默定下基調。"),
 dict(slug="hishaku", level=2, name="柄杓", yomi="hishaku", zh="竹製水杓", num="06",
   lede="舀水用的竹杓。杓斗的大小與杓柄末端的削法，在冬夏之間各有不同。"),
 dict(slug="fukusa", level=2, name="帛紗", yomi="fukusa", zh="絲質方巾", num="07",
   lede="主人繫在腰間的絲質方巾。摺帛紗、以之「清」拭道具，正是點前的開端。"),
 dict(slug="mizusashi", level=2, name="水指", yomi="mizusashi", zh="冷水罐", num="08",
   lede="盛裝冷水的罐，用以調節釜中水溫、涮洗茶碗。冬用陶器，夏則多見玻璃或淺色炻器。"),
]

MINOR_ZH = [
 dict(slug="chaire", level=1, name="茶入", yomi="chaire", zh="濃茶用陶製茶器",
   desc="盛裝濃茶抹茶的小陶罐，收在名為「仕覆」的絲袋中，配象牙蓋。地位在棗之上。"),
 dict(slug="kensui", level=2, name="建水", yomi="kensui", zh="廢水器",
   desc="承接涮洗的廢水。又稱「零」（koboshi），始終低調地待在客人視線之外。"),
 dict(slug="futaoki", level=2, name="蓋置", yomi="futaoki", zh="釜蓋與杓的擱架",
   desc="安放釜蓋與柄杓的小座。最素樸者為一截切竹，講究時則用青瓷或彩繪瓷。"),
 dict(slug="kogo", level=3, name="香合", yomi="kōgō", zh="香盒",
   desc="盛放炭點前所用的香。爐的季節用陶製香合盛練香，風爐的季節則用漆器盛白檀。"),
 dict(slug="hanaire", level=3, name="花入", yomi="hanaire", zh="花器",
   desc="插茶花的器皿，取竹、青瓷或伊賀燒。利休教導：「花要插得如同它長在野地裡一般。」"),
 dict(slug="kakemono", level=3, name="掛物", yomi="kakemono", zh="掛軸",
   desc="懸於床之間的掛軸。以禪語一行書為最上，利休曾說「道具之中無一先於掛物」。"),
 dict(slug="furo", level=2, name="風爐", yomi="furo", zh="可移動的爐",
   desc="五月至十月所用的可移動火爐，材質有唐銅、土與鐵；整理其中的灰形也是主人的功夫之一。"),
 dict(slug="kashiki", level=2, name="菓子器", yomi="kashiki", zh="盛點心的器皿",
   desc="盛裝茶前點心的器皿：濕點心用多層的「緣高」，乾點心用盤。點心本身也是茶的一部分。"),
 dict(slug="ro", level=3, name="爐", yomi="ro", zh="嵌入地板的火爐",
   desc="十一月至四月切入榻榻米中的火爐。切出一方爐，一個房間才成為茶室。"),
 dict(slug="sumitori", level=3, name="炭斗", yomi="sumitori", zh="炭籃",
   desc="炭點前時盛炭的籃子，內附火箸、羽箒、釜環與香合。"),
 dict(slug="haboki", level=3, name="羽箒", yomi="habōki", zh="羽毛刷",
   desc="以鶴、鷹或雁的三支羽毛紮成，用來拂去爐緣的灰。爐與風爐所用的紮法不同。"),
 dict(slug="hibashi", level=3, name="火箸", yomi="hibashi", zh="金屬炭夾",
   desc="夾炭用的金屬長箸：爐用者較長，風爐用者較短，箸頭多有雕飾。"),
 dict(slug="haiki", level=3, name="灰器", yomi="haiki", zh="盛灰的器皿",
   desc="盛濕灰的無釉器皿，連同灰匙一併端出，於炭點前時將灰撒入爐中。"),
 dict(slug="chatsubo", level=3, name="茶壺", yomi="chatsubo", zh="葉茶罐",
   desc="貯藏葉茶的大罐。十一月的「口切」茶會上割開封口，將葉茶碾成抹茶——茶人的一年由此開始。"),
]

DETAIL_SLUGS_ZH = {t["slug"] for t in TOOLS_ZH}
ALL_ZH = {t["slug"]: t for t in TOOLS_ZH + MINOR_ZH}

LV_ZH = {
 1: ("LV.1", "今天就點一碗", "幾件道具與一壺熱水"),
 2: ("LV.2", "款待客人", "在客人面前點茶"),
 3: ("LV.3", "經營一間茶室", "連場域本身一併安排"),
}


def lv_badge_zh(level):
    tag, short, _ = LV_ZH[level]
    return f'<span class="lv-badge lv{level}"><b>{tag}</b>{short}</span>'


LV_INTRO_ZH = [
 (1, "在家享用抹茶",
  "幾件道具，加上一壺熱水，今天下午就能點出一碗茶。從這裡起步，已然足夠。",
  ["chawan", "chasen", "chashaku", "natsume", "chaire"],
  "薄茶盛於棗，濃茶盛於茶入。再添一條麻質茶巾與一只茶筅休息座便已齊備；點心用家中任何一只盤子都無妨。"),
 (2, "舉辦一場茶會",
  "點前所用的道具——從燒水開始，在客人面前點茶。備齊這些，您就能作東辦一場自己的茶會。",
  ["furo", "kama", "hishaku", "fukusa", "mizusashi", "kensui", "futaoki", "kashiki"],
  "火源用電熱器完全可行。先從風爐、釜、水指與建水備起，其餘再慢慢添置。"),
 (3, "經營一間茶室",
  "床之間的佈置，與爐中的火。節令在此顯形，整個房間成為一整篇構成。",
  ["ro", "kakemono", "hanaire", "kogo", "sumitori", "haboki", "hibashi", "haiki", "chatsubo"],
  "掛物、花入、香合為床之間三件。炭斗、羽箒、火箸與灰器構成炭道具，香合亦列其中。"),
]


def lv_section_zh():
    blocks = ""
    for level, title, lede, slugs, note in LV_INTRO_ZH:
        tag, short, sub = LV_ZH[level]
        names = "".join(
            f'<a class="lv-chip" href="{en("tools/" + s + ".html")}">'
            f'{ALL_ZH[s]["name"]}{EN_TAG}</a>'
            if s in DETAIL_SLUGS_ZH else
            f'<span class="lv-chip plain">{ALL_ZH[s]["name"]}</span>'
            for s in slugs)
        blocks += (f'<div class="lv-card lv{level} reveal">'
                   f'<div class="lv-head"><span class="lv-tag">{tag}</span>'
                   f'<div><h3>{title}</h3><p class="lv-sub">{sub}</p></div></div>'
                   f'<p class="lv-lede">{lede}</p>'
                   f'<div class="lv-chips">{names}</div>'
                   f'<p class="lv-note">{note}</p></div>')
    return f'<div class="lv-grid">{blocks}</div>'


def card_zh(t):
    return f'''<a class="tool-card reveal" href="{en("tools/" + t["slug"] + ".html")}">
  <span class="tool-num">{t["num"]}</span>
  {lv_badge_zh(t["level"])}
  <div class="tool-art">{ico(t["slug"])}</div>
  <h3 class="tool-name">{t["name"]}</h3>
  <p class="tool-yomi">{t["yomi"]} — {t["zh"]}</p>
  <p class="tool-desc">{t["lede"]}</p>
  <p class="tool-more">閱讀全文（英文）→</p>
</a>'''


def minor_card_zh(m):
    return f'''<div class="tool-card plain reveal">
  {lv_badge_zh(m["level"])}
  <div class="tool-art">{ico(m["slug"])}</div>
  <h3 class="tool-name">{m["name"]}</h3>
  <p class="tool-yomi">{m["yomi"]} — {m["zh"]}</p>
  <p class="tool-desc">{m["desc"]}</p>
</div>'''


# ------------------------------------------------------------------ index --
TRANSLATED_ZH = set(['chawan-types.html', 'history.html', 'chasen-types.html', 'kama-types.html', 'chaire-types.html', 'natsume-types.html'])

ARTICLES_ZH = [
 ("chawan-types.html", "指南", "茶碗的種類",
  "樂燒、萩燒與唐津；天目與井戶。依系譜、窯口與器形整理，供挑選時參照。"),
 ("kama-types.html", "指南", "釜的種類",
  "蘆屋、天明與京釜，以及從真形到雲龍的各種形制。"),
 ("chaire-types.html", "指南", "茶入的種類",
  "肩衝、茄子、文琳——從器形與仕覆讀懂濃茶用的茶入。"),
 ("natsume-types.html", "指南", "棗的種類",
  "大小、漆的塗法，以及薄茶器這一整個家族。"),
 ("chasen-types.html", "指南", "茶筅的種類",
  "穗數、竹色與流派。如何挑選茶筅，為初學者淺白說明。"),
 ("history.html", "歷史", "茶道的歷史",
  "一碗自中國傳來的藥飲，如何在千年之間成為一條「道」。分七個時代的編年。"),
 ("evolution.html", "歷史", "茶道具的演變",
  "唐物、見立，以及日本自製的器物——透過六件道具追溯五百年。"),
 ("sekki.html", "節令", "二十四節氣與茶道具",
  "節令的花、茶杓的銘、茶碗與茶器的紋樣——整個茶的一年，逐節氣細說。"),
]


def article_cards_zh(depth=1):
    # 已譯出的專文連往中文版，尚未譯出者連往英文版，「EN」標記也隨之調整。
    out = ""
    for href, kicker, title, desc in ARTICLES_ZH:
        done = href in TRANSLATED_ZH
        # トップ（depth=1）からは articles/ を挟む。索引（depth=2）からは直接。
        link = (("articles/" + href) if depth == 1 else href) \
            if done else en("articles/" + href, depth)
        tag = "" if done else EN_TAG
        more = "閱讀 →" if done else "閱讀（英文）→"
        out += (f'<a class="article-card reveal" href="{link}">'
                f'<p class="a-kicker">{kicker}</p><h3>{title}{tag}</h3>'
                f'<p>{desc}</p><p class="tool-more">{more}</p></a>')
    return out


import sencha as _sencha  # 抹茶／煎茶の切り替え（A案）

index_body = f'''
<section class="hero">
  <svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M100 18 a82 82 0 1 0 60 26" fill="none" stroke="#2b2a26" stroke-width="10" stroke-linecap="round"/>
  </svg>
  <div class="hero-inner">
    <p class="hero-kicker">均一價的二手茶道具 — 均一価格の中古茶道具ポータル</p>
    <h1 class="hero-title">選那件<br>讓您心動的。</h1>
    <p class="hero-sub">以<strong>均一價</strong>提供二手日本茶道具，初入門也能安心親近。<br>不必再揣測價格，只要挑您喜歡的那一件。</p>
    <p class="hero-brand-note"><b>Cerendipity</b> ＝ Ceramic（陶瓷）× Serendipity（喜悅的偶然）。<br>享受與器物偶然相遇的悠三堂茶道具部門。<br>把這份相遇帶進生活，日子也隨之豐富起來。</p>
    <div class="hero-cta">
      <a class="btn solid" href="tools.html">瀏覽茶道具</a>
      <a class="btn" href="guide.html">一碗茶是怎麼點成的</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="intro-grid">
    <div class="reveal">
      <p class="intro-tate">喜歡，<br>就是足夠的理由。<small>— 悠三堂古美術藝廊</small></p>
    </div>
    <div class="intro-text reveal">
      <p class="section-kicker" style="text-align:left;text-indent:0">關於本站</p>
      <p>買茶道具時最難的一關，往往是<strong>價格</strong>。兩只看起來相似的茶碗，可能是三千日圓，也可能是三十萬。沒有練過的眼力，總覺得處處是陷阱——於是多數人連開口詢問都不曾。</p>
      <p>悠三堂古美術藝廊是一個<strong>均一價</strong>的二手茶道具入口。把比價這件事拿掉之後，剩下的只有唯一真正重要的尺度：<strong>這件器物是否讓您心動</strong>。這道釉色、這份在手中的重量——這樣就夠了。</p>
      <p>若能知道它的名字與來歷，樂趣自然更深。因此每件道具我們都以淺白的文字寫下讀音、來歷、各部位名稱與使用方式。艱深的部分，可以慢慢再說。</p>
    </div>
  </div>
</section>

<section class="section reveal arrivals" data-arrivals data-ec-root="../">
  <div class="section-head" style="margin-bottom:34px">
    <p class="section-kicker">新入荷 — NEW ARRIVALS</p>
    <h2 class="section-title">新近入藏的茶道具</h2>
    <div class="rule"></div>
    <p class="section-lede">剛入藏悠三堂藝廊的器物。若有讓您留意的一件，歡迎來信詢問；線上販售將於準備妥當後開放。</p>
  </div>
  <div class="ar-slot">
    <p class="ar-loading">讀取中…</p>
  </div>
</section>

<section class="section" style="background:transparent;padding-top:0">
  <div class="section-head reveal">
    <p class="section-kicker">茶道具</p>
    <h2 class="section-title">先從基本道具開始</h2>
    <div class="rule"></div>
    <p class="section-lede" data-tea="matcha">點前不可或缺的道具。各件的細部頁面（目前為英文）涵蓋來歷、部位、使用方式，以及選購二手時的重點。</p>
    {_sencha.home_lede('zh')}
  </div>
  {_sencha.switch('zh')}
  <div data-tea="matcha">
  <div class="tools-grid">
    {"".join(card_zh(t) for t in TOOLS_ZH)}
  </div>
  </div>
  {_sencha.home_grid('zh')}
  <div style="text-align:center;margin-top:44px">
    <a class="btn" href="tools.html" data-tea-link>查看全部茶道具</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:44px">
    <p class="section-kicker">專文</p>
    <h2 class="section-title">再深入一些</h2>
    <div class="rule"></div>
    <p class="section-lede">這些長篇專文目前提供日文版與英文版。</p>
  </div>
  <div class="article-cards">
    {article_cards_zh()}
  </div>
</section>

<section class="care">
  <div class="section tight">
    <div class="section-head reveal" style="margin-bottom:44px">
      <p class="section-kicker">保養</p>
      <h2 class="section-title">與道具長久相處</h2>
    </div>
    <div class="care-grid reveal">
      <div class="care-cell"><h3>茶碗 <span class="en-sub">CHAWAN</span></h3><p>只用溫水，不用清潔劑。完全乾透後再收進盒中；新的陶器在初次使用前先浸泡一夜。</p></div>
      <div class="care-cell"><h3>茶筅 <span class="en-sub">CHASEN</span></h3><p>以熱水沖洗後，穗朝上自然風乾。放在茶筅休息座上可保持穗形。</p></div>
      <div class="care-cell"><h3>漆器 <span class="en-sub">NATSUME</span></h3><p>切勿用水清洗，只以柔軟乾布擦拭。收進桐箱，避免日照。</p></div>
      <div class="care-cell"><h3>鐵釜 <span class="en-sub">KAMA</span></h3><p>倒空後以餘熱烘乾。內壁的水垢是保護層——切勿刷洗，切勿用皂。</p></div>
    </div>
  </div>
</section>
'''
w("zh/index.html", shell_zh(
  "悠三堂古美術藝廊 — 均一價的二手日本茶道具",
  "以均一價提供二手日本茶道具的入口網站，初入門也能安心親近：各件道具的名稱、來歷、部位與使用方式。",
  index_body, root="../", current="home"))


# ------------------------------------------------------------------ tools --
tools_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">茶道具一覽</p>
    <h2 class="section-title">日本茶道的道具</h2>
    <div class="rule"></div>
    <p class="section-lede">茶之湯的主要道具。設有細部頁面者談得更深——來歷、部位、使用方式，以及選購二手時的重點。</p>
  </div>
  {_sencha.switch('zh')}
  <div data-tea="matcha">

  <div class="section-head reveal" style="margin-top:8px">
    <p class="section-kicker">如何備齊 — 三個層級</p>
    <h2 class="section-title">用三個層級來思考</h2>
    <div class="rule"></div>
    <p class="section-lede">不必一次備齊。您是想今天就喝上一碗茶、想邀人來家中，還是想安排整個場域？答案不同，所需的道具也不同。</p>
  </div>
  {lv_section_zh()}

  <div class="cat-head reveal"><h2>點前的道具</h2><span class="en-sub">設有細部頁面</span></div>
  <div class="tools-grid">
    {"".join(card_zh(t) for t in TOOLS_ZH)}
  </div>
  <div class="cat-head reveal"><h2>其他道具</h2><span class="en-sub">概述</span></div>
  <div class="tools-grid">
    {"".join(minor_card_zh(m) for m in MINOR_ZH)}
  </div>
  </div>
  {_sencha.block('zh')}
</section>
'''
w("zh/tools.html", shell_zh(
  "茶道具一覽 — 日本茶道的道具 | 悠三堂古美術藝廊",
  "二十二件日本茶道具的名稱、讀音與作用，依三個層級分類：在家喝抹茶、舉辦茶會、經營一間茶室。",
  tools_body, root="../", current="tools"))


# ------------------------------------------------------------------ guide --
guide_steps_zh = [
 ("1", "清",
  f'以<a href="{en("tools/fukusa.html")}">帛紗</a>拭淨茶器與茶杓，再用熱水涮過<a href="{en("tools/chasen.html")}">茶筅</a>與<a href="{en("tools/chawan.html")}">茶碗</a>。'),
 ("2", "量",
  f'自<a href="{en("tools/natsume.html")}">棗</a>中舀出抹茶入碗——約一杓半，即兩公克。'),
 ("3", "注",
  f'以<a href="{en("tools/hishaku.html")}">柄杓</a>自<a href="{en("tools/kama.html")}">釜</a>中取熱水，緩緩注入。'),
 ("4", "點",
  "茶筅快速而俐落地運行，直到茶湯勻淨、泛起細密的泡沫。"),
 ("5", "奉",
  "將茶碗轉正，使其正面朝向客人，然後奉上。"),
]

guide_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">道具如何運作</p>
    <h2 class="section-title">一碗茶是怎麼點成的</h2>
    <div class="rule"></div>
    <p class="section-lede">每件道具依序被拿起、完成自己的工作，再回到原位。以下是薄茶點前的簡化流程。</p>
  </div>
  <div class="temae-list reveal">
    {"".join(f'<div class="temae-item"><span class="temae-step">{a}</span><div class="temae-body"><h3>{b}</h3><p>{c}</p></div></div>' for a, b, c in guide_steps_zh)}
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:40px">
    <p class="section-kicker">第一套道具</p>
    <h2 class="section-title">最低限度的配備</h2>
    <div class="rule"></div>
  </div>
  <div class="check-grid reveal" style="max-width:820px;margin-left:auto;margin-right:auto">
    <div class="check-cell"><h3>在家點一碗</h3><p>有茶碗、茶筅與茶杓，就足以點出抹茶。廚房的熱水壺與一般茶葉罐即可代替其餘。</p></div>
    <div class="check-cell"><h3>開始上課時</h3><p>再添隨身四件：帛紗、扇子、懷紙與菓子切。顏色與尺寸因流派而異，請先問過老師。</p></div>
    <div class="check-cell"><h3>二手最划算的品項</h3><p>茶碗、茶入、水指與建水的古物市場十分豐富。茶筅與帛紗則建議購買全新品。</p></div>
    <div class="check-cell"><h3>依什麼順序添購</h3><p>不必一次買齊。有銘的茶杓與釜需要練過的眼力——讓您的練習帶著收藏走。</p></div>
  </div>
</section>

<section class="section reveal" style="text-align:center;padding-top:30px">
  <p class="words-quote" style="font-size:clamp(20px,3vw,27px);letter-spacing:.12em;line-height:2">「無名物，<br>則不足以行茶。」</p>
  <p class="en-sub" style="margin-top:16px">— 利休所否定的一種想法</p>
  <p class="section-lede" style="margin-top:22px">千利休教導，茶所需要的是誠意，而非珍寶。年復一年，珍重地使用一套樸素的道具——與二手道具共同生活，正是這份教誨的實踐。</p>
</section>
'''
w("zh/guide.html", shell_zh(
  "點前的流程 — 薄茶的點法 | 悠三堂古美術藝廊",
  "茶道具如何使用：薄茶點前的逐步流程，以及第一套道具的選購指引。",
  guide_body, root="../", current="guide"))


# ------------------------------------------------------------------ setup --
FURO_DIAG_ZH = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">主人座席（簡化）</text>
<rect x="76" y="30" width="40" height="40" fill="none" stroke="#a53f2b" stroke-width="1.6"/>
<circle cx="96" cy="50" r="14" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="96" y="83" text-anchor="middle" class="dg-label strong">風爐與釜</text>
<text x="96" y="94" text-anchor="middle" class="dg-label">（置於敷板上）</text>
<circle cx="152" cy="48" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="152" y="76" text-anchor="middle" class="dg-label strong">水指</text>
<circle cx="120" cy="136" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="120" y="162" text-anchor="middle" class="dg-label strong">主人</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">客人</text>
</svg>'''

RO_DIAG_ZH = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">主人座席（簡化）</text>
<rect x="146" y="96" width="40" height="40" fill="#e2d8c2" stroke="#a53f2b" stroke-width="2"/>
<circle cx="166" cy="116" r="13" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="166" y="150" text-anchor="middle" class="dg-label strong">爐與釜</text>
<circle cx="120" cy="46" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="120" y="74" text-anchor="middle" class="dg-label strong">水指</text>
<circle cx="104" cy="120" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="96" y="146" text-anchor="middle" class="dg-label strong">主人</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">客人</text>
</svg>'''


def ck_zh(name, note, link=None):
    label = f'<a href="{en("tools/" + link + ".html")}">{name}{EN_TAG}</a>' if link else name
    return (f'<label class="ck"><input type="checkbox">'
            f'<span class="ck-name">{label}</span>'
            f'<span class="ck-note">{note}</span></label>')


_LNK = 'style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)"'

setup_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">節令的佈置</p>
    <h2 class="section-title">爐與風爐 — 茶的兩個季節</h2>
    <div class="rule"></div>
    <p class="section-lede">茶人的一年，以火所在的位置一分為二。冬天將爐切入地板，使火靠近客人（爐）；夏天則以風爐讓火退遠，藉此透出涼意（風爐）。整個佈置——以及許多道具——都隨之改變。</p>
  </div>

  <div class="reveal">
    <div class="season-band">
      <div class="ro">爐 11月</div><div class="ro">12月</div><div class="ro">1月</div><div class="ro">2月</div><div class="ro">3月</div><div class="ro">4月</div>
      <div class="fu">風爐 5月</div><div class="fu">6月</div><div class="fu">7月</div><div class="fu">8月</div><div class="fu">9月</div><div class="fu">10月</div>
    </div>
    <p class="cmp-note">十一月的「爐開」被稱作茶人的新年；五月的「初風爐」則讓茶室轉向夏天。</p>
  </div>

  <div class="layout-grid reveal">
    <div class="layout-card">
      <h3>風爐的佈置<span class="en-sub">五月至十月</span></h3>
      {FURO_DIAG_ZH}
      <p class="cap">夏天的姿態：讓火離客人遠些，以示涼意。風爐置於敷板上，配較小的釜；整理其中的灰形也是主人的功夫之一。</p>
    </div>
    <div class="layout-card">
      <h3>爐的佈置<span class="en-sub">十一月至四月</span></h3>
      {RO_DIAG_ZH}
      <p class="cap">冬天的姿態：爐切入榻榻米中，其暖意與客人共享。釜也隨之變大，滾沸之聲更為深厚。</p>
    </div>
  </div>
  <p class="cmp-note reveal">※ 此為一般「運び點前」（本勝手）的簡化示意圖。實際位置會因爐的切法與流派而異。</p>

  <div class="reveal">
    <table class="cmp-table">
      <thead><tr><th style="width:8em;background:var(--paper-deep);color:var(--matcha)"></th><th>爐</th><th class="furo-col">風爐</th></tr></thead>
      <tbody>
        <tr><th>季節</th><td>十一月至四月（十一月爐開）</td><td>五月至十月（五月初風爐）</td></tr>
        <tr><th>火的位置</th><td>沉入地板、靠近客人——共享暖意</td><td>在主人一側、遠離客人——暗示涼意</td></tr>
        <tr><th><a href="{en("tools/kama.html")}" {_LNK}>釜</a></th><td>較大，置於五德之上；另有釣釜、釣瓶等變化</td><td>較小，置於風爐與敷板之上</td></tr>
        <tr><th><a href="{en("tools/hishaku.html")}" {_LNK}>柄杓</a></th><td>杓斗較大；柄端自內側削切</td><td>杓斗較小；柄端自外側削切</td></tr>
        <tr><th>蓋置（竹製）</th><td>原則上取節在中段者（中節）</td><td>原則上取節在上端者（天節）</td></tr>
        <tr><th>炭與香</th><td>炭較大；練香盛於陶製香合</td><td>炭較小；白檀盛於漆製香合</td></tr>
        <tr><th>意趣</th><td>圍暖而聚；沉靜而侘的季節</td><td>「一味涼」；水成為主角</td></tr>
      </tbody>
    </table>
    <p class="cmp-note">※ 蓋置的節位等習慣因流派而異，請以老師的指導為準。</p>
  </div>
</section>

<section class="section tight" style="padding-top:20px">
  <div class="section-head reveal" style="margin-bottom:34px">
    <p class="section-kicker">確認清單</p>
    <h2 class="section-title">實際點前所需的一切</h2>
    <div class="rule"></div>
    <p class="section-lede">以下是基本的薄茶「運び點前」（不使用棚）所需的清單。準備時可逐項勾選。</p>
  </div>

  <div style="max-width:920px;margin:0 auto">
    <div class="ck-group reveal">
      <h3>1 — 事先安置的道具 <span class="en-sub">据えておく道具</span></h3>
      <div class="ck-cols">
        {ck_zh("釜", "水已滾沸——留心聽那「松風」", "kama")}
        {ck_zh("爐或風爐", "依季節選用（參見上方表格）")}
        {ck_zh("水指", "約盛八分滿，置於主人座席", "mizusashi")}
        {ck_zh("炭與灰（或電熱器）", "爐：炭較大、用練香／風爐：炭較小、整灰形")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>2 — 組在茶碗中的道具 <span class="en-sub">茶碗に仕組む道具</span></h3>
      <div class="ck-cols">
        {ck_zh("茶碗", "隨季節：夏用淺碗，冬用深碗", "chawan")}
        {ck_zh("茶筅", "先檢查穗的狀況；薄茶用穗數較多者", "chasen")}
        {ck_zh("茶杓", "伏置於茶碗邊緣", "chashaku")}
        {ck_zh("茶巾", "麻質的方巾，依規定摺法摺好")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>3 — 一併端出的道具 <span class="en-sub">運び出す道具</span></h3>
      <div class="ck-cols">
        {ck_zh("棗", "抹茶過篩後堆成小山", "natsume")}
        {ck_zh("建水", "最後端出，蓋置與柄杓一併置於其中")}
        {ck_zh("柄杓", "分爐用與風爐用——切勿混用", "hishaku")}
        {ck_zh("蓋置", "爐：中節／風爐：天節（竹製）")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>4 — 隨身攜帶的物件 <span class="en-sub">身に着けるもの</span></h3>
      <div class="ck-cols">
        {ck_zh("帛紗", "繫在左腰——主人的標記", "fukusa")}
        {ck_zh("扇子", "行禮時置於膝前")}
        {ck_zh("懷紙與菓子切", "客人同樣不可缺少")}
        {ck_zh("古帛紗", "部分流派於拜見道具與濃茶時使用")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>5 — 為客人準備的道具 <span class="en-sub">客のための道具</span></h3>
      <div class="ck-cols">
        {ck_zh("點心與菓子器", "薄茶配乾點心、用盤；濃茶配濕點心、用緣高")}
        {ck_zh("坐墊、菸盆等", "正式的茶室中，依場合的格調斟酌")}
      </div>
    </div>
    <div class="reveal" style="margin-top:44px;border:1px solid var(--line);background:var(--paper-deep);border-radius:4px;padding:28px 26px">
      <h3 style="font-size:16px;letter-spacing:.14em;font-weight:500">濃茶時的差異 <span class="en-sub">濃茶での違い</span></h3>
      <p style="font-size:13.5px;color:var(--ink-soft);margin-top:12px">棗換成收在仕覆中的<strong>茶入</strong>，茶碗也選用格調較高者，並以<strong>古帛紗或出帛紗</strong>隨茶碗一同奉至客前。一碗茶由數位客人共飲。</p>
    </div>
  </div>
</section>
'''
w("zh/setup.html", shell_zh(
  "爐與風爐的佈置，以及完整的道具清單 | 悠三堂古美術藝廊",
  "以圖解對照冬天的爐與夏天的風爐，並附上薄茶點前所需一切道具的確認清單。",
  setup_body, root="../", current="setup"))


# --------------------------------------------------------------- articles --
articles_index_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">專文 — 読みもの</p>
    <h2 class="section-title">更深入地認識茶道具</h2>
    <div class="rule"></div>
    <p class="section-lede">讓挑選道具這件事更有意思的讀物。從哪一篇開始都可以。<br>
    <span class="en-sub">這些長篇專文目前提供日文版與英文版。</span></p>
  </div>
  <div class="article-cards">
    {article_cards_zh(depth=2)}
  </div>
</section>
'''
w("zh/articles/index.html", shell_zh(
  "專文 — 茶道具指南 | 悠三堂古美術藝廊",
  "關於茶碗、釜、茶入與茶筅的深入指南，茶道的歷史，以及形塑道具面貌的節令曆。",
  articles_index_body, root="../../", current="articles"))

print("繁體中文頁面已寫出")

PAGES_ZH = ["index.html", "tools.html", "setup.html", "guide.html",
            "articles/index.html"]


# ============================================================== 細部頁面 ==
# 圖上的編號位置（parts_dots）與道具的排列順序各語言共用，
# 因此直接取自英文版，不再重抄一份，日後要調整也只需改一處。
from gen_en import TOOLS_EN  # noqa: E402

DOTS = {t["slug"]: t["parts_dots"] for t in TOOLS_EN}

DETAIL_ZH = {
"chawan": dict(
  tags=["主要道具", "陶瓷", "隨節令挑選"],
  names=[("名稱", "茶碗（chawan，點抹茶用的碗）"),
         ("主要窯口", "樂燒、萩燒、唐津、志野、天目等"),
         ("依季節", "夏天用碗口開闊的平茶碗／冬天用較深、保溫的筒茶碗")],
  history=["茶碗的故事，是從隨著茶一同傳入的中國天目碗開始的。室町時代，這些「唐物」地位最高；但隨著侘茶成形，喜好先是轉向高麗茶碗，最後落在日本自製的器物上。",
    "桃山時代，陶工長次郎以樂燒茶碗回應千利休的侘之美學——完全以手捏成，不用轆轤。「一樂二萩三唐津」這句話，排出了茶人最鍾愛的日本窯口，而這三處的茶碗至今仍在茶人手中傳遞。"],
  parts=[("口造（碗口）", "碗的唇緣；厚薄與弧度會改變飲用時的觸感"),
         ("見込（內側）", "碗的內底——需要恰當的寬度才好點茶"),
         ("胴（碗身）", "側面的牆，釉色的「景色」在此顯現"),
         ("腰", "往高台收束的曲線；決定了碗在手中的坐落"),
         ("高台（圈足）", "削出的足圈，最能看出作者的手")],
  usage=[("拜見", "雙手捧持，位置放低、貼近榻榻米。先找出「正面」——碗的臉。"),
         ("受茶", "將碗轉開，避免就著正面飲用；約兩口半飲盡。"),
         ("清洗", "只用溫水，切勿使用清潔劑。完全乾透後再收進盒中。")],
  checks=[("貫入與缺口", "檢查碗口有無小缺（ホツ）與釉裂（ニュウ）。有些反而被視為景色——請向賣家確認狀態說明。"),
          ("修補", "金繼（以金漆修補）未必使價值下降，但能否在茶席上使用，要看修補的品質。"),
          ("共箱", "有共箱（作者署名的木箱）或茶人的箱書，估價會大不相同。"),
          ("高台與土", "高台的削法與露出的土味，是判斷窯口與真偽的關鍵線索。")]),

"chasen": dict(
  tags=["主要道具", "竹工藝", "消耗品"],
  names=[("名稱", "茶筅（chasen，打抹茶用的竹刷）"),
         ("種類", "數穗（約72穗）、八十本立、百本立、百二十本立；濃茶用穗數少而粗的荒穗"),
         ("依流派", "表千家用煤竹／裏千家用白竹／武者小路千家用黑竹")],
  history=["一般認為茶筅是室町時代，應茶道先驅村田珠光之請，在大和（今奈良縣）高山所創。此後五百年間，高山始終是「茶筅之鄉」，技法在各家族內部相傳。",
    "一整支竹子，以一把刀削出百餘支細穗，再逐支以熱水彎出向內或向外的弧度——這是機器無法取代的手工。茶筅至今仍是日本國家指定的傳統工藝品。"],
  parts=[("穗先", "打茶的尖端，分內外兩圈"),
         ("絲線（かがり糸）", "束住外圈穗的線，多為黑色"),
         ("節", "穗與柄之間的竹節"),
         ("柄", "手持之處；竹材依流派而異")],
  usage=[("茶筅通し", "點前途中以熱水涮洗茶筅，同時檢查穗的狀況。"),
         ("點茶", "自手腕發力，快速地畫「m」字，最後輕輕畫一個「の」字提起。"),
         ("乾燥", "使用後沖洗，穗朝上自然風乾；放在茶筅休息座（くせなおし）上可保持穗形。")],
  checks=[("實用者請買全新品", "茶筅會接觸口唇且屬消耗品，要實際使用的請買新的。市面上的二手品多是未曾使用的舊庫存。"),
          ("穗的狀況", "穗若斷裂或外翻就打不出細泡；狀況好的穗會柔和地向內彎。"),
          ("產地", "高山所製者，在平衡與耐用上都勝過大量進口品。"),
          ("是否合乎流派", "請確認竹色是否符合您所習的流派。")]),

"chashaku": dict(
  tags=["主要道具", "竹工藝", "帶有「銘」"],
  names=[("名稱", "茶杓（chashaku，舀抹茶的竹匙）"),
         ("銘", "作者為它取的名字——多取自節令之詞或禪語"),
         ("附件", "共筒（作者署名的竹筒）與木箱，對價值影響極大")],
  history=["茶杓源自中國的象牙茶匙，但侘茶將它改以竹製；現在的形制大約在武野紹鷗與千利休的時代定型。利休親手削的茶杓——尤其是臨終前所作的「淚」——至今仍令茶人動容。",
    "這是茶人習慣親手削製的唯一一件道具。依竹節的位置，分為元節、中節與無節；一旦配上銘與署名的竹筒，一片薄竹便成了整場茶會的聲音。"],
  parts=[("櫂先（前端）", "舀取抹茶的彎曲末端"),
         ("樋", "竹子天然的凹槽——鑑賞的重點之一"),
         ("節", "靠近中段的竹節；以中節最為常見"),
         ("切止（柄端）", "柄端的切法，最能顯出作者的手癖")],
  usage=[("清", "點前開始時以帛紗拭過——這是心意的動作，並非單純的擦拭。"),
         ("舀取", "薄茶一碗約用一杓半，即兩公克左右。"),
         ("拜見", "奉予客人鑑賞；切勿以手指直接觸碰前端。")],
  checks=[("銘與竹筒", "價值集中在署名的竹筒與木箱上。只有茶杓本身而無此二者，價格相差甚遠。"),
          ("斷裂與蟲蛀", "檢查前端是否有缺，杓身是否有蟲蛀；有些已以漆修補。"),
          ("竹的景色", "樋、斑點與染色屬於個人喜好——選您看著順眼的即可。"),
          ("作者", "家元所削者，價格遠高於工房製品。")]),

"natsume": dict(
  tags=["主要道具", "漆器", "薄茶用"],
  names=[("名稱", "棗（natsume，因形似棗子而得名）"),
         ("大小", "大棗、中棗、小棗"),
         ("塗法", "素黑的真塗、溜塗、金蒔繪、螺鈿")],
  history=["棗是日本的發明，一般歸於室町時代的塗師羽田五郎。相對於濃茶所用的陶製茶入，這種輕巧的漆器成了薄茶器的標準。",
    "從利休所好的素黑，到後世以金蒔繪畫上四季的作品，這件可以握在掌中的器物，凝縮了日本漆藝的精華。"],
  parts=[("蓋・甲", "上面——蒔繪大顯身手之處"),
         ("合口", "蓋與身相接之處；此處的精度就是品質的證明"),
         ("胴", "微微隆起的側面"),
         ("底", "可能留有作者的落款")],
  usage=[("拿取", "置於左掌，依既定的手法以帛紗清拭蓋面。"),
         ("盛裝", "將抹茶鬆鬆地堆成一座小山；使用前才過篩。"),
         ("保養", "切勿以水清洗。以柔軟乾布擦拭，收進桐箱保存。")],
  checks=[("漆的狀態", "留意龜裂、剝落與失去光澤。日曬造成的褪色無法復原。"),
          ("蓋的密合", "好的棗，蓋子會帶著一聲輕嘆落下。若有鬆動或喀喀作響，就要當心。"),
          ("蒔繪的磨損", "金彩會隨使用而磨去——請放大照片確認輪廓是否還在。"),
          ("箱與作者", "有署名的木箱，以及輪島、山中等產地，都是價格的依據。")]),

"kama": dict(
  tags=["主要道具", "鑄鐵", "爐與風爐"],
  names=[("名稱", "茶釜（kama，煮水的鐵釜）"),
         ("著名產地", "蘆屋（筑前）、天明（下野）、京都"),
         ("依季節", "冬天用置於地爐的大釜／夏天用置於風爐的小釜")],
  history=["茶釜自十四世紀起，在兩大產地興盛：蘆屋以優雅的浮雕紋樣著稱，天明則以粗獷的肌理受人喜愛。這兩個名字至今仍代表最上乘的古釜。",
    "桃山時代，京都三条釜座的鑄物師崛起，利休的釜師辻与次郎確立了侘釜的樣式。有「值一國一城」之譽的茶釜，為整個茶室定下了基調。"],
  parts=[("摘・蓋", "唐銅或鐵製的蓋；蓋摘是值得細看的一處"),
         ("口", "汲水之處；形制自姥口到廣口，變化多端"),
         ("鐶付", "掛提環用的兩耳"),
         ("胴・肌", "鑄造表面的景色——霰紋等各種紋樣"),
         ("底", "最先磨損之處；古釜多半換過底")],
  usage=[("煮水", "以炭或電熱器將水煮到「松風」的階段。"),
         ("汲水", "以柄杓靜靜地舀取；蓋的處理另有一套作法。"),
         ("乾燥", "使用後倒空，以餘熱徹底烘乾——切勿留著水氣。")],
  checks=[("漏水測試", "注滿水放置一夜，看是否滲漏。小的漏處有時可以修補。"),
          ("鏽", "表面的薄鏽可以處理，內部的深度腐蝕則不行。內壁的水垢反而是好事。"),
          ("換底", "古釜常見，只要出自釜師之手就不算缺點。"),
          ("蓋與鐶", "請確認原配的蓋、鐶與五德是否一併附上。")]),

"hishaku": dict(
  tags=["主要道具", "竹工藝", "爐與風爐"],
  names=[("名稱", "柄杓（hishaku，舀水的竹杓）"),
         ("依季節", "爐用：杓斗較大，柄端自內側削切／風爐用：杓斗較小，自外側削切"),
         ("備註", "庭院蹲踞所用的柄杓是另一種東西")],
  history=["舀水的杓自古即是祭祀之器，但茶道把竹製柄杓提煉成了點前的核心，連尺寸也隨爐與風爐的季節而變。",
    "一支嶄新的白竹柄杓，本身就是一份待客之心——潔淨的色澤是對客人的敬意，而長年使用之後，杓斗會轉為溫潤的琥珀色。"],
  parts=[("合（杓斗）", "盛水的部分"),
         ("月形", "杓斗與柄相接處的新月形缺口"),
         ("柄", "細長的杓柄，竹節的位置有定規"),
         ("切止（柄端）", "爐用與風爐用的斜切方向相反")],
  usage=[("姿勢", "以「鏡柄杓」的姿態持握，如同映照自己的心。"),
         ("汲與注", "注水要成一條線；剩下的水絕不倒回釜中。"),
         ("引柄杓", "風爐的季節，柄杓以伸指的方式收回——是公認優美的一個動作。")],
  checks=[("實用者請買新品", "茶事以潔淨為先；二手柄杓請當作練習用或陳列品看待。"),
          ("裂與彎", "存放過乾會使杓斗開裂；請檢查柄是否彎曲。"),
          ("爐用或風爐用", "從柄端的切法與杓斗大小判別，並配合您正在練習的季節。"),
          ("差通", "杓斗與柄一體成形者格調最高；否則請留意接合處的精度。")]),

"fukusa": dict(
  tags=["主要道具", "織品", "主人隨身"],
  names=[("名稱", "帛紗（fukusa）"),
         ("尺寸", "約 27 × 28 公分；以鹽瀨絹為常規"),
         ("顏色慣例", "男性用紫，女性用紅或朱（依流派而異）；出帛紗與古帛紗是另外的東西")],
  history=["帛紗的形制，相傳出自利休之妻宗恩之手，為清拭道具而設。繫在主人腰間的它，成了「正在點茶的人」的標記。",
    "除了素面的鹽瀨絹之外，以名物裂紋樣織成的古帛紗與出帛紗，會在濃茶時隨茶碗一同奉出——一整部織物史，就摺疊在這一方小小的絹布裡。"],
  parts=[("輪（わさ）", "摺疊的一邊，是操作時的基準側"),
         ("耳", "織邊未收的兩側"),
         ("角", "摺帛紗時手指捏取之處"),
         ("地", "鹽瀨絹；布的挺度決定了手感")],
  usage=[("配戴", "掖在左腰——主人的標記。"),
         ("摺法", "四方捌的一連串動作先撣去灰塵，再摺成形以清拭茶器與茶杓。"),
         ("保養", "絹最怕水。髒了就換新——它是消耗品。")],
  checks=[("以新品為宜", "用來「清」的布，還是買新的好。"),
          ("若要買二手", "以名物裂織成的古帛紗是例外——古物市場十分豐富。請確認紋樣的名稱與年代。"),
          ("絹的挺度", "布若軟塌疲乏就摺不成形，練習時會很不順手。"),
          ("流派的顏色", "請配合您所習流派與身分的顏色慣例。")]),

"mizusashi": dict(
  tags=["主要道具", "陶瓷及其他", "陳設的中心"],
  names=[("名稱", "水指（mizusashi，盛冷水的罐）"),
         ("材質", "陶瓷、曲物（薄木彎製）、玻璃、金屬"),
         ("蓋", "共蓋（原配）或塗蓋（漆製的替代蓋）")],
  history=["水指原是廚房之器，後來被請進茶室。信樂的種壺、備前的甕，經「見立」——在尋常之物中發現美的眼光——而入茶席，最能體現侘的精神。",
    "從中國青瓷到志野、織部，從曲物到夏天的玻璃，沒有一件道具的選擇比它更寬；人們依茶會的季節與格調來挑選它。"],
  parts=[("蓋", "共蓋或塗蓋；各有各的處理方式"),
         ("口", "寬口或窄口——影響柄杓伸入的難易"),
         ("胴", "釉色景色展開的舞台"),
         ("底", "能在榻榻米上放得穩，這一點很要緊")],
  usage=[("安置", "端至主人座席後，由它定下整個畫面。"),
         ("補水", "接近尾聲時，舀一杓水為釜添涼。"),
         ("蓋的處理", "塗蓋要擦乾；共蓋要輕輕開啟，當心磕碰。")],
  checks=[("蓋的損傷", "最先受損的是蓋——請檢查有無缺口與重新上漆的痕跡。"),
          ("裂與漏", "它是要盛水的，所以貫入會實際造成影響。請詢問是否做過盛水測試。"),
          ("替代的蓋", "配上漆製的替代蓋很常見，本身並不算減分。"),
          ("箱與來歷", "有署名的木箱或可考的來歷，會同時提升陳設價值與價格。")]),
}


TYPES_ARTICLE_ZH = {
 "chawan": ("chawan-types.html", "茶碗的種類", "樂燒、萩燒、唐津及其他——系譜與器形"),
 "chasen": ("chasen-types.html", "茶筅的種類", "穗數、竹色與流派"),
 "kama": ("kama-types.html", "釜的種類", "蘆屋、天明、京釜，以及各種形制"),
 "natsume": ("natsume-types.html", "棗的種類", "大小、漆的塗法，與薄茶器這一家族"),
}


def detail_zh(t, i):
    d = DETAIL_ZH[t["slug"]]
    prev_t, next_t = TOOLS_ZH[(i - 1) % len(TOOLS_ZH)], TOOLS_ZH[(i + 1) % len(TOOLS_ZH)]
    names_rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in d["names"])
    parts_items = "".join(
        f'<li><span class="p-num">{n}</span><div><span class="p-name">{p}</span><br>'
        f'<span class="p-note">{note}</span></div></li>'
        for n, (p, note) in enumerate(d["parts"], 1))
    steps = "".join(
        f'<div class="step"><span class="step-no">{n + 1}</span>'
        f'<div class="step-body"><h3>{h}</h3><p>{p}</p></div></div>'
        for n, (h, p) in enumerate(d["usage"]))
    checks = "".join(f'<div class="check-cell"><h3>{h}</h3><p>{p}</p></div>' for h, p in d["checks"])
    hist = "".join(f"<p>{p}</p>" for p in d["history"])
    tags = (f'<span class="tag lv-tag-inline lv{t["level"]}">{LV_ZH[t["level"]][0]} {LV_ZH[t["level"]][1]}</span>'
            + "".join(f'<span class="tag">{x}</span>' for x in d["tags"]))
    art = TYPES_ARTICLE_ZH.get(t["slug"])
    more = (f'<div class="types-link reveal"><a href="{en("articles/" + art[0], 2)}">'
            f'<span class="tl-k">further reading{EN_TAG}</span><span class="tl-n">{art[1]}</span>'
            f'<span class="tl-s">{art[2]}</span></a></div>') if art else ""

    body = f'''
<div class="detail-hero">
  <div class="detail-hero-inner">
    <div>
      <p class="crumbs"><a href="../index.html">首頁</a> / <a href="../tools.html">茶道具一覽</a> / {t["name"]}</p>
      <h1 class="detail-title">{t["name"]}</h1>
      <p class="detail-yomi">{t["yomi"]} — {t["zh"]}</p>
      <p class="detail-lede">{t["lede"]}</p>
      <div class="detail-tags">{tags}</div>
    </div>
    <div class="detail-art">{ico(t["slug"], "ico--hero")}</div>
  </div>
</div>

<div class="detail-body">
  <section class="d-sec reveal">
    <h2>名稱與種類 <span class="en-sub">名前と種類</span></h2>
    <div class="d-rule"></div>
    <table class="name-table">{names_rows}</table>
  </section>
  <section class="d-sec reveal">
    <h2>來歷 <span class="en-sub">歴史</span></h2>
    <div class="d-rule"></div>
    {hist}
  </section>
  <section class="d-sec reveal">
    <h2>各部位的名稱 <span class="en-sub">部位の名称</span></h2>
    <div class="d-rule"></div>
    <div class="parts-wrap">
      <div class="parts-fig">{parts_icon(t["slug"], DOTS[t["slug"]])}</div>
      <ol class="parts-list">{parts_items}</ol>
    </div>
  </section>
  <section class="d-sec reveal">
    <h2>使用方式 <span class="en-sub">使い方</span></h2>
    <div class="d-rule"></div>
    <div class="steps">{steps}</div>
  </section>
  <section class="d-sec reveal">
    <h2>選購二手時的重點 <span class="en-sub">中古で選ぶポイント</span></h2>
    <div class="d-rule"></div>
    <div class="check-grid">{checks}</div>
  </section>
  <section class="d-sec reveal">
    <h2>此類道具的藝廊 <span class="en-sub">GALLERY</span></h2>
    <div class="d-rule"></div>
    <div class="shop-stub" data-ec-category="{t["slug"]}" data-ec-root="../../" data-ec-name="{t["name"]}">
      <div class="listing-slot" id="listings-{t["slug"]}"></div>
      <h3>悠三堂藝廊所藏</h3>
      <p>藝廊現有的此類器物會顯示在這裡。</p>
      <button class="btn" disabled>查看庫存 — 準備中</button>
    </div>
  </section>
</div>

{more}
<nav class="pn">
  <a href="{prev_t["slug"]}.html">← {prev_t["name"]}</a>
  <a href="../tools.html">全部茶道具</a>
  <a href="{next_t["slug"]}.html">{next_t["name"]} →</a>
</nav>
'''
    return shell_zh(
        f'{t["name"]}（{t["zh"]}）— 來歷、部位與使用方式 | 悠三堂古美術藝廊',
        f'{t["name"]}（{t["yomi"]}，{t["zh"]}）的來歷、各部位的名稱、使用方式，'
        f'以及選購二手時應當確認的重點。',
        body, root="../../", current="tools")


for i, t in enumerate(TOOLS_ZH):
    w(f'zh/tools/{t["slug"]}.html', detail_zh(t, i))

PAGES_ZH += [f'tools/{t["slug"]}.html' for t in TOOLS_ZH]
print("繁體中文的細部頁面已寫出")


# ================================================================== 專文 ==
# 長篇專文與英文版共用同一套骨架，只換文字。尚未翻譯的頁面仍連往英文版，
# 並以「EN」標記。
def article_shell_zh(title, desc, kicker, h1, lede, body_secs):
    body = f'''
<div class="article-hero">
  <p class="crumbs"><a href="../index.html">首頁</a> / <a href="index.html">專文</a> / {h1}</p>
  <p class="section-kicker">{kicker}</p>
  <h1 class="article-title">{h1}</h1>
  <p class="article-lede">{lede}</p>
</div>
<div class="detail-body">
{body_secs}
</div>
<nav class="pn">
  <a href="index.html">← 全部專文</a>
  <a href="../tools.html">茶道具一覽</a>
</nav>
'''
    return shell_zh(f'{title} | 悠三堂古美術藝廊', desc, body, root="../../", current="articles")


def sec_zh(title, jp, inner):
    return f'''<section class="d-sec reveal">
  <h2>{title} <span class="en-sub">{jp}</span></h2>
  <div class="d-rule"></div>
  {inner}
</section>'''


def tcard_zh(name, sub, desc, tip):
    return (f'<div class="type-card"><h3>{name}</h3><p class="t-sub">{sub}</p>'
            f'<p>{desc}</p><p class="t-tip">{tip}</p></div>')


def tl_zh(era, years, h, p):
    return (f'<div class="tl-item"><div class="tl-era">{era}<small>{years}</small></div>'
            f'<div class="tl-body"><h3>{h}</h3><p>{p}</p></div></div>')


_L = 'style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)"'

# ---- 1：茶碗的種類 --------------------------------------------------------
a1 = (
sec_zh("三大系譜", "三つの系譜", '''
  <p>茶碗依產地可分為三大系譜：來自中國的<strong>唐物</strong>、來自朝鮮半島的<strong>高麗物</strong>，以及日本自製的<strong>和物</strong>。中國的器物曾居於地位的頂端，但隨著侘茶的普及，高麗與日本茶碗那種不加雕飾的美，逐漸擄獲了茶人的心。</p>
  <p>有一句話值得記住：<strong>「一樂二萩三唐津」</strong>——這是日本三處最受茶人鍾愛的窯口，流傳已久的排序。</p>''')
+ sec_zh("主要的種類", "主要な種類", '<div class="type-grid">'
+ tcard_zh("樂燒", "京都", "不用轆轤、全以手捏成形，一只一只單獨燒製。由長次郎為呼應利休的侘之趣味所創。有黑有紅，入手輕盈，點茶的手感極好。", "習作之器頗多，很適合作為第一只茶碗。")
+ tcard_zh("萩燒", "山口", "柔軟的土，罩上枇杷色的釉。茶湯滲入貫入之中，碗的面貌隨著使用而改變——所謂「萩之七化」。", "請留意貫入染色已經進行到什麼程度。")
+ tcard_zh("唐津燒", "佐賀", "土質粗獷而有力，配上鐵繪的樸拙筆意。繪唐津、斑唐津、朝鮮唐津——變化無窮，百看不厭。", "結實耐用，最適合日常使用的一碗。")
+ tcard_zh("志野燒", "美濃", "日本最早的白色陶器：厚厚的長石釉，在火舌舔過之處泛出緋紅。國寶「卯花牆」便是志野。", "那份溫潤，最合冬日的時節。")
+ tcard_zh("織部燒", "美濃", "銅綠釉，加上大膽扭曲的器形，出自茶道的奇才古田織部的趣味。", "歪斜正是重點；請以入手的感覺來挑選。")
+ tcard_zh("天目", "唐物", "鐵黑色的中國釉，帶有曜變或油滴的景致。曜變天目全世界僅存三只——皆在日本，皆為國寶。", "現代的優良仿作不少；配上天目台者格調更高。")
+ tcard_zh("井戶", "高麗物", "本是朝鮮的日用碗，經茶人之眼而登上高位：器形寬綽、枇杷色釉，高台上有如鯊魚皮的「梅花皮」。「喜左衛門井戶」為國寶。", "高台上梅花皮的縮釉，是行家判斷的關鍵。")
+ tcard_zh("京燒", "京都", "由仁清與乾山開創的彩繪之雅——四季風物繪於碗上。現代作家的天地也十分寬廣。", "請將繪畫的題材，配合您打算使用的節令。")
+ '</div>')
+ sec_zh("依器形挑選", "形で選ぶ", f'''
  <table class="name-table">
    <tr><th>平茶碗</th><td>碗口寬而開闊，宜於夏天：茶湯涼得快，看著也涼爽。</td></tr>
    <tr><th>筒茶碗</th><td>深形的冬碗，將暖意留在掌中。</td></tr>
    <tr><th>碗形</th><td>茶碗最基本的形制，四季皆宜。</td></tr>
    <tr><th>半筒</th><td>介於兩者之間——適合春秋轉涼的時節。</td></tr>
    <tr><th>天目形</th><td>中國傳來的錐狀器形，用於最為正式的點前。</td></tr>
    <tr><th>沓形</th><td>織部所好的扭曲「鞋形」——充滿動勢。</td></tr>
  </table>
  <p style="margin-top:18px">若拿不定主意，先從一只碗形入手；節令的器形日後再添。<a href="../tools/chawan.html" {_L}>茶碗的基礎頁面</a>談了各部位與選購二手時的重點。</p>'''))

w("zh/articles/chawan-types.html", article_shell_zh(
  "茶碗的種類 — 樂燒、萩燒、唐津及其他",
  "依系譜（唐物、高麗物、和物）、窯口（樂、萩、唐津、志野、織部、天目、井戶）與器形，整理茶碗的種類。",
  "專文 — 指南", "茶碗的種類",
  "樂燒、萩燒與唐津；志野與織部；天目與井戶。系譜、窯口、器形三個軸線，為那些有名的名字排出次序。",
  a1))

# ---- 2：茶道的歷史 --------------------------------------------------------
a2 = (
sec_zh("千年之流", "千年の流れ", '''
  <p>茶道的歷史，始於一碗藥飲。茶自中國東渡，隨禪宗而普及，與日本對器物之美的感受相遇，終於成為名為「茶之湯」的綜合藝術。以下依時代略述其脈絡：</p>
  <div class="tl">'''
+ tl_zh("奈良–平安", "8–12世紀", "茶傳入日本", "遣唐使與最澄、空海等僧人帶回了茶——將壓製的茶磚刮下煎煮，作為公卿與僧侶的藥飲與儀式之飲。")
+ tl_zh("鎌倉", "12–14世紀", "榮西與抹茶", "臨濟宗之祖榮西傳入抹茶的飲法，並在《喫茶養生記》中盛讚茶的功效。寺院的茶禮就此扎根；武士之間則流行鬥茶的品評之戲。")
+ tl_zh("室町", "14–15世紀", "書院之茶與唐物", "足利將軍們在珍貴的中國器物之間，舉行格式化的茶會。相對於這份豪奢，村田珠光在樸素之物中發現了美——「繫名馬於茅屋」——開啟了侘的道路。")
+ tl_zh("桃山", "16世紀", "利休完成侘茶", "自武野紹鷗至千利休：二疊的草庵、樂燒的茶碗、竹製的花入——一種做減法的美學。茶與信長、秀吉的政治交纏，器物的價值也因此難以估量。")
+ tl_zh("江戶", "17–19世紀", "三千家與大名茶", "利休的曾孫們創立了表千家、裏千家與武者小路千家；小堀遠州等大名茶人則培育出「綺麗寂」。家元制度成形，茶也走進了町人的生活。")
+ tl_zh("明治–大正", "19–20世紀", "近代的數寄者", "在急速西化之中，茶一度動搖，隨後在實業家收藏者身上找到新的護持者。茶也進入學校課程，作為女性的教養而廣為流傳。")
+ tl_zh("昭和–今日", "20世紀–", "茶向世界敞開", "岡倉天心的《茶之書》將這份精神帶往遠方。美術館陳列名碗，習茶之風擴及海外——而古老的器物，仍不斷與新的手相遇。")
+ '</div>')
+ sec_zh("從器物看歷史", "道具から見る歴史", f'''
  <p>茶的歷史，就是茶道具的歷史：對天目的嚮往、對高麗茶碗的發現、樂燒的創製、竹製的茶杓與花入。每個時代的美感，都留存在至今仍在流轉的器物之中。</p>
  <p>拿起一件古道具，便是觸碰這千年的故事。請瀏覽<a href="../tools.html" {_L}>茶道具一覽</a>，找到那件與您說話的器物。</p>'''))

w("zh/articles/history.html", article_shell_zh(
  "茶道的歷史 — 分七個時代",
  "從奈良時代茶的傳入，經榮西、珠光、利休，直到三千家與今日的茶之湯歷史。",
  "專文 — 歷史", "茶道的歷史",
  "一碗藥飲，在千年之間成為一條「道」。茶與茶道具的故事，分七個時代細說。",
  a2))

# ---- 3：茶筅的種類 --------------------------------------------------------
a3 = (
sec_zh("依穗數挑選", "穂数で選ぶ", '''
  <p>茶筅最主要的變數是<strong>穗數</strong>——也就是竹子被削成幾支細穗。穗數少者較硬挺，穗數多者能打出更細的泡沫。</p>
  <table class="name-table">
    <tr><th>荒穗（16–48）</th><td>穗粗而強韌，用於練濃茶。</td></tr>
    <tr><th>數穗（64–72）</th><td>最為泛用——薄茶濃茶皆可應付。作為第一支茶筅最為自然。</td></tr>
    <tr><th>八十本立</th><td>輕鬆就能打出細泡，宜於薄茶；練習時的基準。</td></tr>
    <tr><th>百本立／百二十本立</th><td>細緻的穗能打出最柔軟的泡沫——對初學者友善，但也較為脆弱。</td></tr>
  </table>''')
+ sec_zh("竹色與流派", "竹の色と流派", '<div class="type-grid">'
+ tcard_zh("白竹", "裏千家等", "漂白後色澤淺淡的竹，市面上最為常見。裏千家偏好穗尖向內彎曲者。", "市售茶筅多為白竹，最容易取得。")
+ tcard_zh("煤竹", "表千家", "琥珀色的竹，在農家的爐灶上經數十年煙燻而成——如今已相當稀少而珍貴。", "真正的煤竹價格不低；請留意染色的仿品。")
+ tcard_zh("紫竹", "武者小路千家", "天然色深的「紫竹」，外觀緊實而俊挺。", "也有人純粹因為好看而選它——並無人會責怪。")
+ '</div>'
+ '<p style="margin-top:18px">若您有所屬的流派，請配合該流派的竹色。若沒有，白竹的數穗或八十本立是最省心的選擇。</p>')
+ sec_zh("產地與品質", "産地と品質", '''
  <p>日本製的茶筅，幾乎全部出自奈良縣生駒市的<strong>高山</strong>——五百年來的「茶筅之鄉」，也是國家指定的傳統工藝品。一支竹、一把刀，百餘支細穗以熱水一支一支彎出弧度：全然是手工。</p>
  <p>市面上也有較便宜的進口茶筅，但在勻整、耐用與打茶的手感上都有差別。若是日常使用，高山所製者物有所值。</p>''')
+ sec_zh("保養與更換的時機", "手入れと替えどき", f'''
  <p>茶筅是消耗品。當穗斷裂、或彎曲的弧度鬆弛時，它便已盡了本分。使用後以熱水沖洗，穗朝上在陰涼處風乾，並置於茶筅休息座上。每年五月，各地會舉行「茶筅供養」，鄭重地送別用舊的茶筅。</p>
  <p>基於衛生考量，實際要使用的茶筅請購買新品。另請參見<a href="../tools/chasen.html" {_L}>茶筅的基礎頁面</a>。</p>'''))

w("zh/articles/chasen-types.html", article_shell_zh(
  "茶筅的種類 — 穗數、竹色與流派",
  "如何挑選茶筅：穗數（數穗、八十本立、百本立）、依流派而異的竹色，以及高山的傳統工藝。",
  "專文 — 指南", "茶筅的種類",
  "數穗或八十本立，白竹或煤竹。即使是最小的一件道具，挑選也自有其道理——以下是三個軸線。",
  a3))

# ---- 4-6：釜／茶入／棗 ----------------------------------------------------
from types_articles import kama_body_zh, chaire_body_zh, natsume_body_zh  # noqa: E402

w("zh/articles/kama-types.html", article_shell_zh(
  "釜的種類 — 蘆屋、天明與京釜",
  "依產地（蘆屋、天明、京都）、器形與鑄肌整理釜的種類，並說明爐用與風爐用的差別。",
  "專文 — 指南", "釜的種類",
  "蘆屋、天明與京釜。這件曾被說成「值一國」的道具，依產地、器形與肌理排出次序。",
  kama_body_zh(sec_zh, tcard_zh)))

w("zh/articles/chaire-types.html", article_shell_zh(
  "茶入的種類 — 肩衝、茄子、文琳",
  "依出身（唐物、島物、和物）與器形整理濃茶用的茶入，並附仕覆、牙蓋與箱書的指引。",
  "專文 — 指南", "茶入的種類",
  "肩衝、茄子、文琳、大海。一旦記住器形的名字，這只盛濃茶的小罐便會有趣得多。",
  chaire_body_zh(sec_zh, tcard_zh)))

w("zh/articles/natsume-types.html", article_shell_zh(
  "棗的種類 — 大小與漆的塗法",
  "依大小與漆的塗法（真塗、溜塗、蒔繪、螺鈿）整理棗，並介紹薄茶器這一整個家族。",
  "專文 — 指南", "棗的種類",
  "中棗或平棗，素黑或蒔金。挑選這只握在掌中的小漆器，自有一套尺度。",
  natsume_body_zh(sec_zh, tcard_zh)))

PAGES_ZH += [f"articles/{a}" for a in ['chawan-types.html', 'history.html', 'chasen-types.html', 'kama-types.html', 'chaire-types.html', 'natsume-types.html']]
