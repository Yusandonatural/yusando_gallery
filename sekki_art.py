# -*- coding: utf-8 -*-
"""Seasonal motif line-art for the 24 solar terms (二十四節気).
One small SVG per sekki, drawn in the same two-tone style as the utensil icons."""

M = '#4a5d3a'   # matcha — main line
G = '#b0965a'   # gold  — accent


def _svg(body):
    return ('<svg viewBox="0 0 120 80" aria-hidden="true">' + body + '</svg>')


def _m(paths, w="2.2"):
    return (f'<g fill="none" stroke="{M}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{paths}</g>')


def _g(paths, w="1.6"):
    return (f'<g fill="none" stroke="{G}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{paths}</g>')


def _petals(cx, cy, path, n, step, extra=""):
    """Repeat one petal path around a centre by rotation."""
    inner = "".join(
        f'<path d="{path}" transform="rotate({i*step})"/>' for i in range(n))
    return f'<g transform="translate({cx},{cy})">{inner}{extra}</g>'


# leaf helper: a simple pointed leaf hanging off a stem
def _leaf(d):
    return f'<path d="{d}"/>'


MOTIF = {}

# ---------------------------------------------------------------- SPRING ----
# 立春 — 椿 camellia (five round petals)
MOTIF["risshun"] = _svg(
    _m('<circle cx="60" cy="22" r="10"/><circle cx="74" cy="32" r="10"/>'
       '<circle cx="69" cy="49" r="10"/><circle cx="51" cy="49" r="10"/>'
       '<circle cx="46" cy="32" r="10"/>'
       '<path d="M60 59 v17"/>'
       '<path d="M60 64 C50 60 42 63 40 70 C48 74 56 71 60 64 Z"/>'
       '<path d="M60 68 C70 64 78 67 80 74 C72 78 63 75 60 68 Z"/>')
    + _g('<circle cx="60" cy="36" r="4.5"/>'))

# 雨水 — 梅 plum blossom on a branch
MOTIF["usui"] = _svg(
    _m('<path d="M12 68 C32 62 52 52 70 34"/>'
       '<circle cx="82" cy="24" r="7"/><circle cx="94" cy="31" r="7"/>'
       '<circle cx="91" cy="44" r="7"/><circle cx="78" cy="46" r="7"/>'
       '<circle cx="72" cy="33" r="7"/>')
    + _g('<circle cx="83" cy="35" r="3"/><circle cx="46" cy="50" r="3.5"/>'
         '<circle cx="30" cy="60" r="2.5"/>'))

# 啓蟄 — 蕨 fiddlehead ferns uncurling
MOTIF["keichitsu"] = _svg(
    _m('<path d="M36 76 C36 50 38 32 47 26 C54 21 61 25 59 32 C57 38 50 38 48 32"/>'
       '<path d="M60 76 C60 44 63 26 73 20 C81 15 88 20 86 27 C84 34 76 34 74 28"/>'
       '<path d="M84 76 C84 58 86 44 92 38"/>')
    + _g('<circle cx="94" cy="34" r="3.5"/>'))

# 春分 — 桜 cherry blossom (notched petals)
MOTIF["shunbun"] = _svg(
    _m(_petals(60, 40, "M0 0 C-7 -9 -7 -19 -3 -24 C-2 -21 2 -21 3 -24 C7 -19 7 -9 0 0 Z", 5, 72))
    + _g('<circle cx="60" cy="40" r="3.6"/>'
         '<path d="M60 40 l0 -9 M60 40 l-8 -4 M60 40 l8 -4"/>'))

# 清明 — 燕 returning swallow
MOTIF["seimei"] = _svg(
    _m('<path d="M60 32 C48 24 32 16 14 12 C24 27 40 38 54 43 '
       'L43 70 L60 53 L77 70 L66 43 '
       'C80 38 96 27 106 12 C88 16 72 24 60 32 Z"/>')
    + _g('<path d="M54 34 C57 38 63 38 66 34"/>'
         '<path d="M20 58 C32 55 44 55 54 58"/>'))

