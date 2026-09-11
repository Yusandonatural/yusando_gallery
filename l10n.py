# -*- coding: utf-8 -*-
"""Shared post-processing for every language edition of the site.

One place decides: the language switcher, canonical/hreflang/OG tags, smart
quotes, cache-busting and the sitemap. Each gen_*.py just writes plain pages;
this module makes them a multilingual set.
"""
import os, re, hashlib
from gen import ROOT
from icons import icon as ico

SITE_URL = "https://gallery.yusando.com"

# prefix -> (html lang, og locale, endonym, short label)
LANGS = {
    "":    ("ja",      "ja_JP",   "日本語",    "日本語"),
    "en/": ("en",      "en_US",   "English",  "EN"),
    "fr/": ("fr",      "fr_FR",   "Français", "FR"),
    "zh/": ("zh-Hant", "zh_TW",   "繁體中文",  "繁中"),
}

SITE_NAME = {
    "":    "悠三堂古美術ギャラリー",
    "en/": "Yusando Antique Gallery",
    "fr/": "Yusando — Galerie d’Art Ancien",
    "zh/": "悠三堂古美術藝廊",
}

# The five pages that exist in every language. Anything outside this set is
# JA/EN only, so a FR/ZH page linking to it falls back to English.
CORE = ["index.html", "tools.html", "setup.html", "guide.html",
        "articles/index.html"] + [f"tools/{s}.html" for s in
        ("chawan", "chasen", "chashaku", "natsume",
         "kama", "hishaku", "fukusa", "mizusashi")]


# --------------------------------------------------------------- switcher --
# Latin sub-labels, so a reader who cannot read the endonym still finds their
# language. Kept short: they sit under the name, not beside it.
SUBLABEL = {
    "":    "JAPANESE",
    "en/": "ENGLISH",
    "fr/": "FRENCH",
    "zh/": "CHINESE \u00b7 TRAD.",
}


def switcher(prefix, page, depth):
    """A <details> disclosure, so open/close and the keyboard come free from
    the browser; lang.js only adds Escape and click-outside."""
    root = "../" * depth
    rows = ""
    for pfx, (code, _loc, endonym, _short) in LANGS.items():
        if pfx in ("fr/", "zh/") and page not in CORE:
            continue
        sub = f'<span class="l-sub">{SUBLABEL[pfx]}</span>'
        name = f'<span class="l-name">{endonym}</span>'
        if pfx == prefix:
            rows += f'<span class="l-row is-current" aria-current="page">{name}{sub}</span>'
        else:
            rows += (f'<a class="l-row" href="{root}{pfx}{page}" lang="{code}" '
                     f'hreflang="{code}">{name}{sub}</a>')
    cur = LANGS[prefix][2]
    return (
        '<details class="lang-sw">'
        f'<summary aria-label="Language / 言語">'
        f'<span class="l-globe">{ico("globe")}</span>'
        f'<span class="l-cur">{cur}</span></summary>'
        f'<div class="lang-menu">{rows}</div>'
        '</details>')


def inject_switcher(path, prefix, page):
    full = os.path.join(ROOT, path)
    html = open(full, encoding="utf-8").read()
    sw = switcher(prefix, page, path.count("/"))
    # replace whatever a previous build left: the <details>, the old <select>
    # wrapper, or the original JA/EN pill
    html = re.sub(r'<details class="lang-sw">.*?</details>', sw, html,
                  count=1, flags=re.S)
    if 'class="lang-sw"' in html:
        html = re.sub(r'<div class="lang-sw">.*?</div>\s*</div>', sw, html,
                      count=1, flags=re.S)
        html = re.sub(r'<a class="lang-sw".*?</a>', sw, html, count=1, flags=re.S)
    if 'class="lang-sw"' not in html:
        html = html.replace('</nav>', sw + '</nav>', 1)
    open(full, "w", encoding="utf-8").write(html)


LANG_JS = """// 言語切替 — <details> が開閉そのものを持つので、足すのは離脱時の始末だけ。
(function () {
  var d = document.querySelector('details.lang-sw');
  if (!d) return;
  document.addEventListener('click', function (e) {
    if (d.open && !d.contains(e.target)) d.open = false;
  });
  d.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' || !d.open) return;
    d.open = false;
    var s = d.querySelector('summary');
    if (s) s.focus();
  });
})();
"""


def write_lang_js():
    js = os.path.join(ROOT, "js", "lang.js")
    os.makedirs(os.path.dirname(js), exist_ok=True)
    open(js, "w", encoding="utf-8").write(LANG_JS)


def inject_lang_js(path):
    full = os.path.join(ROOT, path)
    html = open(full, encoding="utf-8").read()
    if 'js/lang.js' in html:
        return
    up = "../" * path.count("/")
    html = html.replace('</body>', f'<script src="{up}js/lang.js"></script>\n</body>', 1)
    open(full, "w", encoding="utf-8").write(html)


# ------------------------------------------------------------- head tags --
_STRIP = [
    r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?',
    r'<link rel="canonical" href="[^"]*">\n?',
    r'<meta (?:property="og:|name="twitter:)[^>]*>\n?',
    r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n?',
    r'<meta name="theme-color"[^>]*>\n?',
]


def _loc(p):
    u = f"{SITE_URL}/{p}"
    return u[: -len("index.html")] if u.endswith("/index.html") else u


def alternates(page):
    """Every language edition that actually exists for this page."""
    return [p for p in LANGS
            if p not in ("fr/", "zh/") or page in CORE]


