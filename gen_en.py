# -*- coding: utf-8 -*-
"""Generate the English version of the site under en/."""
import os
from gen import FONTS, ROOT
from icons import sprite as ico_sprite, icon as ico, parts_icon

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
{ico_sprite()}
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{root}en/index.html">
      <span class="brand-mark">YUSANDO ANTIQUE GALLERY</span>
      <span class="brand-sub">FLAT-PRICE TEA UTENSILS</span>
    </a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links">
      {nav("index.html","Home","home")}
      {nav("tools.html","Utensils","tools")}
      {nav("setup.html","Ro &amp; Furo","setup")}
      {nav("guide.html","Procedure","guide")}
      {nav("articles/index.html","Reading","articles")}
      {nav("index.html#about","About","about")}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="f-inner">
    <div>
      <p class="f-mark">YUSANDO ANTIQUE GALLERY <span class="en-sub">悠三堂古美術ギャラリー</span></p>
      <p class="f-note">Flat-price pre-loved tea utensils.<br>Choose by delight, not by price.</p>
    </div>
    <nav class="f-nav">
      <a href="{root}en/index.html">HOME</a>
      <a href="{root}en/tools.html">UTENSILS</a>
      <a href="{root}en/setup.html">RO &amp; FURO</a>
      <a href="{root}en/guide.html">PROCEDURE</a>
      <a href="{root}en/articles/index.html">READING</a>
      <a href="{root}en/index.html#about">ABOUT</a>
    </nav>
  </div>
  <p class="f-copy">© 2026 YUSANDO ANTIQUE GALLERY — Demo draft. Online shop integration coming soon.</p>
