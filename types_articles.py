# -*- coding: utf-8 -*-
"""Bodies for the three "types of…" articles: 釜 / 茶入 / 棗.
Each builder takes the sec() and tcard() helpers from the generator so the
markup stays identical to the existing 茶碗の種類 / 茶筅の種類 articles."""

LINK = 'style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)"'


# ============================================================== 釜 (JA) ====
def _kama_body(sec, tcard):
    return (
sec("三つの産地", "THREE CENTRES", f'''
  <p>釜は「一国一城の主」と称されるほど、茶席で重んじられる道具です。産地と時代によって大きく三つの系統に分かれ、<strong>芦屋</strong>と<strong>天明</strong>が古作の 二大産地、そこに桃山以降の<strong>京釜</strong>が続きます。</p>
  <p>釜は席の格を決める道具とされ、湯の音「松風(まつかぜ)」は茶室の主役でもあります。</p>''')
+
sec("主要な釜の種類", "MAJOR TYPES", '<div class="type-grid">'
+ tcard("芦屋釜", "ASHIYA — 筑前(福岡)",
        "南北朝から室町にかけて栄えた名門。真形(しんなり)の端正な姿に、鯰肌(なまずはだ)と呼ばれる滑らかな肌、松竹梅などの繊細な地文を鋳出します。国の重要文化財に指定された釜の大半が芦屋釜です。",
        "古芦屋は美術館級。市場に出るのは写しが中心です。")
+ tcard("天明釜", "TENMYŌ — 下野(栃木)",
        "芦屋と並ぶ古作の産地。ざらりとした荒々しい鋳肌と、飾らない素朴な姿が身上です。その侘びた風情は利休にも好まれ、芦屋の「静」に対する「動」と評されます。",
        "肌の荒れは味わい。錆との区別を確かめて。")
+ tcard("京釜", "KYOGAMA — 京都",
        "桃山時代、三条釜座(かまんざ)に釜師が集まって興った系統。利休の釜師・辻与次郎が侘びた「利休好み」を確立し、江戸期以降は大西家が代々受け継いで現代に至ります。",
        "現行品も入手しやすく、実用ならまずここから。")
+ tcard("与次郎釜", "YOJIRŌ — 利休好み",
        "辻与次郎は利休の意を受けて阿弥陀堂釜・尻張釜などを生み、以後の釜の基本形を定めました。装飾を削ぎ落とした姿が特徴です。",
        "「与次郎写」は稽古用として広く流通。")
+ tcard("浄益・大西家", "ŌNISHI — 千家十職",
        "千家十職の釜師として続く家。歴代が家元の好みに応じて釜を作り、極めのある品は評価が安定しています。",
        "箱書・極めの有無で価格が大きく動きます。")
+ tcard("現代の釜", "MODERN — 電熱対応",
        "近年は電熱器に対応した軽量の釜や、稽古用の量産品も多く作られています。実用重視なら選択肢は広く、価格もこなれています。",
        "自宅稽古なら電熱器+小ぶりの釜が扱いやすい。")
+ '</div>')
+
sec("形で選ぶ", "BY SHAPE", '''
  <table class="name-table">
    <tr><th>真形釜(しんなり)</th><td>肩が張り裾がすぼまる、芦屋以来の基本形。もっとも格が高い。</td></tr>
    <tr><th>阿弥陀堂釜(あみだどう)</th><td>口が広く胴が丸い。湯が汲みやすく、稽古に向く定番。</td></tr>
    <tr><th>富士釜(ふじ)</th><td>富士山のように裾が広がる姿。安定感がある。</td></tr>
    <tr><th>雲龍釜(うんりゅう)</th><td>細身で背が高い。小間や中置のしつらえに。</td></tr>
    <tr><th>平釜(ひら)</th><td>背が低く広い。湯が冷めやすく、風炉の季節向き。</td></tr>
    <tr><th>筒釜(つつ)</th><td>円筒形。炉の季節、狭い小間で使いやすい。</td></tr>
    <tr><th>尻張釜(しりはり)</th><td>下部が大きく張った形。与次郎の代表作。</td></tr>
    <tr><th>責紐釜(せめひも)</th><td>肩に紐を巻いたような突起をめぐらせた、格の高い形。</td></tr>
  </table>''')
+
sec("肌と見どころ", "SKIN & DETAIL", '''
  <table class="name-table">
    <tr><th>霰(あられ)</th><td>粒を一面に鋳出した文様。整然と粒が揃うほど高い技術とされる。</td></tr>
    <tr><th>鯰肌(なまずはだ)</th><td>しっとり滑らかな肌。芦屋釜の身上。</td></tr>
    <tr><th>荒肌(あらはだ)</th><td>ざらりとした粗い肌。天明釜の味わい。</td></tr>
    <tr><th>姥口(うばぐち)</th><td>口縁が内へ落ち込んだ形。侘びた風情で好まれる。</td></tr>
    <tr><th>鐶付(かんつき)</th><td>鐶を掛ける耳。鬼面・遠山・獅子など意匠が多彩。</td></tr>
    <tr><th>地文(じもん)</th><td>胴に鋳出された絵や文様。芦屋の精緻な地文が名高い。</td></tr>
  </table>''')
+
sec("炉用と風炉用", "RO & FURO", f'''
  <p>釜は炉と風炉で大きさを替えます。<strong>炉用</strong>は直径一尺前後の大ぶりなもの、<strong>風炉用</strong>はそれより小さめ。どちらにも使える兼用の釜もありますが、季節に合った寸法のほうが姿が決まります。</p>
  <p>釜だけでなく、風炉・炉縁・敷板との寸法の釣り合いも大切です。詳しくは<a href="../setup.html" {LINK}>「炉と風炉のしつらえ」</a>のページをどうぞ。</p>''')
+
sec("中古で選ぶ", "BUYING SECONDHAND", f'''
  <table class="name-table">
    <tr><th>漏れの確認</th><td>水を張って一晩置き、滲みがないか。小さな漏れは「金気止め」で直ることもある。</td></tr>
    <tr><th>錆の程度</th><td>表面の薄錆は育てられるが、内側の深い腐食は要注意。湯垢が育った釜はむしろ良品。</td></tr>
    <tr><th>底の状態</th><td>古釜は底の入れ替え(共底・替底)が普通。釜師による直しなら価値を損なわない。</td></tr>
    <tr><th>蓋と鐶</th><td>共蓋か替蓋か。鐶・釜敷が付属するかで実用性が変わる。</td></tr>
  </table>
  <p style="margin-top:18px">部位の名称と扱い方は<a href="../tools/kama.html" {LINK}>茶釜の基本ページ</a>にまとめています。</p>'''))


