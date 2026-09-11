# -*- coding: utf-8 -*-
"""Édition française — les cinq pages principales.

Les pages de détail (ustensiles, articles longs) n'existent qu'en japonais et
en anglais ; les liens qui y mènent pointent donc vers l'édition anglaise,
signalés par une puce « EN ». La terminologie suit l'édition anglaise : le mot
japonais d'abord, la traduction en appui.
"""
import os
from gen import FONTS, ROOT
from icons import sprite as ico_sprite, icon as ico


def w(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)
    print("wrote", path)


def en(path, depth=1):
    """Lien vers l'édition anglaise, faute de page française."""
    return "../" * depth + "en/" + path


EN_TAG = '<span class="en-only" title="Page disponible en anglais">EN</span>'


# ------------------------------------------------------------------ shell --
def shell_fr(title, desc, body, root="../", current=""):
    def nav(href, label, key):
        cls = ' class="current"' if current == key else ''
        return f'<a href="{root}fr/{href}"{cls}>{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="fr">
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
    <a class="brand" href="{root}fr/index.html">
      <span class="brand-mark">YUSANDO</span>
      <span class="brand-sub">GALERIE D&rsquo;ART ANCIEN</span>
    </a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links">
      {nav("index.html","Accueil","home")}
      {nav("tools.html","Les ustensiles","tools")}
      {nav("setup.html","Ro et furo","setup")}
      {nav("guide.html","Le temae","guide")}
      {nav("articles/index.html","Lectures","articles")}
      {nav("index.html#about","À propos","about")}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="f-inner">
    <div>
      <p class="f-mark">YUSANDO <span class="en-sub">悠三堂古美術ギャラリー</span></p>
      <p class="f-note">Ustensiles de thé d&rsquo;occasion à prix unique.<br>Choisissez ce qui vous touche, non ce qui coûte.</p>
    </div>
    <nav class="f-nav">
      <a href="{root}fr/index.html">ACCUEIL</a>
      <a href="{root}fr/tools.html">USTENSILES</a>
      <a href="{root}fr/setup.html">RO ET FURO</a>
      <a href="{root}fr/guide.html">LE TEMAE</a>
      <a href="{root}fr/articles/index.html">LECTURES</a>
      <a href="{root}fr/index.html#about">À PROPOS</a>
    </nav>
  </div>
  <p class="f-copy">© 2026 YUSANDO — Maquette de démonstration. La vente en ligne n&rsquo;est pas encore ouverte.</p>