</footer>
<script src="{root}js/site.js"></script>
</body>
</html>'''

# ---------------------------------------------------------------- EN data ----
TOOLS_EN = [
dict(slug="chawan", level=1, name="Chawan", jp="茶碗", en="Tea Bowl", num="01",
  tags=["Core utensil","Ceramics","Chosen by season"],
  lede="The bowl in which tea is whisked and drunk — the utensil that most reveals the host's taste, chosen anew with every season.",
  names=[("Name","Chawan 茶碗 (\"tea bowl\")"),("Major kilns","Raku, Hagi, Karatsu, Shino, Tenmoku and more"),
         ("By season","Summer: shallow, open hira-jawan / Winter: deep tsutsu-jawan that keeps tea warm")],
  history=["The story of the chawan begins with Chinese tenmoku bowls, imported along with tea itself. In the Muromachi period these karamono (Chinese pieces) held the highest rank, but as wabi tea took shape, taste shifted toward Korean bowls and finally to Japanese wares.",
    "In the Momoyama era, the potter Chōjirō answered Sen no Rikyū's wabi aesthetic with the Raku bowl — shaped entirely by hand, without a wheel. The saying \"first Raku, second Hagi, third Karatsu\" ranks the beloved Japanese tea kilns, and bowls from all of them are still cherished in tea people's hands today."],
  parts_dots=[(124,34),(80,46),(38,56),(62,80),(80,96)],
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

dict(slug="chasen", level=1, name="Chasen", jp="茶筅", en="Tea Whisk", num="02",
  tags=["Core utensil","Bamboo craft","Consumable"],
  lede="A whisk carved from a single piece of bamboo. Takayama in Nara has made them for five hundred years.",
  names=[("Name","Chasen 茶筅 (\"tea whisk\")"),("Types","Kazuho (~72 tines), 80-tine, 100-tine, 120-tine; coarse araho for thick tea"),
         ("By school","Omotesenke: smoked bamboo / Urasenke: white bamboo / Mushakōji: black bamboo")],
  history=["The chasen is said to have been devised in the Muromachi period in Takayama, Nara, at the request of tea pioneer Murata Jukō. For five centuries since, Takayama has remained \"the village of the whisk,\" its techniques passed down within families.",
    "One length of bamboo is split into a hundred or more tines with a single knife, then each tine is bent inward or outward in hot water — handwork no machine can replace. It remains a designated Traditional Craft of Japan."],
  parts_dots=[(80,12),(89,59),(80,77),(80,94)],
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

dict(slug="chashaku", level=1, name="Chashaku", jp="茶杓", en="Tea Scoop", num="03",
  tags=["Core utensil","Bamboo craft","Carries a poetic name"],
  lede="A slender bamboo scoop for matcha. Small as it is, a named chashaku can carry the theme of an entire gathering.",
  names=[("Name","Chashaku 茶杓 (\"tea scoop\")"),("Mei","The poetic name given by its maker — often a season word or Zen phrase"),
         ("Accessories","The tomozutsu (maker-inscribed tube) and box strongly affect value")],
  history=["The scoop derives from Chinese ivory tea spoons, but wabi tea remade it in bamboo; its present form settled around the time of Takeno Jōō and Sen no Rikyū. Rikyū's own scoops — above all \"Namida\" (Tears), carved before his death — still move tea people today.",
    "It is the one utensil tea masters habitually carve themselves. The node's position divides scoops into moto-bushi, naka-bushi and fushi-nashi, and with a name and inscribed tube, a sliver of bamboo becomes the voice of the gathering."],
  parts_dots=[(131,29),(100,56),(67,81),(24,89)],
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

dict(slug="natsume", level=1, name="Natsume", jp="棗", en="Tea Caddy", num="04",
  tags=["Core utensil","Lacquerware","For thin tea"],
  lede="A lacquered caddy for thin-tea matcha, named for its jujube-fruit silhouette.",
  names=[("Name","Natsume 棗 (\"jujube\")"),("Sizes","Large (ō-natsume), medium, small"),
         ("Finishes","Plain black shin-nuri, tame-nuri, maki-e gold designs, mother-of-pearl")],
  history=["The natsume is a Japanese invention, attributed to the Muromachi-era lacquerer Haneda Gorō. Against the ceramic chaire used for thick tea, the light lacquered natsume became the standard container for thin tea.",
    "From Rikyū's preferred plain black to later caddies painted with the four seasons in gold maki-e, the palm-sized vessel concentrates the essence of Japanese lacquer craft."],
  parts_dots=[(80,30),(108,52),(80,72),(80,93)],
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

dict(slug="kama", level=2, name="Kama", jp="茶釜", en="Iron Kettle", num="05",
  tags=["Core utensil","Cast iron","Ro & furo"],
  lede="The iron kettle whose simmering voice — matsukaze, \"wind in the pines\" — is the sound of the tea room.",
  names=[("Name","Kama 茶釜 (\"tea kettle\")"),("Famous origins","Ashiya (Chikuzen), Tenmyō (Shimotsuke), Kyoto"),
         ("By season","Winter: large kettle in the sunken hearth / Summer: smaller kettle on the brazier")],
  history=["Tea kettles flourished from the 14th century at two great centers: Ashiya, famed for elegant relief designs, and Tenmyō, loved for its rugged skin. Both names still stand for the finest old kettles.",
    "In the Momoyama era the Kyoto casters of Sanjō Kamanza rose, and Rikyū's kettle-maker Tsuji Yojirō defined the wabi kettle. Ranked \"worth a province and a castle,\" the kama sets the tone of the whole room."],
  parts_dots=[(80,23),(101,43),(43,63),(80,74),(80,93)],
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

dict(slug="hishaku", level=2, name="Hishaku", jp="柄杓", en="Water Ladle", num="06",
  tags=["Core utensil","Bamboo craft","Ro & furo"],
  lede="A bamboo ladle for hot and cold water. Its single, silent pour is one of the beauties of the procedure.",
  names=[("Name","Hishaku 柄杓 (\"ladle\")"),("By season","Ro: larger cup, end cut on the inner face / Furo: smaller cup, cut on the outer face"),
         ("Note","Garden (tsukubai) ladles are a different item")],
  history=["Water ladles are ancient ritual objects, but tea refined the bamboo hishaku into a centerpiece of the procedure, with dimensions that change between hearth and brazier seasons.",
    "A fresh white-bamboo ladle is itself hospitality — its clean pallor honors the guest, and long use turns the cup a warm amber."],
  parts_dots=[(46,80),(64,64),(102,46),(138,27)],
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

dict(slug="fukusa", level=2, name="Fukusa", jp="帛紗", en="Silk Cloth", num="07",
  tags=["Core utensil","Textile","Worn by the host"],
  lede="The silk cloth that purifies the utensils. Folding it — fukusa-sabaki — settles the mind as much as it cleans.",
  names=[("Name","Fukusa 帛紗"),("Size","About 27 × 28 cm; shioze silk is standard"),
         ("Color custom","Purple for men, red or vermilion for women (varies by school); dashibukusa and kobukusa are separate items")],
  history=["The fukusa's form is credited to Sōon, wife of Rikyū, who devised it for purifying utensils. Worn at the host's waist, it became the very badge of the person making tea.",
    "Beyond plain shioze silk, kobukusa and dashibukusa woven with famous meibutsu-gire patterns accompany the bowl in thick tea — a whole history of textiles folded into one small square."],
  parts_dots=[(78,30),(120,48),(41,84),(80,60)],
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

dict(slug="mizusashi", level=2, name="Mizusashi", jp="水指", en="Water Jar", num="08",
  tags=["Core utensil","Ceramics & more","Anchor of the display"],
  lede="The jar of fresh water that anchors the arrangement of the tea-making place.",
  names=[("Name","Mizusashi 水指 (\"fresh-water jar\")"),("Materials","Ceramic, bentwood, glass, metal"),
         ("Lids","Tomobuta (matching) or nuributa (lacquered replacement)")],
  history=["The mizusashi began as kitchen ware promoted to the tea room. Shigaraki seed jars and Bizen pots taken up by \"mitate\" — the eye that finds beauty in the ordinary — express the wabi spirit perfectly.",
    "From Chinese celadon to Shino and Oribe, bentwood and summer glass, no utensil offers a wider choice; it is selected to suit the season and formality of each gathering."],
  parts_dots=[(80,28),(110,33),(80,62),(80,90)],
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
 dict(slug="chaire", level=1, name="Chaire", jp="茶入", en="Thick-tea Caddy",
      desc="A small ceramic jar for thick-tea matcha, kept in a silk pouch (shifuku) with an ivory lid — ranked above the natsume."),
 dict(slug="kensui", level=2, name="Kensui", jp="建水", en="Waste-water Bowl",
      desc="Receives the rinse water. Also called koboshi, it works discreetly out of the guests' view."),
 dict(slug="futaoki", level=2, name="Futaoki", jp="蓋置", en="Lid Rest",
      desc="A small stand for the kettle lid and ladle — plain cut bamboo at its most basic, celadon or painted porcelain at its most playful."),
 dict(slug="kogo", level=3, name="Kōgō", jp="香合", en="Incense Container",
      desc="Holds the incense for the charcoal procedure: kneaded incense in ceramic for the hearth season, sandalwood in lacquer for the brazier."),
 dict(slug="hanaire", level=3, name="Hanaire", jp="花入", en="Flower Vessel",
      desc="Bamboo, celadon or Iga ware for the tea flowers. \"Arrange them as they stand in the field,\" taught Rikyū."),
 dict(slug="kakemono", level=3, name="Kakemono", jp="掛物", en="Hanging Scroll",
      desc="The scroll in the alcove. A single line of Zen ranks highest — \"no utensil comes before the scroll,\" said Rikyū."),
 dict(slug="furo", level=2, name="Furo", jp="風炉", en="Brazier",
      desc="The portable hearth for May through October, in bronze, clay or iron; shaping its ash bed is part of the host's art."),
 dict(slug="kashiki", level=2, name="Kashiki", jp="菓子器", en="Sweets Vessel",
      desc="For the sweets that precede tea: tiered fuchidaka for moist sweets, trays for dry ones. Sweets are part of the tea."),

 dict(slug="ro", level=3, name="Ro", jp="炉", en="Sunken Hearth",
      desc="The hearth cut into the tatami from November to April. Cutting a ro is what turns a room into a tea room."),
 dict(slug="sumitori", level=3, name="Sumitori", jp="炭斗", en="Charcoal Basket",
      desc="The basket that carries charcoal for the sumi-demae, packed with tongs, feather brush, kettle rings and incense box."),
 dict(slug="haboki", level=3, name="Habōki", jp="羽箒", en="Feather Brush",
      desc="Three bound feathers — crane, hawk or wild goose — for sweeping ash from the hearth's edge, set differently for ro and furo."),
 dict(slug="hibashi", level=3, name="Hibashi", jp="火箸", en="Charcoal Tongs",
      desc="Metal tongs for laying charcoal: longer for the hearth, shorter for the brazier, with decorative heads."),
 dict(slug="haiki", level=3, name="Haiki", jp="灰器", en="Ash Container",
      desc="An unglazed vessel of damp ash, served with its spoon and scattered into the hearth during the charcoal procedure."),
 dict(slug="chatsubo", level=3, name="Chatsubo", jp="茶壺", en="Leaf-Tea Jar",
      desc="The great jar of leaf tea. Its seal is cut at the November kuchikiri gathering and the leaf ground to matcha — where the tea year begins."),
]

DETAIL_SLUGS_EN = {t["slug"] for t in TOOLS_EN}
ALL_BY_SLUG_EN = {t["slug"]: t for t in TOOLS_EN + MINOR_EN}

LV_EN = {
 1: ("LV.1", "A bowl today", "A handful of pieces and hot water"),
 2: ("LV.2", "Host a gathering", "Make tea in front of guests"),
 3: ("LV.3", "Keep a tea room", "Compose the setting itself"),
}

def lv_badge_en(level):
    tag, short, _ = LV_EN[level]
    return f'<span class="lv-badge lv{level}"><b>{tag}</b>{short}</span>'

LV_INTRO_EN = [
 (1, "Enjoy matcha at home",
  "A handful of pieces and a kettle of hot water — everything needed to whisk a bowl this afternoon. Starting here is entirely enough.",
  ["chawan", "chasen", "chashaku", "natsume", "chaire"],
  "Thin tea lives in the natsume, thick tea in the chaire. Add a linen chakin and a whisk-shaping stand and you are set; any plate will do for the sweets."),
 (2, "Host a tea gathering",
  "The utensils of temae — making tea in front of your guests, from boiling the water. With these you can hold a gathering of your own.",
  ["furo", "kama", "hishaku", "fukusa", "mizusashi", "kensui", "futaoki", "kashiki"],
  "An electric heater is fine for the fire. Begin with brazier, kettle, water jar and waste bowl, then build from there."),
 (3, "Keep a tea room",
  "The alcove, and the fire in the hearth. This is where the season is given form and the whole room becomes one composition.",
  ["ro", "kakemono", "hanaire", "kogo", "sumitori", "haboki", "hibashi", "haiki", "chatsubo"],
  "Scroll, flower vessel and incense box are the alcove's three. Basket, feather brush, tongs and ash container form the charcoal set, joined by the incense box."),
]

def lv_section_en():
    blocks = ""
    for level, title, lede, slugs, note in LV_INTRO_EN:
        tag, short, sub = LV_EN[level]
        names = "".join(
            f'<a class="lv-chip" href="tools/{s}.html">{ALL_BY_SLUG_EN[s]["name"]}</a>'
            if s in DETAIL_SLUGS_EN else
            f'<span class="lv-chip plain">{ALL_BY_SLUG_EN[s]["name"]}</span>'
            for s in slugs)
        blocks += (f'<div class="lv-card lv{level} reveal">'
                   f'<div class="lv-head"><span class="lv-tag">{tag}</span>'
                   f'<div><h3>{title}</h3><p class="lv-sub">{sub}</p></div></div>'
                   f'<p class="lv-lede">{lede}</p>'
                   f'<div class="lv-chips">{names}</div>'
                   f'<p class="lv-note">{note}</p></div>')
    return (f'<div class="lv-grid">{blocks}</div>')


# ---------------------------------------------------------------- pages ----
def card_en(t):
    return f'''<a class="tool-card reveal" href="tools/{t["slug"]}.html">
  <span class="tool-num">{t["num"]}</span>
  {lv_badge_en(t["level"])}
  <div class="tool-art">{ico(t["slug"])}</div>
  <h3 class="tool-name">{t["name"]}</h3>
  <p class="tool-yomi">{t["jp"]} — {t["en"]}</p>
  <p class="tool-desc">{t["lede"]}</p>
  <p class="tool-more">READ MORE →</p>
