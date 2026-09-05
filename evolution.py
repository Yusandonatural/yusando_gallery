# -*- coding: utf-8 -*-
"""Content for the article 茶道具の進化 / The Evolution of Tea Utensils."""

# ---- three turning points: (title, era, body, tip) --------------------------
TURNS_JA = [
 ("唐物荘厳", "室町 — 14〜15世紀",
  "舶来品こそ最高格だった時代。足利将軍家の書院には、天目茶碗・青磁の花入・唐銅の建水が金襴の卓に飾られました。道具には明確な序列があり、何を持っているかがそのまま主人の格を語りました。",
  "唐物=中国から渡来した道具。今も最高の格式とされます。"),
 ("見立ての発見", "侘び茶の成立 — 15〜16世紀",
  "村田珠光・武野紹鴎が、朝鮮の日用の飯茶碗や信楽の種壺に美を見いだします。道具は「作られるもの」から「選ばれるもの」へ。利休が小田原の陣中で竹を切って花入にした逸話が、この転換を象徴しています。",
  "見立て=日用品を茶道具として選び直すこと。"),
 ("和物の創造", "桃山 — 16世紀",
  "見いだすだけでなく、茶人が寸法や姿を指定して作らせる時代へ。長次郎の楽茶碗、辻与次郎の釜、歪みを愛でた織部の沓茶碗。日本独自の茶陶が、ここでいっせいに生まれました。",
  "「利休好み」「織部好み」——茶人の名が、そのまま様式になりました。"),
]

TURNS_EN = [
 ("Chinese Splendour", "Muromachi — 14th–15th c.",
  "An age when imported wares held the highest rank. In the Ashikaga shoguns' study rooms, tenmoku bowls, celadon flower vessels and bronze waste bowls stood on brocaded stands. Utensils had a strict order of precedence, and what you owned announced who you were.",
  "Karamono = utensils brought from China. Still the highest formal rank."),
 ("The Discovery of Mitate", "Wabi tea takes shape — 15th–16th c.",
  "Murata Jukō and Takeno Jōō found beauty in Korean everyday rice bowls and Shigaraki seed jars. A utensil was no longer only something made — it could be something chosen. Rikyū cutting a length of bamboo at the Odawara camp to serve as a flower vessel is the emblem of this shift.",
  "Mitate = the eye that re-selects an ordinary object as a tea utensil."),
 ("Japanese Wares Created", "Momoyama — 16th c.",
  "Beyond finding, tea masters now commissioned: they specified the size, the stance, the feel. Chōjirō's hand-built Raku bowls, Tsuji Yojirō's kettles, Oribe's deliberately warped shoe-shaped bowls. Japan's own tea ceramics were born all at once.",
  "“Rikyū’s taste,” “Oribe’s taste” — a master's name became a style."),
]