# ============================================================ 茶入 (JA) ====
def _chaire_body(sec, tcard):
    return (
sec("三つの出自", "THREE ORIGINS", '''
  <p>茶入は濃茶の抹茶を納める小さな壺で、茶道具のなかでも最も格の高い品のひとつです。出自によって<strong>唐物(からもの)</strong>・<strong>島物(しまもの)</strong>・<strong>和物(わもの)</strong>に分かれ、この順で格が定められています。</p>
  <table class="name-table">
    <tr><th>唐物</th><td>中国製。「一国に値する」と言われた名物中の名物。肩衝・茄子・文琳などの形が伝わる。</td></tr>
    <tr><th>島物</th><td>呂宋(ルソン)・安南(ベトナム)など東南アジア製。唐物と和物の中間の格とされる。</td></tr>
    <tr><th>和物</th><td>瀬戸を筆頭に国内で焼かれたもの。備前・信楽・高取・膳所・丹波など各地に広がる。</td></tr>
  </table>''')
+
sec("形で選ぶ", "BY SHAPE", '<div class="type-grid">'
+ tcard("肩衝", "KATATSUKI — 肩が張る",
        "肩が水平に角張って張り出した形。もっとも格が高く、伝世品の数も多い。「初花」「楢柴」「新田」は天下三肩衝と称されます。",
        "迷ったらまず肩衝。姿が決まりやすい。")
+ tcard("茄子", "NASU — 丸くふくらむ",
        "茄子の実のように丸くふくらんだ小振りな形。「九十九髪茄子(つくもがみなす)」が名高く、信長・秀吉の手を経ています。",
        "小振りで愛らしく、女性の手にも収まりよい。")
+ tcard("文琳", "BUNRIN — 林檎の意",
        "「文琳」は林檎のこと。丸みのある柔らかな姿で、茄子よりやや大きめ。可憐な印象の形です。",
        "茄子との違いは口造りと胴の張り方。")
+ tcard("大海", "TAIKAI — 平たく口が広い",
        "口が広く平たい形。ゆったりとした姿で、薄茶器として用いられることもあります。内海(うちうみ)はその小振り版。",
        "口が広い分、茶をすくいやすい。")
+ tcard("鶴首", "TSURUKUBI — 首が細い",
        "鶴の首のように、口元がすっと細長く伸びた形。すらりとした立ち姿が身上です。",
        "細い口は仕覆の抜き差しに慣れが要る。")
+ tcard("瓢箪・尻膨", "HYŌTAN & SHIRIBUKURA",
        "瓢箪はくびれのある形、尻膨(しりぶくら)は下部が大きく張った形。どちらも動きのある姿で、席に変化を与えます。",
        "個性的な形は、席の主題に合わせて選ぶ。")
+ '</div>')
+
sec("仕覆と付属", "THE SILK POUCH & FITTINGS", '''
  <p>茶入は<strong>仕覆(しふく)</strong>という袋に納めて扱います。金襴・緞子・間道といった<strong>名物裂(めいぶつぎれ)</strong>が用いられ、格の高い茶入には複数の仕覆が添うこともあります。付属が揃うほど評価は上がります。</p>
  <table class="name-table">
    <tr><th>仕覆(しふく)</th><td>茶入を納める裂の袋。裂の名と時代が価値を左右する。</td></tr>
    <tr><th>牙蓋(げぶた)</th><td>象牙の蓋。裏に金箔を張るのが約束。合いの良さが大切。</td></tr>
    <tr><th>挽家(ひきや)</th><td>茶入を納める木製の容れ物。さらに内箱・外箱と続く。</td></tr>
    <tr><th>箱書・極め</th><td>家元や鑑定家の書付。真贋と評価の拠りどころになる。</td></tr>
  </table>''')
+
sec("茶入と棗のちがい", "CHAIRE OR NATSUME", f'''
  <p>いちばんの違いは<strong>用途と格</strong>です。茶入は<strong>濃茶</strong>用の陶器、棗は<strong>薄茶</strong>用の漆器。茶入のほうが格上とされ、仕覆を脱がせる所作や拝見の作法も改まったものになります。</p>
  <p>はじめての一つなら、扱いのやさしい棗から。濃茶に進むときに茶入を迎えるのが自然な順序です。棗については<a href="natsume-types.html" {LINK}>棗の種類</a>のページをどうぞ。</p>''')
+
sec("中古で選ぶ", "BUYING SECONDHAND", f'''
  <table class="name-table">
    <tr><th>牙蓋の有無と合い</th><td>蓋を失った品も多い。すっと収まるか、隙間がないかを確認。</td></tr>
    <tr><th>釉の景色</th><td>肩から流れる釉の「なだれ」が見どころ。写真では拡大して確かめる。</td></tr>
    <tr><th>仕覆の状態</th><td>裂の傷み・擦れ、緒(ひも)の欠損。裂の名が分かるかも確認を。</td></tr>
    <tr><th>箱と伝来</th><td>挽家・内箱・外箱、書付の有無。揃っているほど価値が上がる。</td></tr>
  </table>
  <p style="margin-top:18px">茶入の基本は<a href="../tools.html" {LINK}>道具一覧</a>のページでも紹介しています。</p>'''))


# ============================================================== 棗 (JA) ====
def _natsume_body(sec, tcard):
    return (
sec("大きさで選ぶ", "BY SIZE", '''
  <p>棗は薄茶用の抹茶を納める漆器で、果実の棗に似たふくらみが名の由来です。まず覚えたいのは大きさの三段階。<strong>迷ったら中棗</strong>——これが最も標準で、どんな点前にも使えます。</p>
  <table class="name-table">
    <tr><th>大棗(おおなつめ)</th><td>堂々とした姿。濃茶の茶入代わりに用いられることもある。</td></tr>
    <tr><th>中棗(なかなつめ)</th><td>もっとも標準的で流通も多い。最初の一つに。</td></tr>
    <tr><th>小棗(こなつめ)</th><td>小振りで愛らしい。旅箪笥や小間のしつらえに。</td></tr>
    <tr><th>平棗(ひらなつめ)</th><td>背が低く平たい形。風炉の薄茶に涼しく映る。</td></tr>
    <tr><th>尻張棗(しりはり)</th><td>下部が張った形。据わりがよく、落ち着いた印象。</td></tr>
  </table>''')
+
sec("塗りと意匠", "LACQUER & DESIGN", '<div class="type-grid">'
+ tcard("真塗", "SHIN-NURI — 黒無地",
        "黒漆を塗り重ねただけの無地。利休好みの基本で、どんな席・どんな季節にも合います。装飾がないぶん、塗りの質がそのまま出ます。",
        "最初の一つは真塗が間違いありません。")
+ tcard("溜塗", "TAME-NURI — 朱を透かす",
        "下地に朱を塗り、その上から半透明の漆を掛けたもの。使い込むほど下の朱が透けて見えてきます。灯りの下で美しい。",
        "経年で表情が育つ、育て甲斐のある塗り。")
+ tcard("蒔絵", "MAKI-E — 金銀の絵",
        "金銀の粉を漆で描く日本の代表的な装飾技法。四季の草花や風景を描いた棗は、棗のいちばんの華です。",
        "図柄の季節を席の時期に合わせて選びます。")
+ tcard("螺鈿", "RADEN — 貝の輝き",
        "貝の内側を薄く切って嵌め込む技法。光の当たり方で青や虹色に変わり、夜咄の灯りに映えます。",
        "貝の浮き・欠けがないか要確認。")
+ tcard("一閑張", "IKKANBARI — 紙と漆",
        "和紙を貼り重ねて漆を塗った軽い作り。飛来一閑に始まる千家十職の技で、侘びた風合いが持ち味です。",
        "非常に軽く、水気には特に弱い。")
+ tcard("木地", "KIJI — 木目を見せる",
        "漆を厚く塗らず、木目をそのまま見せるもの。素朴な席や、名残の頃のしつらえに似合います。",
        "乾燥と湿気の変化に弱いので保管に注意。")
+ '</div>')
+
sec("棗以外の薄茶器", "OTHER THIN-TEA CONTAINERS", '''
  <p>薄茶を入れる器は棗だけではありません。総称して<strong>薄茶器(うすちゃき)</strong>と呼び、形によって名前が変わります。棗はそのうち最も普及した一形式です。</p>
  <table class="name-table">
    <tr><th>中次(なかつぎ)</th><td>円筒形で、胴の中央に蓋の合わせ目がくる形。棗と並ぶ基本。</td></tr>
    <tr><th>雪吹(ふぶき)</th><td>中次の上下の角を面取りしたもの。名は雪の吹きだまりに由来。</td></tr>
    <tr><th>金輪寺(きんりんじ)</th><td>後醍醐天皇ゆかりと伝わる筒形。蓋が深くかぶさる。</td></tr>
    <tr><th>白粉解(おしろいとき)</th><td>化粧道具からの見立て。小振りで愛らしい。</td></tr>
    <tr><th>薬器(やっき)</th><td>薬入れの見立て。すらりとした立ち姿。</td></tr>
    <tr><th>頭切(ずんぎり)</th><td>上部を水平に切り落とした形。潔い姿。</td></tr>
  </table>''')
+
sec("季節と取り合わせ", "SEASON & PAIRING", f'''
  <p>蒔絵の棗は、図柄の季節をその日の席に合わせるのが約束です。桜は春、蛍や流水は夏、薄や月は秋、雪輪や松は冬。無地の真塗は季節を選ばないので、一つ持っておくと重宝します。</p>
  <p>節気ごとの図柄の合わせ方は<a href="sekki.html" {LINK}>「二十四節気と茶道具」</a>のページに一年分まとめてあります。</p>''')
+
sec("中古で選ぶ", "BUYING SECONDHAND", f'''
  <table class="name-table">
    <tr><th>漆の状態</th><td>ひび・剥げ・艶引けを確認。直射日光による退色は戻らない。</td></tr>
    <tr><th>合口の閉まり</th><td>蓋がすっと吸い付くように閉まるものが良品。緩み・がたつきは要注意。</td></tr>
    <tr><th>蒔絵の擦れ</th><td>金蒔絵は使用で擦れる。図柄の輪郭が残っているか拡大して確認。</td></tr>
    <tr><th>共箱・塗師</th><td>塗師の署名箱があるか。輪島・山中など産地の表記も価格の目安。</td></tr>
  </table>
  <p style="margin-top:18px">部位の名称と扱い方は<a href="../tools/natsume.html" {LINK}>棗の基本ページ</a>にまとめています。</p>'''))