# 穀雨 — 藤 wisteria in hanging clusters
MOTIF["kokuu"] = _svg(
    _m('<path d="M14 14 C38 8 68 8 106 14"/>'
       '<circle cx="36" cy="26" r="4.5"/><circle cx="48" cy="26" r="4.5"/>'
       '<circle cx="38" cy="36" r="4"/><circle cx="46" cy="36" r="4"/>'
       '<circle cx="40" cy="45" r="3.4"/><circle cx="45" cy="45" r="3.4"/>'
       '<circle cx="42" cy="53" r="2.8"/>'
       '<circle cx="40" cy="61" r="2.4"/>'
       '<circle cx="72" cy="20" r="4.5"/><circle cx="84" cy="20" r="4.5"/>'
       '<circle cx="74" cy="30" r="4"/><circle cx="82" cy="30" r="4"/>'
       '<circle cx="75" cy="39" r="3.4"/><circle cx="81" cy="39" r="3.4"/>'
       '<circle cx="76" cy="47" r="2.8"/><circle cx="81" cy="47" r="2.8"/>'
       '<circle cx="79" cy="55" r="2.4"/>')
    + _g('<circle cx="42" cy="20" r="2.2"/><circle cx="60" cy="18" r="2.2"/>'
         '<circle cx="88" cy="19" r="2.2"/>'))

# ---------------------------------------------------------------- SUMMER ----
# 立夏 — 若楓 young maple
MOTIF["rikka"] = _svg(
    _m('<path d="M60 74 V48"/>'
       '<path d="M60 48 L47 41 L52 37 L37 30 L46 28 L39 17 L52 22 L54 12 '
       'L60 23 L66 12 L68 22 L81 17 L74 28 L83 30 L68 37 L73 41 Z"/>')
    + _g('<path d="M60 46 V26 M60 38 L48 31 M60 38 L72 31"/>'))

# 小満 — 卯の花 deutzia
MOTIF["shoman"] = _svg(
    _m('<path d="M14 72 C32 62 48 50 60 34"/>'
       '<circle cx="62" cy="22" r="4.6"/><circle cx="69" cy="29" r="4.6"/>'
       '<circle cx="62" cy="36" r="4.6"/><circle cx="55" cy="29" r="4.6"/>'
       '<circle cx="84" cy="16" r="4"/><circle cx="90" cy="22" r="4"/>'
       '<circle cx="84" cy="28" r="4"/><circle cx="78" cy="22" r="4"/>'
       '<circle cx="42" cy="48" r="3.4"/><circle cx="48" cy="53" r="3.4"/>'
       '<circle cx="42" cy="58" r="3.4"/><circle cx="36" cy="53" r="3.4"/>')
    + _g('<circle cx="62" cy="29" r="2.2"/><circle cx="84" cy="22" r="2"/>'
         '<circle cx="42" cy="53" r="1.8"/>'))

# 芒種 — 蛍袋と蛍 campanula with a firefly
MOTIF["boshu"] = _svg(
    _m('<ellipse cx="62" cy="34" rx="13" ry="8" transform="rotate(-20 62 34)"/>'
       '<path d="M55 29 C61 25 69 25 73 29"/>'
       '<circle cx="75" cy="25" r="4.4"/>'
       '<path d="M78 21 C83 15 89 12 96 11"/>'
       '<path d="M79 25 C85 22 91 21 98 21"/>')
    + _g('<circle cx="49" cy="43" r="6"/>'
         '<circle cx="49" cy="43" r="11.5"/>'
         '<path d="M18 70 C25 63 33 55 40 50"/>'
         '<path d="M10 62 C18 58 26 53 32 49"/>'))