</a>'''

def minor_card_en(m):
    return f'''<div class="tool-card plain reveal">
  {lv_badge_en(m["level"])}
  <div class="tool-art">{ico(m["slug"])}</div>
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
    <p class="hero-kicker">FLAT-PRICE USED TEA UTENSILS — 均一価格の中古茶道具ポータル</p>
    <h1 class="hero-title">Choose the one<br>that delights you.</h1>
    <p class="hero-sub">A <strong>flat-price</strong> marketplace for pre-loved Japanese tea utensils, easy to enjoy even as a beginner.<br>No price-guessing — just pick the piece you like.</p>
    <div class="hero-cta">
      <a class="btn solid" href="tools.html">BROWSE THE UTENSILS</a>
      <a class="btn" href="guide.html">HOW A BOWL IS MADE</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="intro-grid">
    <div class="reveal">
      <p class="intro-tate">Choosing what you like<br>is reason enough.<small>— YUSANDO ANTIQUE GALLERY</small></p>
    </div>
    <div class="intro-text reveal">
      <p class="section-kicker" style="text-align:left;text-indent:0">ABOUT THIS SITE</p>
      <p>The hardest part of buying a tea utensil is usually the <strong>price</strong>. Two bowls that look alike can be three thousand yen or three hundred thousand. Without a trained eye it feels like a trap — so most people never reach out at all.</p>
      <p>Yusando Antique Gallery is a <strong>flat-price</strong> portal for pre-loved tea utensils. With the price-comparing removed, what remains is the only measure that matters: <strong>whether a piece delights you</strong>. This glaze, this weight in the hand — that is reason enough.</p>
      <p>Knowing the names and the histories makes it richer still, so for every utensil we set out the reading, the story, the parts and the handling in plain language. The difficult parts can wait.</p>
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
    {"".join(card_en(t) for t in TOOLS_EN)}
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
    <a class="article-card reveal" href="articles/kama-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Kama</h3>
      <p>Ashiya, Tenmyō and Kyoto, and every shape from shinnari to unryū.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/chaire-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Chaire</h3>
      <p>Katatsuki, nasu, bunrin — the thick-tea caddy read through its shapes and its pouch.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/natsume-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Natsume</h3>
      <p>Sizes, lacquer finishes, and the wider family of thin-tea containers.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Whisks</h3>
      <p>Tine counts, bamboo colors, schools. How to choose your chasen, explained for beginners.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/history.html">
      <p class="a-kicker">HISTORY</p><h3>A History of the Tea Ceremony</h3>
      <p>How one cup of medicine from China became, over a thousand years, a Way. A timeline in seven eras.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/evolution.html">
      <p class="a-kicker">HISTORY</p><h3>The Evolution of Tea Utensils</h3>
      <p>Chinese treasures, mitate, and wares made in Japan — five centuries traced through six utensils.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="articles/sekki.html">
      <p class="a-kicker">SEASON</p><h3>The 24 Solar Terms &amp; Tea Utensils</h3>
      <p>Seasonal flowers, tea-scoop names, bowls and caddy motifs — the whole tea year, term by term.</p>
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
w("en/index.html", shell_en("Yusando Antique Gallery — Flat-Price Used Japanese Tea Utensils",
  "A flat-price portal for pre-loved Japanese tea utensils, easy to enjoy as a beginner: names, history, parts and how each one is used.",
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

  <div class="section-head reveal" style="margin-top:8px">
    <p class="section-kicker">HOW TO BUILD A SET — THREE LEVELS</p>
    <h2 class="section-title">Three levels to think in</h2>
    <div class="rule"></div>
    <p class="section-lede">You do not need all of it at once. Do you want a bowl of tea today, to invite people over, or to compose a room? Each answer needs a different set.</p>
  </div>
  {lv_section_en()}

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
  "Twenty-two Japanese tea ceremony utensils with names, readings and roles, sorted into three levels: drinking matcha at home, hosting a gathering, keeping a tea room.",
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
  <p class="words-quote" style="font-size:clamp(20px,3vw,27px);letter-spacing:.12em;line-height:2">“Without famous utensils,<br>one cannot practice tea.”</p>
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
        <tr><th>The mood</th><td>Gathering around warmth; the deep, wabi season</td><td>“One taste of coolness”; water takes the leading role</td></tr>
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
  "A History of the Tea Ceremony in Seven Eras",
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
  "Types of Tea Whisks — Tines, Bamboo, Schools",
  "How to choose a chasen: tine counts (kazuho, 80-tine, 100-tine), bamboo colors by school, and the Takayama craft.",
  "READING — GUIDE","Types of Tea Whisks",
  "Kazuho or 80-tine, white bamboo or smoked. Even the smallest utensil has a logic to choosing it — here are the three axes.",
  a3))