</footer>
<script src="{root}js/site.js"></script>
</body>
</html>'''


# ------------------------------------------------------------------- data --
TOOLS_FR = [
 dict(slug="chawan", level=1, name="Chawan", jp="茶碗", fr="Bol à thé", num="01",
   lede="Le bol dans lequel le thé est fouetté puis bu — l’ustensile qui révèle le mieux le goût de l’hôte, choisi à neuf à chaque saison."),
 dict(slug="chasen", level=1, name="Chasen", jp="茶筅", fr="Fouet en bambou", num="02",
   lede="Taillé d’un seul morceau de bambou en quatre-vingts à cent vingt brins. Un objet d’usage que l’on remplace : c’est lui qui décide de la mousse."),
 dict(slug="chashaku", level=1, name="Chashaku", jp="茶杓", fr="Cuillère à thé", num="03",
   lede="Une mince lame de bambou courbée à la vapeur. Le maître de thé la taille lui-même et lui donne un nom : le plus personnel des ustensiles."),
 dict(slug="natsume", level=1, name="Natsume", jp="棗", fr="Boîte à thé léger", num="04",
   lede="La boîte laquée du thé léger (usucha), nommée d’après le fruit du jujubier dont elle épouse la forme."),
 dict(slug="kama", level=2, name="Kama", jp="釜", fr="Bouilloire de fonte", num="05",
   lede="La bouilloire de fer qui chauffe l’eau. Son murmure — le matsukaze, « vent dans les pins » — donne le ton du silence."),
 dict(slug="hishaku", level=2, name="Hishaku", jp="柄杓", fr="Louche de bambou", num="06",
   lede="La louche de bambou qui puise l’eau. Sa coupe et la coupe de son manche changent entre l’hiver et l’été."),
 dict(slug="fukusa", level=2, name="Fukusa", jp="帛紗", fr="Étoffe de soie", num="07",
   lede="Le carré de soie que l’hôte porte à la ceinture. Le plier et purifier avec lui ouvre le temae."),
 dict(slug="mizusashi", level=2, name="Mizusashi", jp="水指", fr="Jarre à eau fraîche", num="08",
   lede="La jarre d’eau froide, qui rafraîchit la bouilloire et rince le bol. Céramique l’hiver, verre ou grès clair l’été."),
]

MINOR_FR = [
 dict(slug="chaire", level=1, name="Chaire", jp="茶入", fr="Boîte à thé épais",
   desc="Petit pot de céramique pour le koicha, gardé dans une pochette de soie (shifuku) et coiffé d’un couvercle d’ivoire. Il prend rang au-dessus du natsume."),
 dict(slug="kensui", level=2, name="Kensui", jp="建水", fr="Récipient à eau usée",
   desc="Il reçoit l’eau de rinçage. Aussi nommé koboshi, il travaille discrètement, hors du regard des invités."),
 dict(slug="futaoki", level=2, name="Futaoki", jp="蓋置", fr="Repose-couvercle",
   desc="Petit support pour le couvercle de la bouilloire et la louche : simple tronçon de bambou au plus sobre, céladon ou porcelaine peinte au plus libre."),
 dict(slug="kogo", level=3, name="Kōgō", jp="香合", fr="Boîte à encens",
   desc="Elle garde l’encens du service de charbon : encens pétri dans une boîte de céramique à la saison du ro, bois de santal dans une boîte laquée à celle du furo."),
 dict(slug="hanaire", level=3, name="Hanaire", jp="花入", fr="Vase à fleurs",
   desc="Bambou, céladon ou grès d’Iga pour les fleurs de thé. « Disposez-les comme elles sont dans les champs », enseignait Rikyū."),
 dict(slug="kakemono", level=3, name="Kakemono", jp="掛物", fr="Rouleau suspendu",
   desc="Le rouleau de l’alcôve. Une seule ligne de calligraphie zen tient le premier rang : « aucun ustensile ne passe avant le rouleau », disait Rikyū."),
 dict(slug="furo", level=2, name="Furo", jp="風炉", fr="Brasero portatif",
   desc="Le foyer mobile de mai à octobre, en bronze, en terre ou en fer ; modeler son lit de cendres fait partie de l’art de l’hôte."),
 dict(slug="kashiki", level=2, name="Kashiki", jp="菓子器", fr="Récipient à confiseries",
   desc="Pour les douceurs qui précèdent le thé : boîtes à étages (fuchidaka) pour les gâteaux humides, plateaux pour les secs. La confiserie fait partie du thé."),
 dict(slug="ro", level=3, name="Ro", jp="炉", fr="Foyer encastré",
   desc="Le foyer creusé dans le tatami de novembre à avril. Creuser un ro, c’est ce qui fait d’une pièce une salle de thé."),
 dict(slug="sumitori", level=3, name="Sumitori", jp="炭斗", fr="Panier à charbon",
   desc="Le panier qui porte le charbon du sumi-demae, garni de pinces, plumeau, anneaux de bouilloire et boîte à encens."),
 dict(slug="haboki", level=3, name="Habōki", jp="羽箒", fr="Plumeau",
   desc="Trois plumes liées — grue, faucon ou oie sauvage — pour balayer la cendre au bord du foyer ; le montage diffère entre ro et furo."),
 dict(slug="hibashi", level=3, name="Hibashi", jp="火箸", fr="Pinces à charbon",
   desc="Pinces de métal pour disposer le charbon : longues pour le foyer, courtes pour le brasero, à têtes ouvragées."),
 dict(slug="haiki", level=3, name="Haiki", jp="灰器", fr="Récipient à cendre",
   desc="Vase non émaillé de cendre humide, servi avec sa cuillère et répandu dans le foyer pendant le service de charbon."),
 dict(slug="chatsubo", level=3, name="Chatsubo", jp="茶壺", fr="Jarre à feuilles",
   desc="La grande jarre de thé en feuilles. Son sceau est rompu lors du kuchikiri de novembre et la feuille moulue en matcha : là commence l’année du thé."),
]

DETAIL_SLUGS_FR = {t["slug"] for t in TOOLS_FR}
ALL_FR = {t["slug"]: t for t in TOOLS_FR + MINOR_FR}

LV_FR = {
 1: ("LV.1", "Un bol aujourd’hui", "Quelques pièces et de l’eau chaude"),
 2: ("LV.2", "Recevoir", "Préparer le thé devant ses invités"),
 3: ("LV.3", "Tenir une salle de thé", "Composer le cadre lui-même"),
}


def lv_badge_fr(level):
    tag, short, _ = LV_FR[level]
    return f'<span class="lv-badge lv{level}"><b>{tag}</b>{short}</span>'


LV_INTRO_FR = [
 (1, "Boire le matcha chez soi",
  "Quelques ustensiles et une bouilloire d’eau chaude : de quoi fouetter un bol cet après-midi même. Commencer ici suffit amplement.",
  ["chawan", "chasen", "chashaku", "natsume", "chaire"],
  "Le thé léger loge dans le natsume, le thé épais dans le chaire. Ajoutez un chakin de lin et un support à fouet, et vous y êtes ; n’importe quelle assiette fera pour les douceurs."),
 (2, "Donner une réunion de thé",
  "Les ustensiles du temae — préparer le thé devant ses invités, à partir de l’eau que l’on porte à frémir. Avec eux, vous pouvez recevoir chez vous.",
  ["furo", "kama", "hishaku", "fukusa", "mizusashi", "kensui", "futaoki", "kashiki"],
  "Un réchaud électrique convient très bien pour le feu. Commencez par le brasero, la bouilloire, la jarre à eau et le récipient à eau usée, puis complétez."),
 (3, "Tenir une salle de thé",
  "L’alcôve, et le feu dans le foyer. C’est ici que la saison prend forme et que la pièce entière devient une seule composition.",
  ["ro", "kakemono", "hanaire", "kogo", "sumitori", "haboki", "hibashi", "haiki", "chatsubo"],
  "Rouleau, vase et boîte à encens forment les trois de l’alcôve. Panier, plumeau, pinces et récipient à cendre composent le service de charbon, que rejoint la boîte à encens."),
]


def lv_section_fr():
    blocks = ""
    for level, title, lede, slugs, note in LV_INTRO_FR:
        tag, short, sub = LV_FR[level]
        names = "".join(
            f'<a class="lv-chip" href="{en("tools/" + s + ".html")}">'
            f'{ALL_FR[s]["name"]}{EN_TAG}</a>'
            if s in DETAIL_SLUGS_FR else
            f'<span class="lv-chip plain">{ALL_FR[s]["name"]}</span>'
            for s in slugs)
        blocks += (f'<div class="lv-card lv{level} reveal">'
                   f'<div class="lv-head"><span class="lv-tag">{tag}</span>'
                   f'<div><h3>{title}</h3><p class="lv-sub">{sub}</p></div></div>'
                   f'<p class="lv-lede">{lede}</p>'
                   f'<div class="lv-chips">{names}</div>'
                   f'<p class="lv-note">{note}</p></div>')
    return f'<div class="lv-grid">{blocks}</div>'


def card_fr(t):
    return f'''<a class="tool-card reveal" href="{en("tools/" + t["slug"] + ".html")}">
  <span class="tool-num">{t["num"]}</span>
  {lv_badge_fr(t["level"])}
  <div class="tool-art">{ico(t["slug"])}</div>
  <h3 class="tool-name">{t["name"]}</h3>
  <p class="tool-yomi">{t["jp"]} — {t["fr"]}</p>
  <p class="tool-desc">{t["lede"]}</p>
  <p class="tool-more">LIRE LA SUITE (EN) →</p>