def inject_head(path, prefix, page):
    full = os.path.join(ROOT, path)
    html = open(full, encoding="utf-8").read()
    for pat in _STRIP:
        html = re.sub(pat, '', html)
    up = "../" * path.count("/")

    m = re.search(r'<title>(.*?)</title>', html, re.S)
    title = re.sub(r'\s+', ' ', m.group(1)).strip() if m else SITE_NAME[prefix]
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    desc = m.group(1) if m else ""
    title, desc = title.replace('"', '&quot;'), desc.replace('"', '&quot;')

    code, oglocale, _e, _s = LANGS[prefix]
    img = f'{SITE_URL}/assets/ogp.png' if prefix == "" \
        else f'{SITE_URL}/assets/ogp-en.png'

    alts = "".join(
        f'<link rel="alternate" hreflang="{LANGS[p][0]}" href="{_loc(p + page)}">\n'
        for p in alternates(page))
    others = "".join(
        f'<meta property="og:locale:alternate" content="{LANGS[p][1]}">\n'
        for p in alternates(page) if p != prefix)

    tags = (
        f'<link rel="icon" type="image/svg+xml" href="{up}assets/favicon.svg">\n'
        f'<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">\n'
        f'<meta name="theme-color" content="#4a5d3a">\n'
        f'<link rel="canonical" href="{_loc(path)}">\n'
        + alts
        + f'<link rel="alternate" hreflang="x-default" href="{_loc(page)}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:site_name" content="{SITE_NAME[prefix]}">\n'
        f'<meta property="og:locale" content="{oglocale}">\n'
        + others +
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{_loc(path)}">\n'
        f'<meta property="og:image" content="{img}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<meta name="twitter:image" content="{img}">\n'
    )
    open(full, "w", encoding="utf-8").write(
        html.replace('</head>', tags + '</head>', 1))


# ------------------------------------------------------------ typography --
_SKIP = re.compile(r'<(script|style|svg)\b[^>]*>.*?</\1>', re.S | re.I)


def _smart_text(t, fr=False):
    t = re.sub(r'(\w)\'(\w)', '\\1\u2019\\2', t)
    t = re.sub(r'(\w)\'(?=[\s,.;:!?)]|$)', '\\1\u2019', t)
    if fr:
        # French takes guillemets and a narrow no-break space before ; : ! ?
        t = re.sub(r'"([^"\n]+)"', '\u00ab\u202f\\1\u202f\u00bb', t)
        t = re.sub(r'(?<=[^\s\u202f])(?=[;:!?](?:\s|$))', '\u202f', t)
    else:
        t = re.sub(r'"([^"\n]+)"', '\u201c\\1\u201d', t)
    t = re.sub(r'&(?![a-zA-Z#][a-zA-Z0-9]{0,8};)', '&amp;', t)
    return t


def smarten(html, prefix=""):
    """Curly quotes in text nodes only. Skipped for Chinese, which uses its
    own full-width punctuation already."""
    if prefix == "zh/":
        return html
    fr = prefix == "fr/"
    blocks = []

    def stash(m):
        blocks.append(m.group(0))
        return f"\x00{len(blocks) - 1}\x00"

    html = _SKIP.sub(stash, html)
    parts = re.split(r'(<[^>]*>)', html)
    html = "".join(p if i % 2 else _smart_text(p, fr)
                   for i, p in enumerate(parts))
    return re.sub(r'\x00(\d+)\x00', lambda m: blocks[int(m.group(1))], html)


# ---------------------------------------------------------------- runner --
def finish(pages_by_lang):
    """pages_by_lang: {prefix: [page, ...]} — run last, after every generator."""
    ver = {}
    for name in ("site", "lang"):
        ver[name] = hashlib.md5(
            open(os.path.join(ROOT, "js", f"{name}.js"), encoding="utf-8")
            .read().encode()).hexdigest()[:8]

    write_lang_js()
    seen = []
    for prefix, pages in pages_by_lang.items():
        for page in pages:
            path = prefix + page
            full = os.path.join(ROOT, path)
            if not os.path.exists(full):
                print("  ! missing", path)
                continue
            inject_switcher(path, prefix, page)
            inject_lang_js(path)
            src = open(full, encoding="utf-8").read()
            for name, v in ver.items():
                src = re.sub(rf'js/{name}\.js(\?v=[0-9a-f]+)?',
                             f'js/{name}.js?v={v}', src)
            open(full, "w", encoding="utf-8").write(smarten(src, prefix))
            inject_head(path, prefix, page)
            seen.append((prefix, page))
    print(f"l10n: switcher + hreflang + typography on {len(seen)} pages")
    sitemap(pages_by_lang)


def sitemap(pages_by_lang):
    rows = []
    for prefix, pages in pages_by_lang.items():
        for page in pages:
            prio = "1.0" if page == "index.html" else (
                "0.8" if "/" not in page else "0.7")
            alts = "".join(
                f'    <xhtml:link rel="alternate" hreflang="{LANGS[p][0]}" '
                f'href="{_loc(p + page)}"/>\n' for p in alternates(page))
            rows.append(
                "  <url>\n"
                f"    <loc>{_loc(prefix + page)}</loc>\n"
                + alts +
                f'    <xhtml:link rel="alternate" hreflang="x-default" '
                f'href="{_loc(page)}"/>\n'
                f"    <changefreq>monthly</changefreq>\n"
                f"    <priority>{prio}</priority>\n"
                "  </url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"sitemap: {len(rows)} urls")
