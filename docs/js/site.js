// 悠三堂古美術ギャラリー site script
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

// ---- 在庫連携 (Yusando Gallery Worker API) --------------------------------
// 各道具詳細ページの <div class="shop-stub" data-ec-category="chawan"> が受け皿。
// Worker が返す JSON をそのまま並べます。認証不要・公開分のみ。
window.CHADOGU_EC = {
  enabled: true,
  endpoint: "https://yusando-gallery.isozaki-f67.workers.dev",
  // ポータルのスラッグ → API の種別(固定16種)。無いものは在庫枠を出しません。
  categories: {
    chawan: "茶碗", chaire: "茶入", natsume: "棗", mizusashi: "水指",
    kensui: "建水", futaoki: "蓋置", chashaku: "茶杓", hanaire: "花入",
    kogo: "香合", kama: "釜・風炉", furo: "釜・風炉", kashiki: "菓子器",
    kakemono: "掛物"
  },
  // 二十四節気の英語表記(英語ページのチップ用)
  sekkiEn: {"立春":"Risshun","雨水":"Usui","啓蟄":"Keichitsu","春分":"Shunbun","清明":"Seimei","穀雨":"Kokuu","立夏":"Rikka","小満":"Shōman","芒種":"Bōshu","夏至":"Geshi","小暑":"Shōsho","大暑":"Taisho","立秋":"Risshū","処暑":"Shosho","白露":"Hakuro","秋分":"Shūbun","寒露":"Kanro","霜降":"Sōkō","立冬":"Rittō","小雪":"Shōsetsu","大雪":"Taisetsu","冬至":"Tōji","小寒":"Shōkan","大寒":"Daikan"}
};

(function () {
  var EC = window.CHADOGU_EC;
  var stub = document.querySelector('.shop-stub[data-ec-category]');
  if (!stub || !EC.enabled) return;

  var cat = EC.categories[stub.getAttribute('data-ec-category')];
  if (!cat) return;                                   // 取扱いのない種別

  var root = stub.getAttribute('data-ec-root') || '';
  var en = document.documentElement.lang === 'en';
  var T = en
    ? { head: 'In the Yusando Gallery', sold: 'SOLD', detail: 'View details',
        ask: 'Enquire', gone: 'No longer available',
        note: 'Each piece is one of a kind. Online ordering is not yet available.' }
    : { head: '悠三堂ギャラリーにある' + (stub.getAttribute('data-ec-name') || cat),
        sold: '売却済', detail: '詳しく見る',
        ask: 'お問い合わせください', gone: 'お渡し済み',
        note: 'すべて一点ものです。オンラインでの販売は行っておりません。' };

  var esc = function (v) {
    return String(v == null ? '' : v).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };

  // ?debug=1 を付けたときだけ、画面に理由を出す
  var DBG = /[?&]debug=/.test(location.search);
  var note = function (msg) {
    if (!DBG) return;
    var p = document.createElement('p');
    p.style.cssText = 'margin-top:14px;font-size:12px;color:#a53f2b';
    p.textContent = '[stock] ' + msg;
    stub.appendChild(p);
  };
  if (DBG) note('category=' + cat + ' / endpoint=' + EC.endpoint);

  fetch(EC.endpoint + '/api/items').then(function (r) {
    if (!r.ok) throw new Error(r.status);
    return r.json();
  }).then(function (all) {
    var items = (all || []).filter(function (i) {
      return i.category === cat && i.status !== 'hidden';
    });
    if (DBG) note('APIから ' + (all || []).length + ' 件、うち該当 ' + items.length + ' 件');
    if (!items.length) return 0;                      // 準備中の文面を残す

    var cards = items.map(function (i) {
      var sold = i.status === 'sold';
      var photo = (i.photos && i.photos[0])
        ? '<img loading="lazy" alt="' + esc(i.mei) + '" src="'
          + EC.endpoint + '/photos/' + esc(i.photos[0]) + '">'
        : '<span class="st-nophoto"></span>';

      // 英語ページでは英語の項目を優先し、無ければ日本語にもどる
      var pick = function (k) { return (en && i[k + '_en']) ? i[k + '_en'] : i[k]; };

      // sekki は配列でもJSON文字列でも受ける(D1のTEXT列のため)
      var sk = i.sekki;
      if (typeof sk === 'string') {
        try { sk = JSON.parse(sk); } catch (e) { sk = sk.split(/[,・]/); }
      }
      var sekki = (Array.isArray(sk) && sk.length)
        ? '<p class="st-sekki">' + sk.slice(0, 3).map(function (v) {
            return '<span>' + esc(en ? (EC.sekkiEn[v] || v) : v) + '</span>'; }).join('')
          + '</p>' : '';

      // 産地・時代は分かっているものだけ、中黒でつなぐ
      var facts = [pick('kiln'), pick('era')].filter(function (v) {
        return v && !/^(不詳|不明|unknown)$/i.test(String(v).trim()); });
      var meta = facts.length
        ? '<p class="st-meta">' + facts.map(esc).join(en ? ' · ' : ' ・ ') + '</p>' : '';

      return '<a class="stock-card' + (sold ? ' sold' : '') + '" href="'
        + root + 'item.html?id=' + encodeURIComponent(i.id) + '">'
        + '<span class="st-frame">' + photo
        + (sold ? '<span class="st-badge">' + T.sold + '</span>' : '') + '</span>'
        + '<span class="st-body">'
        + '<span class="st-mei">'
        // 銘は訳さない。英語ページではローマ字を主に、漢字を添える
        + esc((en && i.mei_romaji) ? i.mei_romaji : (i.mei || (en ? 'Unnamed' : '無銘'))) + '</span>'
        + (function () {
            var sub = en ? i.mei : i.mei_yomi;
            return sub ? '<span class="st-yomi">' + esc(sub) + '</span>' : '';
          })()
        + meta + sekki
        + '<span class="st-price">' + esc(sold ? T.gone : T.ask) + '</span>'
        + '</span></a>';
    }).join('');

    stub.classList.add('has-stock');
    stub.innerHTML = '<h3>' + esc(T.head) + '</h3>'
      + '<div class="stock-grid">' + cards + '</div>'
      + '<p class="st-note">' + esc(T.note) + '</p>';
    return items.length;
  }).then(function (n) {
    if (DBG) note('在庫 ' + n + ' 件を表示しました (' + cat + ')');
  }).catch(function (e) {
    // 取得できないときは「準備中」のまま残す。?debug=1 で理由を表示。
    console.warn('[stock] 在庫を取得できませんでした:', e);
    note('在庫を取得できませんでした: ' + (e && e.message ? e.message : e));
  });
})();