</a>'''


def minor_card_fr(m):
    return f'''<div class="tool-card plain reveal">
  {lv_badge_fr(m["level"])}
  <div class="tool-art">{ico(m["slug"])}</div>
  <h3 class="tool-name">{m["name"]}</h3>
  <p class="tool-yomi">{m["jp"]} — {m["fr"]}</p>
  <p class="tool-desc">{m["desc"]}</p>
</div>'''


# ------------------------------------------------------------------ index --
ARTICLES_FR = [
 ("chawan-types.html", "GUIDE", "Les types de bols",
  "Raku, Hagi et Karatsu ; tenmoku et ido. Lignées, fours et formes, mis en ordre pour choisir."),
 ("kama-types.html", "GUIDE", "Les types de bouilloires",
  "Ashiya, Tenmyō et Kyoto, et toutes les formes, du shinnari à l’unryū."),
 ("chaire-types.html", "GUIDE", "Les types de chaire",
  "Katatsuki, nasu, bunrin — la boîte à thé épais lue à travers ses formes et sa pochette."),
 ("natsume-types.html", "GUIDE", "Les types de natsume",
  "Tailles, finitions de laque, et toute la famille des boîtes à thé léger."),
 ("chasen-types.html", "GUIDE", "Les types de fouets",
  "Nombre de brins, couleur du bambou, écoles. Choisir son chasen, expliqué simplement."),
 ("history.html", "HISTOIRE", "Une histoire de la voie du thé",
  "Comment une tasse de remède venue de Chine est devenue, en mille ans, une Voie. Une chronologie en sept époques."),
 ("evolution.html", "HISTOIRE", "L’évolution des ustensiles",
  "Trésors chinois, mitate, et céramiques faites au Japon — cinq siècles suivis à travers six ustensiles."),
 ("sekki.html", "SAISONS", "Les 24 sekki et les ustensiles",
  "Fleurs de saison, noms de cuillères, bols et motifs de boîtes — toute l’année du thé, terme par terme."),
]


def article_cards_fr(depth=1):
    return "".join(
        f'<a class="article-card reveal" href="{en("articles/" + href, depth)}">'
        f'<p class="a-kicker">{kicker}</p><h3>{title}{EN_TAG}</h3>'
        f'<p>{desc}</p><p class="tool-more">LIRE (EN) →</p></a>'
        for href, kicker, title, desc in ARTICLES_FR)


index_body = f'''
<section class="hero">
  <svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M100 18 a82 82 0 1 0 60 26" fill="none" stroke="#2b2a26" stroke-width="10" stroke-linecap="round"/>
  </svg>
  <div class="hero-inner">
    <p class="hero-kicker">USTENSILES DE THÉ D&rsquo;OCCASION À PRIX UNIQUE — 均一価格の中古茶道具</p>
    <h1 class="hero-title">Choisissez celui<br>qui vous touche.</h1>
    <p class="hero-sub">Un portail à <strong>prix unique</strong> d&rsquo;ustensiles de thé japonais de seconde main, abordable même pour qui débute.<br>Plus de prix à deviner : prenez simplement la pièce qui vous plaît.</p>
    <div class="hero-cta">
      <a class="btn solid" href="tools.html">VOIR LES USTENSILES</a>
      <a class="btn" href="guide.html">COMMENT NAÎT UN BOL</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="intro-grid">
    <div class="reveal">
      <p class="intro-tate">Aimer une pièce<br>est une raison suffisante.<small>— YUSANDO</small></p>
    </div>
    <div class="intro-text reveal">
      <p class="section-kicker" style="text-align:left;text-indent:0">À PROPOS DE CE SITE</p>
      <p>Le plus difficile, quand on achète un ustensile de thé, c&rsquo;est presque toujours le <strong>prix</strong>. Deux bols qui se ressemblent peuvent valoir trois mille yens ou trois cent mille. Sans œil exercé, on se croit piégé — et la plupart des gens renoncent avant même de demander.</p>
      <p>Yusando est un portail à <strong>prix unique</strong> d&rsquo;ustensiles de thé de seconde main. La comparaison des prix une fois écartée, il ne reste que la seule mesure qui compte : <strong>la pièce vous touche-t-elle ?</strong> Cette glaçure, ce poids dans la main — cela suffit.</p>
      <p>En connaître les noms et les histoires rend le plaisir plus plein encore. Pour chaque ustensile, nous donnons donc la lecture, le récit, les parties et le maniement, en termes simples. Le reste peut attendre.</p>
    </div>
  </div>