# ---- lineages: slug, name, en, [(era, name, note) x3] -----------------------
EVO_JA = [
 ("chawan", "茶碗", "Chawan", [
   ("室町", "唐物天目", "中国建窯の黒釉碗。天目台にのせて飾る、最高格の器でした。"),
   ("侘び茶", "高麗茶碗", "朝鮮の日常の飯茶碗を見立てた井戸・粉引。歪みや土見せを「景色」と呼びはじめます。"),
   ("桃山〜", "楽・志野・織部", "利休の求めに長次郎が手捏ねで応えた楽茶碗。以後、和物茶碗が各地の窯で焼かれます。"),
 ]),
 ("chaire", "茶入・棗", "Chaire & Natsume", [
   ("室町", "唐物茶入", "中国製の小壺。「一国に値する」とまで言われた、名物中の名物。"),
   ("桃山", "和物茶入", "瀬戸で唐物を写して焼かれ、茶入の国産化が始まります。"),
   ("室町後期〜", "棗", "薄茶が広まると、木地に漆を重ねた軽い棗が登場。日本生まれの茶器です。"),
 ]),
 ("hanaire", "花入", "Hanaire", [
   ("室町", "唐銅・青磁", "舶来の金属器と青磁。床に据える「真」の格。"),
   ("桃山", "竹", "利休が小田原の陣中で切った「園城寺」。ただの竹が、最高の花入になりました。"),
   ("桃山〜", "籠・伊賀・信楽", "「草」の格として、素朴な籠や国焼が定着します。"),
 ]),
 ("kama", "茶釜", "Kama", [
   ("南北朝〜室町", "芦屋・天明", "筑前芦屋の優美な文様、下野天明の荒い肌。二大産地が並び立ちます。"),
   ("桃山", "京釜", "三条釜座の釜師が台頭。辻与次郎が「利休好み」の侘びた釜を確立しました。"),
   ("江戸〜", "釜師の家", "大西家をはじめ釜師の家が続き、好みに応じて誂えられるようになります。"),
 ]),
 ("chashaku", "茶杓", "Chashaku", [
   ("伝来", "象牙の茶匙", "もとは中国の薬匙。象牙や塗りの匙が用いられていました。"),
   ("紹鴎・利休", "竹の茶杓", "侘び茶の中で竹に置き換わり、節の位置で格が分かれる形が定まります。"),
   ("桃山〜", "銘と共筒", "茶人自らが削り、銘を付け、筒に書き付ける。小さな竹片が一席の主題を語る道具に。"),
 ]),
 ("mizusashi", "水指", "Mizusashi", [
   ("室町", "唐物青磁・染付", "舶来の磁器。格の高い「真」の水指です。"),
   ("侘び茶", "見立ての壺", "信楽の種壺、備前の芋頭。台所道具や農具からの転用が正式な道具に昇格しました。"),
   ("江戸〜", "木地曲・硝子", "曲物の清らかさ、夏の硝子。素材の幅がもっとも広い道具になります。"),
 ]),
]

EVO_EN = [
 ("chawan", "Chawan", "Tea Bowl", [
   ("Muromachi", "Karamono tenmoku", "Black-glazed bowls from China's Jian kilns, displayed on a lacquered stand — the highest rank."),
   ("Wabi tea", "Kōrai bowls", "Korean everyday rice bowls, re-seen as tea bowls. Warping and bare clay start being called “landscape.”"),
   ("Momoyama on", "Raku, Shino, Oribe", "Chōjirō answered Rikyū by building bowls entirely by hand. Japanese kilns follow everywhere after."),
 ]),
 ("chaire", "Chaire & Natsume", "Tea Caddies", [
   ("Muromachi", "Karamono chaire", "Small Chinese jars, said to be worth a province — the most famous of all famous objects."),
   ("Momoyama", "Japanese chaire", "Seto potters copy the Chinese forms, and the caddy begins to be made at home."),
   ("Late Muromachi on", "Natsume", "As thin tea spread, the light lacquered natsume appeared — a wholly Japanese invention."),
 ]),
 ("hanaire", "Hanaire", "Flower Vessel", [
   ("Muromachi", "Bronze & celadon", "Imported metalwork and celadon: the formal “shin” rank for the alcove."),
   ("Momoyama", "Bamboo", "Rikyū cut “Onjōji” at the Odawara camp. Plain bamboo became the finest of flower vessels."),
   ("Momoyama on", "Baskets, Iga, Shigaraki", "Rustic baskets and domestic wares settle in as the informal “sō” rank."),
 ]),
 ("kama", "Kama", "Iron Kettle", [
   ("14th–15th c.", "Ashiya & Tenmyō", "Chikuzen's elegant relief designs beside Shimotsuke's rugged skin — the two great centres."),
   ("Momoyama", "Kyoto kettles", "The casters of Sanjō Kamanza rise; Tsuji Yojirō defines the wabi kettle of Rikyū's taste."),
   ("Edo on", "Kettle-making houses", "Families such as the Ōnishi carry the craft on, making kettles to a patron's taste."),
 ]),
 ("chashaku", "Chashaku", "Tea Scoop", [
   ("Imported", "Ivory spoon", "It began as a Chinese medicine spoon, in ivory or lacquer."),
   ("Jōō & Rikyū", "Bamboo scoop", "Wabi tea remade it in bamboo, and the node's position settled into a hierarchy of rank."),
   ("Momoyama on", "Name & tube", "Masters carve their own, name them, inscribe the tube — a sliver of bamboo becomes the theme of a gathering."),
 ]),
 ("mizusashi", "Mizusashi", "Water Jar", [
   ("Muromachi", "Celadon & blue-and-white", "Imported porcelain: the formal water jar."),
   ("Wabi tea", "Jars by mitate", "Shigaraki seed jars, Bizen pots. Kitchen and farm vessels are promoted to formal utensils."),
   ("Edo on", "Bentwood & glass", "The clean pallor of bentwood, the coolness of summer glass — the widest range of any utensil."),
 ]),
]