# 夏至 — 紫陽花 hydrangea
MOTIF["geshi"] = _svg(
    _m('<circle cx="60" cy="15" r="4.8"/><circle cx="66" cy="21" r="4.8"/>'
       '<circle cx="60" cy="27" r="4.8"/><circle cx="54" cy="21" r="4.8"/>'
       '<circle cx="44" cy="30" r="4.8"/><circle cx="50" cy="36" r="4.8"/>'
       '<circle cx="44" cy="42" r="4.8"/><circle cx="38" cy="36" r="4.8"/>'
       '<circle cx="76" cy="30" r="4.8"/><circle cx="82" cy="36" r="4.8"/>'
       '<circle cx="76" cy="42" r="4.8"/><circle cx="70" cy="36" r="4.8"/>'
       '<circle cx="60" cy="42" r="4.8"/><circle cx="66" cy="48" r="4.8"/>'
       '<circle cx="60" cy="54" r="4.8"/><circle cx="54" cy="48" r="4.8"/>'
       '<path d="M60 60 v14"/>'
       '<path d="M60 64 C50 60 42 63 40 70 C48 74 56 71 60 64 Z"/>'
       '<path d="M60 66 C70 62 78 65 80 72 C72 76 63 73 60 66 Z"/>')
    + _g('<circle cx="60" cy="21" r="1.8"/><circle cx="44" cy="36" r="1.8"/>'
         '<circle cx="76" cy="36" r="1.8"/><circle cx="60" cy="48" r="1.8"/>'))

# 小暑 — 笹に短冊 tanabata bamboo
MOTIF["shosho_s"] = _svg(
    _m('<path d="M36 78 C36 52 38 30 42 8"/>'
       '<path d="M35 58 h7 M37 36 h7"/>'
       '<path d="M42 28 C54 19 70 17 84 22 C72 31 56 33 42 28 Z"/>'
       '<path d="M40 52 C52 45 68 45 80 52 C68 59 52 59 40 52 Z"/>')
    + _g('<path d="M76 36 h13 v20 h-13 Z"/>'
         '<path d="M82 36 v-6 C82 27 78 27 78 30"/>'))

# 大暑 — 蓮 lotus on water
MOTIF["taisho"] = _svg(
    _m('<path d="M60 46 C44 42 32 31 30 20 C43 20 55 31 60 46 Z"/>'
       '<path d="M60 46 C76 42 88 31 90 20 C77 20 65 31 60 46 Z"/>'
       '<path d="M60 47 C50 42 44 29 46 16 C57 23 63 34 60 47 Z"/>'
       '<path d="M60 47 C70 42 76 29 74 16 C63 23 57 34 60 47 Z"/>'
       '<path d="M60 48 C55 37 55 23 60 12 C65 23 65 37 60 48 Z"/>')
    + _g('<path d="M52 48 C56 54 64 54 68 48"/>'
         '<path d="M16 62 C34 67 86 67 104 62"/>'
         '<path d="M22 72 C40 76 80 76 98 72"/>'))

# ---------------------------------------------------------------- AUTUMN ----
# 立秋 — 桔梗 bellflower star
MOTIF["risshu"] = _svg(
    _m('<path d="M60 14 L67 30 L85 31 L71 44 L76 61 L60 52 L44 61 L49 44 '
       'L35 31 L53 30 Z"/>'
       '<path d="M60 60 v16"/>'
       '<path d="M60 66 C51 62 44 65 42 71 C50 75 57 72 60 66 Z"/>')
    + _g('<circle cx="60" cy="38" r="3.6"/>'
         '<path d="M60 38 l0 -8 M60 38 l-7 4 M60 38 l7 4"/>'))

# 処暑 — 萩 bush clover
MOTIF["shosho_a"] = _svg(
    _m('<path d="M10 12 C34 26 56 48 74 76"/>'
       '<path d="M34 8 C56 22 76 46 92 76"/>'
       '<path d="M30 28 C24 22 17 24 15 30 C21 34 27 32 30 28 Z"/>'
       '<path d="M48 46 C42 40 35 42 33 48 C39 52 45 50 48 46 Z"/>'
       '<path d="M60 24 C56 17 49 16 45 21 C50 26 57 27 60 24 Z"/>')
    + _g('<ellipse cx="40" cy="30" rx="4.2" ry="3.2"/>'
         '<ellipse cx="57" cy="48" rx="4.2" ry="3.2"/>'
         '<ellipse cx="70" cy="66" rx="4.2" ry="3.2"/>'
         '<ellipse cx="66" cy="30" rx="3.8" ry="3"/>'
         '<ellipse cx="82" cy="54" rx="3.8" ry="3"/>'))