</section>

<section class="section" style="background:transparent;padding-top:0">
  <div class="section-head reveal">
    <p class="section-kicker">LES USTENSILES</p>
    <h2 class="section-title">Commencer par huit pièces essentielles</h2>
    <div class="rule"></div>
    <p class="section-lede">Les ustensiles indispensables du service du thé. Chaque fiche détaillée — pour l&rsquo;instant en anglais — couvre l&rsquo;histoire, les parties, l&rsquo;usage et les points à vérifier en occasion.</p>
  </div>
  <div class="tools-grid">
    {"".join(card_fr(t) for t in TOOLS_FR)}
  </div>
  <div style="text-align:center;margin-top:44px">
    <a class="btn" href="tools.html">VOIR TOUS LES USTENSILES</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:44px">
    <p class="section-kicker">LECTURES</p>
    <h2 class="section-title">Aller un peu plus loin</h2>
    <div class="rule"></div>
    <p class="section-lede">Ces articles de fond existent pour l&rsquo;instant en japonais et en anglais.</p>
  </div>
  <div class="article-cards">
    {article_cards_fr()}
  </div>
</section>

<section class="care">
  <div class="section tight">
    <div class="section-head reveal" style="margin-bottom:44px">
      <p class="section-kicker">ENTRETIEN</p>
      <h2 class="section-title">Vivre longtemps avec ses ustensiles</h2>
    </div>
    <div class="care-grid reveal">
      <div class="care-cell"><h3>Le bol <span class="en-sub">CHAWAN</span></h3><p>Eau chaude seule, jamais de détergent. Séchez complètement avant de ranger ; faites tremper une céramique neuve une nuit entière avant le premier usage.</p></div>
      <div class="care-cell"><h3>Le fouet <span class="en-sub">CHASEN</span></h3><p>Rincez à l&rsquo;eau chaude et laissez sécher à l&rsquo;air, brins vers le haut. Un support à fouet lui garde sa courbe.</p></div>
      <div class="care-cell"><h3>La laque <span class="en-sub">NATSUME</span></h3><p>Ne lavez jamais à l&rsquo;eau : un chiffon doux et sec suffit. Rangez dans sa boîte de paulownia, à l&rsquo;abri du soleil.</p></div>
      <div class="care-cell"><h3>Le fer <span class="en-sub">KAMA</span></h3><p>Videz et laissez sécher par la chaleur résiduelle. Le dépôt minéral la protège : ne frottez jamais, n&rsquo;employez jamais de savon.</p></div>
    </div>
  </div>