kama_body = _kama_body
chaire_body = _chaire_body
natsume_body = _natsume_body


# ============================================================== EN ==========
def kama_body_en(sec, tcard):
    return (
sec("THREE CENTRES", "三つの産地", '''
  <p>The kettle is said to be "worth a province and a castle" — no utensil weighs more heavily in the room. Kettles divide into three great lineages: the two ancient centres of <strong>Ashiya</strong> and <strong>Tenmyō</strong>, and the <strong>Kyoto</strong> kettles that rose in the Momoyama era.</p>
  <p>The kama sets the tone of the whole gathering, and the sound of its water — <em>matsukaze</em>, wind in the pines — is the tea room's own voice.</p>''')
+
sec("MAJOR TYPES", "主要な釜の種類", '<div class="type-grid">'
+ tcard("Ashiya", "CHIKUZEN (Fukuoka), 14th–16th c.",
        "The great early centre. Formal shinnari bodies, a smooth \"catfish skin\" surface, and finely cast reliefs of pine, bamboo and plum. Most kettles designated Important Cultural Properties are Ashiya work.",
        "Genuine old Ashiya is museum-grade; the market carries copies.")
+ tcard("Tenmyō", "SHIMOTSUKE (Tochigi), 14th–16th c.",
        "Ashiya's rival and opposite: a rough, gritty cast skin and an unadorned stance. Rikyū loved its austerity — Ashiya the still, Tenmyō the restless.",
        "Rough skin is character; learn to tell it from rust.")
+ tcard("Kyoto kettles", "KYŌGAMA — Momoyama on",
        "Casters gathered at Sanjō Kamanza in Kyoto. Rikyū's smith Tsuji Yojirō defined the wabi kettle, and from the Edo period the Ōnishi family carried the line to the present day.",
        "Current production is easy to find — start here for daily use.")
+ tcard("Yojirō kettles", "In Rikyū's taste",
        "Working to Rikyū's instructions, Tsuji Yojirō produced the amidadō and shiribari forms that became the standard shapes for everything after. Ornament stripped away to the stance itself.",
        "\"After Yojirō\" copies are widely used for practice.")
+ tcard("Ōnishi family", "One of the Senke jisshoku",
        "The hereditary kettle-makers to the Sen houses. Generations have made kettles to each grand master's taste, and pieces with an authenticated box hold their value well.",
        "Box inscriptions move the price considerably.")
+ tcard("Modern kettles", "For electric hearths",
        "Lightweight kettles designed for electric heaters, and volume-made practice kettles, are widely available now. For practical use the choice is broad and prices are reasonable.",
        "An electric heater and a small kettle is the easiest start at home.")
+ '</div>')
+
sec("BY SHAPE", "形で選ぶ", '''
  <table class="name-table">
    <tr><th>Shinnari</th><td>Square shoulders tapering to the foot — the formal shape descended from Ashiya, and the highest in rank.</td></tr>
    <tr><th>Amidadō</th><td>Wide mouth, round body. Easy to draw water from; the standard practice kettle.</td></tr>
    <tr><th>Fuji</th><td>Flaring toward the foot like Mount Fuji. Notably stable.</td></tr>
    <tr><th>Unryū</th><td>Slender and tall — for small rooms and the nakaoki setting.</td></tr>
    <tr><th>Hira</th><td>Low and wide. The water cools quickly; suits the brazier season.</td></tr>
    <tr><th>Tsutsu</th><td>Cylindrical. Easy to place in a tight room during the hearth season.</td></tr>
    <tr><th>Shiribari</th><td>Swelling strongly at the base — Yojirō's signature form.</td></tr>
    <tr><th>Semehimo</th><td>A raised band circling the shoulder like bound cord. A formal shape.</td></tr>
  </table>''')
+
sec("SKIN & DETAIL", "肌と見どころ", '''
  <table class="name-table">
    <tr><th>Arare</th><td>Hailstone studs cast across the body. The more evenly ranked, the higher the skill.</td></tr>
    <tr><th>Namazu-hada</th><td>The smooth, damp "catfish skin" that is Ashiya's hallmark.</td></tr>
    <tr><th>Ara-hada</th><td>The coarse, gritty surface prized in Tenmyō work.</td></tr>
    <tr><th>Uba-guchi</th><td>A mouth that dips inward — a wabi profile much liked by tea people.</td></tr>
    <tr><th>Kantsuki</th><td>The lugs that take the lifting rings: demon masks, distant hills, lions.</td></tr>
    <tr><th>Jimon</th><td>Relief designs cast into the body; Ashiya's fine work is the most admired.</td></tr>
  </table>''')
+
sec("RO & FURO", "炉用と風炉用", f'''
  <p>Kettles change size with the season. A <strong>ro</strong> kettle is large, roughly a shaku across; a <strong>furo</strong> kettle is smaller. Kettles that serve both exist, but a piece sized for its season simply sits better.</p>
  <p>Kettle, brazier, hearth frame and board all have to balance in scale. The <a href="../setup.html" {LINK}>Ro &amp; Furo</a> page covers this in detail.</p>''')
+
sec("BUYING SECONDHAND", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>Leak test</th><td>Fill overnight and check for seepage. Small leaks can sometimes be sealed.</td></tr>
    <tr><th>Rust</th><td>Light surface rust can be tamed; deep interior corrosion cannot. Seasoned mineral scale is a virtue.</td></tr>
    <tr><th>The bottom</th><td>Old kettles commonly have replaced bottoms — no flaw if done by a kettle-smith.</td></tr>
    <tr><th>Lid & rings</th><td>Original lid or replacement? Confirm whether rings and trivet come with it.</td></tr>
  </table>
  <p style="margin-top:18px">Parts and handling are covered on the <a href="../tools/kama.html" {LINK}>kama page</a>.</p>'''))


def chaire_body_en(sec, tcard):
    return (
sec("THREE ORIGINS", "三つの出自", '''
  <p>The chaire is the small jar that holds matcha for thick tea, and it ranks among the most formal of all utensils. Origin sets that rank: <strong>karamono</strong> (Chinese), <strong>shimamono</strong> (Southeast Asian) and <strong>wamono</strong> (Japanese), in that order.</p>
  <table class="name-table">
    <tr><th>Karamono</th><td>Chinese-made, and said to be worth a province. The katatsuki, nasu and bunrin shapes come down from these.</td></tr>
    <tr><th>Shimamono</th><td>From Luzon, Annam and elsewhere in Southeast Asia — ranked between Chinese and Japanese wares.</td></tr>
    <tr><th>Wamono</th><td>Made in Japan, led by Seto, then Bizen, Shigaraki, Takatori, Zeze and Tanba.</td></tr>
  </table>''')
+
sec("BY SHAPE", "形で選ぶ", '<div class="type-grid">'
+ tcard("Katatsuki", "Square shoulders",
        "Shoulders that break out horizontally. The highest in rank and the most numerous in the transmitted repertory — Hatsuhana, Narashiba and Nitta are the \"three great katatsuki.\"",
        "If undecided, start here: the stance composes easily.")
+ tcard("Nasu", "Aubergine",
        "Small and rounded like the fruit it is named for. Tsukumogami Nasu, which passed through the hands of Nobunaga and Hideyoshi, is the most celebrated.",
        "Small and charming; sits well in a smaller hand.")
+ tcard("Bunrin", "Apple",
        "Bunrin is an old word for apple. Softly rounded, a little larger than the nasu, with a notably graceful presence.",
        "Told apart from nasu by the mouth and the swell of the body.")
+ tcard("Taikai", "Wide mouth, flattened",
        "Broad-mouthed and low. Its relaxed posture also makes it usable as a thin-tea container; the uchiumi is the smaller version.",
        "The wide mouth makes scooping easy.")
+ tcard("Tsurukubi", "Crane's neck",
        "The mouth drawn out long and slender like a crane's neck. Its upright, tapering stance is the whole point.",
        "The narrow neck takes practice with the pouch.")
+ tcard("Hyōtan & Shiribukura", "Gourd & swelling base",
        "The gourd is waisted; the shiribukura swells strongly below. Both bring movement to an arrangement.",
        "Distinctive shapes are chosen to match a gathering's theme.")
+ '</div>')
+
sec("THE SILK POUCH & FITTINGS", "仕覆と付属", '''
  <p>A chaire is kept in a <strong>shifuku</strong>, a drawstring pouch sewn from <strong>meibutsu-gire</strong> — historic brocades, damasks and striped weaves. A high-ranking caddy may carry several pouches, and the more of its fittings survive, the higher the valuation.</p>
  <table class="name-table">
    <tr><th>Shifuku</th><td>The silk pouch. The name and age of the cloth carry real weight.</td></tr>
    <tr><th>Gebuta</th><td>The ivory lid, gold-leafed underneath by convention. Fit matters.</td></tr>
    <tr><th>Hikiya</th><td>The turned wooden case, itself kept in inner and outer boxes.</td></tr>
    <tr><th>Box inscriptions</th><td>Written authentications by a grand master or connoisseur — the basis for attribution.</td></tr>
  </table>''')
+
sec("CHAIRE OR NATSUME", "茶入と棗のちがい", f'''
  <p>The difference is <strong>use and rank</strong>. The chaire is ceramic and holds <strong>thick tea</strong>; the natsume is lacquer and holds <strong>thin tea</strong>. The chaire ranks higher, and the movements around it — slipping off the pouch, presenting it for viewing — are correspondingly formal.</p>
  <p>For a first caddy, the natsume is far easier to handle. Take up a chaire when you move on to thick tea. See <a href="natsume-types.html" {LINK}>Types of Natsume</a>.</p>''')
+
sec("BUYING SECONDHAND", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>The ivory lid</th><td>Often lost. Check that it settles cleanly with no gap.</td></tr>
    <tr><th>Glaze landscape</th><td>The glaze "cascade" running from the shoulder is the thing to look at — zoom in on photographs.</td></tr>
    <tr><th>Pouch condition</th><td>Wear, thinning, missing cords. Ask whether the weave has a name.</td></tr>
    <tr><th>Boxes & provenance</th><td>Case, inner box, outer box, inscriptions — a complete set lifts the value sharply.</td></tr>
  </table>
  <p style="margin-top:18px">The chaire also appears on the <a href="../tools.html" {LINK}>utensils list</a>.</p>'''))


