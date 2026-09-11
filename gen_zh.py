# -*- coding: utf-8 -*-
"""繁體中文版——五個主要頁面。

各項道具的細部頁面與長篇文章目前僅有日文版與英文版，因此相關連結皆指向英文版，
並以「EN」標記。用語依日文原名為主：漢字直接沿用，必要時補上說明，
純日語的讀音則附上羅馬字。
"""
import os
from gen import ROOT
from icons import sprite as ico_sprite, icon as ico


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
    <a class="brand" href="{root}zh/index.html">
      <span class="brand-mark">悠三堂古美術藝廊</span>
      <span class="brand-sub">YUSANDO ANTIQUE GALLERY</span>
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
    return "".join(
        f'<a class="article-card reveal" href="{en("articles/" + href, depth)}">'
        f'<p class="a-kicker">{kicker}</p><h3>{title}{EN_TAG}</h3>'
        f'<p>{desc}</p><p class="tool-more">閱讀（英文）→</p></a>'
        for href, kicker, title, desc in ARTICLES_ZH)


index_body = f'''
<section class="hero">
  <svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M100 18 a82 82 0 1 0 60 26" fill="none" stroke="#2b2a26" stroke-width="10" stroke-linecap="round"/>
  </svg>
  <div class="hero-inner">
    <p class="hero-kicker">均一價的二手茶道具 — 均一価格の中古茶道具ポータル</p>
    <h1 class="hero-title">選那件<br>讓您心動的。</h1>
    <p class="hero-sub">以<strong>均一價</strong>提供二手日本茶道具，初入門也能安心親近。<br>不必再揣測價格，只要挑您喜歡的那一件。</p>
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

<section class="section" style="background:transparent;padding-top:0">
  <div class="section-head reveal">
    <p class="section-kicker">茶道具</p>
    <h2 class="section-title">先從八件基本道具開始</h2>
    <div class="rule"></div>
    <p class="section-lede">點前不可或缺的道具。各件的細部頁面（目前為英文）涵蓋來歷、部位、使用方式，以及選購二手時的重點。</p>
  </div>
  <div class="tools-grid">
    {"".join(card_zh(t) for t in TOOLS_ZH)}
  </div>
  <div style="text-align:center;margin-top:44px">
    <a class="btn" href="tools.html">查看全部茶道具</a>
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

<section class="section reveal" style="text-align:center">
  <p class="section-kicker">藝廊</p>
  <h2 class="section-title">本藝廊現有的茶道具</h2>
  <div class="rule"></div>
  <p class="section-lede">各件道具的頁面會顯示悠三堂藝廊現有的器物。若有讓您留意的一件，歡迎來信詢問；線上販售將於準備妥當後開放。</p>
  <div style="margin-top:30px"><span class="btn" style="opacity:.5;cursor:default">線上販售 — 尚未開放</span></div>
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
