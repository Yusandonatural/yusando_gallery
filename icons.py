# -*- coding: utf-8 -*-
"""24x24 line-icon set for the utensils.

Each entry holds geometry only — no stroke, fill or stroke-width. Those are
inherited from the host `<svg class="ico">`, so one symbol serves every size
and colour (currentColor) on the site.
"""

ICONS = {

# ---------------------------------------------------------------- 点前道具 --
"chawan": """
<ellipse cx="12" cy="7.6" rx="8" ry="2.2"/>
<path d="M4 7.6c.35 6.1 3.5 10.2 8 10.2s7.65-4.1 8-10.2"/>
<path d="M9.9 17.6 9.3 20.4M14.1 17.6l.6 2.8M8.7 20.4h6.6"/>
""",

"chasen": """
<path d="M9.9 12.3C8.7 9.5 8.1 6.8 8.1 4.5"/>
<path d="M11 12.3c-.6-3.1-.8-5.8-.7-8.1"/>
<path d="M12 12.3V3.8"/>
<path d="M13 12.3c.6-3.1.8-5.8.7-8.1"/>
<path d="M14.1 12.3c1.2-2.8 1.8-5.5 1.8-7.8"/>
<path d="M8.6 12.6h6.8"/>
<path d="M9.8 12.6v7.2M14.2 12.6v7.2M9.8 19.8h4.4"/>
""",

"chashaku": """
<path d="M3.8 20.2 15.9 8.1"/>
<path d="M9.3 14.7l1.1 1.1"/>
<path d="M15.9 4.5c1.1-1.1 2.5-1.4 3.2-.7.7.7.4 2.1-.7 3.2s-2.5 1.4-3.2.7c-.7-.7-.4-2.1.7-3.2z"/>
""",

"natsume": """
<path d="M8.6 4.6h6.8"/>
<path d="M8.6 4.6c-1.1 1-1.7 2.3-1.7 3.9v6.8c0 2.6 2.2 4.5 5.1 4.5s5.1-1.9 5.1-4.5V8.5c0-1.6-.6-2.9-1.7-3.9"/>
<path d="M6.9 12.5h10.2"/>
""",

"kama": """
<path d="M4.6 12.2h14.8"/>
<path d="M6 12.2c0-3.6 2.7-5.9 6-5.9s6 2.3 6 5.9"/>
<path d="M4.6 12.2c.4 4.4 3.4 7.3 7.4 7.3s7-2.9 7.4-7.3"/>
<path d="M9.2 7.1h5.6M12 7V4.9"/>
<path d="M4.6 10.6H3M19.4 10.6H21"/>
""",

"hishaku": """
<path d="M4.2 10.2h7.4v3.1a3.7 3.7 0 0 1-7.4 0z"/>
<path d="M11.6 10.6 20.4 4.6"/>
<path d="M15.4 8 16.4 9.1"/>
""",

"fukusa": """
<path d="M4.6 6.6c2.5-1.4 4.9-1.4 7.4 0s4.9 1.4 7.4 0v9.4c-2.5 1.4-4.9 1.4-7.4 0s-4.9-1.4-7.4 0z"/>
<path d="M6.6 12.1c1.8-1 3.6-1 5.4 0s3.6 1 5.4 0"/>
""",

"mizusashi": """
<path d="M5.4 7.6h13.2M12 7.6V5.6"/>
<path d="M6.8 7.6c-.7 2.3-1 4.4-1 6.3 0 3.4 2.3 5.4 6.2 5.4s6.2-2 6.2-5.4c0-1.9-.3-4-1-6.3"/>
""",

"chaire": """
<path d="M9.6 5.4h4.8"/>
<path d="M8.4 8.6c0-1.9 1.6-3.2 3.6-3.2s3.6 1.3 3.6 3.2"/>
<path d="M8.4 8.6c-1.1 2-1.6 4-1.6 5.9 0 3 2.1 5 4.8 5h.8c2.7 0 4.8-2 4.8-5 0-1.9-.5-3.9-1.6-5.9"/>
""",

"kensui": """
<ellipse cx="12" cy="8.6" rx="7.4" ry="2.2"/>
<path d="M4.6 8.6c.4 5.2 2.9 8.4 7.4 8.4s7-3.2 7.4-8.4"/>
""",

"futaoki": """
<ellipse cx="12" cy="8.8" rx="5.2" ry="2"/>
<path d="M6.8 8.8v5.6M17.2 8.8v5.6"/>
<path d="M6.8 14.4a5.2 2 0 0 0 10.4 0"/>
""",

# ------------------------------------------------------------------ 炭道具 --
"sumitori": """
<path d="M4.4 9.6h15.2l-1.7 8.3a2.1 2.1 0 0 1-2.1 1.7H8.2a2.1 2.1 0 0 1-2.1-1.7z"/>
<path d="M8 9.6c0-3.1 1.8-4.8 4-4.8s4 1.7 4 4.8"/>
<path d="M6.8 14h10.4"/>
""",

"hibashi": """
<path d="M9.4 20.5 11.5 6.5"/>
<path d="M14.6 20.5 12.5 6.5"/>
<circle cx="12" cy="4.9" r="1.5"/>
""",

"haiki": """
<ellipse cx="10.6" cy="10.4" rx="7.2" ry="2.2"/>
<path d="M3.4 10.4c.4 4.8 2.8 7.7 7.2 7.7s6.8-2.9 7.2-7.7"/>
<path d="M6 13.4c1.5.9 3 1.3 4.6 1.3s3.1-.4 4.6-1.3"/>
""",

"kogo": """
<path d="M4.6 11.8c0-3.5 3.3-5.6 7.4-5.6s7.4 2.1 7.4 5.6"/>
<path d="M4.6 11.8h14.8"/>
<path d="M5.6 11.8v2a6.4 2.6 0 0 0 12.8 0v-2"/>
""",

"haboki": """
<path d="M5.4 19.6 17.6 6.4"/>
<path d="M17.6 6.4c-4.8.3-8.4 3-10 7.3 4.8.7 8.7-2 10-7.3z"/>
""",

# ------------------------------------------------------------ 席のしつらえ --
"kashiki": """
<ellipse cx="12" cy="8.6" rx="7.8" ry="2.4"/>
<path d="M4.2 8.6c.6 3.4 3.6 5.6 7.8 5.6s7.2-2.2 7.8-5.6"/>
<path d="M12 14.2v4.1M8 18.6h8"/>
""",

"hanaire": """
<path d="M8.8 8.2h6.4"/>
<path d="M9.4 8.2v9.6a2.4 2.4 0 0 0 2.4 2.4h.4a2.4 2.4 0 0 0 2.4-2.4V8.2"/>
<path d="M12 8.2c-.5-2.6.7-4.3 3-5.2"/>
<path d="M15 3c1.7.7 2.3 2.2 1.6 3.9C14.9 6.2 14.3 4.7 15 3z"/>
""",

"kakemono": """
<path d="M4.6 3.8h14.8"/>
<path d="M7.6 3.8v14.2M16.4 3.8v14.2"/>
<path d="M4.4 18h15.2a1.15 1.15 0 0 1 0 2.3H4.4a1.15 1.15 0 0 1 0-2.3z"/>
<path d="M10.8 7.6c2.1 1.6 2.8 3.8 1.8 6"/>
""",

"chatsubo": """
<path d="M9.4 4.6h5.2"/>
<path d="M7.8 8.2c0-2.1 1.9-3.6 4.2-3.6s4.2 1.5 4.2 3.6"/>
<path d="M7.8 8.2c-1.6 2.3-2.4 4.6-2.4 6.9 0 3.1 2.6 4.9 6.6 4.9s6.6-1.8 6.6-4.9c0-2.3-.8-4.6-2.4-6.9"/>
<path d="M7 9.6H5.6M17 9.6h1.4"/>
""",

# ------------------------------------------------------------------- 炉相 --
"ro": """
<path d="M2.6 13.5h6.4M15 13.5h6.4"/>
<path d="M9 13.5v5.9h6v-5.9"/>
<path d="M6.6 7.9h10.8"/>
<path d="M7.6 7.9c0-2 1.9-3.3 4.4-3.3s4.4 1.3 4.4 3.3"/>
<path d="M6.6 7.9c.3 2.6 2.5 4.4 5.4 4.4s5.1-1.8 5.4-4.4"/>
<path d="M10.1 4.6h3.8"/>
""",

"furo": """
<path d="M5.6 9.4h12.8"/>
<path d="M6.2 9.4c.5 5 2.7 7.8 5.8 7.8s5.3-2.8 5.8-7.8"/>
<path d="M9.6 13.4a2.4 2.4 0 0 1 4.8 0"/>
<path d="M3.4 19.6h17.2"/>
""",
}