def natsume_body_en(sec, tcard):
    return (
sec("BY SIZE", "大きさで選ぶ", '''
  <p>The natsume is the lacquered container for thin-tea matcha, named for its resemblance to the jujube fruit. Size comes first, and there are three: <strong>when in doubt, take the medium</strong> — it is the standard, and serves every procedure.</p>
  <table class="name-table">
    <tr><th>Ō-natsume (large)</th><td>An imposing stance; sometimes used in place of a chaire for thick tea.</td></tr>
    <tr><th>Naka-natsume (medium)</th><td>The standard size and the most widely available. The one to start with.</td></tr>
    <tr><th>Ko-natsume (small)</th><td>Small and endearing — for the travelling cabinet and small rooms.</td></tr>
    <tr><th>Hira-natsume (flat)</th><td>Low and wide. Reads cool for thin tea in the brazier season.</td></tr>
    <tr><th>Shiribari</th><td>Swelling at the base. Settles firmly, with a composed air.</td></tr>
  </table>''')
+
sec("LACQUER & DESIGN", "塗りと意匠", '<div class="type-grid">'
+ tcard("Shin-nuri", "Plain black",
        "Layer upon layer of black lacquer and nothing else. Rikyū's basic taste, at home in any room and any season — and with no ornament to hide behind, the quality of the lacquer shows plainly.",
        "For a first caddy, plain black never goes wrong.")
+ tcard("Tame-nuri", "Vermilion beneath",
        "Vermilion ground under a translucent top coat. With use the red beneath begins to show through. Especially beautiful under lamplight.",
        "A finish that ripens — worth living with.")
+ tcard("Maki-e", "Gold and silver",
        "Designs drawn in gold and silver powder — Japan's signature lacquer technique, and the natsume's great showpiece. Seasonal flowers and landscapes.",
        "Match the motif's season to the day of the gathering.")
+ tcard("Raden", "Mother-of-pearl",
        "Thin shell inlaid into the lacquer, shifting blue and iridescent as the light moves. It comes alive at an evening gathering.",
        "Check carefully for lifted or missing shell.")
+ tcard("Ikkanbari", "Paper and lacquer",
        "Layered paper finished with lacquer — very light, with a quiet wabi surface. The technique of Hiki Ikkan, one of the Senke jisshoku.",
        "Extremely light, and especially vulnerable to moisture.")
+ tcard("Kiji", "Bare wood",
        "Lightly finished so the grain shows through. Suits a plain room, or the austere weeks of nagori.",
        "Sensitive to changes in humidity — store with care.")
+ '</div>')
+
sec("OTHER THIN-TEA CONTAINERS", "棗以外の薄茶器", '''
  <p>The natsume is not the only vessel for thin tea. The family is called <strong>usuchaki</strong>, and the names change with the form; the natsume is simply the most widespread of them.</p>
  <table class="name-table">
    <tr><th>Nakatsugi</th><td>Cylindrical, with the lid meeting at the middle of the body. The other basic form.</td></tr>
    <tr><th>Fubuki</th><td>A nakatsugi with the top and bottom edges chamfered. Named for drifting snow.</td></tr>
    <tr><th>Kinrinji</th><td>A cylinder with a deep lid, said to descend from Emperor Go-Daigo.</td></tr>
    <tr><th>Oshiroi-toki</th><td>Taken by mitate from a cosmetics container. Small and charming.</td></tr>
    <tr><th>Yakki</th><td>From a medicine jar. A slender, upright stance.</td></tr>
    <tr><th>Zungiri</th><td>Cut off flat at the top. A decisive, clean-cut shape.</td></tr>
  </table>''')
+
sec("SEASON & PAIRING", "季節と取り合わせ", f'''
  <p>A maki-e natsume is chosen so its motif matches the day: cherry in spring, fireflies and flowing water in summer, pampas and the moon in autumn, snow-rings and pine in winter. Plain black belongs to no season, which is exactly why one is worth owning.</p>
  <p>A full year of motif pairings is set out on the <a href="sekki.html" {LINK}>24 Solar Terms</a> page.</p>''')
+
sec("BUYING SECONDHAND", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>Lacquer condition</th><td>Cracks, flaking, dulling. Sun-fading cannot be reversed.</td></tr>
    <tr><th>Fit of the lid</th><td>A good caddy's lid settles with a gentle sigh. Rattling is a warning.</td></tr>
    <tr><th>Maki-e wear</th><td>Gold wears with use — zoom in and confirm the outlines survive.</td></tr>
    <tr><th>Box & maker</th><td>A signed box, and origins such as Wajima or Yamanaka, guide the price.</td></tr>
  </table>
  <p style="margin-top:18px">Parts and handling are on the <a href="../tools/natsume.html" {LINK}>natsume page</a>.</p>'''))


# =========================================================== français / 繁體 ==
# Mêmes articles, mêmes helpers (sec, tcard) — seul le texte change.

def natsume_body_fr(sec, tcard):
    return (
sec("PAR LA TAILLE", "大きさで選ぶ", '''
  <p>Le natsume est le récipient laqué du thé léger, nommé d’après sa ressemblance avec le fruit du jujubier. La taille vient d’abord, et il y en a trois : <strong>dans le doute, prenez le moyen</strong> — c’est la référence, et il convient à tous les temae.</p>
  <table class="name-table">
    <tr><th>Ō-natsume (grand)</th><td>Une allure imposante ; on l’emploie parfois à la place d’un chaire pour le thé épais.</td></tr>
    <tr><th>Naka-natsume (moyen)</th><td>La taille ordinaire, et la plus répandue. Celle par laquelle commencer.</td></tr>
    <tr><th>Ko-natsume (petit)</th><td>Petit et attachant — pour le meuble de voyage et les petites pièces.</td></tr>
    <tr><th>Hira-natsume (plat)</th><td>Bas et large. Il donne une impression de fraîcheur au thé léger, à la saison du brasero.</td></tr>
    <tr><th>Shiribari</th><td>Renflé à la base. Il se pose fermement, d’un air posé.</td></tr>
  </table>''')
+
sec("LAQUE ET DÉCOR", "塗りと意匠", '<div class="type-grid">'
+ tcard("Shin-nuri", "Noir uni",
        "Couche sur couche de laque noire, et rien d’autre. Le goût élémentaire de Rikyū, à son aise dans toute pièce et toute saison — et comme aucun ornement ne vient couvrir, la qualité de la laque se voit franchement.",
        "Pour une première boîte, le noir uni ne trompe jamais.")
+ tcard("Tame-nuri", "Vermillon dessous",
        "Un fond vermillon sous une couche translucide. À l’usage, le rouge du dessous commence à transparaître. Particulièrement beau à la lumière d’une lampe.",
        "Une finition qui mûrit — elle mérite qu’on vive avec.")
+ tcard("Maki-e", "Or et argent",
        "Des motifs tracés à la poudre d’or et d’argent — la technique emblématique de la laque japonaise, et le grand terrain d’honneur du natsume. Fleurs de saison et paysages.",
        "Accordez la saison du motif au jour de la réunion.")
+ tcard("Raden", "Nacre",
        "De minces lames de coquillage incrustées dans la laque, bleues et changeantes à mesure que la lumière bouge. Elles prennent vie lors d’une réunion du soir.",
        "Vérifiez soigneusement qu’aucune nacre ne se soulève ou ne manque.")
+ tcard("Ikkanbari", "Papier et laque",
        "Du papier superposé puis laqué — très léger, d’une surface wabi discrète. La technique de Hiki Ikkan, l’un des dix artisans des Senke.",
        "Extrêmement léger, et particulièrement sensible à l’humidité.")
+ tcard("Kiji", "Bois nu",
        "À peine fini, de sorte que le fil du bois reste visible. Convient à une pièce sobre, ou aux semaines austères du nagori.",
        "Sensible aux variations d’humidité — rangez-le avec soin.")
+ '</div>')
+
sec("LES AUTRES BOÎTES À THÉ LÉGER", "棗以外の薄茶器", '''
  <p>Le natsume n’est pas le seul récipient du thé léger. La famille s’appelle <strong>usuchaki</strong>, et les noms changent avec la forme ; le natsume en est simplement le plus répandu.</p>
  <table class="name-table">
    <tr><th>Nakatsugi</th><td>Cylindrique, le couvercle rejoignant le corps en son milieu. L’autre forme fondamentale.</td></tr>
    <tr><th>Fubuki</th><td>Un nakatsugi dont les arêtes du haut et du bas sont abattues. Nommé d’après la neige qui tourbillonne.</td></tr>
    <tr><th>Kinrinji</th><td>Un cylindre à couvercle profond, que l’on dit descendre de l’empereur Go-Daigo.</td></tr>
    <tr><th>Oshiroi-toki</th><td>Pris par mitate à un pot de fard. Petit et charmant.</td></tr>
    <tr><th>Yakki</th><td>Venu d’un pot à remèdes. Une stature élancée, bien droite.</td></tr>
    <tr><th>Zungiri</th><td>Coupé net et plat au sommet. Une forme décidée, sans bavure.</td></tr>
  </table>'''))


def natsume_body_zh(sec, tcard):
    return (
sec("依大小挑選", "大きさで選ぶ", '''
  <p>棗是盛裝薄茶抹茶的漆器，因形似棗子的果實而得名。首先要看的是大小，主要有三種：<strong>拿不定主意時，就取中棗</strong>——它是基準，任何點前都能應付。</p>
  <table class="name-table">
    <tr><th>大棗</th><td>器度堂堂；有時也代替茶入盛裝濃茶。</td></tr>
    <tr><th>中棗</th><td>標準的尺寸，也最容易取得。入門就從它開始。</td></tr>
    <tr><th>小棗</th><td>小巧可愛——適合旅簞笥與小間。</td></tr>
    <tr><th>平棗</th><td>矮而寬。在風爐的季節盛薄茶，看來格外清涼。</td></tr>
    <tr><th>尻張</th><td>底部微微鼓起。放得穩當，有一份沉著之氣。</td></tr>
  </table>''')
+
sec("塗法與紋樣", "塗りと意匠", '<div class="type-grid">'
+ tcard("真塗", "素黑",
        "一層又一層的黑漆，此外別無他物。是利休最根本的趣味，任何茶室、任何季節都自在——而且沒有紋樣可以遮掩，漆的好壞一望即知。",
        "作為第一只茶器，素黑絕不會出錯。")
+ tcard("溜塗", "底下的朱色",
        "朱色的底，罩上半透明的面漆。隨著使用，底下的紅會漸漸透出來。在燈火下尤其美。",
        "是一種會熟成的塗法——值得長久相處。")
+ tcard("蒔繪", "金銀",
        "以金銀粉描繪的紋樣——日本漆藝的代表技法，也是棗大顯身手之處。四季的花草與風景。",
        "請讓紋樣的節令，配合茶會當天的時節。")
+ tcard("螺鈿", "貝殼",
        "將薄薄的貝片嵌入漆中，隨光線移動而泛出藍色的虹彩。在夜咄的茶會上最為生動。",
        "請仔細確認貝片有無翹起或脫落。")
+ tcard("一閑張", "紙與漆",
        "以紙層層裱糊後上漆——極輕，表面帶著安靜的侘味。出自千家十職之一飛來一閑的技法。",
        "極輕，但也格外怕潮。")
+ tcard("木地", "素木",
        "只作最低限度的處理，讓木紋透出來。適合樸素的茶室，或是名殘那幾週的清簡。",
        "對濕度的變化敏感——收藏時請留意。")
+ '</div>')
+
sec("棗以外的薄茶器", "棗以外の薄茶器", '''
  <p>盛裝薄茶的器物不只有棗。這一整個家族稱為<strong>薄茶器</strong>，名稱隨器形而異；棗只是其中最為普及的一種。</p>
  <table class="name-table">
    <tr><th>中次</th><td>筒形，蓋與身在腰部中段相接。另一種基本的形制。</td></tr>
    <tr><th>吹雪</th><td>將中次的上下邊緣削去稜角者。因風雪捲揚之貌而得名。</td></tr>
    <tr><th>金輪寺</th><td>筒形而蓋深，相傳源自後醍醐天皇。</td></tr>
    <tr><th>白粉解</th><td>由妝粉容器見立而來。小巧而有趣味。</td></tr>
    <tr><th>藥器</th><td>由藥罐而來。器形細長而挺立。</td></tr>
    <tr><th>寸切</th><td>頂部平平切斷。形制果斷而俐落。</td></tr>
  </table>'''))


def chaire_body_fr(sec, tcard):
    return (
sec("TROIS ORIGINES", "三つの出自", '''
  <p>Le chaire est le petit pot qui garde le matcha du thé épais, et il compte parmi les ustensiles les plus formels. C’est l’origine qui fixe ce rang : <strong>karamono</strong> (de Chine), <strong>shimamono</strong> (d’Asie du Sud-Est) et <strong>wamono</strong> (du Japon), dans cet ordre.</p>
  <table class="name-table">
    <tr><th>Karamono</th><td>De fabrication chinoise, et dits valoir une province. Les formes katatsuki, nasu et bunrin en descendent.</td></tr>
    <tr><th>Shimamono</th><td>De Luçon, d’Annam et d’ailleurs en Asie du Sud-Est — au rang intermédiaire entre les pièces chinoises et japonaises.</td></tr>
    <tr><th>Wamono</th><td>Faits au Japon, Seto en tête, puis Bizen, Shigaraki, Takatori, Zeze et Tanba.</td></tr>
  </table>''')
+
sec("PAR LA FORME", "形で選ぶ", '<div class="type-grid">'
+ tcard("Katatsuki", "Épaules carrées",
        "Des épaules qui se détachent à l’horizontale. Le rang le plus élevé et le plus nombreux du répertoire transmis — Hatsuhana, Narashiba et Nitta sont les « trois grands katatsuki ».",
        "Dans l’hésitation, commencez ici : la stature se compose sans peine.")
+ tcard("Nasu", "Aubergine",
        "Petit et rond comme le fruit dont il porte le nom. Le Tsukumogami Nasu, passé entre les mains de Nobunaga et de Hideyoshi, est le plus fameux.",
        "Petit et attachant ; il tient bien dans une main menue.")
+ tcard("Bunrin", "Pomme",
        "Bunrin est un vieux mot pour la pomme. Doucement arrondi, un peu plus grand que le nasu, d’une présence remarquablement gracieuse.",
        "On le distingue du nasu à la bouche et au renflement de la panse.")
+ tcard("Taikai", "Bouche large, aplati",
        "Bouche large et corps bas. Sa posture détendue permet aussi de l’employer comme boîte à thé léger ; l’uchiumi en est la version réduite.",
        "La bouche large rend le prélèvement facile.")
+ tcard("Tsurukubi", "Col de grue",
        "La bouche étirée, longue et mince comme un col de grue. Sa stature droite et fuselée est tout le propos.",
        "Le col étroit demande de l’habitude avec la pochette.")
+ tcard("Hyōtan et shiribukura", "Gourde et base renflée",
        "La gourde est resserrée à la taille ; le shiribukura se renfle fortement vers le bas. L’un et l’autre apportent du mouvement à une composition.",
        "On choisit ces formes marquées pour répondre au thème d’une réunion.")
+ '</div>')
+
sec("LA POCHETTE DE SOIE ET LES ACCESSOIRES", "仕覆と付属", '''
  <p>Un chaire se garde dans un <strong>shifuku</strong>, une pochette à cordon cousue dans un <strong>meibutsu-gire</strong> — brocarts, damas et tissus rayés historiques. Une boîte de haut rang peut posséder plusieurs pochettes, et plus ses accessoires subsistent, plus l’estimation monte.</p>
  <table class="name-table">
    <tr><th>Shifuku</th><td>La pochette de soie. Le nom et l’époque de l’étoffe pèsent réellement.</td></tr>
    <tr><th>Gebuta</th><td>Le couvercle d’ivoire, doré à la feuille par-dessous selon l’usage. L’ajustement compte.</td></tr>
    <tr><th>Hikiya</th><td>L’étui de bois tourné, lui-même gardé dans une boîte intérieure et une boîte extérieure.</td></tr>
    <tr><th>Inscriptions de boîte</th><td>Authentifications écrites d’un grand maître ou d’un connaisseur — la base de l’attribution.</td></tr>
  </table>''')
+
sec("CHAIRE OU NATSUME", "茶入と棗のちがい", f'''
  <p>La différence tient à <strong>l’usage et au rang</strong>. Le chaire est de céramique et contient le <strong>thé épais</strong> ; le natsume est de laque et contient le <strong>thé léger</strong>. Le chaire est d’un rang plus élevé, et les gestes qui l’entourent — ôter la pochette, le présenter à l’examen — sont d’autant plus formels.</p>
  <p>Pour une première boîte, le natsume est bien plus facile à manier. Prenez un chaire lorsque vous passerez au thé épais. Voyez <a href="natsume-types.html" {LINK}>Les types de natsume</a>.</p>''')
+
sec("ACHETER D’OCCASION", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>Le couvercle d’ivoire</th><td>Souvent perdu. Vérifiez qu’il se pose net, sans jour.</td></tr>
    <tr><th>Paysage de glaçure</th><td>La « cascade » de glaçure qui descend de l’épaule est ce qu’il faut regarder — agrandissez les photographies.</td></tr>
    <tr><th>État de la pochette</th><td>Usure, tissu aminci, cordons manquants. Demandez si le tissage porte un nom.</td></tr>
    <tr><th>Boîtes et provenance</th><td>Étui, boîte intérieure, boîte extérieure, inscriptions — un ensemble complet élève nettement la valeur.</td></tr>
  </table>
  <p style="margin-top:18px">Le chaire figure aussi dans <a href="../tools.html" {LINK}>la liste des ustensiles</a>.</p>'''))