# ---- article 4: sekki ----
from sekki_art import MOTIF
from sekki_data import SEKKI_EN
from sekki_ko import KO_EN

def sk_en(key, kanji, romaji, date, fire, firelabel, note, hana, mei, chawan, natsume):
    rows = "".join(
        f'<div class="sk-row"><dt>{label}</dt><dd>{value}</dd></div>'
        for label, value in (("Flowers", hana), ("Scoop names", mei),
                             ("Bowl", chawan), ("Caddy motifs", natsume)))
    return (f'<div class="sk-card reveal">'
            f'<div class="sk-top"><div><p class="sk-name">{kanji}</p>'
            f'<p class="sk-yomi">{romaji}</p></div>'
            f'<span class="sk-fire {fire}">{firelabel}</span></div>'
            f'<p class="sk-date">{date}</p>'
            f'<div class="sk-motif">{MOTIF[key]}</div>'
            f'<p class="sk-note">{note}</p>'
            f'<dl class="sk-rows">{rows}</dl>'
            f'{ko_block_en(key)}</div>')

def ko_block_en(key):
    items = "".join(
        f'<div class="ko-item"><div class="ko-head">'
        f'<span class="ko-ord">{ordinal}</span>'
        f'<span class="ko-date">{date}</span></div>'
        f'<p class="ko-name">{kanji}<span class="ko-yomi">{romaji}</span></p>'
        f'<p class="ko-note">{note}</p></div>'
        for ordinal, kanji, romaji, date, note in KO_EN[key])
    return (f'<div class="ko-block"><p class="ko-label">72 KŌ'
            f'<span>MICRO-SEASONS</span></p>{items}</div>')

