# -*- coding: utf-8 -*-
"""七十二候 — the 72 micro-seasons, three to each sekki (本朝七十二候).
Each entry: (ordinal, kanji, reading, date range, one-line gloss)."""

KO_JA = {
"risshun": [
 ("初候", "東風解凍", "はるかぜ こおりを とく", "2/4–2/8頃", "春の東風が、厚い氷を解かしはじめる。"),
 ("次候", "黄鶯睍睆", "うぐいす なく", "2/9–2/13頃", "山里に鶯の初音がひびく。"),
 ("末候", "魚上氷", "うお こおりを いずる", "2/14–2/18頃", "割れた氷の間から魚が跳ねる。"),
],
"usui": [
 ("初候", "土脉潤起", "つちのしょう うるおい おこる", "2/19–2/23頃", "雨に土がしめり、いのちが動きだす。"),
 ("次候", "霞始靆", "かすみ はじめて たなびく", "2/24–2/28頃", "遠くの山に霞がたなびきはじめる。"),
 ("末候", "草木萌動", "そうもく めばえ いずる", "3/1–3/5頃", "草木がいっせいに芽を吹く。"),
],
"keichitsu": [
 ("初候", "蟄虫啓戸", "すごもりむし とを ひらく", "3/6–3/10頃", "土の中の虫が戸を開けて出てくる。"),
 ("次候", "桃始笑", "もも はじめて さく", "3/11–3/15頃", "桃のつぼみがほころぶ。「笑う」は咲くこと。"),
 ("末候", "菜虫化蝶", "なむし ちょうと なる", "3/16–3/20頃", "青虫が羽化して紋白蝶になる。"),
],
"shunbun": [
 ("初候", "雀始巣", "すずめ はじめて すくう", "3/21–3/25頃", "雀が巣づくりをはじめる。"),
 ("次候", "桜始開", "さくら はじめて ひらく", "3/26–3/30頃", "桜がほころびはじめる。"),
 ("末候", "雷乃発声", "かみなり すなわち こえを はっす", "3/31–4/4頃", "春の雷が遠くで鳴りはじめる。"),
],
"seimei": [
 ("初候", "玄鳥至", "つばめ きたる", "4/5–4/9頃", "南から燕が帰ってくる。"),
 ("次候", "鴻雁北", "こうがん かえる", "4/10–4/14頃", "雁が北へ帰っていく。"),
 ("末候", "虹始見", "にじ はじめて あらわる", "4/15–4/19頃", "雨上がりに虹が見えはじめる。"),
],
"kokuu": [
 ("初候", "葭始生", "あし はじめて しょうず", "4/20–4/24頃", "水辺に葦の若芽が伸びる。"),
 ("次候", "霜止出苗", "しも やんで なえ いずる", "4/25–4/29頃", "霜が終わり、苗代の苗が育つ。"),
 ("末候", "牡丹華", "ぼたん はなさく", "4/30–5/4頃", "牡丹が大輪の花をひらく。"),
],
"rikka": [
 ("初候", "蛙始鳴", "かわず はじめて なく", "5/5–5/9頃", "田に蛙の声が満ちる。"),
 ("次候", "蚯蚓出", "みみず いずる", "5/10–5/14頃", "蚯蚓が土から顔を出す。"),
 ("末候", "竹笋生", "たけのこ しょうず", "5/15–5/20頃", "筍が地面を割って伸びる。"),
],
"shoman": [
 ("初候", "蚕起食桑", "かいこ おきて くわを はむ", "5/21–5/25頃", "蚕が桑の葉を盛んに食べはじめる。"),
 ("次候", "紅花栄", "べにばな さかう", "5/26–5/30頃", "紅花が一面に咲きそろう。"),
 ("末候", "麦秋至", "むぎのとき いたる", "5/31–6/5頃", "麦が黄金に熟す「麦の秋」。"),
],
"boshu": [
 ("初候", "螳螂生", "かまきり しょうず", "6/6–6/10頃", "蟷螂が卵からかえる。"),
 ("次候", "腐草為蛍", "くされたるくさ ほたると なる", "6/11–6/15頃", "朽ちた草が蛍になる、と信じられた頃。"),
 ("末候", "梅子黄", "うめのみ きばむ", "6/16–6/20頃", "梅の実が黄色く熟す。梅雨の語源とも。"),
],
"geshi": [
 ("初候", "乃東枯", "なつかれくさ かるる", "6/21–6/26頃", "靫草(うつぼぐさ)だけが夏に枯れる。"),
 ("次候", "菖蒲華", "あやめ はなさく", "6/27–7/1頃", "あやめが花をひらく。"),
 ("末候", "半夏生", "はんげ しょうず", "7/2–7/6頃", "半夏が生え、田植えを終える目安。"),
],
"shosho_s": [
 ("初候", "温風至", "あつかぜ いたる", "7/7–7/11頃", "熱を含んだ風が吹きはじめる。"),
 ("次候", "蓮始開", "はす はじめて ひらく", "7/12–7/16頃", "蓮が夜明けに花をひらく。"),
 ("末候", "鷹乃学習", "たか すなわち わざを ならう", "7/17–7/22頃", "鷹の幼鳥が飛ぶことを覚える。"),
],
"taisho": [
 ("初候", "桐始結花", "きり はじめて はなを むすぶ", "7/23–7/28頃", "桐が来年の花芽を結ぶ。"),
 ("次候", "土潤溽暑", "つち うるおうて むしあつし", "7/29–8/2頃", "土が湿り、蒸し暑さが極まる。"),
 ("末候", "大雨時行", "たいう ときどきに ふる", "8/3–8/7頃", "夕立が時おり激しく降る。"),
],
"risshu": [
 ("初候", "涼風至", "すずかぜ いたる", "8/8–8/12頃", "風の中に、かすかな涼しさが混じる。"),
 ("次候", "寒蝉鳴", "ひぐらし なく", "8/13–8/17頃", "蜩が朝夕に鳴く。"),
 ("末候", "蒙霧升降", "ふかききり まとう", "8/18–8/22頃", "深い霧が立ちこめる。"),
],
"shosho_a": [
 ("初候", "綿柎開", "わたのはなしべ ひらく", "8/23–8/27頃", "綿を包む萼(がく)がひらく。"),
 ("次候", "天地始粛", "てんち はじめて さむし", "8/28–9/1頃", "暑さがようやく鎮まりはじめる。"),
 ("末候", "禾乃登", "こくもの すなわち みのる", "9/2–9/7頃", "稲が実り、穂を垂れる。"),
],
"hakuro": [
 ("初候", "草露白", "くさのつゆ しろし", "9/8–9/12頃", "草の露が白く光る。"),
 ("次候", "鶺鴒鳴", "せきれい なく", "9/13–9/17頃", "鶺鴒が鳴きはじめる。"),
 ("末候", "玄鳥去", "つばめ さる", "9/18–9/22頃", "燕が南へ帰っていく。"),
],
"shubun": [
 ("初候", "雷乃収声", "かみなり すなわち こえを おさむ", "9/23–9/27頃", "雷が鳴りやみ、空が澄む。"),
 ("次候", "蟄虫坏戸", "むし かくれて とを ふさぐ", "9/28–10/2頃", "虫が土に戸を閉ざす。"),
 ("末候", "水始涸", "みず はじめて かるる", "10/3–10/7頃", "田の水を落とし、稲刈りにそなえる。"),
],
"kanro": [
 ("初候", "鴻雁来", "こうがん きたる", "10/8–10/12頃", "雁が北から渡ってくる。"),
 ("次候", "菊花開", "きくのはな ひらく", "10/13–10/17頃", "菊が咲きそろう。重陽の名残。"),
 ("末候", "蟋蟀在戸", "きりぎりす とに あり", "10/18–10/22頃", "蟋蟀が戸口で鳴く。"),
],
"soko": [
 ("初候", "霜始降", "しも はじめて ふる", "10/23–10/27頃", "初霜が降りる。"),
 ("次候", "霎時施", "こさめ ときどき ふる", "10/28–11/1頃", "時雨がぱらぱらと通りすぎる。"),
 ("末候", "楓蔦黄", "もみじ つた きばむ", "11/2–11/6頃", "楓や蔦が色づく。"),
],
"ritto": [
 ("初候", "山茶始開", "つばき はじめて ひらく", "11/7–11/11頃", "山茶花が咲きはじめる。"),
 ("次候", "地始凍", "ち はじめて こおる", "11/12–11/16頃", "大地が凍りはじめる。"),
 ("末候", "金盞香", "きんせんか さく", "11/17–11/21頃", "水仙が香りはじめる。"),
],
"shosetsu": [
 ("初候", "虹蔵不見", "にじ かくれて みえず", "11/22–11/26頃", "虹を見かけなくなる。"),
 ("次候", "朔風払葉", "きたかぜ このはを はらう", "11/27–12/1頃", "北風が木の葉を払い落とす。"),
 ("末候", "橘始黄", "たちばな はじめて きばむ", "12/2–12/6頃", "橘の実が黄色く色づく。"),
],
"taisetsu": [
 ("初候", "閉塞成冬", "そら さむく ふゆと なる", "12/7–12/11頃", "空が閉ざされ、真冬になる。"),
 ("次候", "熊蟄穴", "くま あなに こもる", "12/12–12/16頃", "熊が穴にこもる。"),
 ("末候", "鱖魚群", "さけのうお むらがる", "12/17–12/21頃", "鮭が群れて川をのぼる。"),
],
"toji": [
 ("初候", "乃東生", "なつかれくさ しょうず", "12/22–12/26頃", "靫草だけが芽を出す。"),
 ("次候", "麋角解", "さわしかの つの おつる", "12/27–12/31頃", "大鹿の角が落ちる。"),
 ("末候", "雪下出麦", "ゆきわたりて むぎ いずる", "1/1–1/5頃", "雪の下で麦が芽を出す。"),
],
"shokan": [
 ("初候", "芹乃栄", "せり すなわち さかう", "1/6–1/10頃", "芹が盛んに育つ。七草の頃。"),
 ("次候", "水泉動", "しみず あたたかを ふくむ", "1/11–1/15頃", "凍った泉が動きはじめる。"),
 ("末候", "雉始雊", "きじ はじめて なく", "1/16–1/19頃", "雉の雄が鳴きはじめる。"),
],
"daikan": [
 ("初候", "款冬華", "ふきのはな さく", "1/20–1/24頃", "蕗の薹が顔を出す。"),
 ("次候", "水沢腹堅", "さわみず こおりつめる", "1/25–1/29頃", "沢の水が厚く凍りつめる。"),
 ("末候", "鶏始乳", "にわとり はじめて とやにつく", "1/30–2/3頃", "鶏が春を感じて卵を産みはじめる。"),
],
}