def chaire_body_zh(sec, tcard):
    return (
sec("三種出身", "三つの出自", '''
  <p>茶入是盛裝濃茶抹茶的小罐，在所有道具之中屬於格調最高的一類。決定這份格調的，是它的出身：<strong>唐物</strong>（中國）、<strong>島物</strong>（東南亞）、<strong>和物</strong>（日本），依此為序。</p>
  <table class="name-table">
    <tr><th>唐物</th><td>中國所製，素有「值一國」之譽。肩衝、茄子、文琳等器形皆源自於此。</td></tr>
    <tr><th>島物</th><td>來自呂宋、安南等東南亞各地——地位介於唐物與和物之間。</td></tr>
    <tr><th>和物</th><td>日本所製，以瀨戶為首，其次有備前、信樂、高取、膳所與丹波。</td></tr>
  </table>''')
+
sec("依器形挑選", "形で選ぶ", '<div class="type-grid">'
+ tcard("肩衝", "方肩",
        "肩部向水平方向張出。在傳世品中格調最高、數量也最多——「初花」「楢柴」「新田」合稱天下三肩衝。",
        "若拿不定主意就從它入手：姿態容易與其他道具相配。")
+ tcard("茄子", "茄子形",
        "小而渾圓，如其名所指的果實。經織田信長與豐臣秀吉之手的「九十九髮茄子」最負盛名。",
        "小巧可愛；手小的人也好拿。")
+ tcard("文琳", "蘋果形",
        "「文琳」是蘋果的古稱。柔和渾圓，比茄子稍大，姿態格外優雅。",
        "與茄子的分別，在於口部與腹部隆起的方式。")
+ tcard("大海", "廣口而扁",
        "口寬而器身低。那份從容的姿態，也可以當作薄茶器使用；較小的版本稱為「內海」。",
        "口寬，舀取時較為順手。")
+ tcard("鶴首", "鶴的頸子",
        "口部拉得細長，一如鶴的頸子。挺立而漸收的姿態，正是它的看點。",
        "頸細，穿脫仕覆需要一些熟練。")
+ tcard("瓢簞・尻膨", "葫蘆與下腹鼓起",
        "瓢簞在腰部收束；尻膨則在下方強烈鼓起。兩者都能為取合帶來動勢。",
        "形制鮮明者，多是為了呼應茶會的主題而選。")
+ '</div>')
+
sec("仕覆與附件", "仕覆と付属", '''
  <p>茶入收在<strong>仕覆</strong>之中——那是以<strong>名物裂</strong>縫製的束口袋，用的是歷代的金襴、緞子與間道。格調高的茶入可能配有數個仕覆，而附件保存得越齊全，估價也越高。</p>
  <table class="name-table">
    <tr><th>仕覆</th><td>絲質的袋。布的名稱與年代，分量相當重。</td></tr>
    <tr><th>牙蓋</th><td>象牙製的蓋，依慣例在內側貼金箔。密合與否很要緊。</td></tr>
    <tr><th>挽家</th><td>旋木製成的容器，其本身又收在內箱與外箱之中。</td></tr>
    <tr><th>箱書</th><td>家元或鑑賞家所寫的鑑定文字——是判定來歷的依據。</td></tr>
  </table>''')
+
sec("茶入與棗的分別", "茶入と棗のちがい", f'''
  <p>分別在於<strong>用途與格調</strong>。茶入是陶製的，盛<strong>濃茶</strong>；棗是漆製的，盛<strong>薄茶</strong>。茶入的格調較高，圍繞它的動作——脫下仕覆、奉出拜見——也相應地更為正式。</p>
  <p>作為第一件茶器，棗要好操作得多。等進入濃茶的階段，再取用茶入即可。請參見<a href="natsume-types.html" {LINK}>棗的種類</a>。</p>''')
+
sec("選購二手時", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>象牙的蓋</th><td>時常佚失。請確認蓋子能否毫無縫隙地落穩。</td></tr>
    <tr><th>釉的景色</th><td>自肩部流下的釉「瀑布」最值得細看——請放大照片確認。</td></tr>
    <tr><th>仕覆的狀態</th><td>磨損、布質變薄、緒繩缺失。請詢問所用的裂是否有名。</td></tr>
    <tr><th>箱與來歷</th><td>挽家、內箱、外箱、箱書——一整套齊全，價值會大幅提升。</td></tr>
  </table>
  <p style="margin-top:18px">茶入也收錄在<a href="../tools.html" {LINK}>茶道具一覽</a>之中。</p>'''))


def kama_body_fr(sec, tcard):
    return (
sec("TROIS CENTRES", "三つの産地", '''
  <p>On dit de la bouilloire qu’elle « vaut une province et un château » — aucun ustensile ne pèse plus lourd dans la pièce. Les kama se répartissent en trois grandes lignées : les deux centres anciens d’<strong>Ashiya</strong> et de <strong>Tenmyō</strong>, et les bouilloires de <strong>Kyoto</strong>, qui s’élèvent à l’ère de Momoyama.</p>
  <p>La kama donne le ton de toute la réunion, et le bruit de son eau — le <em>matsukaze</em>, vent dans les pins — est la voix même de la salle de thé.</p>''')
+
sec("LES PRINCIPAUX TYPES", "主要な釜の種類", '<div class="type-grid">'
+ tcard("Ashiya", "CHIKUZEN (Fukuoka), XIVᵉ–XVIᵉ s.",
        "Le grand centre des origines. Corps shinnari de forme formelle, surface lisse dite « peau de silure », et reliefs finement fondus de pin, de bambou et de prunier. La plupart des bouilloires classées Biens culturels importants sont d’Ashiya.",
        "Un véritable Ashiya ancien est de qualité muséale ; le marché regorge de copies.")
+ tcard("Tenmyō", "SHIMOTSUKE (Tochigi), XIVᵉ–XVIᵉ s.",
        "La rivale et le contraire d’Ashiya : une peau de fonte rugueuse et grenue, une stature sans ornement. Rikyū en aimait l’austérité — Ashiya le calme, Tenmyō l’inquiet.",
        "La peau rugueuse est un caractère ; apprenez à la distinguer de la rouille.")
+ tcard("Bouilloires de Kyoto", "KYŌGAMA — à partir de Momoyama",
        "Les fondeurs se rassemblent au Sanjō Kamanza, à Kyoto. Tsuji Yojirō, le fondeur de Rikyū, définit la bouilloire wabi, et depuis l’époque d’Edo la famille Ōnishi porte cette lignée jusqu’à nous.",
        "La production actuelle se trouve facilement — commencez ici pour l’usage quotidien.")
+ tcard("Bouilloires de Yojirō", "Au goût de Rikyū",
        "Travaillant sur les instructions de Rikyū, Tsuji Yojirō produisit les formes amidadō et shiribari, devenues les formes de référence de tout ce qui suivit. L’ornement retranché jusqu’à la stature seule.",
        "Les copies « d’après Yojirō » servent couramment à l’exercice.")
+ tcard("Famille Ōnishi", "L’un des dix artisans des Senke",
        "Les fondeurs héréditaires des maisons Sen. Des générations ont fait des bouilloires au goût de chaque grand maître, et les pièces à boîte authentifiée tiennent bien leur valeur.",
        "Les inscriptions de boîte déplacent sensiblement le prix.")
+ tcard("Bouilloires modernes", "Pour foyers électriques",
        "On trouve aujourd’hui des bouilloires légères conçues pour les réchauds électriques, et des bouilloires d’exercice fabriquées en série. Pour l’usage pratique, le choix est large et les prix raisonnables.",
        "Un réchaud électrique et une petite bouilloire : le départ le plus simple chez soi.")
+ '</div>')
+
sec("PAR LA FORME", "形で選ぶ", '''
  <table class="name-table">
    <tr><th>Shinnari</th><td>Épaules carrées se resserrant vers le pied — la forme formelle héritée d’Ashiya, et la plus haute en rang.</td></tr>
    <tr><th>Amidadō</th><td>Bouche large, corps rond. Facile à puiser ; la bouilloire d’exercice ordinaire.</td></tr>
    <tr><th>Fuji</th><td>Évasée vers le pied comme le mont Fuji. Remarquablement stable.</td></tr>
    <tr><th>Unryū</th><td>Élancée et haute — pour les petites pièces et la disposition nakaoki.</td></tr>
    <tr><th>Hira</th><td>Basse et large. L’eau refroidit vite ; convient à la saison du brasero.</td></tr>
    <tr><th>Tsutsu</th><td>Cylindrique. Facile à placer dans une pièce étroite, à la saison du foyer.</td></tr>
    <tr><th>Shiribari</th><td>Fortement renflée à la base — la forme signature de Yojirō.</td></tr>
    <tr><th>Semehimo</th><td>Un bandeau en relief ceignant l’épaule comme une corde liée. Une forme formelle.</td></tr>
  </table>''')
+
sec("PEAU ET DÉTAILS", "肌と見どころ", '''
  <table class="name-table">
    <tr><th>Arare</th><td>Des clous de grêle semés sur le corps. Plus leur alignement est régulier, plus grande est l’habileté.</td></tr>
    <tr><th>Namazu-hada</th><td>La « peau de silure », lisse et comme humide, qui est la marque d’Ashiya.</td></tr>
    <tr><th>Ara-hada</th><td>La surface grossière et grenue que l’on prise dans le travail de Tenmyō.</td></tr>
    <tr><th>Uba-guchi</th><td>Une bouche qui plonge vers l’intérieur — un profil wabi très aimé des gens de thé.</td></tr>
    <tr><th>Kantsuki</th><td>Les attaches qui reçoivent les anneaux : masques de démon, collines lointaines, lions.</td></tr>
    <tr><th>Jimon</th><td>Motifs en relief fondus dans le corps ; le travail fin d’Ashiya est le plus admiré.</td></tr>
  </table>''')
+
sec("RO ET FURO", "炉用と風炉用", f'''
  <p>Les bouilloires changent de taille avec la saison. Une kama de <strong>ro</strong> est grande, environ un shaku de diamètre ; une kama de <strong>furo</strong> est plus petite. Il existe des bouilloires qui servent aux deux, mais une pièce à la mesure de sa saison s’assied tout simplement mieux.</p>
  <p>Bouilloire, brasero, cadre du foyer et planche doivent s’équilibrer en échelle. La page <a href="../setup.html" {LINK}>Ro et furo</a> traite cela en détail.</p>''')
+
sec("ACHETER D’OCCASION", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>Essai d’étanchéité</th><td>Remplissez une nuit entière et guettez le suintement. De petites fuites se colmatent parfois.</td></tr>
    <tr><th>Rouille</th><td>Une rouille de surface se maîtrise ; une corrosion profonde à l’intérieur, non. Le dépôt minéral, lui, est une vertu.</td></tr>
    <tr><th>Le fond</th><td>Les vieilles bouilloires ont couramment un fond refait — nullement un défaut s’il est l’œuvre d’un fondeur.</td></tr>
    <tr><th>Couvercle et anneaux</th><td>Couvercle d’origine ou de remplacement ? Vérifiez si les anneaux et le trépied l’accompagnent.</td></tr>
  </table>
  <p style="margin-top:18px">Les parties et le maniement sont traités sur la <a href="../tools/kama.html" {LINK}>fiche du kama</a>.</p>'''))