sekki_inner = """
  <p>The 24 sekki divide the solar year into two-week seasons, and the tea room turns with them. There is no single right answer in choosing utensils — but a tea person keeps half a step ahead of the season. Here is the whole year: the flowers, the poetic names carved on tea scoops, and the bowls and caddies that suit each term.</p>
  <p class="sk-legend"><span class="sk-fire ro">RO</span>Nov–Apr&nbsp;&nbsp;<span class="sk-fire fu">FURO</span>May–Oct&nbsp;&nbsp;<span class="sk-fire nagori">NAGORI</span>the turning weeks</p>
"""
for season, items in SEKKI_EN:
    cards = "".join(sk_en(*it) for it in items)
    sekki_inner += (f'<div class="sekki-season"><h3>{season}</h3>'
                    f'<div class="sekki-grid">{cards}</div></div>')
sekki_inner += """
  <p style="margin-top:44px">A mei is the poetic name a maker gives a tea scoop, and it carries the theme of the gathering. Those listed here are the well-worn classics — but a name is chosen by looking at the day's sky or garden, not from a rulebook. If a word moves you, that is your mei.</p>
  <p>The hearth-to-brazier changeover is covered in full on the <a href="../setup.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">Ro &amp; Furo</a> page.</p>
"""

w("en/articles/sekki.html", article_shell_en(
  "The 24 Solar Terms &amp; Tea Utensils",
  "Seasonal tea flowers, chashaku names, bowl and caddy motifs for each of the 24 solar terms, from Risshun to Daikan.",
  "READING — SEASON","The 24 Solar Terms",
  "The tea year turns with the calendar. Flowers, scoop names, bowls and caddy motifs for every one of the 24 terms.",
  sec_en("THE TURNING YEAR","一年のめぐり", sekki_inner)))

