# -*- coding: utf-8 -*-
"""Generate the multi-page chadogu portal site."""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600&family=Zen+Kaku+Gothic+New:wght@300;400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">'''

# ---------------------------------------------------------------- SVG art ----
ART = {
"chawan": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M25 34 q55 -14 110 0 q2 34 -22 50 q-14 9 -33 9 t-33 -9 q-24 -16 -22 -50z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M58 97 h44 v6 h-44z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M38 42 q42 10 84 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"chasen": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M74 62 h12 v40 h-12z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M80 62 C 46 44 42 24 44 10 M80 62 C 60 42 56 22 60 8 M80 62 C 74 40 73 20 75 7 M80 62 C 86 40 87 20 85 7 M80 62 C 100 42 104 22 100 8 M80 62 C 114 44 118 24 116 10" fill="none" stroke="#4a5d3a" stroke-width="2.4" stroke-linecap="round"/>
<path d="M66 58 q14 8 28 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"chashaku": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M20 88 L 118 40 q6 -3 12 -6 q8 -4 12 -12 q2 -5 -2 -7 q-4 -2 -8 2 q-6 6 -8 14 l-4 10" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linecap="round"/>
<circle cx="60" cy="68" r="2.4" fill="#b0965a"/></svg>''',
"natsume": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M52 38 q28 -10 56 0 q6 26 -4 48 q-4 12 -24 12 t-24 -12 q-10 -22 -4 -48z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M52 38 q28 8 56 0" fill="none" stroke="#4a5d3a" stroke-width="2.4"/>
<path d="M58 20 q22 -8 44 0 l2 18 M56 38 l2 -18" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M70 12 q10 -3 20 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"kama": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M40 42 q40 -14 80 0 q14 24 0 46 q-8 14 -40 14 t-40 -14 q-14 -22 0 -46z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M40 42 q40 10 80 0" fill="none" stroke="#4a5d3a" stroke-width="2.4"/>
<path d="M64 30 h32 M72 30 v-8 h16 v8" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M36 56 q-8 2 -6 8 M124 56 q8 2 6 8" fill="none" stroke="#b0965a" stroke-width="2.4" stroke-linecap="round"/></svg>''',
"hishaku": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M30 78 q0 -14 16 -14 q16 0 16 14 q0 12 -16 12 q-16 0 -16 -12z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M62 72 L 138 34" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linecap="round"/>
<path d="M132 30 l8 6" fill="none" stroke="#b0965a" stroke-width="2.4" stroke-linecap="round"/></svg>''',
"fukusa": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M42 26 h76 l-8 62 h-76z" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linejoin="round"/>
<path d="M42 26 l30 30 46 -30" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"mizusashi": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M46 34 h68 q8 30 0 58 q-2 10 -34 10 t-34 -10 q-8 -28 0 -58z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M42 34 h76 M50 24 h60 l4 10 h-68z" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linejoin="round"/>
<path d="M56 52 q24 8 48 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
# minor utensils (list page only)
"chaire": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M62 40 q18 -8 36 0 q8 24 0 50 q-2 10 -18 10 t-18 -10 q-8 -26 0 -50z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M66 40 h28 M70 30 h20 l3 10 h-26z" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linejoin="round"/>
<path d="M74 24 q6 -2 12 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"kensui": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M38 44 q42 -12 84 0 l-10 44 q-3 12 -32 12 t-32 -12z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M38 44 q42 10 84 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"futaoki": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M58 46 h44 v34 h-44z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<ellipse cx="80" cy="46" rx="22" ry="7" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M58 80 q22 8 44 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"kogo": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<ellipse cx="80" cy="66" rx="34" ry="18" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M50 60 q30 -26 60 0" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M68 46 q12 -5 24 0" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"hanaire": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M66 30 h28 v14 q10 8 10 26 q0 30 -24 30 t-24 -30 q0 -18 10 -26z" fill="none" stroke="#4a5d3a" stroke-width="3" stroke-linejoin="round"/>
<path d="M80 30 q-4 -14 6 -22 M84 30 q10 -10 22 -8" fill="none" stroke="#b0965a" stroke-width="2" stroke-linecap="round"/></svg>''',
"kakemono": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M58 14 h44 M62 20 h36 v72 h-36z M58 98 h44" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<circle cx="80" cy="52" r="11" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
"furo": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M44 36 q36 -10 72 0 q8 20 0 40 q-6 16 -36 16 t-36 -16 q-8 -20 0 -40z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M60 50 h40 v14 h-40z" fill="none" stroke="#b0965a" stroke-width="2"/>
<path d="M56 92 h8 M96 92 h8" stroke="#4a5d3a" stroke-width="3"/></svg>''',
"kashiki": '''<svg viewBox="0 0 160 110" aria-hidden="true">
<path d="M34 62 q46 -16 92 0 q-4 20 -46 20 t-46 -20z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<path d="M64 80 h32 v8 h-32z" fill="none" stroke="#4a5d3a" stroke-width="3"/>
<circle cx="72" cy="54" r="5" fill="none" stroke="#b0965a" stroke-width="2"/>
<circle cx="90" cy="50" r="5" fill="none" stroke="#b0965a" stroke-width="2"/></svg>''',
}

def parts_svg(slug, dots):
    """Return the base art with numbered part-dots overlaid."""
    base = ART[slug]
    overlay = ""
    for i, (x, y) in enumerate(dots, 1):
        overlay += f'<circle cx="{x}" cy="{y}" r="7.5" fill="#a53f2b"/>'
        overlay += f'<text x="{x}" y="{y+3.4}" text-anchor="middle" font-size="9" fill="#f7f3ea" font-family="sans-serif">{i}</text>'
    return base.replace("</svg>", overlay + "</svg>")

# ---------------------------------------------------------------- data ----
TOOLS = [
dict(slug="chawan", name="茶碗", yomi="ちゃわん", romaji="Chawan", en="Tea Bowl", num="01",
  cat="点前道具", tags=["点前道具","陶磁器","季節で使い分け"],
  lede="茶を点て、そのまま口に運ぶ器。亭主の好みと季節がもっとも表れる、茶道具の主役です。",
  lede_en="The bowl in which tea is whisked and drunk — the centerpiece of the utensils.",
  names=[("正式名称","茶碗(ちゃわん)"),("英語名","Chawan / Tea Bowl"),
         ("主な分類","楽茶碗・萩茶碗・唐津茶碗・志野茶碗・天目茶碗 など"),
         ("季節の別","夏=平茶碗(浅く広い) / 冬=筒茶碗(深く湯が冷めにくい)")],
  history=["茶碗の歴史は、茶とともに中国から渡来した唐物(からもの)天目茶碗に始まります。室町時代には唐物が最高の格式とされましたが、侘び茶の成立とともに朝鮮半島の高麗茶碗、さらに国内の和物茶碗へと好みが移っていきました。",
    "桃山時代、千利休の侘びの美意識に応えて長次郎が焼いた楽茶碗は、轆轤を使わず手捏ねで成形される日本独自の茶碗です。以後「一楽二萩三唐津」と称されるように、楽・萩・唐津をはじめ各地の窯で茶碗が焼かれ、いまも茶人の掌中で愛され続けています。"],
  parts_dots=[(80,30),(80,55),(30,60),(48,84),(80,100)],
  parts=[("口造り(くちづくり)","口をつける縁の部分。厚み・反りで飲み心地が変わる"),
         ("見込み(みこみ)","碗の内側。茶が点てやすい広さと深さが要"),
         ("胴(どう)","碗の側面。景色(釉薬の変化)の見どころ"),
         ("腰(こし)","胴から高台への曲がり。手取りの印象を決める"),
         ("高台(こうだい)","底の足。削りに作者の個性が表れる")],
  usage=[("拝見する","両手で扱い、畳の上では低い位置で。正面(景色のよい側)を確かめます。"),
         ("茶を受ける","出された茶碗は正面を避けて口をつけるのが客の作法。二口半ほどでいただきます。"),
         ("清める","使用後はぬるま湯のみで洗い、洗剤は使いません。よく乾かしてから箱に納めます。")],
  checks=[("ニュウ・ホツ","口縁の小さな欠け(ホツ)や釉のひび(ニュウ)は要確認。景色として好まれる場合もあり、状態表記を確かめます。"),
          ("直しの有無","金継ぎ・銀継ぎなどの直しは価値を下げるとは限りませんが、茶席で使えるかは直しの質によります。"),
          ("共箱・箱書","作者の署名箱(共箱)や茶人の書付があるかで評価が大きく変わります。"),
          ("高台と土","高台の削りと土見せは真贋・窯の判断材料。写真だけでなく実物確認が安心です。")]),

dict(slug="chasen", name="茶筅", yomi="ちゃせん", romaji="Chasen", en="Tea Whisk", num="02",
  cat="点前道具", tags=["点前道具","竹工芸","消耗品"],
  lede="一本の竹から削り出される、茶を点てるための道具。奈良・高山で五百年続く竹の工芸です。",
  lede_en="A whisk carved from a single piece of bamboo, used to froth the tea.",
  names=[("正式名称","茶筅(ちゃせん)※「茶筌」とも書く"),("英語名","Chasen / Tea Whisk"),
         ("主な種類","数穂(70本前後)・八十本立・百本立・百二十本立 など"),
         ("使い分け","濃茶=穂の少ない荒穂 / 薄茶=穂の多いもの")],
  history=["茶筅の起源は室町時代、奈良・高山の領主の子息が村田珠光の依頼を受けて考案したと伝えられます。以来、高山は「茶筅の里」として五百年にわたり全国シェアのほとんどを担い、その技は一子相伝で守られてきました。",
    "一本の竹を小刀だけで百本余りの穂に割り、湯に浸けて一本ずつ内へ外へと曲げていく——機械化できない手仕事です。流派によって竹の種類も異なり、表千家は煤竹、裏千家は白竹、武者小路千家は紫竹を用います。"],
  parts_dots=[(80,12),(97,40),(80,58),(80,80)],
  parts=[("穂先(ほさき)","茶を攪拌する先端。内穂と外穂の二重構造"),
         ("かがり糸","外穂の根元を編む糸。黒糸が一般的"),
         ("節(ふし)","竹の節。穂と柄の境目"),
         ("柄(え)","持ち手。流派により竹の種類が異なる")],
  usage=[("茶筅通し","点前の中で湯にくぐらせ、穂先を検めながら清めます。"),
         ("点てる","手首のスナップで「m」の字を描くように細かく振り、最後は「の」の字で引き上げます。"),
         ("乾かす","使用後は湯ですすぎ、穂先を上に陰干し。くせ直しに掛けると形が長持ちします。")],
  checks=[("中古より新品を","口に触れる消耗品のため、実用には新品が原則。中古で流通するのは未使用保管品が中心です。"),
          ("穂の状態","穂折れ・開きすぎは点てにくさに直結。穂先が内側に緩く曲がっているものが良品です。"),
          ("産地表記","国産(高山茶筅)か海外産かで価格も耐久性も異なります。伝統的工芸品表記が目印。"),
          ("流派との適合","竹の色(煤竹・白竹・紫竹)が自分の流派に合うか確認しましょう。")]),

dict(slug="chashaku", name="茶杓", yomi="ちゃしゃく", romaji="Chashaku", en="Tea Scoop", num="03",
  cat="点前道具", tags=["点前道具","竹工芸","銘のある道具"],
  lede="抹茶をすくう細身の匙。小さな道具ながら銘を持ち、一席の主題を担う「一番の道具」です。",
  lede_en="A slender bamboo scoop for matcha, often carved and named by tea masters.",
  names=[("正式名称","茶杓(ちゃしゃく)"),("英語名","Chashaku / Tea Scoop"),
         ("銘(めい)","作者が付ける雅名。季語や禅語が多い"),
         ("付属","共筒(作者自筆の筒)・箱。評価を大きく左右する")],
  history=["もとは中国の象牙の匙(茶匙)に由来しますが、侘び茶の中で竹に置き換えられ、武野紹鴎・千利休の頃に現在の形が定まりました。利休が自ら削った茶杓は、切腹前に削った「泪(なみだ)」をはじめ、いまも茶人の心をとらえて離しません。",
    "茶杓は茶人自身が削る唯一の道具ともいわれ、節の位置で「元節」「中節」「節なし」に分かれます。銘と共筒が添うことで小さな竹片は一席の主題を語る道具となり、茶道具の中でも特別な敬意を払われます。"],
  parts_dots=[(133,17),(112,42),(60,68),(22,86)],
  parts=[("櫂先(かいさき)","茶をすくう先端。丸め方に個性が出る"),
         ("樋(ひ)","竹の内側の溝。景色の見どころ"),
         ("節(ふし)","中央付近の竹節。中節が最も一般的"),
         ("切止(きりどめ)","手元の切り口。削ぎ方に作者の癖が残る")],
  usage=[("清める","点前の初めに帛紗で「拭き清め」ます。物理的な掃除ではなく心を込める所作です。"),
         ("すくう","棗から約1杓半(薄茶一服分・約2g)をすくい、茶碗へ。"),
         ("拝見に出す","客の求めに応じ、銘とともに拝見に回します。素手で櫂先に触れないのが約束です。")],
  checks=[("銘と筒","共筒・共箱に銘や花押があるかが価値の中心。筒だけ・杓だけの「バラ」は評価が下がります。"),
          ("折れ・虫食い","櫂先の欠けと虫穴は要確認。漆で直したものもあります。"),
          ("樋と景色","樋の通り方・胡麻・染みなど竹の景色が見どころ。好みで選んで構いません。"),
          ("作者","家元・宗匠の作か、職人(削り師)の作かで市場価格は大きく異なります。")]),

dict(slug="natsume", name="棗", yomi="なつめ", romaji="Natsume", en="Tea Caddy", num="04",
  cat="点前道具", tags=["点前道具","漆芸","薄茶用"],
  lede="薄茶用の抹茶を納める漆塗りの容れ物。果実の棗に似たふくらみが名の由来です。",
  lede_en="A lacquered caddy for thin-tea matcha, named after the jujube fruit.",
  names=[("正式名称","棗(なつめ)※薄茶器の代表"),("英語名","Natsume / Tea Caddy"),
         ("大きさ","大棗・中棗・小棗"),
         ("装飾","真塗(黒無地)・溜塗・蒔絵・螺鈿 など")],
  history=["棗は室町時代後期、塗師の羽田五郎が考案したと伝えられる日本生まれの茶器です。濃茶用の陶製茶入(唐物)に対し、木地に漆を重ねた軽やかな棗は薄茶用として定着しました。",
    "利休が好んだ黒の真塗を基本に、時代が下るとともに蒔絵や螺鈿で四季を描いた華やかな意匠が生まれました。手の中に納まる小さな漆の器に、日本の工芸の粋が凝縮されています。"],
  parts_dots=[(80,14),(56,38),(80,60),(80,96)],
  parts=[("蓋・甲(こう)","蓋の天面。蒔絵の見せ場"),
         ("合口(あいくち)","蓋と身の合わせ目。精度が品質の証"),
         ("胴(どう)","ふくらみのある側面"),
         ("底(そこ)","作者の花押や銘が入ることも")],
  usage=[("持ち方","左手のひらに乗せ、右手で蓋を「こ」の字に清めます(帛紗さばき)。"),
         ("茶を入れる","抹茶は山なりに盛る「山盛り」に。使う直前に篩(ふるい)を通すとよく点ちます。"),
         ("扱いの注意","水洗い厳禁。柔らかい布で乾拭きし、桐箱で保管します。")],
  checks=[("漆の状態","ひび・剥げ・艶引けを確認。直射日光による退色は戻りません。"),
          ("合口の閉まり","蓋がすっと吸い付くように閉まるものが良品。緩み・がたつきは要注意。"),
          ("蒔絵の擦れ","金蒔絵は使用で擦れます。図柄の輪郭が残っているか写真で拡大確認を。"),
          ("共箱・作家","塗師の署名箱があるか。産地(輪島・山中など)の表記も価格の目安です。")]),

dict(slug="kama", name="茶釜", yomi="ちゃがま", romaji="Kama", en="Iron Kettle", num="05",
  cat="点前道具", tags=["点前道具","鋳物","炉・風炉"],
  lede="湯を沸かす鉄の釜。煮え音は「松風」と呼ばれ、静かな茶室に響く音の主役です。",
  lede_en="The iron kettle whose simmering voice, matsukaze, is the sound of the tea room.",
  names=[("正式名称","茶釜(ちゃがま)/ 釜"),("英語名","Kama / Iron Kettle"),
         ("主な産地","芦屋釜(筑前)・天明釜(下野)・京釜"),
         ("季節の別","冬=炉に掛ける大ぶりの釜 / 夏=風炉に掛ける小ぶりの釜")],
  history=["茶の湯釜は、南北朝〜室町期に筑前芦屋と下野天明という二大産地で発達しました。優美な文様の芦屋釜、荒々しい肌の天明釜はいまも名釜の代名詞です。",
    "桃山時代には京都三条釜座の釜師が台頭し、利休の釜師・辻与次郎が「利休好み」の侘びた釜を確立しました。釜は「一国一城の主」と呼ばれるほど茶道具の中で重んじられ、席の格を定める道具とされています。"],
  parts_dots=[(80,22),(80,36),(36,58),(80,70),(80,100)],
  parts=[("摘み(つまみ)・蓋","蓋は唐銅や鉄。摘みの意匠も見どころ"),
         ("口(くち)","湯を汲む口。姥口・広口など形が多彩"),
         ("鐶付(かんつき)","釜を上げ下げする鐶を掛ける耳"),
         ("胴・肌","鋳肌の景色。霰(あられ)などの文様"),
         ("底(そこ)","傷みやすく、後年「底の入れ替え」も行われる")],
  usage=[("湯相を整える","炭や電熱で「松風」の煮え音になるまで湯を育てます。"),
         ("汲む","柄杓で静かに汲み、注いだら釜に「置き柄杓」。蓋の開け閉めにも作法があります。"),
         ("乾かす","使用後は湯を捨て、余熱で完全に乾燥。濡れたままの放置が最大の敵です。")],
  checks=[("漏れの確認","水を張って一晩置き、滲みがないか。小さな漏れは「金気止め」で直ることもあります。"),
          ("錆の程度","表面の薄錆は育てられますが、内側の深い腐食は要注意。湯垢が育った釜はむしろ良品です。"),
          ("底の状態","古釜は底の入れ替え(共底・替底)が普通。釜師による直しなら価値を損ないません。"),
          ("蓋・鐶の有無","共蓋か替蓋か、鐶・釜敷が付属するかで実用性が変わります。")]),

dict(slug="hishaku", name="柄杓", yomi="ひしゃく", romaji="Hishaku", en="Water Ladle", num="06",
  cat="点前道具", tags=["点前道具","竹工芸","炉・風炉"],
  lede="湯や水を汲む竹の杓。釜から茶碗へ、一筋に注ぐ所作は点前の見せ場のひとつです。",
  lede_en="A bamboo ladle for drawing water — its single quiet pour is a highlight of temae.",
  names=[("正式名称","柄杓(ひしゃく)"),("英語名","Hishaku / Water Ladle"),
         ("季節の別","炉用=合が大きく柄の切止が身の側 / 風炉用=合が小さく切止が皮の側"),
         ("類品","蹲踞(つくばい)用の露地柄杓は別物")],
  history=["水を汲む杓そのものは神事に古くからありますが、茶の湯では点前の中心的な道具として洗練されました。侘び茶の成立とともに竹製が定着し、炉と風炉で寸法を替える現在の形式が整えられました。",
    "新品の白竹を使うのが基本で、青々とした清らかさそのものが客へのもてなしとされます。使い込むほどに飴色へ変わる合の色も、竹の道具ならではの味わいです。"],
  parts_dots=[(46,64),(62,72),(100,53),(138,34)],
  parts=[("合(ごう)","湯水を汲むカップ部分"),
         ("月形(つきがた)","合と柄の接合部の切り込み"),
         ("柄(え)","長い持ち手。節の位置が決まっている"),
         ("切止(きりどめ)","柄の末端。炉用と風炉用で削ぎの向きが逆")],
  usage=[("構える","「鏡柄杓」と呼ばれる構えで自身の心を映すように持ちます。"),
         ("汲む・注ぐ","釜の湯は汲み切り、注ぐときは一筋に。残りは釜に戻さないのが約束です。"),
         ("引き柄杓","風炉の点前では、注ぎ終えた柄杓を指を伸ばして静かに引く所作が美しいとされます。")],
  checks=[("実用は新品が基本","茶席では清潔さが第一。中古品は稽古用・飾り用と割り切りましょう。"),
          ("割れ・狂い","合の竹の割れ、柄の反りを確認。乾燥した保管環境だと割れやすくなります。"),
          ("炉用か風炉用か","切止の削ぎと合の大きさで見分けます。自分の稽古の季節に合わせて。"),
          ("差し通しか","合と柄が一本竹の「差し通し」は上位品。継ぎの精度も見どころです。")]),

dict(slug="fukusa", name="帛紗", yomi="ふくさ", romaji="Fukusa", en="Silk Cloth", num="07",
  cat="点前道具", tags=["点前道具","裂・織物","身に着ける道具"],
  lede="道具を清めるための絹の布。帛紗さばきは、道具とともに心を整える所作です。",
  lede_en="A silk cloth for purifying the utensils — folding it settles the mind as well.",
  names=[("正式名称","帛紗・袱紗(ふくさ)"),("英語名","Fukusa / Silk Cloth"),
         ("寸法","約27×28cm(流派で異同あり)。生地は塩瀬が基本"),
         ("色の習わし","男性=紫 / 女性=朱・赤(流派による)。出し帛紗・古帛紗は別種")],
  history=["帛紗の原型は、利休の妻・宗恩が道具を清めるために工夫したと伝えられます。以来、亭主が腰に着ける帛紗は「点前をする人」のしるしとなりました。",
    "無地の塩瀬のほか、名物裂を写した出し帛紗・古帛紗は濃茶の際に茶碗に添えて用いられます。小さな布一枚にも、裂地の歴史と格式が織り込まれています。"],
  parts_dots=[(42,26),(118,26),(72,56),(110,88)],
  parts=[("わさ(輪)","折りたたんだ際の折り目側。扱いの基準になる辺"),
         ("耳(みみ)","縫い留めのない裁ち端"),
         ("角(かど)","さばきで指を掛ける位置"),
         ("地(じ)","塩瀬の生地。厚みで扱いやすさが変わる")],
  usage=[("腰につける","帯・ベルトの左腰に挟みます。これが亭主のしるしです。"),
         ("さばく","「四方さばき」で塵を払い、折りたたんで棗・茶杓を清めます。"),
         ("扱いの注意","絹は水気厳禁。汚れたら買い替えが基本の消耗品です。")],
  checks=[("基本は新品で","直接口に入らないものの、清めの道具は新品が望ましいとされます。"),
          ("中古で探すなら","出し帛紗・古帛紗の名物裂は中古市場が豊富。裂の名称と時代を確認しましょう。"),
          ("生地の張り","塩瀬の張りが失われたものはさばきにくく稽古に不向きです。"),
          ("流派の色","自分の流派・性別の習わしに合う色かを確認してください。")]),

dict(slug="mizusashi", name="水指", yomi="みずさし", romaji="Mizusashi", en="Water Jar", num="08",
  cat="点前道具", tags=["点前道具","陶磁器ほか","据えの道具"],
  lede="釜に足す水、茶碗をすすぐ水を蓄える器。点前座の景色の要となる、どっしりとした存在です。",
  lede_en="A jar of fresh water that anchors the composition of the tea-making place.",
  names=[("正式名称","水指(みずさし)"),("英語名","Mizusashi / Fresh Water Jar"),
         ("素材","陶磁器・木地曲(きじまげ)・硝子・金属"),
         ("蓋の別","共蓋(同素材)/ 塗蓋(漆の替蓋)")],
  history=["水指はもと台所道具の転用から始まり、侘び茶の中で正式な道具に昇格しました。信楽や備前の種壺・芋頭など、日用の壺を「見立て」で取り上げた例は侘び茶の精神をよく伝えます。",
    "唐物の青磁や染付から、和物の志野・織部、木地の曲物まで素材は多彩で、夏には水を張った硝子の涼やかさも好まれます。季節と席の格に応じて最も選択肢の広い道具のひとつです。"],
  parts_dots=[(80,28),(52,38),(80,64),(80,102)],
  parts=[("蓋(ふた)","共蓋と塗蓋がある。扱いの所作も異なる"),
         ("口(くち)","広口・小口など。柄杓の出し入れに関わる"),
         ("胴(どう)","釉景色の見せ場"),
         ("底(そこ)","畳に据える安定感が大切")],
  usage=[("据える","点前座に運び、席中の「据えの景色」を作ります。"),
         ("水を差す","点前の終盤、釜に水を一杓差して湯相を整えます。"),
         ("蓋の扱い","塗蓋は水滴を残さず、共蓋は欠けに注意して静かに開閉します。")],
  checks=[("蓋の欠け・直し","もっとも傷みやすいのは蓋。共蓋の欠けや塗蓋の塗直しを確認します。"),
          ("ニュウと水漏れ","水を張る道具なのでひびは実用上の問題に。水張り確認済みかを尋ねましょう。"),
          ("替蓋の有無","共蓋を失い塗蓋を誂えた品も多く、それ自体は珍しくありません。"),
          ("箱と伝来","共箱・書付・伝来があれば飾り映えも価値も上がります。")]),
]

MINOR = [
 dict(slug="chaire", name="茶入", yomi="ちゃいれ / Chaire", en="Thick-tea Caddy",
      desc="濃茶用の抹茶を入れる陶製の小壺。象牙の蓋と仕覆(しふく)と呼ばれる袋に納められ、棗より格上の道具とされます。"),
 dict(slug="kensui", name="建水", yomi="けんすい / Kensui", en="Waste-water Bowl",
      desc="茶碗をすすいだ湯水を受ける器。「こぼし」とも呼ばれ、点前中は客から見えない位置で控えめに働きます。"),
 dict(slug="futaoki", name="蓋置", yomi="ふたおき / Futaoki", en="Lid Rest",
      desc="釜の蓋や柄杓を置くための小さな道具。竹の引切りが基本で、青磁や染付など趣向の凝った品も使われます。"),
 dict(slug="kogo", name="香合", yomi="こうごう / Kōgō", en="Incense Container",
      desc="炭点前で焚く香を納める小さな蓋物。炉の季節は練香に陶器、風炉の季節は白檀に漆器を用います。"),
 dict(slug="hanaire", name="花入", yomi="はないれ / Hanaire", en="Flower Vessel",
      desc="茶席の花を入れる器。竹・青磁・伊賀など。「花は野にあるように」と利休が説いた、席の生命感を担う道具です。"),
 dict(slug="kakemono", name="掛物", yomi="かけもの / Kakemono", en="Hanging Scroll",
      desc="床の間に掛ける書画。禅語の一行物が最も格が高く、「掛物ほど第一の道具はなし」と利休は言い切りました。"),
 dict(slug="furo", name="風炉", yomi="ふろ / Furo", en="Brazier",
      desc="五月から十月に釜を掛ける持ち運び式の炉。唐銅・土・鉄などがあり、灰形(はいがた)づくりも亭主の腕の見せどころ。"),
 dict(slug="kashiki", name="菓子器", yomi="かしき / Kashiki", en="Sweets Vessel",
      desc="茶菓子を盛る器。主菓子には縁高や食籠、干菓子には盆や振出を。菓子は茶の一部といわれる大切な脇役です。"),
]

# ---------------------------------------------------------------- shell ----
def shell(title, desc, body, root="", current="", extra_head=""):
    def nav(href, label, key):
        cls = ' class="current"' if current == key else ''
        return f'<a href="{root}{href}"{cls}>{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="{root}css/style.css">
{extra_head}
</head>
<body>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{root}index.html">
      <span class="brand-mark">悠三堂古美術ギャラリー</span>
      <span class="brand-sub">YUSANDO ANTIQUE GALLERY</span>
    </a>
    <button class="nav-toggle" aria-label="メニュー" onclick="document.querySelector('.nav-links').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links">
      {nav("index.html","トップ","home")}
      {nav("tools.html","道具一覧","tools")}
      {nav("setup.html","炉と風炉のしつらえ","setup")}
      {nav("guide.html","使い方・点前","guide")}
      {nav("articles/index.html","読みもの","articles")}
      {nav("index.html#about","このサイトについて","about")}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="f-inner">
    <div>
      <p class="f-mark">悠三堂古美術ギャラリー <span class="en-sub">YUSANDO ANTIQUE GALLERY</span></p>
      <p class="f-note">中古茶道具のためのポータルサイト。<br>道具の知識と、次の使い手への橋渡しを。<br>Used tea utensils — knowledge first, commerce to follow.</p>
    </div>
    <nav class="f-nav">
      <a href="{root}index.html">トップ TOP</a>
      <a href="{root}tools.html">道具一覧 UTENSILS</a>
      <a href="{root}setup.html">炉と風炉のしつらえ SETUP</a>
      <a href="{root}guide.html">使い方・点前 GUIDE</a>
      <a href="{root}articles/index.html">読みもの ARTICLES</a>
    </nav>
  </div>
  <p class="f-copy">© 2026 YUSANDO ANTIQUE GALLERY — このサイトはデモ・下書きです。オンラインショップ(EC)連携は準備中。</p>
</footer>
<script src="{root}js/site.js"></script>
</body>
</html>'''

# ---------------------------------------------------------------- pages ----
def card(t, root=""):
    return f'''<a class="tool-card reveal" href="{root}tools/{t["slug"]}.html">
  <span class="tool-num">{t["num"]}</span>
  <div class="tool-art">{ART[t["slug"]]}</div>
  <h3 class="tool-name">{t["name"]}</h3>
  <p class="tool-yomi">{t["yomi"]} / {t["romaji"]} — {t["en"]}</p>
  <p class="tool-desc">{t["lede"]}</p>
  <p class="tool-more">くわしく見る →</p>
</a>'''

def minor_card(m):
    return f'''<div class="tool-card plain reveal">
  <div class="tool-art">{ART[m["slug"]]}</div>
  <h3 class="tool-name">{m["name"]}</h3>
  <p class="tool-yomi">{m["yomi"]} — {m["en"]}</p>
  <p class="tool-desc">{m["desc"]}</p>
</div>'''

# ---- index ----
index_body = f'''
<section class="hero">
  <svg class="hero-enso" viewBox="0 0 200 200" aria-hidden="true">
    <path d="M100 18 a82 82 0 1 0 60 26" fill="none" stroke="#2b2a26" stroke-width="10" stroke-linecap="round"/>
  </svg>
  <div class="hero-inner">
    <p class="hero-kicker">中古茶道具ポータル — USED TEA UTENSILS PORTAL</p>
    <h1 class="hero-title">茶道具をもっと楽しく<br>身近に感じて</h1>
    <p class="hero-sub">わかりにくいお茶の道具を、わかりやすく。<br>手に取りやすく、買いやすくしました。<br><span class="en-sub">Tea utensils made easy — to understand, to hold, and to buy.</span></p>
    <div class="hero-cta">
      <a class="btn solid" href="tools.html">道具一覧を見る</a>
      <a class="btn" href="guide.html">使い方・点前を知る</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="intro-grid">
    <div class="reveal">
      <p class="intro-tate">一服の楽しみは、<br>ひとつの道具から。<small>― 悠三堂古美術ギャラリー</small></p>
    </div>
    <div class="intro-text reveal">
      <p class="section-kicker" style="text-align:left;text-indent:0">このサイトについて — ABOUT</p>
      <p>「茶道具って、なんだか難しそう」。読めない名前、見当のつかない値段、こまかい作法——最初の一歩を踏み出しにくい世界だと感じていませんか。</p>
      <p>悠三堂古美術ギャラリーは、そんな茶道具を<strong>わかりやすく、手に取りやすく、買いやすく</strong>お届けするためのサイトです。道具ごとに名前の読み方から歴史、部位、使い方、中古で選ぶときの見どころまで、はじめての方にもわかる言葉で整理しました。</p>
      <p>むずかしいことは、あとからで大丈夫。まずは気になる道具をひとつ見つけて、暮らしのそばに置いてみる——そこから茶道具はぐっと楽しく、身近になります。オンラインショップとの連携も準備中です。<br><span class="en-sub">Tea utensils, made friendly — easy to understand, to hold, and to buy.</span></p>
    </div>
  </div>
</section>

<section class="section" style="background:transparent;padding-top:0">
  <div class="section-head reveal">
    <p class="section-kicker">道具紹介 — THE UTENSILS</p>
    <h2 class="section-title">まずは、八つの道具から</h2>
    <div class="rule"></div>
    <p class="section-lede">点前に欠かせない代表的な道具。それぞれの詳細ページで、歴史・部位・使い方・中古選びのポイントを紹介しています。</p>
  </div>
  <div class="tools-grid">
    {"".join(card(t) for t in TOOLS[:4])}
  </div>
  <div style="text-align:center;margin-top:44px">
    <a class="btn" href="tools.html">すべての道具を見る — VIEW ALL</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:44px">
    <p class="section-kicker">読みもの — ARTICLES</p>
    <h2 class="section-title">もっと知りたくなったら</h2>
    <div class="rule"></div>
  </div>
  <div class="article-cards">
    <a class="article-card reveal" href="articles/chawan-types.html">
      <p class="a-kicker">GUIDE</p><h3>茶碗の種類</h3>
      <p>楽・萩・唐津から天目・井戸まで。焼き物の系譜と形の種類を、選び方の目線で整理しました。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="articles/history.html">
      <p class="a-kicker">HISTORY</p><h3>茶道の歴史</h3>
      <p>唐から渡った一杯の茶が、道具とともに「道」になるまで。千年の流れを年表でたどります。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="articles/chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>茶筅の種類</h3>
      <p>穂数・竹の色・形。流派と用途で変わる茶筅の選び方を、はじめての方向けに解説します。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="articles/sekki.html">
      <p class="a-kicker">SEASON</p><h3>二十四節気と茶道具</h3>
      <p>立春から大寒まで。節気ごとのしつらえと道具合わせを、一年のカレンダーにしました。</p>
      <p class="tool-more">読む →</p>
    </a>
  </div>
</section>

<section class="care">
  <div class="section tight">
    <div class="section-head reveal" style="margin-bottom:44px">
      <p class="section-kicker">お手入れ — CARE</p>
      <h2 class="section-title">道具と長く付き合う</h2>
    </div>
    <div class="care-grid reveal">
      <div class="care-cell"><h3>茶碗 <span class="en-sub">CHAWAN</span></h3><p>洗剤は使わず、ぬるま湯で洗って布で拭き、よく乾かしてから箱へ。使い始めの陶器は一晩水に浸けて目を締めます。</p></div>
      <div class="care-cell"><h3>茶筅 <span class="en-sub">CHASEN</span></h3><p>使用後は湯ですすぎ、穂先を上にして陰干しに。くせ直しに掛けると形が長持ちします。</p></div>
      <div class="care-cell"><h3>漆器・棗 <span class="en-sub">NATSUME</span></h3><p>水洗いは避け、柔らかい乾いた布で拭くだけに。直射日光と乾燥が大敵、桐箱で保管を。</p></div>
      <div class="care-cell"><h3>鉄器・釜 <span class="en-sub">KAMA</span></h3><p>使用後は湯を捨て、余熱でしっかり乾燥。湯垢が育つと錆に強くなるため、洗剤や研磨は禁物です。</p></div>
    </div>
  </div>
</section>

<section class="section reveal" style="text-align:center">
  <p class="section-kicker">オンラインショップ — SHOP</p>
  <h2 class="section-title">EC連携は、準備中です</h2>
  <div class="rule"></div>
  <p class="section-lede">このサイトは将来、オンラインショップと連携し、道具ページから直接「いま買える中古在庫」を見られるようにする設計になっています。各道具ページの在庫枠は、その受け皿です。</p>
  <div style="margin-top:30px"><span class="btn" style="opacity:.5;cursor:default">オンラインショップ(準備中)</span></div>
</section>
'''

# ---- tools list ----
tools_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">道具一覧 — LIST OF UTENSILS</p>
    <h2 class="section-title">日本の茶道具一覧</h2>
    <div class="rule"></div>
    <p class="section-lede">茶の湯で用いられる主な道具の一覧です。詳細ページのある道具は、歴史・部位・使い方・中古選びのポイントまで掘り下げています。</p>
  </div>

  <div class="cat-head reveal"><h2>点前道具</h2><span class="en-sub">UTENSILS OF THE PROCEDURE — 詳細ページあり</span></div>
  <div class="tools-grid">
    {"".join(card(t) for t in TOOLS)}
  </div>

  <div class="cat-head reveal"><h2>そのほかの道具</h2><span class="en-sub">FURTHER UTENSILS — 概説</span></div>
  <div class="tools-grid">
    {"".join(minor_card(m) for m in MINOR)}
  </div>
</section>
'''

# ---- guide ----
guide_steps = [
 ("一","清める — Purify","帛紗で<a href='tools/natsume.html'>棗</a>と<a href='tools/chashaku.html'>茶杓</a>を拭き清め、湯で<a href='tools/chasen.html'>茶筅</a>と<a href='tools/chawan.html'>茶碗</a>をあらためます。"),
 ("二","茶を入れる — Measure","茶杓で棗から抹茶をすくい、茶碗へ。およそ一杓半(約2g)が薄茶一服の目安です。"),
 ("三","湯を注ぐ — Pour","<a href='tools/hishaku.html'>柄杓</a>で<a href='tools/kama.html'>釜</a>の湯を汲み、茶碗に静かに注ぎます。"),
 ("四","点てる — Whisk","茶筅を細かく振り、きめの整った一碗に点て上げます。"),
 ("五","差し出す — Offer","茶碗の正面を客に向けて差し出し、一服が始まります。"),
]
guide_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">使い方・点前 — HOW THE UTENSILS WORK</p>
    <h2 class="section-title">一碗ができるまで</h2>
    <div class="rule"></div>
    <p class="section-lede">道具は順に手に取られ、それぞれの役目を果たして戻っていきます。薄茶点前のおおまかな流れと、そこで働く道具たちです。<br><span class="en-sub">A simplified outline of the thin-tea procedure.</span></p>
  </div>
  <div class="temae-list reveal">
    {"".join(f'<div class="temae-item"><span class="temae-step">{a}</span><div class="temae-body"><h3>{b}</h3><p>{c}</p></div></div>' for a,b,c in guide_steps)}
  </div>
</section>

<section class="section tight" style="padding-top:0">
  <div class="section-head reveal" style="margin-bottom:40px">
    <p class="section-kicker">はじめてのひと揃え — A FIRST SET</p>
    <h2 class="section-title">最低限そろえたい道具</h2>
    <div class="rule"></div>
  </div>
  <div class="check-grid reveal" style="max-width:820px;margin-left:auto;margin-right:auto">
    <div class="check-cell"><h3>自宅で一服なら</h3><p>茶碗・茶筅・茶杓の三点があれば、抹茶は点てられます。湯はやかんで、棗は茶缶で代用できます。</p></div>
    <div class="check-cell"><h3>稽古を始めるなら</h3><p>帛紗・扇子・懐紙・菓子切の「四点セット」を。流派によって帛紗の色や寸法が異なるため、先生に確認を。</p></div>
    <div class="check-cell"><h3>中古を活かすなら</h3><p>茶碗・棗・水指・建水は中古市場が豊富で狙い目。口に触れる茶筅と、清めに使う帛紗は新品がおすすめです。</p></div>
    <div class="check-cell"><h3>そろえる順番</h3><p>点前の道具は一度に揃えず、稽古の進みに合わせて。銘のある茶杓や釜は、目が育ってからが失敗しません。</p></div>
  </div>
</section>

<section class="section reveal" style="text-align:center;padding-top:30px">
  <p class="words-quote" style="font-size:clamp(20px,3vw,27px);letter-spacing:.2em;line-height:2.2">名物を持たざる者は<br>茶の湯すまじきこと</p>
  <p class="en-sub" style="margin-top:16px">— THE IDEA RIKYŪ REFUSED</p>
  <p class="section-lede" style="margin-top:22px">千利休は、高価な名物がなくとも心を尽くせば茶の湯は成り立つと説きました。手元のひと揃えを大切に使い込むこと——中古の道具と付き合うことは、その精神の実践でもあります。</p>
</section>
'''

# ---- setup page (炉と風炉) ----
FURO_DIAG = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">点前畳(略式・本勝手)</text>
<rect x="76" y="30" width="40" height="40" fill="none" stroke="#a53f2b" stroke-width="1.6"/>
<circle cx="96" cy="50" r="14" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="96" y="83" text-anchor="middle" class="dg-label strong">風炉+釜</text>
<text x="96" y="94" text-anchor="middle" class="dg-label">(敷板の上)</text>
<circle cx="152" cy="48" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="152" y="76" text-anchor="middle" class="dg-label strong">水指</text>
<circle cx="120" cy="136" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="120" y="162" text-anchor="middle" class="dg-label strong">亭主</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="208" y="95" text-anchor="middle" class="dg-label" writing-mode="tb">客 座</text>
<text x="30" y="95" text-anchor="middle" class="dg-label" writing-mode="tb">勝手(水屋)側</text>
</svg>'''
RO_DIAG = '''<svg viewBox="0 0 240 175" aria-hidden="true">
<rect x="60" y="14" width="120" height="140" fill="#efe8d8" stroke="#8a8c78" stroke-width="1.6"/>
<text x="120" y="10" text-anchor="middle" class="dg-label">点前畳(略式・四畳半切)</text>
<rect x="146" y="96" width="40" height="40" fill="#e2d8c2" stroke="#a53f2b" stroke-width="2"/>
<circle cx="166" cy="116" r="13" fill="none" stroke="#a53f2b" stroke-width="2"/>
<text x="166" y="150" text-anchor="middle" class="dg-label strong">炉+釜</text>
<circle cx="120" cy="46" r="12" fill="none" stroke="#4a5d3a" stroke-width="2"/>
<text x="120" y="74" text-anchor="middle" class="dg-label strong">水指</text>
<circle cx="104" cy="120" r="9" fill="none" stroke="#2b2a26" stroke-width="1.6"/>
<text x="96" y="146" text-anchor="middle" class="dg-label strong">亭主</text>
<path d="M196 60 v60" stroke="#8a8c78" stroke-width="1" stroke-dasharray="3 3"/>
<text x="208" y="95" text-anchor="middle" class="dg-label" writing-mode="tb">客 座</text>
<text x="30" y="95" text-anchor="middle" class="dg-label" writing-mode="tb">勝手(水屋)側</text>
</svg>'''

def ck(name, note, link=None):
    label = f'<a href="tools/{link}.html">{name}</a>' if link else name
    return (f'<label class="ck"><input type="checkbox">'
            f'<span class="ck-name">{label}</span>'
            f'<span class="ck-note">{note}</span></label>')

setup_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">季節のしつらえ — SEASONAL SETUP</p>
    <h2 class="section-title">炉と風炉、ふたつの季節</h2>
    <div class="rule"></div>
    <p class="section-lede">茶の湯の一年は、火の置き方でふたつに分かれます。畳を切って火を客に近づける冬の「炉」、火を客から遠ざけて涼を演出する夏の「風炉」。しつらえも道具も、この二季で入れ替わります。<br><span class="en-sub">The tea year has two seasons: the sunken hearth (ro) of winter and the brazier (furo) of summer.</span></p>
  </div>

  <div class="reveal">
    <div class="season-band">
      <div class="ro">炉 11月</div><div class="ro">12月</div><div class="ro">1月</div><div class="ro">2月</div><div class="ro">3月</div><div class="ro">4月</div>
      <div class="fu">風炉 5月</div><div class="fu">6月</div><div class="fu">7月</div><div class="fu">8月</div><div class="fu">9月</div><div class="fu">10月</div>
    </div>
    <p class="cmp-note">11月の「炉開き」は茶人の正月とも呼ばれ、5月の「初風炉」で夏のしつらえに替わります。</p>
  </div>

  <div class="layout-grid reveal">
    <div class="layout-card">
      <h3>風炉のしつらえ<span class="en-sub">FURO — MAY TO OCTOBER</span></h3>
      {FURO_DIAG}
      <p class="cap">火を客から遠ざけ、涼しさを演出する夏の構え。風炉は敷板の上に据え、釜は小ぶりのものを掛けます。灰形(はいがた)を整えるのも亭主の仕事です。</p>
    </div>
    <div class="layout-card">
      <h3>炉のしつらえ<span class="en-sub">RO — NOVEMBER TO APRIL</span></h3>
      {RO_DIAG}
      <p class="cap">畳を切った炉壇に五徳を据え、火を客に近づけて暖を分かち合う冬の構え。釜は大ぶりになり、湯の煮え音も豊かに響きます。</p>
    </div>
  </div>
  <p class="cmp-note reveal">※配置は本勝手・運び点前の略式図です。炉の切り方(四畳半切・台目切など)や流派によって位置・向きは変わります。</p>

  <div class="reveal">
    <table class="cmp-table">
      <thead><tr><th style="width:8em;background:var(--paper-deep);color:var(--matcha)"></th><th>炉(ろ)</th><th class="furo-col">風炉(ふろ)</th></tr></thead>
      <tbody>
        <tr><th>季節</th><td>11月〜4月(炉開きは11月)</td><td>5月〜10月(初風炉は5月)</td></tr>
        <tr><th>火の位置</th><td>畳に切った炉壇。客に近く、暖かさを分かち合う</td><td>点前畳の勝手付寄り。客から遠ざけて涼を演出</td></tr>
        <tr><th><a href="tools/kama.html" style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)">釜</a></th><td>大ぶりの釜。五徳に据える(釣釜・透木釜の変化も)</td><td>小ぶりの釜。風炉に掛け、敷板の上に据える</td></tr>
        <tr><th><a href="tools/hishaku.html" style="border-bottom:1px solid rgba(74,93,58,.3);color:var(--matcha)">柄杓</a></th><td>合が大きい。切止は身(内)側を削ぐ</td><td>合が小さい。切止は皮(外)側を削ぐ</td></tr>
        <tr><th>蓋置(竹)</th><td>節が中ほどの「中節」を用いるのが一般的</td><td>節が上端の「天節」を用いるのが一般的</td></tr>
        <tr><th>炭・香</th><td>炭は大きめ。香は練香、香合は陶器</td><td>炭は小さめ。香は白檀など、香合は漆器</td></tr>
        <tr><th>心もち</th><td>火を囲む暖かさ。侘びた深まりの季節</td><td>涼一味。水を主役にした爽やかさの季節</td></tr>
      </tbody>
    </table>
    <p class="cmp-note">※蓋置の節の位置などは流派により習わしが異なります。お稽古の先生の教えを優先してください。</p>
  </div>
</section>

<section class="section tight" style="padding-top:20px">
  <div class="section-head reveal" style="margin-bottom:34px">
    <p class="section-kicker">持ち物チェックリスト — CHECKLIST</p>
    <h2 class="section-title">実際の点前で必要な道具</h2>
    <div class="rule"></div>
    <p class="section-lede">薄茶の運び点前(棚を使わない基本の点前)を想定した道具一覧です。チェックを付けて、水屋の準備にお使いください。</p>
  </div>

  <div style="max-width:920px;margin:0 auto">
    <div class="ck-group reveal">
      <h3>一、据えておく道具 <span class="en-sub">SET IN PLACE BEFOREHAND</span></h3>
      <div class="ck-cols">
        {ck("茶釜","湯を沸かしておく。松風の煮え音が合図","kama")}
        {ck("炉 または 風炉","季節のしつらえに合わせて(上の表を参照)")}
        {ck("水指","水を八分目ほど張って点前座へ","mizusashi")}
        {ck("炭・灰(または電熱)","炉=大きめの炭と練香/風炉=小さめの炭と灰形")}
      </div>
    </div>

    <div class="ck-group reveal">
      <h3>二、茶碗に仕組んで運ぶ道具 <span class="en-sub">CARRIED IN THE BOWL</span></h3>
      <div class="ck-cols">
        {ck("茶碗","季節に合うものを。夏=平茶碗/冬=筒茶碗","chawan")}
        {ck("茶筅","穂先を検めておく。薄茶は穂数の多いもの","chasen")}
        {ck("茶杓","茶碗に伏せて乗せる","chashaku")}
        {ck("茶巾","麻の布。たたみ方にも作法がある")}
      </div>
    </div>

    <div class="ck-group reveal">
      <h3>三、そのほか運び出す道具 <span class="en-sub">ALSO CARRIED OUT</span></h3>
      <div class="ck-cols">
        {ck("棗","抹茶を篩(ふるい)にかけて山盛りに","natsume")}
        {ck("建水","柄杓と蓋置を仕組んで、最後に運び出す")}
        {ck("柄杓","炉用・風炉用を間違えずに","hishaku")}
        {ck("蓋置","炉=中節/風炉=天節(竹の場合)")}
      </div>
    </div>

    <div class="ck-group reveal">
      <h3>四、身に着けるもの <span class="en-sub">WORN BY THE HOST</span></h3>
      <div class="ck-cols">
        {ck("帛紗","腰に着ける亭主のしるし。流派の色で","fukusa")}
        {ck("扇子","挨拶のときに膝前へ")}
        {ck("懐紙・菓子切","客としても必携の一組")}
        {ck("古帛紗","裏千家など。道具拝見・濃茶で用いる")}
      </div>
    </div>

    <div class="ck-group reveal">
      <h3>五、客をもてなす道具 <span class="en-sub">FOR THE GUESTS</span></h3>
      <div class="ck-cols">
        {ck("菓子器と菓子","薄茶=干菓子を盆に/濃茶=主菓子を縁高などに")}
        {ck("煙草盆・座布団など","広間の茶席なら。席の格に合わせて")}
      </div>
    </div>

    <div class="reveal" style="margin-top:44px;border:1px solid var(--line);background:var(--paper-deep);border-radius:4px;padding:28px 26px">
      <h3 style="font-size:16px;letter-spacing:.14em;font-weight:500">濃茶点前では、ここが変わります <span class="en-sub">FOR THICK TEA</span></h3>
      <p style="font-size:13.5px;color:var(--ink-soft);margin-top:12px">棗に代えて<strong>茶入</strong>(仕覆に入れる)を用い、茶碗には格の高い一碗を選びます。客に茶碗を出す際は<strong>古帛紗・出し帛紗</strong>を添え、菓子は主菓子を先に。茶は一碗を数人で回し飲む「吸い茶」となります。</p>
    </div>
  </div>
</section>
'''

# ---- detail pages ----
def detail(t, i):
    prev_t = TOOLS[(i-1) % len(TOOLS)]
    next_t = TOOLS[(i+1) % len(TOOLS)]
    names_rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in t["names"])
    parts_items = "".join(
        f'<li><span class="p-num">{n}</span><div><span class="p-name">{p}</span><br><span class="p-note">{d}</span></div></li>'
        for n, (p, d) in enumerate(t["parts"], 1))
    steps = "".join(
        f'<div class="step"><span class="step-no">{"一二三四五"[n]}</span><div class="step-body"><h3>{h}</h3><p>{p}</p></div></div>'
        for n, (h, p) in enumerate(t["usage"]))
    checks = "".join(
        f'<div class="check-cell"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["checks"])
    hist = "".join(f"<p>{p}</p>" for p in t["history"])
    tags = "".join(f'<span class="tag">{x}</span>' for x in t["tags"])
    body = f'''
<div class="detail-hero">
  <div class="detail-hero-inner">
    <div>
      <p class="crumbs"><a href="../index.html">トップ</a> / <a href="../tools.html">道具一覧</a> / {t["name"]}</p>
      <h1 class="detail-title">{t["name"]}</h1>
      <p class="detail-yomi">{t["yomi"]} / {t["romaji"]} — {t["en"]}</p>
      <p class="detail-lede">{t["lede"]}<br><span class="en-sub">{t["lede_en"]}</span></p>
      <div class="detail-tags">{tags}</div>
    </div>
    <div class="detail-art">{ART[t["slug"]]}</div>
  </div>
</div>

<div class="detail-body">
  <section class="d-sec reveal">
    <h2>名前と種類 <span class="en-sub">NAME &amp; TYPES</span></h2>
    <div class="d-rule"></div>
    <table class="name-table">{names_rows}</table>
  </section>

  <section class="d-sec reveal">
    <h2>歴史 <span class="en-sub">HISTORY</span></h2>
    <div class="d-rule"></div>
    {hist}
  </section>

  <section class="d-sec reveal">
    <h2>部位の名称 <span class="en-sub">PARTS</span></h2>
    <div class="d-rule"></div>
    <div class="parts-wrap">
      <div class="parts-fig">{parts_svg(t["slug"], t["parts_dots"])}</div>
      <ol class="parts-list">{parts_items}</ol>
    </div>
  </section>

  <section class="d-sec reveal">
    <h2>使い方 <span class="en-sub">HOW TO USE</span></h2>
    <div class="d-rule"></div>
    <div class="steps">{steps}</div>
  </section>

  <section class="d-sec reveal">
    <h2>中古で選ぶポイント <span class="en-sub">BUYING SECONDHAND</span></h2>
    <div class="d-rule"></div>
    <div class="check-grid">{checks}</div>
  </section>

  <section class="d-sec reveal">
    <h2>この道具の在庫 <span class="en-sub">AVAILABLE PIECES</span></h2>
    <div class="d-rule"></div>
    <div class="shop-stub" data-ec-category="{t["slug"]}">
      <div class="listing-slot" id="listings-{t["slug"]}"></div>
      <h3>オンラインショップ 準備中</h3>
      <p>EC連携後、この枠に「いま買える中古の{t["name"]}」が表示されます。<br>Listings will appear here once the online shop is connected.</p>
      <button class="btn" disabled>在庫を見る — COMING SOON</button>
    </div>
  </section>
</div>

<nav class="pn">
  <a href="{prev_t["slug"]}.html">← {prev_t["name"]}({prev_t["yomi"]})</a>
  <a href="../tools.html">一覧へ</a>
  <a href="{next_t["slug"]}.html">{next_t["name"]}({next_t["yomi"]})→</a>
</nav>
'''
    return shell(
        f'{t["name"]}({t["yomi"]})とは — 歴史・部位・使い方 | 悠三堂古美術ギャラリー',
        f'{t["name"]}({t["yomi"]} / {t["romaji"]})の歴史、部位の名称、使い方、中古で選ぶポイントを解説します。',
        body, root="../", current="tools")

# ---------------------------------------------------------------- write ----
os.makedirs(os.path.join(ROOT, "tools"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "js"), exist_ok=True)

def w(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

w("index.html", shell("悠三堂古美術ギャラリー — 中古茶道具ポータル | Yusando Antique Gallery",
  "中古茶道具のポータルサイト。茶碗・茶筅・茶杓など日本の茶道具の歴史・部位・使い方と、中古で選ぶポイントを紹介します。",
  index_body, root="", current="home"))

w("tools.html", shell("道具一覧 — 日本の茶道具 | 悠三堂古美術ギャラリー",
  "日本の茶道具一覧。点前道具から装飾の道具まで、名前・読み方・役割を一覧で紹介します。",
  tools_body, root="", current="tools"))

w("setup.html", shell("炉と風炉のしつらえ・点前で必要な道具 | 悠三堂古美術ギャラリー",
  "炉(11月〜4月)と風炉(5月〜10月)のしつらえの違いを配置図と比較表で解説。薄茶点前に必要な道具のチェックリスト付き。",
  setup_body, root="", current="setup"))

w("guide.html", shell("使い方・点前のながれ | 悠三堂古美術ギャラリー",
  "茶道具の使い方と薄茶点前のながれ。はじめてそろえる道具のガイドも。",
  guide_body, root="", current="guide"))

for i, t in enumerate(TOOLS):
    w(f'tools/{t["slug"]}.html', detail(t, i))

# ---- site.js (nav + reveal + EC-ready listings stub) ----
w("js/site.js", '''// 悠三堂古美術ギャラリー site script
// ---- scroll reveal ----
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('on'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  els.forEach(function (el) { io.observe(el); });
})();

// ---- EC integration point -------------------------------------------------
// 将来のオンラインショップ連携用フック。
// 各道具詳細ページの <div class="shop-stub" data-ec-category="chawan"> が受け皿です。
// Shopify Storefront API 等に接続する場合は、下の fetchListings を実装して
// CHADOGU_EC.enabled を true にするだけで、全ページに在庫が表示されます。
window.CHADOGU_EC = {
  enabled: false,            // ← EC連携を有効化するときに true
  endpoint: "",              // 例: Shopify Storefront API のエンドポイント
  fetchListings: async function (category) {
    // 実装例(Shopify):
    //   const res = await fetch(this.endpoint, {method:"POST", headers:{...},
    //     body: JSON.stringify({query: `{ products(query:"tag:${category}", first:6){...} }`})});
    //   return (await res.json()).data.products;
    return [];
  },
  renderCard: function (p) {
    return '<a class="tool-card" href="' + p.url + '">' +
      '<h3 class="tool-name">' + p.title + '</h3>' +
      '<p class="tool-yomi">' + (p.condition || '') + '</p>' +
      '<p class="tool-desc">' + (p.price || '') + '</p></a>';
  }
};
(function () {
  var stub = document.querySelector('.shop-stub[data-ec-category]');
  if (!stub || !window.CHADOGU_EC.enabled) return;
  var cat = stub.getAttribute('data-ec-category');
  window.CHADOGU_EC.fetchListings(cat).then(function (items) {
    if (!items || !items.length) return;
    var slot = stub.querySelector('.listing-slot');
    slot.innerHTML = '<div class="tools-grid" style="text-align:left">' +
      items.map(window.CHADOGU_EC.renderCard).join('') + '</div>';
    stub.querySelectorAll('h3, p, button').forEach(function (el) { el.style.display = 'none'; });
  });
})();
''')

print("done")

# ================================================================ articles ----
os.makedirs(os.path.join(ROOT, "articles"), exist_ok=True)

def article_shell(title, desc, kicker, h1, lede, body_secs):
    body = f'''
<div class="article-hero">
  <p class="crumbs"><a href="../index.html">トップ</a> / <a href="index.html">読みもの</a> / {h1}</p>
  <p class="section-kicker">{kicker}</p>
  <h1 class="article-title">{h1}</h1>
  <p class="article-lede">{lede}</p>
</div>
<div class="detail-body">
{body_secs}
</div>
<nav class="pn">
  <a href="index.html">← 読みもの一覧へ</a>
  <a href="../tools.html">道具一覧へ</a>
</nav>
'''
    return shell(f'{title} | 悠三堂古美術ギャラリー', desc, body, root="../", current="articles")

def sec(title, en, inner):
    return f'''<section class="d-sec reveal">
  <h2>{title} <span class="en-sub">{en}</span></h2>
  <div class="d-rule"></div>
  {inner}
</section>'''

def tcard(name, sub, desc, tip):
    return (f'<div class="type-card"><h3>{name}</h3><p class="t-sub">{sub}</p>'
            f'<p>{desc}</p><p class="t-tip">{tip}</p></div>')

# ---------------------------------------------------- 1) 茶碗の種類 ----
chawan_types_body = (
sec("三つの系譜","THREE LINEAGES", '''
  <p>茶碗は生まれた土地によって、大きく三つの系譜に分けられます。中国から渡来した<strong>唐物(からもの)</strong>、朝鮮半島から渡った<strong>高麗物(こうらいもの)</strong>、そして日本で焼かれた<strong>和物(わもの)</strong>。格式は唐物を頂点としつつ、侘び茶の広がりとともに高麗物・和物の飾らない美しさが愛されるようになりました。</p>
  <p>覚えておきたい言葉が「<strong>一楽二萩三唐津</strong>」。茶人が和物茶碗の好みを語った言い回しで、楽・萩・唐津が三大茶陶とされています。</p>''')
+
sec("主要な茶碗の種類","MAJOR TYPES", '<div class="type-grid">'
+ tcard("楽茶碗","RAKU — 京都","轆轤を使わず手捏ねで成形し、内窯で一碗ずつ焼く。利休の侘びに応えて長次郎が創始。黒楽・赤楽があり、軽く手になじみ、茶が点てやすい。","初めての一碗にも稽古用の写しが豊富。")
+ tcard("萩茶碗","HAGI — 山口","柔らかな土と枇杷色の釉。使うほど茶が染みて表情が変わる「萩の七化け」が身上。貫入(細かなひび)は景色のうち。","中古は貫入への茶染みの進み具合を確認。")
+ tcard("唐津茶碗","KARATSU — 佐賀","砂気のある土の力強さと素朴な絵付け。絵唐津・斑唐津・朝鮮唐津など種類が多彩で、飽きのこない実用の美。","日常の一服に使いやすい丈夫さが魅力。")
+ tcard("志野茶碗","SHINO — 美濃","長石釉の白にほんのり緋色が差す、日本初の白い焼き物。鼠志野・紅志野も。国宝「卯花墻」で知られる。","ぽってりした厚みで冬の一碗に向く。")
+ tcard("織部茶碗","ORIBE — 美濃","古田織部好みの、緑釉と大胆な歪み・文様。「ひょうげもの」と呼ばれた自由な造形が身上。","形の歪みは個性。手取りの収まりで選ぶ。")
+ tcard("天目茶碗","TENMOKU — 唐物","鉄釉の深い黒に星や油滴が浮かぶ唐物の最高峰。曜変天目は世界に三碗のみ、すべて日本にあり国宝。","写し(再現作)が多く流通。台付きは格別の扱い。")
+ tcard("井戸茶碗","IDO — 高麗物","朝鮮の日用雑器を茶人が見立てた大ぶりの碗。枇杷色の肌と高台の梅花皮(かいらぎ)が見どころ。国宝「喜左衛門井戸」が名高い。","梅花皮の縮れ具合が評価の的。")
+ tcard("京焼・色絵","KYOYAKI — 京都","仁清・乾山に始まる雅な色絵。四季の意匠を纏い、席に華を添える。現代作家の裾野も広い。","絵柄の季節を席の時期に合わせて。")
+ '</div>')
+
sec("形で選ぶ","BY SHAPE", '''
  <table class="name-table">
    <tr><th>平茶碗(ひら)</th><td>浅く口が開いた夏の碗。湯が早く冷め、見た目にも涼しい。</td></tr>
    <tr><th>筒茶碗(つつ)</th><td>深い円筒形の冬の碗。湯が冷めにくく、両手に温かい。</td></tr>
    <tr><th>碗形(わんなり)</th><td>最も標準的な形。季節を問わず使える基本の一碗。</td></tr>
    <tr><th>半筒(はんづつ)</th><td>碗形と筒の中間。春や秋の肌寒い時期に。</td></tr>
    <tr><th>天目形(てんもくなり)</th><td>すり鉢状に開く唐物由来の形。格の高い点前に用いる。</td></tr>
    <tr><th>沓形(くつがた)</th><td>楕円に歪ませた織部好みの形。動きのある景色が楽しい。</td></tr>
  </table>
  <p style="margin-top:18px">迷ったら、まず<strong>碗形をひとつ</strong>。季節の平茶碗・筒茶碗は二碗目以降で揃えると失敗がありません。<a href="../tools/chawan.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">茶碗の基本ページ</a>には部位の名称と中古選びのポイントをまとめています。</p>'''))

w("articles/chawan-types.html", article_shell(
  "茶碗の種類 — 楽・萩・唐津から天目まで",
  "茶碗の種類を系譜(唐物・高麗物・和物)、産地(楽・萩・唐津・志野・織部など)、形(平茶碗・筒茶碗など)から解説します。",
  "読みもの — GUIDE","茶碗の種類",
  "楽・萩・唐津、志野に織部、天目に井戸。名前は聞くけれど、何がどう違う? 系譜・産地・形の三つの軸で、すっきり整理します。",
  chawan_types_body))

# ---------------------------------------------------- 2) 茶道の歴史 ----
def tl(era, years, h, p):
    return (f'<div class="tl-item"><div class="tl-era">{era}<small>{years}</small></div>'
            f'<div class="tl-body"><h3>{h}</h3><p>{p}</p></div></div>')

history_body = (
sec("千年の流れ","A THOUSAND YEARS", '''
  <p>茶道の歴史は、一杯の薬湯から始まりました。中国から渡った茶が、禅とともに広まり、道具の美意識と出会い、「茶の湯」という総合芸術になるまで——大きな流れを年表でたどります。</p>
  <div class="tl">''' 
+ tl("奈良・平安","8〜12世紀","茶、日本へ渡る","遣唐使や最澄・空海ら留学僧が茶を持ち帰る。当時は固めた茶を削って煮る団茶で、貴族や僧侶の薬・儀礼の飲み物だった。嵯峨天皇に永忠が茶を献じた記録が残る。")
+ tl("鎌倉","12〜14世紀","栄西と抹茶の伝来","臨済宗の開祖・栄西が宋から抹茶法を伝え、『喫茶養生記』で茶の効能を説く。禅寺の儀礼として喫茶が定着し、やがて茶の産地を当てる「闘茶」が武士に流行する。")
+ tl("室町","14〜15世紀","書院の茶と唐物荘厳","足利将軍家が唐物(中国渡来の名物)を飾り立てる書院の茶を確立。一方で村田珠光が「藁屋に名馬をつなぎたるがよし」と、簡素な道具に美を見いだす侘び茶の精神を開く。")
+ tl("戦国・桃山","16世紀","利休、侘び茶を大成","武野紹鴎を経て千利休が登場。二畳の草庵、楽茶碗、竹の花入——引き算の美学で茶の湯を大成する。信長・秀吉の政治とも深く結びつき、茶道具は一国一城に値する宝となった。")
+ tl("江戸","17〜19世紀","家元制度と大名茶","利休の孫・宗旦の子らが表千家・裏千家・武者小路千家の三千家を立てる。小堀遠州や片桐石州ら大名茶人が「きれいさび」の茶を展開。家元制度が整い、町人にも茶が広がる。")
+ tl("明治・大正","19〜20世紀","近代数寄者の時代","文明開化で一時衰退するも、益田鈍翁ら財界人が名物道具を収集し茶の湯を支える。学校教育に取り入れられ、女性の教養として裾野が大きく広がった。")
+ tl("昭和〜現在","20世紀〜","世界へ開く茶の湯","岡倉天心『茶の本』が茶の心を世界へ伝える。美術館が名碗を公開し、稽古人口は海外にも。道具は美術品として、また暮らしの器として、新しい使い手と出会い続けている。")
+ '</div>')
+
sec("歴史を道具から見る","THROUGH THE UTENSILS", '''
  <p>茶道の歴史は、そのまま道具の歴史でもあります。唐物天目への憧れ、高麗茶碗の見立て、楽茶碗の創造、竹の茶杓や花入——時代ごとの美意識が、いまも中古市場に残る道具ひとつひとつに刻まれています。</p>
  <p>だからこそ、古い道具を手に取ることは、この千年の物語に触れること。<a href="../tools.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">道具一覧</a>から、気になる一点を探してみてください。</p>'''))

w("articles/history.html", article_shell(
  "茶道の歴史 — 千年の流れを年表でたどる",
  "茶道の歴史を奈良時代の伝来から、栄西・珠光・利休、三千家の成立、近代まで年表形式でわかりやすく解説します。",
  "読みもの — HISTORY","茶道の歴史",
  "一杯の薬湯が、千年をかけて「道」になった。茶と道具がたどってきた物語を、七つの時代でたどります。",
  history_body))

# ---------------------------------------------------- 3) 茶筅の種類 ----
chasen_types_body = (
sec("穂数で選ぶ","BY TINE COUNT", '''
  <p>茶筅の個性を決めるいちばんの要素が「穂数(ほすう)」——竹を割った穂の本数です。少ないほど腰が強く、多いほどきめ細かく点ちます。</p>
  <table class="name-table">
    <tr><th>荒穂(16〜48本)</th><td>穂が太く腰が強い。練るように点てる濃茶向き。</td></tr>
    <tr><th>数穂(64〜72本)</th><td>最も標準的。薄茶・濃茶どちらもこなす万能型で、最初の一本に。</td></tr>
    <tr><th>八十本立</th><td>薄茶がきめ細かく点てやすい。稽古の定番。</td></tr>
    <tr><th>百本立・百二十本立</th><td>穂が繊細で、ふんわりとした泡立ちに。初心者にも点てやすいが穂は折れやすい。</td></tr>
  </table>''')
+
sec("竹の色と流派","BAMBOO & SCHOOLS", '<div class="type-grid">'
+ tcard("白竹(しらたけ)","裏千家など","淡竹を晒した明るい竹。最も流通が多く、迷ったらまずこれ。裏千家では先が内に曲がった形を用いる。","市販の茶筅の大半は白竹。入手が容易。")
+ tcard("煤竹(すすたけ)","表千家","古民家の囲炉裏の煙で百年燻された飴色の竹。表千家が好む。年々希少になっている。","本物の煤竹は高価。色付け品と区別を。")
+ tcard("紫竹(しちく)","武者小路千家","黒竹とも呼ばれる自然の黒い竹。武者小路千家が用いる。締まった精悍な印象。","流派不問で見た目から選ぶ人も。")
+ '</div>'
+ '<p style="margin-top:18px">流派が決まっている方は竹の色を合わせるのが基本。決まっていなければ白竹の数穂〜八十本立が扱いやすい選択です。</p>')
+
sec("産地と品質","ORIGIN & QUALITY", '''
  <p>国産茶筅のほぼすべては、奈良県生駒市<strong>高山</strong>で作られています。室町時代から五百年続く「茶筅の里」で、経済産業大臣指定の伝統的工芸品「高山茶筅」として知られます。一本の竹を小刀だけで百余りの穂に割り、湯で一本ずつ曲げる——すべて手仕事です。</p>
  <p>海外産の安価な茶筅も流通していますが、穂の均一さ・耐久性・点てやすさには差があります。毎日使うなら高山茶筅がおすすめです。</p>''')
+
sec("替えどきと手入れ","CARE & REPLACEMENT", '''
  <p>茶筅は消耗品です。穂先が折れたり、開きが戻らなくなったら替えどき。使用後は湯ですすいで穂先を上に陰干しし、「くせ直し」に掛けると形が長持ちします。古い茶筅は5月の「茶筅供養」で労って手放す習わしもあります。</p>
  <p>なお衛生上、実用の茶筅は新品を求めるのが基本です。<a href="../tools/chasen.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">茶筅の基本ページ</a>もあわせてどうぞ。</p>'''))

w("articles/chasen-types.html", article_shell(
  "茶筅の種類 — 穂数・竹の色・流派での選び方",
  "茶筅の種類を穂数(数穂・八十本立・百本立)、竹の色(白竹・煤竹・紫竹)と流派、産地(高山茶筅)から解説します。",
  "読みもの — GUIDE","茶筅の種類",
  "数穂に八十本立、白竹に煤竹。小さな竹の道具にも、選び方の筋道があります。穂数・竹・流派の三つの軸でどうぞ。",
  chasen_types_body))

# ---------------------------------------------------- 4) 二十四節気と茶道具 ----
def sk(name, yomi, date, fire, firelabel, note):
    return (f'<div class="sk-card"><div class="sk-top"><div><p class="sk-name">{name}</p>'
            f'<p class="sk-yomi">{yomi}</p></div><span class="sk-fire {fire}">{firelabel}</span></div>'
            f'<p class="sk-date">{date}</p><p class="sk-note">{note}</p></div>')

SEKKI = {
"春 — SPRING": [
 sk("立春","りっしゅん","2月4日頃","ro","炉","春の始まり。逆勝手の大炉(2月)や、結び柳の名残に新春の気分を。花は椿に梅一枝。"),
 sk("雨水","うすい","2月19日頃","ro","炉","雪が雨に変わる頃。雛の趣向で貝合わせの香合、桃の絵の茶碗が愛らしい季節。"),
 sk("啓蟄","けいちつ","3月6日頃","ro","炉","虫が目覚める頃。炉の火を畳から離す釣釜に替え、春の野の意匠を茶碗に。"),
 sk("春分","しゅんぶん","3月21日頃","ro","炉","彼岸の頃。3月末の利休忌を意識し、侘びた道具組で静かな一服を。"),
 sk("清明","せいめい","4月5日頃","ro","炉","桜の盛り。炉に透木釜を掛けて火を隠し、桜の茶碗・花筏の棗を存分に。"),
 sk("穀雨","こくう","4月20日頃","ro","炉の名残","春の雨が田畑を潤す頃。炉の季節の終わり、八十八夜の新茶に思いを寄せて。"),
],
"夏 — SUMMER": [
 sk("立夏","りっか","5月6日頃","fu","風炉","初風炉。しつらえ一新、青楓の絵に新緑の爽やかさを。茶壺の口切りから半年の折り返し。"),
 sk("小満","しょうまん","5月21日頃","fu","風炉","万物が満ちる頃。新茶の季節、若葉の意匠と青竹の蓋置で瑞々しく。"),
 sk("芒種","ぼうしゅ","6月6日頃","fu","風炉","梅雨の入り。紫陽花や蛍の意匠、雨音を楽しむ道具組を。"),
 sk("夏至","げし","6月21日頃","fu","風炉","一年で最も昼が長い日。平茶碗と義山(ガラス)の水指で、目にも涼しい一服を。"),
 sk("小暑","しょうしょ","7月7日頃","fu","風炉","七夕。梶の葉の趣向、葉蓋の点前で涼一味。朝茶事の季節が始まる。"),
 sk("大暑","たいしょ","7月23日頃","fu","風炉","暑さの極み。名水点や洗い茶巾の点前で、水の涼を客に届ける。"),
],
"秋 — AUTUMN": [
 sk("立秋","りっしゅう","8月8日頃","fu","風炉","暦の上の秋。残暑の中に秋草の意匠をひとつ忍ばせるのが心憎い。"),
 sk("処暑","しょしょ","8月23日頃","fu","風炉","暑さがおさまる頃。虫の音、武蔵野の意匠。棗に薄の蒔絵を。"),
 sk("白露","はくろ","9月8日頃","fu","風炉","露が白く光る頃。月の意匠が主役に。土物の茶碗で秋の気配を。"),
 sk("秋分","しゅうぶん","9月23日頃","fu","風炉(中置)","名月の頃。風炉を畳の中央に寄せる「中置」で、火をすこし客に近づける。"),
 sk("寒露","かんろ","10月8日頃","fu","風炉(中置)","露が冷たくなる頃。中置の続き、実りと紅葉の意匠を。"),
 sk("霜降","そうこう","10月23日頃","nagori","名残","風炉の名残。破れ風炉に侘びた道具を合わせ、一年で最も渋い茶を楽しむ。"),
],
"冬 — WINTER": [
 sk("立冬","りっとう","11月7日頃","ro","炉","炉開き・口切の茶事。茶人の正月。新しい茶壺を開け、善哉で祝う。"),
 sk("小雪","しょうせつ","11月22日頃","ro","炉","初時雨の頃。照葉や初雪の意匠、織部の沓茶碗が映える。"),
 sk("大雪","たいせつ","12月7日頃","ro","炉","本格的な冬。日が短く、夜咄の茶事へ。短檠の灯りで囲む一服。"),
 sk("冬至","とうじ","12月22日頃","ro","炉","一陽来復。柚子の香合で無病息災を願い、太陽の還りを祝う。"),
 sk("小寒","しょうかん","1月6日頃","ro","炉","寒の入り、初釜の季節。結び柳に嶋台茶碗、晴れやかな正月のしつらえ。"),
 sk("大寒","だいかん","1月20日頃","ro","炉","寒さの極み。筒茶碗に絞り茶巾の点前で、湯気ごと温かさを差し出す。"),
]}

sekki_inner = '''
  <p>二十四節気は、太陽の動きで一年を二十四に分けた暦。茶の湯のしつらえは、この暦とともにめぐります。道具合わせに正解はありませんが、季節を半歩先取りするのが茶人の心得。節気ごとの定番の趣向を、一年のカレンダーにまとめました。</p>
'''
for season, cards in SEKKI.items():
    sekki_inner += f'<div class="sekki-season"><h3>{season}</h3><div class="sekki-grid">{"".join(cards)}</div></div>'
sekki_inner += '''
  <p style="margin-top:40px">炉と風炉の替わり目やしつらえの基本は<a href="../setup.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">「炉と風炉のしつらえ」</a>のページで詳しく解説しています。</p>
'''

w("articles/sekki.html", article_shell(
  "二十四節気と茶道具 — 一年のしつらえカレンダー",
  "立春から大寒まで、二十四節気ごとの茶道具の合わせ方・しつらえの趣向を一覧で紹介します。",
  "読みもの — SEASON","二十四節気と茶道具",
  "茶の湯の一年は、暦とともにめぐる。立春から大寒まで、節気ごとの道具合わせとしつらえの趣向を一枚のカレンダーに。",
  sec("一年のめぐり","THE TURNING YEAR", sekki_inner)))

# ---------------------------------------------------- articles index ----
articles_index_body = f'''
<section class="section">
  <div class="section-head reveal">
    <p class="section-kicker">読みもの — ARTICLES</p>
    <h2 class="section-title">茶道具を、もっと深く</h2>
    <div class="rule"></div>
    <p class="section-lede">道具選びが楽しくなる読みものを集めました。気になるところから、どうぞ。</p>
  </div>
  <div class="article-cards">
    <a class="article-card reveal" href="chawan-types.html">
      <p class="a-kicker">GUIDE</p><h3>茶碗の種類</h3>
      <p>楽・萩・唐津から天目・井戸まで。焼き物の系譜と形の種類を、選び方の目線で整理しました。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="history.html">
      <p class="a-kicker">HISTORY</p><h3>茶道の歴史</h3>
      <p>唐から渡った一杯の茶が、道具とともに「道」になるまで。千年の流れを年表でたどります。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="chasen-types.html">
      <p class="a-kicker">GUIDE</p><h3>茶筅の種類</h3>
      <p>穂数・竹の色・形。流派と用途で変わる茶筅の選び方を、はじめての方向けに解説します。</p>
      <p class="tool-more">読む →</p>
    </a>
    <a class="article-card reveal" href="sekki.html">
      <p class="a-kicker">SEASON</p><h3>二十四節気と茶道具</h3>
      <p>立春から大寒まで。節気ごとのしつらえと道具合わせを、一年のカレンダーにしました。</p>
      <p class="tool-more">読む →</p>
    </a>
  </div>
</section>
'''
w("articles/index.html", shell("読みもの — 茶道具コラム | 悠三堂古美術ギャラリー",
  "茶碗の種類、茶道の歴史、茶筅の種類、二十四節気と茶道具——道具選びが楽しくなる読みもの集。",
  articles_index_body, root="../", current="articles"))

print("articles done")