</section>

<section class="section reveal" style="text-align:center">
  <p class="section-kicker">GALERIE</p>
  <h2 class="section-title">Les pièces que nous gardons</h2>
  <div class="rule"></div>
  <p class="section-lede">Chaque fiche d&rsquo;ustensile présente les pièces conservées à la galerie Yusando. Écrivez-nous au sujet de ce qui retient votre regard ; la vente en ligne suivra lorsqu&rsquo;elle sera prête.</p>
  <div style="margin-top:30px"><span class="btn" style="opacity:.5;cursor:default">VENTE EN LIGNE — PAS ENCORE</span></div>
</section>
'''
w("fr/index.html", shell_fr(
  "Yusando — Ustensiles de thé japonais d’occasion à prix unique",
  "Un portail à prix unique d’ustensiles de thé japonais de seconde main, abordable pour qui débute : noms, histoire, parties et usage de chaque pièce.",
  index_body, root="../", current="home"))


# ------------------------------------------------------------------ tools --
tools_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">LISTE DES USTENSILES</p>
    <h2 class="section-title">Les ustensiles du thé japonais</h2>
    <div class="rule"></div>
    <p class="section-lede">Les principaux ustensiles du chanoyu. Ceux qui possèdent une fiche détaillée vont plus loin : histoire, parties, usage et points à vérifier en occasion.</p>
  </div>

  <div class="section-head reveal" style="margin-top:8px">
    <p class="section-kicker">CONSTITUER SON NÉCESSAIRE — TROIS NIVEAUX</p>
    <h2 class="section-title">Trois niveaux pour s&rsquo;y retrouver</h2>
    <div class="rule"></div>
    <p class="section-lede">Tout n&rsquo;est pas à acquérir d&rsquo;un coup. Voulez-vous un bol de thé aujourd&rsquo;hui, inviter des amis, ou composer une pièce entière ? Chaque réponse demande un nécessaire différent.</p>
  </div>
  {lv_section_fr()}

  <div class="cat-head reveal"><h2>Les ustensiles du temae</h2><span class="en-sub">FICHES DÉTAILLÉES</span></div>
  <div class="tools-grid">
    {"".join(card_fr(t) for t in TOOLS_FR)}
  </div>
  <div class="cat-head reveal"><h2>Les autres ustensiles</h2><span class="en-sub">PRÉSENTATION</span></div>
  <div class="tools-grid">
    {"".join(minor_card_fr(m) for m in MINOR_FR)}
  </div>
</section>
'''
w("fr/tools.html", shell_fr(
  "Les ustensiles — Liste des ustensiles de thé japonais | Yusando",
  "Vingt-deux ustensiles de la cérémonie du thé japonaise, avec leurs noms, leurs lectures et leur rôle, classés en trois niveaux : boire le matcha chez soi, recevoir, tenir une salle de thé.",
  tools_body, root="../", current="tools"))


# ------------------------------------------------------------------ guide --
guide_steps_fr = [
 ("1", "Purifier",
  f'La boîte et la cuillère sont essuyées avec le <a href="{en("tools/fukusa.html")}">fukusa</a> ; le <a href="{en("tools/chasen.html")}">fouet</a> et le <a href="{en("tools/chawan.html")}">bol</a> sont rincés à l’eau chaude.'),
 ("2", "Doser",
  f'Le matcha est prélevé du <a href="{en("tools/natsume.html")}">natsume</a> et versé dans le bol — environ une cuillerée et demie, soit deux grammes.'),
 ("3", "Verser",
  f'L’eau chaude est puisée dans la <a href="{en("tools/kama.html")}">bouilloire</a> avec le <a href="{en("tools/hishaku.html")}">hishaku</a>, puis versée doucement.'),
 ("4", "Fouetter",
  "Le chasen va vite et droit, jusqu’à ce que le thé se tienne, lisse et couvert d’une mousse fine."),
 ("5", "Offrir",
  "Le bol est tourné pour que sa face salue l’invité, et le thé est servi."),
]