# ---- article 5: evolution ----
from evolution import TURNS_EN, EVO_EN, FORCES_EN, CLOSING_EN

def turn_card_en(i, name, era, body, tip):
    return (f'<div class="turn-card"><span class="turn-no">{i:02d}</span>'
            f'<h3>{name}</h3><p class="turn-era">{era}</p>'
            f'<p>{body}</p><p class="t-tip">{tip}</p></div>')

def evo_item_en(slug, name, en, steps):
    chain = ""
    for n, (era, label, note) in enumerate(steps):
        if n:
            chain += '<div class="evo-arrow" aria-hidden="true">→</div>'
        chain += (f'<div class="evo-step"><span class="evo-era">{era}</span>'
                  f'<p class="evo-name">{label}</p><p class="evo-note">{note}</p></div>')
    return (f'<div class="evo-item reveal"><div class="evo-head">'
            f'<div class="evo-art">{ico(slug)}</div>'
            f'<div><h3>{name}</h3><p class="evo-en">{en}</p></div></div>'
            f'<div class="evo-chain">{chain}</div></div>')

def force_row_en(name, en, body):
    return (f'<div class="force-row"><div class="force-name"><h3>{name}</h3>'
            f'<p class="en-sub">{en}</p></div><p>{body}</p></div>')

evolution_body = (
sec_en("THREE TURNS","三つの転換", '''
  <p>Over five centuries the tea utensil changed its meaning three times: an age that ranked imported treasures, an age that found beauty in ordinary vessels, and an age when tea masters had utensils made to their own design. Knowing the three turns, you can see which current a bowl in front of you came out of.</p>
  <div class="turn-grid">'''
+ "".join(turn_card_en(i, *t) for i, t in enumerate(TURNS_EN, 1))
+ '</div>')
+
sec_en("LINEAGES","道具別の系譜", '''
  <p>Utensils that share a name can look nothing alike from one century to the next. Here are six of them, traced from where they came to what they became.</p>'''
+ "".join(evo_item_en(*e) for e in EVO_EN))
+
sec_en("WHAT DROVE IT","進化を動かした三つの力", '''
  <p>Through all that change the tea utensil kept a single thread, and three habits of mind are the reason. Each is still at work whenever a utensil is chosen today.</p>'''
+ "".join(force_row_en(*f) for f in FORCES_EN))
+
sec_en("AND NOW","そして今", CLOSING_EN))

w("en/articles/evolution.html", article_shell_en(
  "The Evolution of Tea Utensils",
  "How tea utensils changed: the three turns of Chinese splendour, mitate and Japanese creation, traced through six utensils.",
  "READING — HISTORY","The Evolution of Tea Utensils",
  "From longing for Chinese treasures, to the discovery of mitate, to wares made in Japan — how one bowl changed shape over five hundred years.",
  evolution_body))

# ---- articles 6-8: kama / chaire / natsume types ----
from types_articles import kama_body_en, chaire_body_en, natsume_body_en

w("en/articles/kama-types.html", article_shell_en(
  "Types of Kama — Ashiya, Tenmyō and Kyoto",
  "Kettle types by origin (Ashiya, Tenmyo, Kyoto), by shape, by cast skin, and the difference between ro and furo kettles.",
  "READING — GUIDE", "Types of Kama",
  "Ashiya, Tenmyō and the Kyoto kettles. The utensil once called worth a province, sorted by origin, shape and skin.",
  kama_body_en(sec_en, tcard_en)))

w("en/articles/chaire-types.html", article_shell_en(
  "Types of Chaire — Katatsuki, Nasu, Bunrin",
  "Thick-tea caddies by origin (Chinese, Southeast Asian, Japanese) and by shape, with a guide to pouches, ivory lids and boxes.",
  "READING — GUIDE", "Types of Chaire",
  "Katatsuki, nasu, bunrin, taikai. The small jar for thick tea gets far more interesting once the shape names land.",
  chaire_body_en(sec_en, tcard_en)))