# ---- the three forces: (name, en, body) -------------------------------------
FORCES_JA = [
 ("見立て", "MITATE — choosing",
  "選ぶことが、創ること。日用の器を茶席に持ち込む眼が、道具の範囲を広げ続けました。いまも「これは水指に使えそうだ」と思った瞬間に、この五百年の作法をなぞっていることになります。"),
 ("好み", "KONOMI — commissioning",
  "茶人が寸法や意匠を指定して作らせること。「利休好み」「遠州好み」「宗旦好み」は、今も道具を注文するときの生きた言葉です。様式に人の名が残る、めずらしい世界でもあります。"),
 ("写し", "UTSUSHI — copying",
  "名物を写して作ること。オリジナルへの敬意であり、失われやすい様式を後世へ伝える手段でもありました。中古市場で「〜写」と記された品は、この系譜に連なるものです。"),
]

FORCES_EN = [
 ("Mitate", "見立て — choosing",
  "To choose is to create. The eye that carries an everyday vessel into the tea room kept widening what a utensil could be. Even now, the moment you think “that would make a good water jar,” you are repeating a five-hundred-year-old gesture."),
 ("Konomi", "好み — commissioning",
  "A master specifies the size and the design and has it made. “Rikyū’s taste,” “Enshū’s taste,” “Sōtan’s taste” are still live phrases when ordering a utensil today — a rare world where styles keep their author's name."),
 ("Utsushi", "写し — copying",
  "Making a piece after a famous original: an act of respect, and the means by which fragile styles were carried forward. A piece marked “after —” in today's market belongs to this lineage."),
]

CLOSING_JA = '''
  <p>明治の廃仏毀釈と大名家の没落によって、蔵にあった名物が市場に流れ出しました。それを受け止めたのが益田鈍翁ら近代の数寄者で、多くは戦後に美術館へ収まっています。もう二度と手に入らない道具です。</p>
  <p>いっぽうで、稽古のための道具は明治以降に大量に作られました。だからいま中古市場には、かつて一国一城に値するとされた種類の道具が、数千円から並んでいます。名物ではないけれど、同じ系譜の末に生まれた器です。</p>
  <p>そして進化は、まだ続いています。硝子の茶碗、現代作家の茶杓、電熱の炉。あなたが選ぶ一点も、この五百年の続きの上にあります。<a href="../tools.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">道具一覧</a>から、気になるものを探してみてください。</p>
'''

CLOSING_EN = '''
  <p>The Meiji dissolution of temple treasuries and the fall of the daimyō houses pushed famous utensils onto the market. Modern connoisseurs such as Masuda Donō caught them, and most now rest in museums. They will not come round again.</p>
  <p>At the same time, utensils for practice were made in great quantity from Meiji onward. So today's secondhand market carries, from a few thousand yen, the same kinds of objects once said to be worth a province and a castle. Not famous pieces — but born at the end of the same lineage.</p>
  <p>And the evolution has not stopped: glass bowls, scoops by living carvers, electric hearths. Whatever single piece you choose sits on top of these five hundred years. Start from the <a href="../tools.html" style="color:var(--matcha);border-bottom:1px solid rgba(74,93,58,.3)">utensils list</a>.</p>
'''
