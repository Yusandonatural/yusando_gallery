# -*- coding: utf-8 -*-
"""Top-page hero and the three promises beneath it, shared by every language.

Each gen_*.py passes its own words; the markup (and so the CSS in
css/style.css under "hero (top page)") stays identical across languages.
"""
from icons import icon as ico

# 筆で引いた円相。右下の朱の落款は Cerendipity の C（反転版）。
# 太い本線に細い掠れ線を重ねて、筆の抜けを出す。
_ENSO = '''<svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
      <path class="enso-main" d="M112 20 A80 80 0 1 0 172 62"/>
      <path class="enso-dry" d="M104 27 A73 73 0 1 0 166 70"/>
    </svg>'''


def hero(t, root=""):
    """t: kicker, title, sub, cta (list of (label, href)), note.

    CTA hrefs are relative to the page (same language folder); root points
    at the site root, for the shared logo asset only."""
    ctas = "".join(
        f'<a class="btn{" solid" if i == 0 else ""}" href="{href}">{label}</a>'
        for i, (label, href) in enumerate(t["cta"]))
    return f'''
<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <p class="hero-kicker">{t["kicker"]}</p>
      <h1 class="hero-title">{t["title"]}</h1>
      <p class="hero-sub">{t["sub"]}</p>
      <div class="hero-cta">{ctas}</div>
      <p class="hero-brand-note">{t["note"]}</p>
    </div>
    <figure class="hero-art" aria-hidden="true">
      {_ENSO}
      <div class="hero-bowl">{ico("chawan", "ico--hero")}</div>
      <div class="hero-tools">{ico("chasen", "ico--hero")}{ico("chashaku", "ico--hero")}</div>
      <span class="hero-seal"><img src="{root}assets/cerendipity-symbol-reverse.svg" alt="" width="40" height="40"></span>
    </figure>
  </div>
</section>'''


def promises(items, label):
    """items: list of (title, en, body). label: aria-label for the strip."""
    cells = "".join(
        f'''<div class="promise-cell">
      <span class="promise-num">{n}</span>
      <h2>{title}<span class="en-sub">{en}</span></h2>
      <p>{body}</p>
    </div>''' for n, (title, en, body) in zip(("一", "二", "三"), items))
    return f'''
<section class="promise reveal" aria-label="{label}">
  <div class="promise-grid">
    {cells}
  </div>
</section>'''
