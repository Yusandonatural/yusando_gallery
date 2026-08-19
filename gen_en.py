# -*- coding: utf-8 -*-
"""Generate the English version of the site under en/."""
import os
from gen import ART, parts_svg, FONTS, ROOT

def w(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

# ---------------------------------------------------------------- EN shell ----
def shell_en(title, desc, body, root="../", current=""):
    def nav(href, label, key):
        cls = ' class="current"' if current == key else ''
        return f'<a href="{root}en/{href}"{cls}>{label}</a>' if not href.startswith("!") else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{root}en/index.html">
      <span class="brand-mark">悠三堂 YUSANDO</span>
      <span class="brand-sub">ANTIQUE GALLERY — USED TEA UTENSILS</span>
    </a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links">
      {nav("index.html","Home","home")}
      {nav("tools.html","Utensils","tools")}
      {nav("setup.html","Ro &amp; Furo","setup")}
      {nav("guide.html","How It Works","guide")}
      {nav("articles/index.html","Reading","articles")}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="f-inner">
    <div>
      <p class="f-mark">YUSANDO ANTIQUE GALLERY <span class="en-sub">悠三堂古美術ギャラリー</span></p>
      <p class="f-note">A portal for pre-loved Japanese tea utensils.<br>Knowledge first — commerce to follow.</p>
    </div>
    <nav class="f-nav">
      <a href="{root}en/index.html">HOME</a>
      <a href="{root}en/tools.html">UTENSILS</a>
      <a href="{root}en/setup.html">RO &amp; FURO SETUP</a>
      <a href="{root}en/guide.html">HOW IT WORKS</a>
      <a href="{root}en/articles/index.html">READING</a>
    </nav>
  </div>
  <p class="f-copy">© 2026 YUSANDO ANTIQUE GALLERY — Demo draft. Online shop integration coming soon.</p>
</footer>
<script src="{root}js/site.js"></script>
</body>
</html>'''

# ---------------------------------------------------------------- EN data ----
TOOLS_EN = [
dict(slug="chawan", name="Chawan", jp="茶碗", en="Tea Bowl", num="01",
  tags=["Core utensil","Ceramics","Chosen by season"],
  lede="The bowl in which tea is whisked and drunk — the utensil that most reveals the host's taste, chosen anew with every season.",
  names=[("Name","Chawan 茶碗 (\"tea bowl\")"),("Major kilns","Raku, Hagi, Karatsu, Shino, Tenmoku and more"),
         ("By season","Summer: shallow, open hira-jawan / Winter: deep tsutsu-jawan that keeps tea warm")],
  history=["The story of the chawan begins with Chinese tenmoku bowls, imported along with tea itself. In the Muromachi period these karamono (Chinese pieces) held the highest rank, but as wabi tea took shape, taste shifted toward Korean bowls and finally to Japanese wares.",
    "In the Momoyama era, the potter Chōjirō answered Sen no Rikyū's wabi aesthetic with the Raku bowl — shaped entirely by hand, without a wheel. The saying \"first Raku, second Hagi, third Karatsu\" ranks the beloved Japanese tea kilns, and bowls from all of them are still cherished in tea people's hands today."],
  parts_dots=[(80,30),(80,55),(30,60),(48,84),(80,100)],
  parts=[("Kuchi-zukuri (rim)","The lip; its thickness and curve change the feel of drinking"),
         ("Mikomi (interior)","The inner well — needs the right breadth for whisking"),
         ("Dō (body)","The side wall, where the glaze \"landscape\" shows"),
         ("Koshi (hip)","The curve toward the foot; defines the bowl in the hand"),
         ("Kōdai (foot)","The carved foot ring, where the maker's hand is most visible")],
  usage=[("Appreciating","Handle with both hands, kept low over the tatami. Find the shōmen — the bowl's \"face\"."),
         ("Receiving tea","Turn the bowl to avoid drinking from its face; empty it in about two and a half sips."),
         ("Cleaning","Rinse with warm water only — never detergent. Dry fully before boxing.")],
  checks=[("Hairlines & chips","Check the rim for small chips (hotsu) and glaze cracks (nyū). Some are prized as landscape — confirm the condition notes."),
          ("Repairs","Gold-lacquer repair (kintsugi) doesn't necessarily lower value, but usability in the tea room depends on its quality."),
          ("Signed box","A tomobako (box signed by the maker) or an inscription by a tea master changes the valuation greatly."),
          ("Foot & clay","The carving of the foot and the exposed clay are key clues to kiln and authenticity.")]),

dict(slug="chasen", name="Chasen", jp="茶筅", en="Tea Whisk", num="02",
  tags=["Core utensil","Bamboo craft","Consumable"],
  lede="A whisk carved from a single piece of bamboo. Takayama in Nara has made them for five hundred years.",
  names=[("Name","Chasen 茶筅 (\"tea whisk\")"),("Types","Kazuho (~72 tines), 80-tine, 100-tine, 120-tine; coarse araho for thick tea"),
         ("By school","Omotesenke: smoked bamboo / Urasenke: white bamboo / Mushakōji: black bamboo")],
  history=["The chasen is said to have been devised in the Muromachi period in Takayama, Nara, at the request of tea pioneer Murata Jukō. For five centuries since, Takayama has remained \"the village of the whisk,\" its techniques passed down within families.",
    "One length of bamboo is split into a hundred or more tines with a single knife, then each tine is bent inward or outward in hot water — handwork no machine can replace. It remains a designated Traditional Craft of Japan."],
  parts_dots=[(80,12),(97,40),(80,58),(80,80)],
  parts=[("Hosaki (tines)","The whisking tips, in an inner and outer ring"),
         ("Kagari thread","The thread binding the outer tines, usually black"),
         ("Fushi (node)","The bamboo node between tines and handle"),
         ("E (handle)","The grip; the bamboo differs by school")],
  usage=[("Chasen-tōshi","During the procedure the whisk is rinsed in hot water while its tines are inspected."),
         ("Whisking","Whisk briskly in an \"m\" pattern from the wrist, then lift off with a gentle \"no\" stroke."),
         ("Drying","Rinse after use and air-dry tines-up; a shaping stand (kusenaoshi) keeps its form.")],
  checks=[("Buy new for use","As it touches the mouth and wears out, a whisk for actual use should be new. Secondhand stock is mostly unused old inventory."),
          ("Tine condition","Broken or splayed tines whisk poorly; good tines curve gently inward."),
          ("Origin","Takayama-made whisks outperform mass imports in balance and durability."),
          ("School match","Check that the bamboo color suits your school of tea.")]),

dict(slug="chashaku", name="Chashaku", jp="茶杓", en="Tea Scoop", num="03",
  tags=["Core utensil","Bamboo craft","Carries a poetic name"],
  lede="A slender bamboo scoop for matcha. Small as it is, a named chashaku can carry the theme of an entire gathering.",
  names=[("Name","Chashaku 茶杓 (\"tea scoop\")"),("Mei","The poetic name given by its maker — often a season word or Zen phrase"),
         ("Accessories","The tomozutsu (maker-inscribed tube) and box strongly affect value")],
  history=["The scoop derives from Chinese ivory tea spoons, but wabi tea remade it in bamboo; its present form settled around the time of Takeno Jōō and Sen no Rikyū. Rikyū's own scoops — above all \"Namida\" (Tears), carved before his death — still move tea people today.",
    "It is the one utensil tea masters habitually carve themselves. The node's position divides scoops into moto-bushi, naka-bushi and fushi-nashi, and with a name and inscribed tube, a sliver of bamboo becomes the voice of the gathering."],
  parts_dots=[(133,17),(112,42),(60,68),(22,86)],
  parts=[("Kaisaki (tip)","The curved end that scoops the tea"),
         ("Hi (groove)","The natural channel of the bamboo — a point of appreciation"),
         ("Fushi (node)","The node near the middle; naka-bushi is most common"),
         ("Kiridome (butt end)","The cut at the handle end, bearing the maker's habit")],
  usage=[("Purifying","Wiped with the fukusa at the start of the procedure — a gesture of the heart, not mere cleaning."),
         ("Scooping","About one and a half scoops (roughly 2 g) per bowl of thin tea."),
         ("Viewing","Offered to guests for appreciation; never touch the tip with bare fingers.")],
  checks=[("Name & tube","Value centers on a signed tube and box. A loose scoop without them is worth much less."),
          ("Breaks & worm holes","Inspect the tip for chips and the shaft for insect damage; some are lacquer-repaired."),
          ("The bamboo's landscape","Groove, speckles and staining are matters of taste — choose what pleases you."),
          ("Maker","Scoops by grand masters command far higher prices than workshop pieces.")]),

dict(slug="natsume", name="Natsume", jp="棗", en="Tea Caddy", num="04",
  tags=["Core utensil","Lacquerware","For thin tea"],
  lede="A lacquered caddy for thin-tea matcha, named for its jujube-fruit silhouette.",
  names=[("Name","Natsume 棗 (\"jujube\")"),("Sizes","Large (ō-natsume), medium, small"),
         ("Finishes","Plain black shin-nuri, tame-nuri, maki-e gold designs, mother-of-pearl")],
  history=["The natsume is a Japanese invention, attributed to the Muromachi-era lacquerer Haneda Gorō. Against the ceramic chaire used for thick tea, the light lacquered natsume became the standard container for thin tea.",
    "From Rikyū's preferred plain black to later caddies painted with the four seasons in gold maki-e, the palm-sized vessel concentrates the essence of Japanese lacquer craft."],
  parts_dots=[(80,14),(56,38),(80,60),(80,96)],
  parts=[("Futa / kō (lid & crown)","The top face — the showpiece for maki-e"),
         ("Aikuchi (joint)","Where lid meets body; precision here is the mark of quality"),
         ("Dō (body)","The gently swelling side"),
         ("Soko (base)","May carry the maker's signature")],
  usage=[("Handling","Rest it on the left palm and purify the lid with the fukusa in the prescribed strokes."),
         ("Filling","Mound the matcha softly like a small mountain; sift it just before use."),
         ("Care","Never wash with water. Wipe with a soft dry cloth and store in its wooden box.")],
  checks=[("Lacquer condition","Look for cracks, flaking and dulling. Sun-fading cannot be reversed."),
          ("Fit of the lid","A fine caddy's lid settles with a gentle sigh. Rattling or looseness is a warning."),
          ("Maki-e wear","Gold designs wear with use — zoom in on photos to confirm the outlines survive."),
          ("Box & maker","A signed box, and origins such as Wajima or Yamanaka, guide the price.")]),

dict(slug="kama", name="Kama", jp="茶釜", en="Iron Kettle", num="05",
  tags=["Core utensil","Cast iron","Ro & furo"],
  lede="The iron kettle whose simmering voice — matsukaze, \"wind in the pines\" — is the sound of the tea room.",
  names=[("Name","Kama 茶釜 (\"tea kettle\")"),("Famous origins","Ashiya (Chikuzen), Tenmyō (Shimotsuke), Kyoto"),
         ("By season","Winter: large kettle in the sunken hearth / Summer: smaller kettle on the brazier")],
  history=["Tea kettles flourished from the 14th century at two great centers: Ashiya, famed for elegant relief designs, and Tenmyō, loved for its rugged skin. Both names still stand for the finest old kettles.",
    "In the Momoyama era the Kyoto casters of Sanjō Kamanza rose, and Rikyū's kettle-maker Tsuji Yojirō defined the wabi kettle. Ranked \"worth a province and a castle,\" the kama sets the tone of the whole room."],
  parts_dots=[(80,22),(80,36),(36,58),(80,70),(80,100)],
  parts=[("Tsumami & futa (knob & lid)","Lids of bronze or iron; the knob is a detail to savor"),
         ("Kuchi (mouth)","Where water is drawn; shapes vary from uba-guchi to wide"),
         ("Kantsuki (lugs)","The ears that take the rings for lifting"),
         ("Dō / hada (body & skin)","The cast surface landscape — hailstone (arare) and other patterns"),
         ("Soko (bottom)","Wears first; old kettles often have replaced bottoms")],
  usage=[("Tending the water","Bring the water to the matsukaze stage over charcoal or an electric hearth."),
         ("Drawing","Draw quietly with the hishaku; lid handling follows its own etiquette."),
         ("Drying","Empty after use and dry completely with residual heat — never leave it wet.")],
  checks=[("Leak test","Fill overnight and check for seepage. Small leaks can sometimes be sealed."),
          ("Rust","Light surface rust can be tamed; deep interior corrosion cannot. A seasoned mineral scale is a virtue."),
          ("Replaced bottom","Common in old kettles and no flaw if done by a kettle-smith."),
          ("Lid & rings","Confirm whether the original lid, rings and trivet accompany the kettle.")]),

dict(slug="hishaku", name="Hishaku", jp="柄杓", en="Water Ladle", num="06",
  tags=["Core utensil","Bamboo craft","Ro & furo"],
  lede="A bamboo ladle for hot and cold water. Its single, silent pour is one of the beauties of the procedure.",
  names=[("Name","Hishaku 柄杓 (\"ladle\")"),("By season","Ro: larger cup, end cut on the inner face / Furo: smaller cup, cut on the outer face"),
         ("Note","Garden (tsukubai) ladles are a different item")],
  history=["Water ladles are ancient ritual objects, but tea refined the bamboo hishaku into a centerpiece of the procedure, with dimensions that change between hearth and brazier seasons.",
    "A fresh white-bamboo ladle is itself hospitality — its clean pallor honors the guest, and long use turns the cup a warm amber."],
  parts_dots=[(46,64),(62,72),(100,53),(138,34)],
  parts=[("Gō (cup)","The vessel that holds the water"),
         ("Tsukigata","The crescent cut where cup meets handle"),
         ("E (handle)","The long stem with its fixed node position"),
         ("Kiridome (end cut)","Bevelled opposite ways for ro and furo")],
  usage=[("The stance","Held in the \"mirror ladle\" pose, as if reflecting one's own heart."),
         ("Drawing & pouring","Pour in a single thread; what remains never returns to the kettle."),
         ("Hiki-bishaku","In the brazier season, the ladle is drawn back with extended fingers — a famously graceful move.")],
  checks=[("New for use","Cleanliness comes first at tea; treat secondhand ladles as practice or display pieces."),
          ("Cracks & warp","Dry storage splits the cup; check the handle for bowing."),
          ("Ro or furo","Identify by the end cut and cup size, and match your season of practice."),
          ("Sashi-tōshi","One-piece cup-and-handle ladles rank highest; check joint precision otherwise.")]),

dict(slug="fukusa", name="Fukusa", jp="帛紗", en="Silk Cloth", num="07",
  tags=["Core utensil","Textile","Worn by the host"],
  lede="The silk cloth that purifies the utensils. Folding it — fukusa-sabaki — settles the mind as much as it cleans.",
  names=[("Name","Fukusa 帛紗"),("Size","About 27 × 28 cm; shioze silk is standard"),
         ("Color custom","Purple for men, red or vermilion for women (varies by school); dashibukusa and kobukusa are separate items")],
  history=["The fukusa's form is credited to Sōon, wife of Rikyū, who devised it for purifying utensils. Worn at the host's waist, it became the very badge of the person making tea.",
    "Beyond plain shioze silk, kobukusa and dashibukusa woven with famous meibutsu-gire patterns accompany the bowl in thick tea — a whole history of textiles folded into one small square."],
  parts_dots=[(42,26),(118,26),(72,56),(110,88)],
  parts=[("Wasa (fold)","The folded edge, the reference side for handling"),
         ("Mimi (edges)","The raw selvedge sides"),
         ("Kado (corners)","Where the fingers take hold in the folding sequence"),
         ("Ji (cloth)","Shioze silk; its body decides the handling")],
  usage=[("Wearing","Tucked at the left waist — the sign of the host."),
         ("Folding","The shihō-sabaki sequence dusts the cloth, then folds it to wipe caddy and scoop."),
         ("Care","Silk hates water. When soiled, replace it — it is a consumable.")],
  checks=[("Prefer new","A purifying cloth is best bought new."),
          ("If secondhand","Kobukusa in meibutsu-gire weaves are the exception — a rich vintage market. Verify the pattern name and age."),
          ("Body of the silk","A limp, tired cloth folds badly and frustrates practice."),
          ("School color","Match the color custom of your school and role.")]),

dict(slug="mizusashi", name="Mizusashi", jp="水指", en="Water Jar", num="08",
  tags=["Core utensil","Ceramics & more","Anchor of the display"],
  lede="The jar of fresh water that anchors the arrangement of the tea-making place.",
  names=[("Name","Mizusashi 水指 (\"fresh-water jar\")"),("Materials","Ceramic, bentwood, glass, metal"),
         ("Lids","Tomobuta (matching) or nuributa (lacquered replacement)")],
  history=["The mizusashi began as kitchen ware promoted to the tea room. Shigaraki seed jars and Bizen pots taken up by \"mitate\" — the eye that finds beauty in the ordinary — express the wabi spirit perfectly.",
    "From Chinese celadon to Shino and Oribe, bentwood and summer glass, no utensil offers a wider choice; it is selected to suit the season and formality of each gathering."],
  parts_dots=[(80,28),(52,38),(80,64),(80,102)],
  parts=[("Futa (lid)","Matching or lacquered; each has its own handling"),
         ("Kuchi (mouth)","Wide or narrow — affecting the ladle's reach"),
         ("Dō (body)","The stage for the glaze landscape"),
         ("Soko (base)","A stable seat on the tatami matters")],
  usage=[("Placing","Carried out to the tea-making place, it composes the scene."),
         ("Adding water","Near the end, one ladleful refreshes the kettle."),
         ("Lids","Wipe lacquered lids dry; open matching lids gently, minding chips.")],
  checks=[("Lid damage","The lid suffers first — check for chips and re-lacquering."),
          ("Cracks & leaks","It holds water, so hairlines matter practically. Ask whether it has been water-tested."),
          ("Replacement lids","A lacquered replacement lid is common and no demerit in itself."),
          ("Box & provenance","A signed box or documented history lifts both display value and price.")]),
]

MINOR_EN = [
 dict(slug="chaire", name="Chaire", jp="茶入", en="Thick-tea Caddy",
      desc="A small ceramic jar for thick-tea matcha, kept in a silk pouch (shifuku) with an ivory lid — ranked above the natsume."),
 dict(slug="kensui", name="Kensui", jp="建水", en="Waste-water Bowl",
      desc="Receives the rinse water. Also called koboshi, it works discreetly out of the guests' view."),
 dict(slug="futaoki", name="Futaoki", jp="蓋置", en="Lid Rest",
      desc="A small stand for the kettle lid and ladle — plain cut bamboo at its most basic, celadon or painted porcelain at its most playful."),
 dict(slug="kogo", name="Kōgō", jp="香合", en="Incense Container",
      desc="Holds the incense for the charcoal procedure: kneaded incense in ceramic for the hearth season, sandalwood in lacquer for the brazier."),
 dict(slug="hanaire", name="Hanaire", jp="花入", en="Flower Vessel",
      desc="Bamboo, celadon or Iga ware for the tea flowers. \"Arrange them as they stand in the field,\" taught Rikyū."),
 dict(slug="kakemono", name="Kakemono", jp="掛物", en="Hanging Scroll",
      desc="The scroll in the alcove. A single line of Zen ranks highest — \"no utensil comes before the scroll,\" said Rikyū."),
 dict(slug="furo", name="Furo", jp="風炉", en="Brazier",
      desc="The portable hearth for May through October, in bronze, clay or iron; shaping its ash bed is part of the host's art."),
 dict(slug="kashiki", name="Kashiki", jp="菓子器", en="Sweets Vessel",
      desc="For the sweets that precede tea: tiered fuchidaka for moist sweets, trays for dry ones. Sweets are part of the tea."),
]

# ---------------------------------------------------------------- pages ----
def card_en(t):
    return f'''<a class="tool-card reveal" href="tools/{t["slug"]}.html">
  <span class="tool-num">{t["num"]}</span>
  <div class="tool-art">{ART[t["slug"]]}</div>
  <h3 class="tool-name">{t["name"]}</h3>
  <p class="tool-yomi">{t["jp"]} — {t["en"]}</p>
  <p class="tool-desc">{t["lede"]}</p>
  <p class="tool-more">READ MORE →</p>
</a>'''

def minor_card_en(m):
    return f'''<div class="tool-card plain reveal">
  <div class="tool-art">{ART[m["slug"]]}</div>
  <h3 class="tool-name">{m["name"]}</h3>
  <p class="tool-yomi">{m["jp"]} — {m["en"]}</p>
  <p class="tool-desc">{m["desc"]}</p>
</div>'''

# ---- index ----
index_body = f'''
<section class="hero">
  <svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M100 18 a82 82 0 1 0 60 26" fill="none" stroke="#2b2a26" stroke-width="10" stroke-linecap="round"/>
  </svg>
  <div class="hero-inner">
    <p class="hero-kicker">USED JAPANESE TEA UTENSILS — 中古茶道具ポータル</p>
    <h1 class="hero-title">Tea utensils,<br>made friendly.</h1>
    <p class="hero-sub">Easy to understand. Easy to hold. Easy to buy.<br>A guide to the beautiful, bewildering world of Japanese tea utensils — and to giving old pieces a new hand.</p>
    <div class="hero-cta">
      <a class="btn solid" href="tools.html">BROWSE THE UTENSILS</a>
      <a class="btn" href="guide.html">HOW A BOWL IS MADE</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="intro-grid">
    <div class="reveal">
      <p class="intro-tate">One utensil is enough<br>to begin the pleasure of tea.<small>— YUSANDO ANTIQUE GALLERY</small></p>
    </div>
    <div class="intro-text reveal">
      <p class="section-kicker" style="text-align:left;text-indent:0">ABOUT THIS SITE</p>
      <p>"Tea utensils seem… difficult." Unreadable names, unguessable prices, intricate etiquette — it can feel like a world with no front door.</p>
      <p>Yusando Antique Gallery exists to open one. For each utensil we explain the name and its reading, the history, the parts, how it is used — and what to look for when buying secondhand — in plain language for first-timers.</p>
      <p>The difficult parts can wait. Find one piece you like, keep it near your daily life, and tea utensils quickly become friendly. An online shop connection is on its way.</p>
    </div>
  </div>
</section>

<section class="section" style="background:transparent;padding-top:0">
  <div class="section-head reveal">
    <p class="section-kicker">THE UTENSILS</p>
    <h2 class="section-title">Start with Eight Essential Pieces</h2>
    <div class="rule"></div>
    <p class="section-lede">The indispensable utensils of the tea procedure. Each detail page covers history, parts, use, and secondhand buying points.</p>
  </div>
  <div class="tools-grid">
    {"".join(card_en(t) for t in TOOLS_EN[:4])}
  </div>
  <div style="text-align:center;margin-top:44px">
    <a class="btn" href="tools.html">VIEW ALL UTENSILS</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:44px">
    <p class="section-kicker">READING</p>
    <h2 class="section-title">Go a Little Deeper</h2>
    <div class="rule"></div>
  </div>
  <div class="article-cards">
    <a class="article-card reveal" href="articles/chawan-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Bowls</h3>
      <p>Raku, Hagi and Karatsu; tenmoku and ido. The lineages, kilns and shapes — sorted for choosing.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/history.html">
      <p class="a-kicker">HISTORY</p><h3>A History of the Tea Ceremony</h3>
      <p>How one cup of medicine from China became, over a thousand years, a Way. A timeline in seven eras.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Whisks</h3>
      <p>Tine counts, bamboo colors, schools. How to choose your chasen, explained for beginners.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/sekki.html">
      <p class="a-kicker">SEASON</p><h3>The 24 Solar Terms &amp; Tea Utensils</h3>
      <p>From Risshun to Daikan — a year-round calendar of seasonal utensil pairings.</p>
      <p class="tool-more">READ →</p>
    </a>
  </div>
</section>

<section class="care">
  <div class="section tight">
    <div class="section-head reveal" style="margin-bottom:44px">
      <p class="section-kicker">CARE</p>
      <h2 class="section-title">Living Long with Your Utensils</h2>
    </div>
    <div class="care-grid reveal">
      <div class="care-cell"><h3>Tea Bowl <span class="en-sub">CHAWAN</span></h3><p>Warm water only, no detergent. Dry fully before boxing; soak new ceramics overnight before first use.</p></div>
      <div class="care-cell"><h3>Whisk <span class="en-sub">CHASEN</span></h3><p>Rinse in hot water and air-dry tines-up. A shaping stand keeps its curve.</p></div>
      <div class="care-cell"><h3>Lacquer <span class="en-sub">NATSUME</span></h3><p>Never wash with water — a soft dry cloth only. Store in its paulownia box, away from sun.</p></div>
      <div class="care-cell"><h3>Iron <span class="en-sub">KAMA</span></h3><p>Empty and dry with residual heat. The mineral scale protects it — never scrub, never soap.</p></div>
    </div>
  </div>
</section>

<section class="section reveal" style="text-align:center">
  <p class="section-kicker">SHOP</p>
  <h2 class="section-title">Online Shop — Coming Soon</h2>
  <div class="rule"></div>
  <p class="section-lede">This site is built to connect to an online shop, so each utensil page will show pre-loved pieces available right now. The listing slots on the detail pages are waiting for it.</p>
  <div style="margin-top:30px"><span class="btn" style="opacity:.5;cursor:default">SHOP (COMING SOON)</span></div>
</section>
'''
w("en/index.html", shell_en("Yusando Antique Gallery — Used Japanese Tea Utensils",
  "A friendly portal for pre-loved Japanese tea utensils: names, history, parts, use, and how to buy secondhand.",
  index_body, root="../", current="home"))

# ---- tools list ----
tools_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">LIST OF UTENSILS</p>
    <h2 class="section-title">The Japanese Tea Utensils</h2>
    <div class="rule"></div>
    <p class="section-lede">The principal utensils of chanoyu. Those with detail pages go deeper — history, parts, use, and secondhand buying points.</p>
  </div>
  <div class="cat-head reveal"><h2>Utensils of the Procedure</h2><span class="en-sub">DETAIL PAGES AVAILABLE</span></div>
  <div class="tools-grid">
    {"".join(card_en(t) for t in TOOLS_EN)}
  </div>
  <div class="cat-head reveal"><h2>Further Utensils</h2><span class="en-sub">OVERVIEW</span></div>
  <div class="tools-grid">
    {"".join(minor_card_en(m) for m in MINOR_EN)}
  </div>
</section>
'''
w("en/tools.html", shell_en("The Utensils — Japanese Tea Utensil List | Yusando Antique Gallery",
  "A list of Japanese tea ceremony utensils with names, readings, and roles.",
  tools_body, root="../", current="tools"))

# ---- guide ----
guide_steps_en = [
 ("1","Purify","The caddy and scoop are wiped with the <a href='tools/fukusa.html'>fukusa</a>; the <a href='tools/chasen.html'>whisk</a> and <a href='tools/chawan.html'>bowl</a> are rinsed with hot water."),
 ("2","Measure","Matcha is scooped from the <a href='tools/natsume.html'>natsume</a> into the bowl — about a scoop and a half (2 g)."),
 ("3","Pour","Hot water is drawn from the <a href='tools/kama.html'>kettle</a> with the <a href='tools/hishaku.html'>hishaku</a> and poured gently."),
 ("4","Whisk","The chasen moves briskly until the tea stands smooth and fine-frothed."),
 ("5","Offer","The bowl is turned so its face greets the guest, and the tea is served."),
]
guide_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">HOW THE UTENSILS WORK</p>
    <h2 class="section-title">How a Bowl Comes to Be</h2>
    <div class="rule"></div>
    <p class="section-lede">Each utensil is taken up in turn, does its work, and returns to rest. A simplified outline of the thin-tea procedure.</p>
  </div>
  <div class="temae-list reveal">
    {"".join(f'<div class="temae-item"><span class="temae-step">{a}</span><div class="temae-body"><h3>{b}</h3><p>{c}</p></div></div>' for a,b,c in guide_steps_en)}
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:40px">
    <p class="section-kicker">A FIRST SET</p>
    <h2 class="section-title">The Minimum Kit</h2>
    <div class="rule"></div>
  </div>
  <div class="check-grid reveal" style="max-width:820px;margin-left:auto;margin-right:auto">
    <div class="check-cell"><h3>A bowl at home</h3><p>A chawan, chasen and chashaku are enough to whisk matcha. A kettle from the kitchen and a tea tin will stand in for the rest.</p></div>
    <div class="check-cell"><h3>Starting lessons</h3><p>Add the personal four: fukusa, folding fan, kaishi paper and a sweets pick. Colors and sizes vary by school — ask your teacher.</p></div>
    <div class="check-cell"><h3>Where secondhand shines</h3><p>Bowls, caddies, water jars and kensui have rich vintage markets. The whisk and fukusa are best bought new.</p></div>
    <div class="check-cell"><h3>In what order</h3><p>Don't buy everything at once. Named scoops and kettles reward a trained eye — let your practice lead your collection.</p></div>
  </div>
</section>

<section class="section reveal" style="text-align:center;padding-top:30px">
  <p class="words-quote" style="font-size:clamp(20px,3vw,27px);letter-spacing:.12em;line-height:2">"Without famous utensils,<br>one cannot practice tea."</p>
  <p class="en-sub" style="margin-top:16px">— THE IDEA RIKYŪ REFUSED</p>
  <p class="section-lede" style="margin-top:22px">Sen no Rikyū taught that tea needs sincerity, not treasures. To use one modest set with care, year after year — living with pre-loved utensils is that teaching in practice.</p>
</section>
'''
w("en/guide.html", shell_en("How It Works — The Thin-Tea Procedure | Yusando Antique Gallery",
  "How the tea utensils are used: the thin-tea procedure step by step, and a first-set guide.",
  guide_body, root="../", current="guide"))

print("en core pages done")

# ---------------------------------------------------------------- setup ----
FURO_DIAG_EN = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">Host's mat (simplified)</text>
<rect x="76" y="30" width="40" height="40" fill="none" stroke="#a53f2b" stroke-width="1.6"/>
<circle cx="96" cy="50" r="14" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="96" y="83" text-anchor="middle" class="dg-label strong">Furo + kettle</text>
<text x="96" y="94" text-anchor="middle" class="dg-label">(on its board)</text>
<circle cx="152" cy="48" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="152" y="76" text-anchor="middle" class="dg-label strong">Water jar</text>
<circle cx="120" cy="136" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="120" y="162" text-anchor="middle" class="dg-label strong">Host</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">Guests</text>
</svg>'''
RO_DIAG_EN = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">Host's mat (simplified)</text>
<rect x="146" y="96" width="40" height="40" fill="#e2d8c2" stroke="#a53f2b" stroke-width="2"/>
<circle cx="166" cy="116" r="13" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="166" y="150" text-anchor="middle" class="dg-label strong">Ro + kettle</text>
<circle cx="120" cy="46" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="120" y="74" text-anchor="middle" class="dg-label strong">Water jar</text>
<circle cx="104" cy="120" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="96" y="146" text-anchor="middle" class="dg-label strong">Host</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">Guests</text>
</svg>'''

def ck_en(name, note, link=None):
    label = f'<a href="tools/{link}.html">{name}</a>' if link else name
    return (f'<label class="ck"><input type="checkbox">'
            f'<span class="ck-name">{label}</span>'
            f'<span class="ck-note">{note}</span></label>')

setup_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">SEASONAL SETUP</p>
    <h2 class="section-title">Ro and Furo — The Two Seasons of Tea</h2>
    <div class="rule"></div>
    <p class="section-lede">The tea year is divided by where the fire sits. In winter the hearth is cut into the floor and brought near the guests (ro); in summer a brazier keeps the fire away and lends coolness (furo). The whole arrangement — and many utensils — change with it.</p>
  </div>

  <div class="reveal">
    <div class="season-band">
      <div class="ro">RO Nov</div><div class="ro">Dec</div><div class="ro">Jan</div><div class="ro">Feb</div><div class="ro">Mar</div><div class="ro">Apr</div>
      <div class="fu">FURO May</div><div class="fu">Jun</div><div class="fu">Jul</div><div class="fu">Aug</div><div class="fu">Sep</div><div class="fu">Oct</div>
    </div>
    <p class="cmp-note">The November "opening of the hearth" (robiraki) is called the tea person's New Year; the first furo in May turns the room to summer.</p>
  </div>

  <div class="layout-grid reveal">
    <div class="layout-card">
      <h3>The Furo Arrangement<span class="en-sub">MAY TO OCTOBER</span></h3>
      {FURO_DIAG_EN}
      <p class="cap">The summer stance: fire kept from the guests to suggest coolness. The brazier sits on its board with a smaller kettle; shaping its ash bed is part of the host's art.</p>
    </div>
    <div class="layout-card">
      <h3>The Ro Arrangement<span class="en-sub">NOVEMBER TO APRIL</span></h3>
      {RO_DIAG_EN}
      <p class="cap">The winter stance: a hearth cut into the tatami, its warmth shared with the guests. The kettle grows larger and its simmering voice richer.</p>
    </div>
  </div>
  <p class="cmp-note reveal">* Simplified diagrams for the standard (hongatte) carrying procedure. Positions vary with the hearth cut and the school.</p>

  <div class="reveal">
    <table class="cmp-table">
      <thead><tr><th style="width:8em;background:var(--paper-deep);color:var(--matcha)"></th><th>RO (hearth)</th><th class="furo-col">FURO (brazier)</th></tr></thead>
      <tbody>
        <tr><th>Season</th><td>November – April (robiraki in November)</td><td>May – October (first furo in May)</td></tr>
        <tr><th>The fire</th><td>Sunk into the floor, near the guests — warmth shared</td><td>On the host's side, away from guests — coolness implied</td></tr>
        <tr><th><a href="tools/kama.html" style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)">Kettle</a></th><td>Large, set on a trivet; hanging and tsurube variants appear</td><td>Smaller, set on the brazier and its board</td></tr>
        <tr><th><a href="tools/hishaku.html" style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)">Ladle</a></th><td>Larger cup; end cut on the inner face</td><td>Smaller cup; end cut on the outer face</td></tr>
        <tr><th>Lid rest (bamboo)</th><td>Node at mid-height (naka-bushi), as a rule</td><td>Node at the top (ten-bushi), as a rule</td></tr>
        <tr><th>Charcoal &amp; incense</th><td>Larger charcoal; kneaded incense in a ceramic kōgō</td><td>Smaller charcoal; sandalwood in a lacquered kōgō</td></tr>
        <tr><th>The mood</th><td>Gathering around warmth; the deep, wabi season</td><td>"One taste of coolness"; water takes the leading role</td></tr>
      </tbody>
    </table>
    <p class="cmp-note">* Customs such as lid-rest nodes differ by school — your teacher's word comes first.</p>
  </div>
</section>

<section class="section tight" style="padding-top:20px">
  <div class="section-head reveal" style="margin-bottom:34px">
    <p class="section-kicker">CHECKLIST</p>
    <h2 class="section-title">What an Actual Procedure Requires</h2>
    <div class="rule"></div>
    <p class="section-lede">A checklist for the basic thin-tea "carrying" procedure (no display stand). Tick items off as you prepare.</p>
  </div>

  <div style="max-width:920px;margin:0 auto">
    <div class="ck-group reveal">
      <h3>1 — Set in place beforehand <span class="en-sub">据えておく道具</span></h3>
      <div class="ck-cols">
        {ck_en("Kettle","Water simmering — listen for the matsukaze","kama")}
        {ck_en("Ro or furo","Match the season (see the table above)")}
        {ck_en("Water jar","Filled about four-fifths, placed at the host's mat","mizusashi")}
        {ck_en("Charcoal & ash (or electric)","Ro: larger charcoal & kneaded incense / Furo: smaller & ash bed")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>2 — Carried in the bowl <span class="en-sub">茶碗に仕組む道具</span></h3>
      <div class="ck-cols">
        {ck_en("Tea bowl","Seasonal: shallow in summer, deep in winter","chawan")}
        {ck_en("Whisk","Inspect the tines; more tines for thin tea","chasen")}
        {ck_en("Scoop","Rested face-down on the bowl","chashaku")}
        {ck_en("Chakin","The linen cloth, folded in the prescribed way")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>3 — Also carried out <span class="en-sub">運び出す道具</span></h3>
      <div class="ck-cols">
        {ck_en("Tea caddy","Matcha sifted and mounded","natsume")}
        {ck_en("Kensui","Carried last, with lid rest and ladle set in it")}
        {ck_en("Ladle","Ro type or furo type — don't mix them up","hishaku")}
        {ck_en("Lid rest","Ro: mid node / Furo: top node (bamboo)")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>4 — Worn by the host <span class="en-sub">身に着けるもの</span></h3>
      <div class="ck-cols">
        {ck_en("Fukusa","At the left waist — the host's badge","fukusa")}
        {ck_en("Folding fan","Set before the knees at greetings")}
        {ck_en("Kaishi & sweets pick","The guest's essentials, too")}
        {ck_en("Kobukusa","In some schools, for viewing utensils and thick tea")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>5 — For the guests <span class="en-sub">客のための道具</span></h3>
      <div class="ck-cols">
        {ck_en("Sweets & vessel","Dry sweets on a tray for thin tea; moist sweets in fuchidaka for thick")}
        {ck_en("Cushions, tabako-bon etc.","For a full room, to match the formality")}
      </div>
    </div>
    <div class="reveal" style="margin-top:44px;border:1px solid var(--line);background:var(--paper-deep);border-radius:4px;padding:28px 26px">
      <h3 style="font-size:16px;letter-spacing:.14em;font-weight:500">What changes for thick tea <span class="en-sub">濃茶での違い</span></h3>
      <p style="font-size:13.5px;color:var(--ink-soft);margin-top:12px">The natsume gives way to the <strong>chaire</strong> in its silk pouch, a higher-ranked bowl is chosen, and a <strong>kobukusa or dashibukusa</strong> accompanies the bowl to the guests. One bowl is shared among several guests.</p>
    </div>
  </div>
</section>
'''
w("en/setup.html", shell_en("Ro & Furo Setup and the Full Utensil Checklist | Yusando Antique Gallery",
  "The winter hearth (ro) and summer brazier (furo) compared, with diagrams — plus a checklist of every utensil a thin-tea procedure needs.",
  setup_body, root="../", current="setup"))

# ---------------------------------------------------------------- articles ----
def article_shell_en(title, desc, kicker, h1, lede, body_secs):
    body = f'''
<div class="article-hero">
  <p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Reading</a> / {h1}</p>
  <p class="section-kicker">{kicker}</p>
  <h1 class="article-title">{h1}</h1>
  <p class="article-lede">{lede}</p>
</div>
<div class="detail-body">
{body_secs}
</div>
<nav class="pn">
  <a href="index.html">← ALL READING</a>
  <a href="../tools.html">THE UTENSILS</a>
</nav>
'''
    return shell_en(f'{title} | Yusando Antique Gallery', desc, body, root="../../", current="articles")

def sec_en(title, jp, inner):
    return f'''<section class="d-sec reveal">
  <h2>{title} <span class="en-sub">{jp}</span></h2>
  <div class="d-rule"></div>
  {inner}
</section>'''

def tcard_en(name, sub, desc, tip):
    return (f'<div class="type-card"><h3>{name}</h3><p class="t-sub">{sub}</p>'
            f'<p>{desc}</p><p class="t-tip">{tip}</p></div>')

# ---- article 1: chawan types ----
a1 = (
sec_en("Three Lineages","三つの系譜", '''
  <p>Tea bowls fall into three great lineages by birthplace: <strong>karamono</strong> from China, <strong>kōraimono</strong> from the Korean peninsula, and <strong>wamono</strong> made in Japan. Chinese pieces once stood at the top of the hierarchy, but as wabi tea spread, the unadorned beauty of Korean and Japanese bowls won tea people's hearts.</p>
  <p>One phrase worth remembering: <strong>"first Raku, second Hagi, third Karatsu"</strong> — the classic ranking of Japan's three beloved tea kilns.</p>''')
+ sec_en("The Major Types","主要な種類", '<div class="type-grid">'
+ tcard_en("Raku","KYOTO","Hand-built without a wheel and fired one at a time, created by Chōjirō for Rikyū's wabi taste. Black or red, light in the hand, wonderful to whisk in.","Plentiful study pieces make a fine first bowl.")
+ tcard_en("Hagi","YAMAGUCHI","Soft clay under a loquat-colored glaze. Tea seeps into its crackle and the bowl's face changes with use — \"the seven disguises of Hagi.\"","Check how far the crackle staining has advanced.")
+ tcard_en("Karatsu","SAGA","Gritty, forceful clay with rustic iron brushwork. E-garatsu, madara-garatsu, chōsen-garatsu — endless variety, never tiring.","Sturdy and easy to love for everyday bowls of tea.")
+ tcard_en("Shino","MINO","Japan's first white ware: thick feldspar glaze blushing red where the fire touched. The National Treasure \"Unohanagaki\" is a Shino.","Its warmth suits the winter months.")
+ tcard_en("Oribe","MINO","Green copper glaze and daringly warped shapes, after the taste of Furuta Oribe — tea's great eccentric.","Distortion is the point; choose by how it sits in the hand.")
+ tcard_en("Tenmoku","KARAMONO","Iron-black Chinese glaze with starry or oil-spot effects. Only three yōhen tenmoku exist — all in Japan, all National Treasures.","Fine modern reproductions abound; stand versions rank formal.")
+ tcard_en("Ido","KŌRAIMONO","Korean everyday bowls elevated by the tea eye: generous form, loquat glaze, and the shark-skin kairagi on the foot. The \"Kizaemon Ido\" is a National Treasure.","The kairagi shrinkage on the foot decides connoisseurs.")
+ tcard_en("Kyō ware","KYOTO","The polychrome elegance begun by Ninsei and Kenzan — four seasons painted on the bowl. A wide field of modern makers.","Match the painted motif to the season you'll use it.")
+ '</div>')
+ sec_en("Choosing by Shape","形で選ぶ", '''
  <table class="name-table">
    <tr><th>Hira (shallow)</th><td>Wide and open for summer — the tea cools quickly and looks cool too.</td></tr>
    <tr><th>Tsutsu (cylinder)</th><td>Deep winter bowl that keeps the warmth in your hands.</td></tr>
    <tr><th>Wan-nari</th><td>The standard bowl form, at home in any season.</td></tr>
    <tr><th>Han-zutsu</th><td>Between the two — for the cool ends of spring and autumn.</td></tr>
    <tr><th>Tenmoku-nari</th><td>The conical Chinese form, used in the most formal procedures.</td></tr>
    <tr><th>Kutsu-gata</th><td>The warped \"shoe\" shape loved by Oribe — full of movement.</td></tr>
  </table>
  <p style="margin-top:18px">If in doubt, begin with one wan-nari bowl; add the seasonal shapes later. The <a href="../tools/chawan.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">chawan basics page</a> covers parts and secondhand checkpoints.</p>'''))

w("en/articles/chawan-types.html", article_shell_en(
  "Types of Tea Bowls — Raku, Hagi, Karatsu and Beyond",
  "Tea bowl types by lineage (karamono, kōraimono, wamono), kiln (Raku, Hagi, Karatsu, Shino, Oribe, Tenmoku, Ido) and shape.",
  "READING — GUIDE","Types of Tea Bowls",
  "Raku, Hagi and Karatsu; Shino and Oribe; tenmoku and ido. Three axes — lineage, kiln and shape — put the famous names in order.",
  a1))

# ---- article 2: history ----
def tl_en(era, years, h, p):
    return (f'<div class="tl-item"><div class="tl-era">{era}<small>{years}</small></div>'
            f'<div class="tl-body"><h3>{h}</h3><p>{p}</p></div></div>')

a2 = (
sec_en("A Thousand Years","千年の流れ", '''
  <p>The history of the tea ceremony begins with a cup of medicine. Tea crossed from China, spread with Zen, met a native sense of beauty in objects, and became the composite art called chanoyu. The broad strokes, era by era:</p>
  <div class="tl">'''
+ tl_en("Nara–Heian","8th–12th c.","Tea Reaches Japan","Envoys to Tang China and the monks Saichō and Kūkai bring back tea — pressed bricks shaved and boiled, a medicine and ritual drink for courtiers and clergy.")
+ tl_en("Kamakura","12th–14th c.","Eisai and Powdered Tea","Eisai, founder of Rinzai Zen, imports the powdered-tea method and praises tea's virtues in the Kissa Yōjōki. Temple tea rites take root; samurai amuse themselves with tōcha tasting contests.")
+ tl_en("Muromachi","14th–15th c.","Shoin Tea and Chinese Treasures","The Ashikaga shoguns stage formal tea amid prized Chinese objects. Against this splendor, Murata Jukō finds beauty in plain things — \"a fine horse tethered to a thatched hut\" — and opens the way of wabi.")
+ tl_en("Momoyama","16th c.","Rikyū Perfects Wabi Tea","Through Takeno Jōō to Sen no Rikyū: the two-mat hut, the Raku bowl, the bamboo vase — an aesthetic of subtraction. Tea entwines with the politics of Nobunaga and Hideyoshi, and utensils become priceless.")
+ tl_en("Edo","17th–19th c.","The Three Houses and Daimyo Tea","Rikyū's great-grandsons found the Omote, Ura and Mushakōji Senke schools; Kobori Enshū and other daimyo masters cultivate \"refined rusticity.\" The iemoto system forms and tea reaches the townsfolk.")
+ tl_en("Meiji–Taishō","19th–20th c.","The Modern Collectors","Tea wavers in the rush to Westernize, then finds new patrons among industrialist collectors. It enters school curricula and spreads widely as an accomplishment for women.")
+ tl_en("Shōwa–today","20th c.–","Tea Opens to the World","Okakura Tenshin's *The Book of Tea* carries the spirit abroad. Museums display the great bowls, practice spreads overseas — and old utensils keep meeting new hands.")
+ '</div>')
+ sec_en("History, Seen Through the Utensils","道具から見る歴史", '''
  <p>The history of tea is the history of its utensils: the longing for tenmoku, the discovery of Korean bowls, the invention of Raku, the bamboo scoop and vase. Each era's sense of beauty survives in the pieces that still circulate today.</p>
  <p>To pick up an old utensil is to touch this thousand-year story. Browse <a href="../tools.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">the utensils</a> and find the piece that speaks to you.</p>'''))

w("en/articles/history.html", article_shell_en(
  "A History of the Tea Ceremony — A Thousand Years in Seven Eras",
  "The history of chanoyu from tea's arrival in Nara times through Eisai, Jukō and Rikyū to the three Senke schools and the modern day.",
  "READING — HISTORY","A History of the Tea Ceremony",
  "One cup of medicine became, over a thousand years, a Way. The story of tea and its utensils, in seven eras.",
  a2))

# ---- article 3: chasen types ----
a3 = (
sec_en("By Tine Count","穂数で選ぶ", '''
  <p>The chief variable of a whisk is its <strong>tine count</strong> — how many splints the bamboo is split into. Fewer tines are stiffer; more tines froth finer.</p>
  <table class="name-table">
    <tr><th>Araho (16–48)</th><td>Thick, strong tines for kneading thick tea.</td></tr>
    <tr><th>Kazuho (64–72)</th><td>The all-rounder — handles thin and thick tea alike. The natural first whisk.</td></tr>
    <tr><th>80-tine</th><td>Easy, fine frothing for thin tea; the practice standard.</td></tr>
    <tr><th>100 / 120-tine</th><td>Delicate tines give the softest froth — beginner-friendly, but fragile.</td></tr>
  </table>''')
+ sec_en("Bamboo Color and School","竹の色と流派", '<div class="type-grid">'
+ tcard_en("Shiratake (white)","URASENKE etc.","Bleached pale bamboo — the most widely sold. Urasenke favors tips curled inward.","Most retail whisks are white bamboo; easiest to find.")
+ tcard_en("Susutake (smoked)","OMOTESENKE","Amber bamboo smoked for decades over farmhouse hearths — now scarce and prized.","True susutake is costly; beware dyed imitations.")
+ tcard_en("Shichiku (black)","MUSHAKŌJI SENKE","Naturally dark \"purple\" bamboo with a taut, handsome look.","Some choose it purely for its looks — no school police here.")
+ '</div>'
+ '<p style="margin-top:18px">If you belong to a school, match its bamboo. If not, a white-bamboo kazuho or 80-tine whisk is the easy choice.</p>')
+ sec_en("Origin and Quality","産地と品質", '''
  <p>Nearly all Japanese-made whisks come from <strong>Takayama</strong> in Ikoma, Nara — the \"village of the chasen\" for five hundred years, and a government-designated Traditional Craft. One bamboo, one knife, a hundred tines bent one by one in hot water: entirely handwork.</p>
  <p>Cheaper imported whisks exist, but differ in evenness, durability and whisking feel. For daily use, a Takayama whisk repays itself.</p>''')
+ sec_en("Care and Retirement","手入れと替えどき", '''
  <p>A whisk is a consumable. When tines snap or the curl gives out, it has served. Rinse in hot water after use, dry tines-up in the shade, and rest it on a shaping stand. In May, old whisks are honored and retired at chasen-kuyō memorial services.</p>
  <p>For hygiene, buy whisks for actual use new. See also the <a href="../tools/chasen.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">chasen basics page</a>.</p>'''))

w("en/articles/chasen-types.html", article_shell_en(
  "Types of Tea Whisks — Tine Counts, Bamboo and Schools",
  "How to choose a chasen: tine counts (kazuho, 80-tine, 100-tine), bamboo colors by school, and the Takayama craft.",
  "READING — GUIDE","Types of Tea Whisks",
  "Kazuho or 80-tine, white bamboo or smoked. Even the smallest utensil has a logic to choosing it — here are the three axes.",
  a3))

# ---- article 4: sekki ----
def sk_en(name, romaji, date, fire, firelabel, note):
    return (f'<div class="sk-card"><div class="sk-top"><div><p class="sk-name">{name}</p>'
            f'<p class="sk-yomi">{romaji}</p></div><span class="sk-fire {fire}">{firelabel}</span></div>'
            f'<p class="sk-date">{date}</p><p class="sk-note">{note}</p></div>')

SEKKI_EN = {
"SPRING — 春": [
 sk_en("立春","RISSHUN — spring begins","c. Feb 4","ro","RO","Spring on the calendar. February's grand hearth and the last of the New Year willow; camellia and a plum branch for the alcove."),
 sk_en("雨水","USUI — snow to rain","c. Feb 19","ro","RO","Snow softens to rain. Dolls' festival motifs: shell-pair kōgō, peach-blossom bowls."),
 sk_en("啓蟄","KEICHITSU — insects wake","c. Mar 6","ro","RO","The hanging kettle lifts the fire from the floor; spring-field motifs on the bowl."),
 sk_en("春分","SHUNBUN — spring equinox","c. Mar 21","ro","RO","Equinox week. With Rikyū's memorial at month's end, a quiet, wabi arrangement suits."),
 sk_en("清明","SEIMEI — clear and bright","c. Apr 5","ro","RO","Full cherry blossom. The sukigi kettle hides the fire; let sakura bowls and caddies bloom."),
 sk_en("穀雨","KOKUU — grain rains","c. Apr 20","nagori","LAST RO","Rains for the seedlings. The hearth season closes, thoughts turn to the 88th-night new tea."),
],
"SUMMER — 夏": [
 sk_en("立夏","RIKKA — summer begins","c. May 6","fu","FURO","First furo: the whole room refitted. Green maple motifs, half a year from the jar-opening."),
 sk_en("小満","SHŌMAN — all things fill","c. May 21","fu","FURO","New-tea season. Young-leaf motifs and a green bamboo lid rest, all freshness."),
 sk_en("芒種","BŌSHU — grains sown","c. Jun 6","fu","FURO","The rains arrive. Hydrangea and firefly motifs; utensils that enjoy the sound of rain."),
 sk_en("夏至","GESHI — summer solstice","c. Jun 21","fu","FURO","Longest day. A shallow bowl and a glass water jar — coolness for the eyes."),
 sk_en("小暑","SHŌSHO — lesser heat","c. Jul 7","fu","FURO","Tanabata. Mulberry-leaf lid trick (habuta) and star-festival motifs; morning tea begins."),
 sk_en("大暑","TAISHO — greater heat","c. Jul 23","fu","FURO","Peak heat. The famous-water and wrung-cloth procedures serve coolness itself."),
],
"AUTUMN — 秋": [
 sk_en("立秋","RISSHŪN — autumn begins","c. Aug 8","fu","FURO","Autumn on the calendar. Slip one autumn-grass motif in among the lingering heat."),
 sk_en("処暑","SHOSHO — heat retreats","c. Aug 23","fu","FURO","Insect voices. Musashino-plain motifs; pampas grass in gold on the caddy."),
 sk_en("白露","HAKURO — white dew","c. Sep 8","fu","FURO","Dew glints white. Moon motifs take the lead, earthy bowls carry the season."),
 sk_en("秋分","SHŪBUN — autumn equinox","c. Sep 23","fu","NAKAOKI","Harvest-moon weeks. The brazier moves to the mat's center (nakaoki), edging the fire toward the guests."),
 sk_en("寒露","KANRO — cold dew","c. Oct 8","fu","NAKAOKI","Dew turns cold. Nakaoki continues, with motifs of fruit and turning leaves."),
 sk_en("霜降","SŌKŌ — first frost","c. Oct 23","nagori","NAGORI","The furo's farewell. A worn brazier and humble utensils — the year's most wabi tea."),
],
"WINTER — 冬": [
 sk_en("立冬","RITTŌ — winter begins","c. Nov 7","ro","RO","Robiraki and the jar-opening: the tea person's New Year, toasted with sweet zenzai."),
 sk_en("小雪","SHŌSETSU — light snow","c. Nov 22","ro","RO","First cold showers. Glossy-leaf and first-snow motifs; an Oribe shoe-shaped bowl shines."),
 sk_en("大雪","TAISETSU — heavy snow","c. Dec 7","ro","RO","Deep winter, short days. Toward evening gatherings (yobanashi) by lamplight."),
 sk_en("冬至","TŌJI — winter solstice","c. Dec 22","ro","RO","The sun turns. A yuzu kōgō wishes health; light returns from here."),
 sk_en("小寒","SHŌKAN — lesser cold","c. Jan 6","ro","RO","Into the cold — and hatsugama, the first kettle: knotted willow and festive stacked bowls."),
 sk_en("大寒","DAIKAN — greater cold","c. Jan 20","ro","RO","Coldest of all. A cylinder bowl and the wrung hot cloth hand warmth, steam and all, to the guest."),
]}

sekki_inner = '''
  <p>The 24 solar terms divide the year by the sun's path, and the tea room turns with them. There is no single correct pairing — but anticipating the season by half a step is the host's art. Here is the classic year, term by term.</p>
'''
for season, cards in SEKKI_EN.items():
    sekki_inner += f'<div class="sekki-season"><h3>{season}</h3><div class="sekki-grid">{"".join(cards)}</div></div>'
sekki_inner += '''
  <p style="margin-top:40px">For the ro–furo changeover itself, see <a href="../setup.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">Ro &amp; Furo Setup</a>.</p>
'''
w("en/articles/sekki.html", article_shell_en(
  "The 24 Solar Terms and Tea Utensils — A Year of Arrangements",
  "From Risshun to Daikan: seasonal tea-utensil pairings and arrangements for each of the 24 solar terms.",
  "READING — SEASON","The 24 Solar Terms &amp; Tea Utensils",
  "The tea year turns with the old solar calendar. From Risshun to Daikan, a term-by-term guide to seasonal arrangements.",
  sec_en("The Turning Year","一年のめぐり", sekki_inner)))

# ---- articles index ----
articles_index_body = '''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">READING — 読みもの</p>
    <h2 class="section-title">Go Deeper into Tea Utensils</h2>
    <div class="rule"></div>
    <p class="section-lede">Reading that makes choosing utensils more fun. Start anywhere.</p>
  </div>
  <div class="article-cards">
    <a class="article-card reveal" href="chawan-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Bowls</h3>
      <p>Raku, Hagi and Karatsu; tenmoku and ido. Lineages, kilns and shapes, sorted for choosing.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="history.html">
      <p class="a-kicker">HISTORY</p><h3>A History of the Tea Ceremony</h3>
      <p>How one cup of medicine became a Way — a thousand years in seven eras.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Whisks</h3>
      <p>Tine counts, bamboo colors, schools — choosing a chasen, explained simply.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="sekki.html">
      <p class="a-kicker">SEASON</p><h3>The 24 Solar Terms &amp; Tea Utensils</h3>
      <p>A year-round calendar of seasonal utensil pairings, from Risshun to Daikan.</p>
      <p class="tool-more">READ →</p>
    </a>
  </div>
</section>
'''
w("en/articles/index.html", shell_en("Reading — Tea Utensil Guides | Yusando Antique Gallery",
  "Guides to tea bowls, whisks, tea history and the seasonal calendar of utensils.",
  articles_index_body, root="../../", current="articles"))

print("en articles done")

# ---------------------------------------------------------------- EN details ----
def detail_en(t, i):
    prev_t = TOOLS_EN[(i-1) % len(TOOLS_EN)]
    next_t = TOOLS_EN[(i+1) % len(TOOLS_EN)]
    names_rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in t["names"])
    parts_items = "".join(
        f'<li><span class="p-num">{n}</span><div><span class="p-name">{p}</span><br><span class="p-note">{d}</span></div></li>'
        for n, (p, d) in enumerate(t["parts"], 1))
    steps = "".join(
        f'<div class="step"><span class="step-no">{n+1}</span><div class="step-body"><h3>{h}</h3><p>{p}</p></div></div>'
        for n, (h, p) in enumerate(t["usage"]))
    checks = "".join(f'<div class="check-cell"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["checks"])
    hist = "".join(f"<p>{p}</p>" for p in t["history"])
    tags = "".join(f'<span class="tag">{x}</span>' for x in t["tags"])
    body = f'''
<div class="detail-hero">
  <div class="detail-hero-inner">
    <div>
      <p class="crumbs"><a href="../index.html">Home</a> / <a href="../tools.html">Utensils</a> / {t["name"]}</p>
      <h1 class="detail-title">{t["name"]}</h1>
      <p class="detail-yomi">{t["jp"]} — {t["en"]}</p>
      <p class="detail-lede">{t["lede"]}</p>
      <div class="detail-tags">{tags}</div>
    </div>
    <div class="detail-art">{ART[t["slug"]]}</div>
  </div>
</div>

<div class="detail-body">
  <section class="d-sec reveal">
    <h2>Name &amp; Types <span class="en-sub">名前と種類</span></h2>
    <div class="d-rule"></div>
    <table class="name-table">{names_rows}</table>
  </section>
  <section class="d-sec reveal">
    <h2>History <span class="en-sub">歴史</span></h2>
    <div class="d-rule"></div>
    {hist}
  </section>
  <section class="d-sec reveal">
    <h2>Parts <span class="en-sub">部位の名称</span></h2>
    <div class="d-rule"></div>
    <div class="parts-wrap">
      <div class="parts-fig">{parts_svg(t["slug"], t["parts_dots"])}</div>
      <ol class="parts-list">{parts_items}</ol>
    </div>
  </section>
  <section class="d-sec reveal">
    <h2>How to Use <span class="en-sub">使い方</span></h2>
    <div class="d-rule"></div>
    <div class="steps">{steps}</div>
  </section>
  <section class="d-sec reveal">
    <h2>Buying Secondhand <span class="en-sub">中古で選ぶポイント</span></h2>
    <div class="d-rule"></div>
    <div class="check-grid">{checks}</div>
  </section>
  <section class="d-sec reveal">
    <h2>Available Pieces <span class="en-sub">この道具の在庫</span></h2>
    <div class="d-rule"></div>
    <div class="shop-stub" data-ec-category="{t["slug"]}">
      <div class="listing-slot" id="listings-{t["slug"]}"></div>
      <h3>Online Shop — Coming Soon</h3>
      <p>Once the shop is connected, pre-loved {t["en"].lower()}s available now will appear right here.</p>
      <button class="btn" disabled>VIEW STOCK — COMING SOON</button>
    </div>
  </section>
</div>

<nav class="pn">
  <a href="{prev_t["slug"]}.html">← {prev_t["name"]}</a>
  <a href="../tools.html">ALL UTENSILS</a>
  <a href="{next_t["slug"]}.html">{next_t["name"]} →</a>
</nav>
'''
    return shell_en(
        f'{t["name"]} ({t["en"]}) — History, Parts & How to Use | Yusando Antique Gallery',
        f'The {t["en"].lower()} ({t["name"]}, {t["jp"]}): its history, the names of its parts, how it is used, and what to check when buying secondhand.',
        body, root="../../", current="tools")

for i, t in enumerate(TOOLS_EN):
    w(f'en/tools/{t["slug"]}.html', detail_en(t, i))

# ---------------------------------------------------------------- lang links ----
# Inject JA<->EN switch links into every page's nav.
import glob, re

def inject(path, label, href):
    full = os.path.join(ROOT, path)
    html = open(full, encoding="utf-8").read()
    link = f'<a class="lang-sw" href="{href}" style="color:var(--gold);border:1px solid var(--line);border-radius:999px;padding:4px 14px;margin-left:6px">{label}</a>'
    if 'class="lang-sw"' in html:
        html = re.sub(r'<a class="lang-sw".*?</a>', link, html, count=1)
    else:
        html = html.replace('</nav>\n  </div>\n</header>', link + '\n    </nav>\n  </div>\n</header>')
        # fallback: insert before first </nav>
        if 'lang-sw' not in html:
            html = html.replace('</nav>', link + '</nav>', 1)
    open(full, "w", encoding="utf-8").write(html)

ja_pages = ["index.html","tools.html","setup.html","guide.html","articles/index.html",
            "articles/chawan-types.html","articles/history.html","articles/chasen-types.html","articles/sekki.html"] + \
           [f"tools/{t['slug']}.html" for t in TOOLS_EN]
for p in ja_pages:
    depth = p.count("/")
    prefix = "../" * depth
    inject(p, "EN", f"{prefix}en/{p}")
    inject(f"en/{p}", "日本語", f"{'../' * (depth+1)}{p}")
print("lang links injected")