def kama_body_zh(sec, tcard):
    return (
sec("三大產地", "三つの産地", '''
  <p>釜素有「值一國一城」之譽——茶室之中，沒有一件道具比它更有分量。釜可分為三大系譜：古老的兩處產地<strong>蘆屋</strong>與<strong>天明</strong>，以及桃山時代崛起的<strong>京釜</strong>。</p>
  <p>釜為整場茶會定下基調，而釜中的水聲——所謂<em>松風</em>——正是茶室自身的聲音。</p>''')
+
sec("主要的釜", "主要な釜の種類", '<div class="type-grid">'
+ tcard("蘆屋釜", "筑前（福岡）・14–16世紀",
        "最早的大產地。器身多為格調端正的真形，表面是光潤的「鯰肌」，並鑄有松竹梅等細緻的浮雕紋樣。被指定為重要文化財的釜，多半出自蘆屋。",
        "真正的古蘆屋已屬博物館等級；市面上多為仿作。")
+ tcard("天明釜", "下野（栃木）・14–16世紀",
        "蘆屋的對手，也是它的反面：鑄肌粗糙帶砂，姿態不加修飾。利休喜愛它的枯淡——蘆屋是靜，天明是動。",
        "粗肌是它的個性；請學會與鏽蝕區分。")
+ tcard("京釜", "桃山時代以降",
        "鑄物師聚集於京都三条釜座。利休的釜師辻与次郎確立了侘釜的樣式，自江戶時代起，大西家將這一脈延續至今。",
        "現行品容易取得——日常使用就從這裡入手。")
+ tcard("与次郎釜", "利休好み",
        "辻与次郎依利休的指示製作，創出阿彌陀堂與尻張等形制，成為此後所有釜的基準形。剝去裝飾，只剩姿態本身。",
        "「与次郎寫」的仿作廣泛用於練習。")
+ tcard("大西家", "千家十職之一",
        "千家世襲的釜師。歷代依各家元的喜好製釜，附有鑑定箱書者，價值相當穩固。",
        "箱書對價格的影響相當大。")
+ tcard("現代の釜", "電熱器用",
        "如今可以買到為電熱器設計的輕量釜，以及量產的練習用釜。就實用而言選擇很廣，價格也合理。",
        "電熱器配一只小釜，是在家起步最省事的組合。")
+ '</div>')
+
sec("依器形挑選", "形で選ぶ", '''
  <table class="name-table">
    <tr><th>真形</th><td>方肩向下漸收——承自蘆屋的正式形制，格調最高。</td></tr>
    <tr><th>阿彌陀堂</th><td>口寬、身圓。汲水順手；是最常見的練習用釜。</td></tr>
    <tr><th>富士</th><td>向下擺開，狀如富士山。格外安定。</td></tr>
    <tr><th>雲龍</th><td>細長而高——適合小間與中置的擺法。</td></tr>
    <tr><th>平釜</th><td>低而寬。水涼得快，宜於風爐的季節。</td></tr>
    <tr><th>筒釜</th><td>筒形。爐的季節裡，在狹窄的茶室中容易安置。</td></tr>
    <tr><th>尻張</th><td>下部強烈鼓起——与次郎的代表形制。</td></tr>
    <tr><th>責紐</th><td>肩部環著一道凸起的帶，如綁縛的繩。屬於正式的形制。</td></tr>
  </table>''')
+
sec("肌與看點", "肌と見どころ", '''
  <table class="name-table">
    <tr><th>霰</th><td>器身鑄滿如冰雹般的凸粒。排列越勻整，技術越高。</td></tr>
    <tr><th>鯰肌</th><td>光潤而似帶濕氣的「鯰魚皮」，是蘆屋的標誌。</td></tr>
    <tr><th>荒肌</th><td>粗糙帶砂的表面，在天明釜中備受珍視。</td></tr>
    <tr><th>姥口</th><td>口部向內凹陷——茶人十分喜愛的侘之輪廓。</td></tr>
    <tr><th>鐶付</th><td>掛提環的兩耳：鬼面、遠山、獅子等造型。</td></tr>
    <tr><th>地紋</th><td>鑄在器身上的浮雕紋樣；以蘆屋的細膩之作最受推崇。</td></tr>
  </table>''')
+
sec("爐用與風爐用", "炉用と風炉用", f'''
  <p>釜的大小隨季節而變。<strong>爐</strong>用的釜較大，口徑約一尺；<strong>風爐</strong>用的則較小。也有兩用的釜，但合乎季節尺寸的一只，看起來就是更安穩。</p>
  <p>釜、風爐、爐緣與敷板的大小必須彼此相稱。<a href="../setup.html" {LINK}>爐與風爐</a>的頁面有詳細說明。</p>''')
+
sec("選購二手時", "中古で選ぶ", f'''
  <table class="name-table">
    <tr><th>漏水測試</th><td>注滿水放置一夜，看是否滲漏。小的漏處有時可以修補。</td></tr>
    <tr><th>鏽</th><td>表面的薄鏽可以處理，內部的深度腐蝕則不行。內壁的水垢反而是好事。</td></tr>
    <tr><th>底</th><td>古釜多半換過底——只要出自釜師之手就不算缺點。</td></tr>
    <tr><th>蓋與鐶</th><td>是原配的蓋還是後配？請確認鐶與五德是否一併附上。</td></tr>
  </table>
  <p style="margin-top:18px">各部位與使用方式，請見<a href="../tools/kama.html" {LINK}>釜的頁面</a>。</p>'''))