guide_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">LE TRAVAIL DES USTENSILES</p>
    <h2 class="section-title">Comment naît un bol de thé</h2>
    <div class="rule"></div>
    <p class="section-lede">Chaque ustensile est pris à son tour, fait son travail, et retourne au repos. Voici, simplifié, le déroulé du temae de thé léger.</p>
  </div>
  <div class="temae-list reveal">
    {"".join(f'<div class="temae-item"><span class="temae-step">{a}</span><div class="temae-body"><h3>{b}</h3><p>{c}</p></div></div>' for a, b, c in guide_steps_fr)}
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:40px">
    <p class="section-kicker">UN PREMIER NÉCESSAIRE</p>
    <h2 class="section-title">Le strict minimum</h2>
    <div class="rule"></div>
  </div>
  <div class="check-grid reveal" style="max-width:820px;margin-left:auto;margin-right:auto">
    <div class="check-cell"><h3>Un bol chez soi</h3><p>Un chawan, un chasen et un chashaku suffisent à fouetter le matcha. Une bouilloire de cuisine et une boîte à thé ordinaire feront le reste.</p></div>
    <div class="check-cell"><h3>Commencer les cours</h3><p>Ajoutez les quatre objets personnels : fukusa, éventail pliant, papiers kaishi et pique à gâteau. Couleurs et tailles varient selon l&rsquo;école — demandez à votre professeur.</p></div>
    <div class="check-cell"><h3>Où l&rsquo;occasion excelle</h3><p>Bols, boîtes à thé, jarres à eau et kensui ont un marché ancien très riche. Le fouet et le fukusa, eux, s&rsquo;achètent neufs.</p></div>
    <div class="check-cell"><h3>Dans quel ordre</h3><p>N&rsquo;achetez pas tout d&rsquo;un coup. Les cuillères nommées et les bouilloires récompensent un œil formé : laissez votre pratique guider votre collection.</p></div>
  </div>
</section>

<section class="section reveal" style="text-align:center;padding-top:30px">
  <p class="words-quote" style="font-size:clamp(20px,3vw,27px);letter-spacing:.12em;line-height:2">« Sans ustensiles célèbres,<br>on ne saurait pratiquer le thé. »</p>
  <p class="en-sub" style="margin-top:16px">— L&rsquo;IDÉE QUE RIKYŪ A REFUSÉE</p>
  <p class="section-lede" style="margin-top:22px">Sen no Rikyū enseignait que le thé demande de la sincérité, non des trésors. User d&rsquo;un seul nécessaire modeste avec soin, année après année : vivre avec des ustensiles de seconde main, c&rsquo;est cet enseignement mis en pratique.</p>
</section>
'''
w("fr/guide.html", shell_fr(
  "Le temae — Le déroulé du thé léger | Yusando",
  "Comment s’emploient les ustensiles : le temae de thé léger pas à pas, et un guide pour constituer son premier nécessaire.",
  guide_body, root="../", current="guide"))


# ------------------------------------------------------------------ setup --
FURO_DIAG_FR = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">Natte de l&rsquo;hôte (simplifiée)</text>
<rect x="76" y="30" width="40" height="40" fill="none" stroke="#a53f2b" stroke-width="1.6"/>
<circle cx="96" cy="50" r="14" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="96" y="83" text-anchor="middle" class="dg-label strong">Furo + bouilloire</text>
<text x="96" y="94" text-anchor="middle" class="dg-label">(sur sa planche)</text>
<circle cx="152" cy="48" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="152" y="76" text-anchor="middle" class="dg-label strong">Jarre à eau</text>
<circle cx="120" cy="136" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="120" y="162" text-anchor="middle" class="dg-label strong">Hôte</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">Invités</text>
</svg>'''