w("en/articles/natsume-types.html", article_shell_en(
  "Types of Natsume — Sizes & Lacquer Finishes",
  "Natsume by size and lacquer finish (plain black, tame-nuri, maki-e, raden), plus the wider family of thin-tea containers.",
  "READING — GUIDE", "Types of Natsume",
  "Medium or flat, plain black or gold. A measure for choosing the small lacquered caddy that sits in the palm.",
  natsume_body_en(sec_en, tcard_en)))

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
    <a class="article-card reveal" href="kama-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Kama</h3>
      <p>Ashiya, Tenmyō and Kyoto, and every shape from shinnari to unryū.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="chaire-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Chaire</h3>
      <p>Katatsuki, nasu, bunrin — the thick-tea caddy read through its shapes and its pouch.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="natsume-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Natsume</h3>
      <p>Sizes, lacquer finishes, and the wider family of thin-tea containers.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>Types of Tea Whisks</h3>
      <p>Tine counts, bamboo colors, schools — choosing a chasen, explained simply.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="history.html">
      <p class="a-kicker">HISTORY</p><h3>A History of the Tea Ceremony</h3>
      <p>How one cup of medicine became a Way — a thousand years in seven eras.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="evolution.html">
      <p class="a-kicker">HISTORY</p><h3>The Evolution of Tea Utensils</h3>
      <p>Chinese treasures, mitate, and wares made in Japan — five centuries traced through six utensils.</p>
      <p class="tool-more">READ →</p>
    </a>
    <a class="article-card reveal" href="sekki.html">
      <p class="a-kicker">SEASON</p><h3>The 24 Solar Terms &amp; Tea Utensils</h3>
      <p>Seasonal flowers, tea-scoop names, bowls and caddy motifs for all 24 terms.</p>
      <p class="tool-more">READ →</p>
    </a>
  </div>
</section>
'''
w("en/articles/index.html", shell_en("Reading — Tea Utensil Guides | Yusando Antique Gallery",
  "Long-form guides to tea bowls, kettles, caddies and whisks, to the history of the tea ceremony, and to the seasonal calendar that shapes the utensils.",
  articles_index_body, root="../../", current="articles"))

print("en articles done")

# ---------------------------------------------------------------- EN details ----
TYPES_ARTICLE_EN = {
 "chawan": ("chawan-types.html", "Types of Chawan", "Raku, Hagi, Karatsu and beyond — lineage and shape"),
 "chasen": ("chasen-types.html", "Types of Chasen", "Tine counts, bamboo colours, and schools"),
 "kama":   ("kama-types.html",   "Types of Kama",   "Ashiya, Tenmyō, Kyoto, and choosing by shape"),
 "natsume":("natsume-types.html","Types of Natsume","Sizes, lacquer finishes and thin-tea containers"),
}

def types_link_en(slug):
    if slug not in TYPES_ARTICLE_EN:
        return ""
    href, name, sub = TYPES_ARTICLE_EN[slug]
    return (f'<a class="more-band" href="../articles/{href}">'
            f'<span class="mb-kicker">READ MORE</span>'
            f'<span class="mb-name">{name}</span>'
            f'<span class="mb-sub">{sub}</span>'
            f'<span class="mb-arrow">→</span></a>')

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
    tags = (f'<span class="tag lv-tag-inline lv{t["level"]}">{LV_EN[t["level"]][0]} {LV_EN[t["level"]][1]}</span>'
            + "".join(f'<span class="tag">{x}</span>' for x in t["tags"]))
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
    <div class="detail-art">{ico(t["slug"], "ico--hero")}</div>
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
      <div class="parts-fig">{parts_icon(t["slug"], t["parts_dots"])}</div>
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
    <div class="shop-stub" data-ec-category="{t["slug"]}" data-ec-root="../../" data-ec-name="{t["name"]}">
      <div class="listing-slot" id="listings-{t["slug"]}"></div>
      <h3>Online Shop — Coming Soon</h3>
      <p>Once the shop is connected, pre-loved {t["en"].lower()}s available now will appear right here.</p>
      <button class="btn" disabled>VIEW STOCK — COMING SOON</button>
    </div>
  </section>
</div>

{types_link_en(t["slug"])}
<nav class="pn">
  <a href="{prev_t["slug"]}.html">← {prev_t["name"]}</a>
  <a href="../tools.html">ALL UTENSILS</a>
  <a href="{next_t["slug"]}.html">{next_t["name"]} →</a>
</nav>
'''
    return shell_en(
        f'{t["name"]} ({t["en"]}) — History, Parts & Use | Yusando Antique Gallery',
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
            "articles/chawan-types.html","articles/history.html","articles/chasen-types.html","articles/sekki.html","articles/evolution.html","articles/kama-types.html","articles/chaire-types.html","articles/natsume-types.html"] + \
           [f"tools/{t['slug']}.html" for t in TOOLS_EN]
SITE_URL = "https://gallery.yusando.com"   # CNAME on the repo root

SITE_JA = "悠三堂古美術ギャラリー"
SITE_EN = "Yusando Antique Gallery"