# 白露 — 芒 pampas grass
MOTIF["hakuro"] = _svg(
    _m('<path d="M26 78 C30 56 36 40 43 28"/>'
       '<path d="M56 78 C58 54 62 34 67 22"/>'
       '<path d="M86 78 C86 58 90 42 95 32"/>')
    + _g('<path d="M43 28 C36 23 31 18 28 12 M43 28 C39 21 37 16 36 10 '
         'M43 28 C44 20 45 14 46 9 M43 28 C48 21 53 17 58 14 '
         'M43 28 C50 25 56 23 62 22"/>'
         '<path d="M67 22 C60 17 55 12 52 6 M67 22 C63 15 61 10 60 4 '
         'M67 22 C68 14 69 9 70 4 M67 22 C72 15 77 11 82 8 '
         'M67 22 C74 19 80 17 86 16"/>'
         '<path d="M95 32 C88 27 83 22 80 16 M95 32 C91 25 89 20 88 14 '
         'M95 32 C96 24 97 19 98 14 M95 32 C100 25 105 21 110 18"/>'))

# 秋分 — 竜胆 gentian
MOTIF["shubun"] = _svg(
    _m('<path d="M60 78 V42"/>'
       '<path d="M46 42 C42 31 45 18 51 12 C57 19 57 33 53 42 Z"/>'
       '<path d="M60 40 C56 27 58 12 62 6 C68 13 68 29 64 40 Z"/>'
       '<path d="M72 44 C70 33 74 21 80 17 C84 25 82 37 78 44 Z"/>'
       '<path d="M60 56 C50 52 43 54 41 60 C49 64 57 62 60 56 Z"/>'
       '<path d="M60 64 C70 60 77 62 79 68 C71 72 63 70 60 64 Z"/>')
    + _g('<path d="M50 20 v16 M62 14 v20 M78 25 v14"/>'))

# 寒露 — 野菊 wild chrysanthemum
MOTIF["kanro"] = _svg(
    _m(_petals(60, 34, "M0 -8 C-3.6 -12 -3.6 -20 0 -24 C3.6 -20 3.6 -12 0 -8 Z", 12, 30))
    + _m('<path d="M60 46 v30"/>'
         '<path d="M60 56 C51 52 44 55 42 61 C50 65 57 62 60 56 Z"/>'
         '<path d="M60 66 C69 62 76 65 78 71 C70 75 63 72 60 66 Z"/>')
    + _g('<circle cx="60" cy="34" r="5.5"/>'))

# 霜降 — 紅葉 turning maple
MOTIF["soko"] = _svg(
    _m('<path d="M46 70 V48"/>'
       '<path d="M46 48 L34 42 L39 38 L25 32 L33 30 L27 20 L38 24 L40 15 '
       'L46 25 L52 15 L54 24 L65 20 L59 30 L67 32 L53 38 L58 42 Z"/>')
    + _g('<path d="M88 62 L80 58 L83 55 L74 51 L79 49 L75 43 L82 46 L84 40 '
         'L88 47 L92 40 L94 46 L101 43 L97 49 L102 51 L93 55 L96 58 Z"/>'
         '<path d="M88 62 V72"/>'
         '<path d="M46 46 V28 M46 38 L36 33 M46 38 L56 33"/>'))

# ---------------------------------------------------------------- WINTER ----
# 立冬 — 侘助椿 wabisuke camellia bud
MOTIF["ritto"] = _svg(
    _m('<path d="M60 16 C51 21 47 33 49 46 C51 55 69 55 71 46 C73 33 69 21 60 16 Z"/>'
       '<path d="M53 30 C57 25 63 25 67 30"/>'
       '<path d="M50 48 C55 55 65 55 70 48"/>'
       '<path d="M60 54 v20"/>'
       '<path d="M60 60 C50 56 42 59 40 66 C48 70 57 67 60 60 Z"/>'
       '<path d="M60 66 C70 62 78 65 80 72 C72 76 63 73 60 66 Z"/>')
    + _g('<circle cx="60" cy="20" r="2.6"/>'))