KO_EN = {
"risshun": [
 ("1st", "東風解凍", "Harukaze kōri o toku", "Feb 4–8", "The east wind begins to melt the thick ice."),
 ("2nd", "黄鶯睍睆", "Uguisu naku", "Feb 9–13", "The bush warbler's first song sounds in the hills."),
 ("3rd", "魚上氷", "Uo kōri o izuru", "Feb 14–18", "Fish leap through cracks in the ice."),
],
"usui": [
 ("1st", "土脉潤起", "Tsuchi no shō uruoi okoru", "Feb 19–23", "Rain softens the earth and life begins to stir."),
 ("2nd", "霞始靆", "Kasumi hajimete tanabiku", "Feb 24–28", "Mist begins to trail across the far hills."),
 ("3rd", "草木萌動", "Sōmoku mebae izuru", "Mar 1–5", "Grass and trees put out their first shoots."),
],
"keichitsu": [
 ("1st", "蟄虫啓戸", "Sugomori mushi to o hiraku", "Mar 6–10", "Insects open their doors and leave the soil."),
 ("2nd", "桃始笑", "Momo hajimete saku", "Mar 11–15", "Peach buds open — the old word for it is “laugh.”"),
 ("3rd", "菜虫化蝶", "Namushi chō to naru", "Mar 16–20", "Caterpillars become cabbage-white butterflies."),
],
"shunbun": [
 ("1st", "雀始巣", "Suzume hajimete sukuu", "Mar 21–25", "Sparrows begin to build their nests."),
 ("2nd", "桜始開", "Sakura hajimete hiraku", "Mar 26–30", "The cherry blossom begins to open."),
 ("3rd", "雷乃発声", "Kaminari sunawachi koe o hassu", "Mar 31–Apr 4", "Distant spring thunder is heard."),
],
"seimei": [
 ("1st", "玄鳥至", "Tsubame kitaru", "Apr 5–9", "Swallows return from the south."),
 ("2nd", "鴻雁北", "Kōgan kaeru", "Apr 10–14", "Wild geese fly north again."),
 ("3rd", "虹始見", "Niji hajimete arawaru", "Apr 15–19", "Rainbows begin to appear after rain."),
],
"kokuu": [
 ("1st", "葭始生", "Ashi hajimete shōzu", "Apr 20–24", "Reeds send up shoots at the water's edge."),
 ("2nd", "霜止出苗", "Shimo yande nae izuru", "Apr 25–29", "Frost ends and rice seedlings grow."),
 ("3rd", "牡丹華", "Botan hana saku", "Apr 30–May 4", "Peonies open their great blooms."),
],
"rikka": [
 ("1st", "蛙始鳴", "Kawazu hajimete naku", "May 5–9", "Frogs begin to call across the paddies."),
 ("2nd", "蚯蚓出", "Mimizu izuru", "May 10–14", "Earthworms surface from the soil."),
 ("3rd", "竹笋生", "Takenoko shōzu", "May 15–20", "Bamboo shoots break through the ground."),
],
"shoman": [
 ("1st", "蚕起食桑", "Kaiko okite kuwa o hamu", "May 21–25", "Silkworms wake and feed hungrily on mulberry."),
 ("2nd", "紅花栄", "Benibana sakau", "May 26–30", "Safflower blooms across the fields."),
 ("3rd", "麦秋至", "Mugi no toki itaru", "May 31–Jun 5", "Barley ripens gold — “the barley autumn.”"),
],
"boshu": [
 ("1st", "螳螂生", "Kamakiri shōzu", "Jun 6–10", "Mantises hatch from their egg cases."),
 ("2nd", "腐草為蛍", "Kusaretaru kusa hotaru to naru", "Jun 11–15", "Rotting grass was once believed to turn into fireflies."),
 ("3rd", "梅子黄", "Ume no mi kibamu", "Jun 16–20", "Plums ripen yellow — said to name the plum rains."),
],
"geshi": [
 ("1st", "乃東枯", "Natsu-karekusa karuru", "Jun 21–26", "Self-heal alone withers in the heat of summer."),
 ("2nd", "菖蒲華", "Ayame hana saku", "Jun 27–Jul 1", "Irises come into flower."),
 ("3rd", "半夏生", "Hange shōzu", "Jul 2–6", "Crow-dipper sprouts — the mark for finishing the planting."),
],
"shosho_s": [
 ("1st", "温風至", "Atsukaze itaru", "Jul 7–11", "The wind begins to carry heat."),
 ("2nd", "蓮始開", "Hasu hajimete hiraku", "Jul 12–16", "Lotus flowers open at daybreak."),
 ("3rd", "鷹乃学習", "Taka sunawachi waza o narau", "Jul 17–22", "Young hawks learn to fly."),
],
"taisho": [
 ("1st", "桐始結花", "Kiri hajimete hana o musubu", "Jul 23–28", "Paulownia sets next year's flower buds."),
 ("2nd", "土潤溽暑", "Tsuchi uruōte mushiatsushi", "Jul 29–Aug 2", "The ground is damp and the air at its most humid."),
 ("3rd", "大雨時行", "Taiu tokidoki ni furu", "Aug 3–7", "Heavy showers fall from time to time."),
],
"risshu": [
 ("1st", "涼風至", "Suzukaze itaru", "Aug 8–12", "A faint coolness enters the wind."),
 ("2nd", "寒蝉鳴", "Higurashi naku", "Aug 13–17", "Evening cicadas call at dawn and dusk."),
 ("3rd", "蒙霧升降", "Fukaki kiri matou", "Aug 18–22", "Thick mists rise and settle."),
],
"shosho_a": [
 ("1st", "綿柎開", "Wata no hanashibe hiraku", "Aug 23–27", "The calyx sheathing the cotton boll opens."),
 ("2nd", "天地始粛", "Tenchi hajimete samushi", "Aug 28–Sep 1", "Heaven and earth begin at last to cool."),
 ("3rd", "禾乃登", "Kokumono sunawachi minoru", "Sep 2–7", "The rice ripens and the ears bow down."),
],
"hakuro": [
 ("1st", "草露白", "Kusa no tsuyu shiroshi", "Sep 8–12", "Dew on the grass glitters white."),
 ("2nd", "鶺鴒鳴", "Sekirei naku", "Sep 13–17", "Wagtails begin to call."),
 ("3rd", "玄鳥去", "Tsubame saru", "Sep 18–22", "The swallows depart for the south."),
],
"shubun": [
 ("1st", "雷乃収声", "Kaminari sunawachi koe o osamu", "Sep 23–27", "Thunder falls silent and the sky clears."),
 ("2nd", "蟄虫坏戸", "Mushi kakurete to o fusagu", "Sep 28–Oct 2", "Insects shut their doors in the earth."),
 ("3rd", "水始涸", "Mizu hajimete karuru", "Oct 3–7", "The paddies are drained ready for harvest."),
],
"kanro": [
 ("1st", "鴻雁来", "Kōgan kitaru", "Oct 8–12", "Wild geese arrive from the north."),
 ("2nd", "菊花開", "Kiku no hana hiraku", "Oct 13–17", "Chrysanthemums come into bloom."),
 ("3rd", "蟋蟀在戸", "Kirigirisu to ni ari", "Oct 18–22", "Crickets sing at the doorway."),
],
"soko": [
 ("1st", "霜始降", "Shimo hajimete furu", "Oct 23–27", "The first frost falls."),
 ("2nd", "霎時施", "Kosame tokidoki furu", "Oct 28–Nov 1", "Brief showers pass through."),
 ("3rd", "楓蔦黄", "Momiji tsuta kibamu", "Nov 2–6", "Maple and ivy turn colour."),
],
"ritto": [
 ("1st", "山茶始開", "Tsubaki hajimete hiraku", "Nov 7–11", "The sasanqua camellia begins to flower."),
 ("2nd", "地始凍", "Chi hajimete kōru", "Nov 12–16", "The ground begins to freeze."),
 ("3rd", "金盞香", "Kinsenka saku", "Nov 17–21", "Narcissus releases its scent."),
],
"shosetsu": [
 ("1st", "虹蔵不見", "Niji kakurete miezu", "Nov 22–26", "Rainbows hide and are seen no more."),
 ("2nd", "朔風払葉", "Kitakaze konoha o harau", "Nov 27–Dec 1", "The north wind strips the leaves away."),
 ("3rd", "橘始黄", "Tachibana hajimete kibamu", "Dec 2–6", "Mandarin fruit turns yellow."),
],
"taisetsu": [
 ("1st", "閉塞成冬", "Sora samuku fuyu to naru", "Dec 7–11", "The sky closes over and true winter sets in."),
 ("2nd", "熊蟄穴", "Kuma ana ni komoru", "Dec 12–16", "Bears withdraw into their dens."),
 ("3rd", "鱖魚群", "Sake no uo muragaru", "Dec 17–21", "Salmon gather and run up the rivers."),
],
"toji": [
 ("1st", "乃東生", "Natsu-karekusa shōzu", "Dec 22–26", "Self-heal alone puts out its shoots."),
 ("2nd", "麋角解", "Sawashika no tsuno otsuru", "Dec 27–31", "The great deer shed their antlers."),
 ("3rd", "雪下出麦", "Yuki watarite mugi izuru", "Jan 1–5", "Barley sprouts beneath the snow."),
],
"shokan": [
 ("1st", "芹乃栄", "Seri sunawachi sakau", "Jan 6–10", "Water dropwort flourishes — the seven-herb season."),
 ("2nd", "水泉動", "Shimizu atataka o fukumu", "Jan 11–15", "Frozen springs begin to move again."),
 ("3rd", "雉始雊", "Kiji hajimete naku", "Jan 16–19", "The cock pheasant begins to call."),
],
"daikan": [
 ("1st", "款冬華", "Fuki no hana saku", "Jan 20–24", "Butterbur buds push up through the cold."),
 ("2nd", "水沢腹堅", "Sawamizu kōri tsumeru", "Jan 25–29", "Mountain streams freeze thick and hard."),
 ("3rd", "鶏始乳", "Niwatori hajimete toya ni tsuku", "Jan 30–Feb 3", "Hens sense the spring and begin to lay."),
],
}