SLUGS = tuple(ICONS)


def sprite():
    """The hidden symbol sheet, emitted once per page just after <body>."""
    syms = "".join(
        f'<symbol id="ico-{k}" viewBox="0 0 24 24">{v.strip()}</symbol>'
        for k, v in ICONS.items())
    return ('<svg class="ico-sprite" aria-hidden="true" '
            'style="position:absolute;width:0;height:0;overflow:hidden">'
            f'{syms}</svg>')


def icon(slug, cls=""):
    """A single icon instance. Colour and weight come from CSS."""
    c = ("ico " + cls).strip()
    return (f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true">'
            f'<use href="#ico-{slug}"></use></svg>')


def parts_icon(slug, dots, cls="ico--plate"):
    """Icon with numbered part markers, for the detail pages.

    `dots` are (x, y) in the 24-unit icon space.
    """
    marks = ""
    for i, (x, y) in enumerate(dots, 1):
        marks += (f'<circle cx="{x}" cy="{y}" r="1.15" fill="#a53f2b" '
                  f'stroke="none"/>'
                  f'<text x="{x}" y="{y + .48}" text-anchor="middle" '
                  f'font-size="1.35" fill="#f7f3ea" stroke="none" '
                  f'font-family="var(--sans),sans-serif">{i}</text>')
    c = ("ico " + cls).strip()
    return (f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true">'
            f'<use href="#ico-{slug}"></use>{marks}</svg>')