# 小雪 — 山茶花 sasanqua (many slender petals)
MOTIF["shosetsu"] = _svg(
    _m(_petals(60, 34, "M0 -5 C-5 -10 -5 -19 0 -24 C5 -19 5 -10 0 -5 Z", 8, 45))
    + _m('<path d="M60 44 v30"/>'
         '<path d="M60 54 C50 50 43 53 41 59 C49 63 57 60 60 54 Z"/>'
         '<path d="M60 64 C70 60 77 63 79 69 C71 73 63 70 60 64 Z"/>')
    + _g('<circle cx="60" cy="34" r="4.6"/>'
         '<path d="M60 34 l0 -7 M60 34 l-6 4 M60 34 l6 4"/>'))

# 大雪 — 水仙 narcissus
MOTIF["taisetsu"] = _svg(
    _m(_petals(60, 30, "M0 -8 C-7 -12 -7 -22 0 -26 C7 -22 7 -12 0 -8 Z", 6, 60))
    + _m('<path d="M60 44 C57 56 54 68 51 78"/>'
         '<path d="M60 44 C64 56 68 68 71 78"/>'
         '<path d="M60 44 v34"/>')
    + _g('<circle cx="60" cy="30" r="7.5"/><circle cx="60" cy="30" r="3.4"/>'))

# 冬至 — 南天 nandina berries
MOTIF["toji"] = _svg(
    _m('<path d="M60 78 V44"/>'
       '<path d="M60 52 C50 48 42 51 40 57 C48 61 57 58 60 52 Z"/>'
       '<path d="M60 62 C70 58 78 61 80 67 C72 71 63 68 60 62 Z"/>'
       '<path d="M60 44 C60 34 58 26 56 20"/>')
    + _g('<circle cx="60" cy="12" r="4.6"/>'
         '<circle cx="51" cy="19" r="4.6"/><circle cx="69" cy="19" r="4.6"/>'
         '<circle cx="44" cy="27" r="4.6"/><circle cx="60" cy="27" r="4.6"/>'
         '<circle cx="76" cy="27" r="4.6"/>'
         '<circle cx="51" cy="35" r="4.6"/><circle cx="69" cy="35" r="4.6"/>'))

# 小寒 — 結び柳 the looped New Year willow
MOTIF["shokan"] = _svg(
    _m('<path d="M54 46 h13 v32 h-13 Z"/>'
       '<path d="M54 60 h13"/>'
       '<path d="M60 46 C57 36 55 27 60 19 C66 10 78 14 76 25 C74 33 64 34 61 26"/>'
       '<path d="M62 28 C58 43 52 59 48 77"/>'
       '<path d="M67 30 C72 45 76 61 77 77"/>')
    + _g('<path d="M55 46 l-7 3 M71 48 l7 3 M51 60 l-7 3 M74 62 l7 3 '
         'M49 70 l-6 3 M76 70 l6 3"/>'))

# 大寒 — 蝋梅 wintersweet on a bare branch
MOTIF["daikan"] = _svg(
    _m('<path d="M12 74 C32 62 50 46 66 22"/>'
       '<path d="M40 50 C50 44 60 42 70 44"/>')
    + _g('<circle cx="68" cy="16" r="3"/><circle cx="72" cy="19" r="3"/>'
         '<circle cx="70" cy="23" r="3"/><circle cx="66" cy="23" r="3"/>'
         '<circle cx="64" cy="19" r="3"/>'
         '<circle cx="72" cy="38" r="2.8"/><circle cx="76" cy="41" r="2.8"/>'
         '<circle cx="74" cy="45" r="2.8"/><circle cx="70" cy="45" r="2.8"/>'
         '<circle cx="68" cy="41" r="2.8"/>'
         '<circle cx="47" cy="42" r="2.6"/><circle cx="51" cy="45" r="2.6"/>'
         '<circle cx="49" cy="49" r="2.6"/><circle cx="45" cy="49" r="2.6"/>'
         '<circle cx="43" cy="45" r="2.6"/>'
         '<circle cx="26" cy="64" r="2.4"/>'))