def inject_hreflang(path, page):
    """hreflang pair + canonical + Open Graph / Twitter card for one page."""
    full = os.path.join(ROOT, path)
    html = open(full, encoding="utf-8").read()
    en = path.startswith("en/")

    # strip anything a previous run wrote, so this stays idempotent
    html = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', '', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*">\n?', '', html)
    html = re.sub(r'<meta (?:property="og:|name="twitter:)[^>]*>\n?', '', html)
    html = re.sub(r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n?', '', html)
    html = re.sub(r'<meta name="theme-color"[^>]*>\n?', '', html)
    up = "../" * path.count("/")

    m = re.search(r'<title>(.*?)</title>', html, re.S)
    title = re.sub(r'\s+', ' ', m.group(1)).strip() if m else SITE_EN
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    desc = m.group(1) if m else ""
    title = title.replace('"', '&quot;')
    desc = desc.replace('"', '&quot;')

    url = f'{SITE_URL}/{path}'
    if url.endswith("/index.html"):
        url = url[: -len("index.html")]
    img = f'{SITE_URL}/assets/ogp-en.png' if en else f'{SITE_URL}/assets/ogp.png'

    tags = (
        f'<link rel="icon" type="image/svg+xml" href="{up}assets/favicon.svg">\n'
        f'<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">\n'
        f'<meta name="theme-color" content="#4a5d3a">\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<link rel="alternate" hreflang="ja" href="{SITE_URL}/{page}">\n'
        f'<link rel="alternate" hreflang="en" href="{SITE_URL}/en/{page}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{page}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:site_name" content="{SITE_EN if en else SITE_JA}">\n'
        f'<meta property="og:locale" content="{"en_US" if en else "ja_JP"}">\n'
        f'<meta property="og:locale:alternate" content="{"ja_JP" if en else "en_US"}">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:image" content="{img}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<meta name="twitter:image" content="{img}">\n'
    )
    html = html.replace('</head>', tags + '</head>', 1)
    open(full, "w", encoding="utf-8").write(html)

# ------------------------------------------------------------- typography ----
# Straight quotes read as unfinished on a page set in a serif face; normalise
# them to curly ones in text nodes only (never inside tags, script, style, svg).
_SKIP = re.compile(r'<(script|style|svg)\b[^>]*>.*?</\1>', re.S | re.I)


def _smart_text(t):
    t = re.sub(r'(\w)\'(\w)', '\\1\u2019\\2', t)              # don't, Rikyū's
    t = re.sub(r'(\w)\'(?=[\s,.;:!?)]|$)', '\\1\u2019', t)    # the bowls' face
    t = re.sub(r'"([^"\n]+)"', '\u201c\\1\u201d', t)          # "quoted phrase"
    t = re.sub(r'&(?![a-zA-Z#][a-zA-Z0-9]{0,8};)', '&amp;', t)  # bare ampersands
    return t


def smarten(html):
    blocks = []

    def stash(m):
        blocks.append(m.group(0))
        return f"\x00{len(blocks) - 1}\x00"

    html = _SKIP.sub(stash, html)
    parts = re.split(r'(<[^>]*>)', html)
    html = "".join(p if i % 2 else _smart_text(p) for i, p in enumerate(parts))
    return re.sub(r'\x00(\d+)\x00', lambda m: blocks[int(m.group(1))], html)


for p in ja_pages:
    depth = p.count("/")
    prefix = "../" * depth
    inject(p, "EN", f"{prefix}en/{p}")
    inject(f"en/{p}", "日本語", f"{'../' * (depth+1)}{p}")
    for q in (p, f"en/{p}"):
        full = os.path.join(ROOT, q)
        src = open(full, encoding="utf-8").read()
        open(full, "w", encoding="utf-8").write(smarten(src))
    inject_hreflang(p, p)
    inject_hreflang(f"en/{p}", p)
print("lang links + hreflang + smart quotes applied")

# ------------------------------------------------------- sitemap / robots ----
def _loc(p):
    u = f"{SITE_URL}/{p}"
    return u[: -len("index.html")] if u.endswith("/index.html") else u


rows = []
for p in ja_pages:
    prio = "1.0" if p == "index.html" else ("0.8" if "/" not in p else "0.7")
    for q in (p, f"en/{p}"):
        rows.append(
            "  <url>\n"
            f"    <loc>{_loc(q)}</loc>\n"
            f'    <xhtml:link rel="alternate" hreflang="ja" href="{_loc(p)}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="en" href="{_loc("en/" + p)}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{_loc(p)}"/>\n'
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>{prio}</priority>\n"
            "  </url>")

open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + "\n".join(rows) + "\n</urlset>\n")

open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\n\n" f"Sitemap: {SITE_URL}/sitemap.xml\n")

print(f"sitemap.xml ({len(rows)} urls) + robots.txt written")