RO_DIAG_FR = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">Natte de l&rsquo;hôte (simplifiée)</text>
<rect x="146" y="96" width="40" height="40" fill="#e2d8c2" stroke="#a53f2b" stroke-width="2"/>
<circle cx="166" cy="116" r="13" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="166" y="150" text-anchor="middle" class="dg-label strong">Ro + bouilloire</text>
<circle cx="120" cy="46" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="120" y="74" text-anchor="middle" class="dg-label strong">Jarre à eau</text>
<circle cx="104" cy="120" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="96" y="146" text-anchor="middle" class="dg-label strong">Hôte</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="212" y="93" text-anchor="middle" class="dg-label">Invités</text>
</svg>'''


def ck_fr(name, note, link=None):
    label = f'<a href="{en("tools/" + link + ".html")}">{name}{EN_TAG}</a>' if link else name
    return (f'<label class="ck"><input type="checkbox">'
            f'<span class="ck-name">{label}</span>'
            f'<span class="ck-note">{note}</span></label>')


_LNK = 'style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)"'

setup_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">LA DISPOSITION SAISONNIÈRE</p>
    <h2 class="section-title">Ro et furo — les deux saisons du thé</h2>
    <div class="rule"></div>
    <p class="section-lede">L&rsquo;année du thé se partage selon l&rsquo;endroit où siège le feu. L&rsquo;hiver, le foyer est creusé dans le sol et rapproché des invités (ro) ; l&rsquo;été, un brasero tient le feu à distance et suggère la fraîcheur (furo). Toute la disposition — et bien des ustensiles — changent avec lui.</p>
  </div>

  <div class="reveal">
    <div class="season-band">
      <div class="ro">RO nov.</div><div class="ro">déc.</div><div class="ro">janv.</div><div class="ro">févr.</div><div class="ro">mars</div><div class="ro">avr.</div>
      <div class="fu">FURO mai</div><div class="fu">juin</div><div class="fu">juill.</div><div class="fu">août</div><div class="fu">sept.</div><div class="fu">oct.</div>
    </div>
    <p class="cmp-note">L&rsquo;ouverture du foyer en novembre (robiraki) est appelée le Nouvel An des gens de thé ; le premier furo, en mai, tourne la pièce vers l&rsquo;été.</p>
  </div>

  <div class="layout-grid reveal">
    <div class="layout-card">
      <h3>La disposition du furo<span class="en-sub">DE MAI À OCTOBRE</span></h3>
      {FURO_DIAG_FR}
      <p class="cap">La posture d&rsquo;été : le feu tenu loin des invités pour suggérer la fraîcheur. Le brasero repose sur sa planche avec une bouilloire plus petite ; modeler son lit de cendres fait partie de l&rsquo;art de l&rsquo;hôte.</p>
    </div>
    <div class="layout-card">
      <h3>La disposition du ro<span class="en-sub">DE NOVEMBRE À AVRIL</span></h3>
      {RO_DIAG_FR}
      <p class="cap">La posture d&rsquo;hiver : un foyer creusé dans le tatami, dont la chaleur est partagée avec les invités. La bouilloire grandit et sa voix, en frémissant, s&rsquo;enrichit.</p>
    </div>
  </div>
  <p class="cmp-note reveal">* Schémas simplifiés pour le temae « porté » ordinaire (hongatte). Les positions varient selon la coupe du foyer et l&rsquo;école.</p>

  <div class="reveal">
    <table class="cmp-table">
      <thead><tr><th style="width:8em;background:var(--paper-deep);color:var(--matcha)"></th><th>RO (foyer encastré)</th><th class="furo-col">FURO (brasero)</th></tr></thead>
      <tbody>
        <tr><th>Saison</th><td>Novembre – avril (robiraki en novembre)</td><td>Mai – octobre (premier furo en mai)</td></tr>
        <tr><th>Le feu</th><td>Enfoncé dans le sol, près des invités — la chaleur se partage</td><td>Du côté de l&rsquo;hôte, loin des invités — la fraîcheur se suggère</td></tr>
        <tr><th><a href="{en("tools/kama.html")}" {_LNK}>Bouilloire</a></th><td>Grande, posée sur un trépied ; variantes suspendue et tsurube</td><td>Plus petite, posée sur le brasero et sa planche</td></tr>
        <tr><th><a href="{en("tools/hishaku.html")}" {_LNK}>Louche</a></th><td>Coupe plus grande ; extrémité taillée sur la face interne</td><td>Coupe plus petite ; extrémité taillée sur la face externe</td></tr>
        <tr><th>Repose-couvercle (bambou)</th><td>Nœud à mi-hauteur (naka-bushi), en règle générale</td><td>Nœud au sommet (ten-bushi), en règle générale</td></tr>
        <tr><th>Charbon et encens</th><td>Charbon plus gros ; encens pétri dans une boîte de céramique</td><td>Charbon plus fin ; bois de santal dans une boîte laquée</td></tr>
        <tr><th>Le climat</th><td>Se rassembler autour de la chaleur ; la saison profonde, wabi</td><td>« Un goût de fraîcheur » ; l&rsquo;eau tient le premier rôle</td></tr>
      </tbody>
    </table>
    <p class="cmp-note">* Les usages, tel le nœud du repose-couvercle, diffèrent selon l&rsquo;école : la parole de votre professeur passe avant tout.</p>
  </div>
</section>

<section class="section tight" style="padding-top:20px">
  <div class="section-head reveal" style="margin-bottom:34px">
    <p class="section-kicker">AIDE-MÉMOIRE</p>
    <h2 class="section-title">Ce qu&rsquo;un temae réel demande</h2>
    <div class="rule"></div>
    <p class="section-lede">Une liste pour le temae de thé léger « porté », sans étagère d&rsquo;apparat. Cochez à mesure que vous préparez.</p>
  </div>

  <div style="max-width:920px;margin:0 auto">
    <div class="ck-group reveal">
      <h3>1 — À mettre en place à l&rsquo;avance <span class="en-sub">据えておく道具</span></h3>
      <div class="ck-cols">
        {ck_fr("Bouilloire", "L’eau frémit — écoutez le matsukaze", "kama")}
        {ck_fr("Ro ou furo", "Selon la saison (voir le tableau ci-dessus)")}
        {ck_fr("Jarre à eau", "Remplie aux quatre cinquièmes, posée sur la natte de l’hôte", "mizusashi")}
        {ck_fr("Charbon et cendre (ou électrique)", "Ro : charbon plus gros et encens pétri / Furo : plus fin et lit de cendres")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>2 — Disposés dans le bol <span class="en-sub">茶碗に仕組む道具</span></h3>
      <div class="ck-cols">
        {ck_fr("Bol à thé", "Selon la saison : évasé l’été, profond l’hiver", "chawan")}
        {ck_fr("Fouet", "Vérifiez les brins ; davantage de brins pour le thé léger", "chasen")}
        {ck_fr("Cuillère", "Posée face contre le bord du bol", "chashaku")}
        {ck_fr("Chakin", "Le linge de lin, plié de la manière prescrite")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>3 — Portés également <span class="en-sub">運び出す道具</span></h3>
      <div class="ck-cols">
        {ck_fr("Boîte à thé", "Matcha tamisé et dressé en monticule", "natsume")}
        {ck_fr("Kensui", "Porté en dernier, repose-couvercle et louche posés dedans")}
        {ck_fr("Louche", "Type ro ou type furo — ne les confondez pas", "hishaku")}
        {ck_fr("Repose-couvercle", "Ro : nœud médian / Furo : nœud au sommet (bambou)")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>4 — Portés sur soi <span class="en-sub">身に着けるもの</span></h3>
      <div class="ck-cols">
        {ck_fr("Fukusa", "À la taille, côté gauche — l’insigne de l’hôte", "fukusa")}
        {ck_fr("Éventail pliant", "Posé devant les genoux lors des salutations")}
        {ck_fr("Kaishi et pique à gâteau", "Indispensables aux invités aussi")}
        {ck_fr("Kobukusa", "Dans certaines écoles, pour l’examen des ustensiles et le thé épais")}
      </div>
    </div>
    <div class="ck-group reveal">
      <h3>5 — Pour les invités <span class="en-sub">客のための道具</span></h3>
      <div class="ck-cols">
        {ck_fr("Confiseries et récipient", "Gâteaux secs sur plateau pour le thé léger ; humides en fuchidaka pour le thé épais")}
        {ck_fr("Coussins, tabako-bon, etc.", "Pour une salle complète, à la mesure de la formalité")}
      </div>
    </div>
    <div class="reveal" style="margin-top:44px;border:1px solid var(--line);background:var(--paper-deep);border-radius:4px;padding:28px 26px">
      <h3 style="font-size:16px;letter-spacing:.14em;font-weight:500">Ce qui change pour le thé épais <span class="en-sub">濃茶での違い</span></h3>
      <p style="font-size:13.5px;color:var(--ink-soft);margin-top:12px">Le natsume cède la place au <strong>chaire</strong> dans sa pochette de soie, un bol de rang plus élevé est choisi, et un <strong>kobukusa ou dashibukusa</strong> accompagne le bol jusqu&rsquo;aux invités. Un seul bol se partage entre plusieurs personnes.</p>
    </div>
  </div>
</section>
'''
w("fr/setup.html", shell_fr(
  "Ro et furo : la disposition saisonnière et la liste complète des ustensiles | Yusando",
  "Le foyer d’hiver (ro) et le brasero d’été (furo) comparés, schémas à l’appui — avec la liste de tous les ustensiles qu’un temae de thé léger réclame.",
  setup_body, root="../", current="setup"))


# --------------------------------------------------------------- articles --
articles_index_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">LECTURES — 読みもの</p>
    <h2 class="section-title">Entrer plus avant dans les ustensiles</h2>
    <div class="rule"></div>
    <p class="section-lede">Des lectures qui rendent le choix des ustensiles plus vivant. Commencez où vous voulez.<br>
    <span class="en-sub">Ces articles de fond existent pour l&rsquo;instant en japonais et en anglais.</span></p>
  </div>
  <div class="article-cards">
    {article_cards_fr(depth=2)}
  </div>
</section>
'''
w("fr/articles/index.html", shell_fr(
  "Lectures — Guides des ustensiles de thé | Yusando",
  "Des guides approfondis sur les bols, les bouilloires, les boîtes et les fouets, sur l’histoire de la voie du thé, et sur le calendrier des saisons qui façonne les ustensiles.",
  articles_index_body, root="../../", current="articles"))

print("pages françaises écrites")

PAGES_FR = ["index.html", "tools.html", "setup.html", "guide.html",
            "articles/index.html"]
