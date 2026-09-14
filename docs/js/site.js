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
  catEn: {"茶碗":"Chawan","茶入":"Chaire","棗":"Natsume","水指":"Mizusashi",
    "建水":"Kensui","蓋置":"Futaoki","茶杓":"Chashaku","花入":"Hanaire","香合":"Kōgō",
    "釜・風炉":"Kama / Furo","急須・宝瓶":"Kyūsu / Hōhin","湯冷まし":"Yuzamashi",
    "湯呑・茶托":"Yunomi / Chataku","菓子器":"Kashiki","掛物":"Kakemono","その他":"Other"},
  sekkiEn: {"立春":"Risshun","雨水":"Usui","啓蟄":"Keichitsu","春分":"Shunbun","清明":"Seimei","穀雨":"Kokuu","立夏":"Rikka","小満":"Shōman","芒種":"Bōshu","夏至":"Geshi","小暑":"Shōsho","大暑":"Taisho","立秋":"Risshū","処暑":"Shosho","白露":"Hakuro","秋分":"Shūbun","寒露":"Kanro","霜降":"Sōkō","立冬":"Rittō","小雪":"Shōsetsu","大雪":"Taisetsu","冬至":"Tōji","小寒":"Shōkan","大寒":"Daikan"}
};

(function () {
  var EC = window.CHADOGU_EC;
  var stub = document.querySelector('.shop-stub[data-ec-category]');
  if (!stub || !EC.enabled) return;

  var cat = EC.categories[stub.getAttribute('data-ec-category')];
  if (!cat) return;                                   // 取扱いのない種別

  var root = stub.getAttribute('data-ec-root') || '';
  // ページの言語で文言を選ぶ。仏語・繁体字の道具詳細にも在庫枠があるので、
  // 英語以外をすべて日本語に倒すと、そこだけ日本語が出てしまう。
  var lang = document.documentElement.lang || 'ja';
  var en = lang === 'en';
  var name = stub.getAttribute('data-ec-name') || cat;
  var STR = {
    ja: { head: '悠三堂ギャラリーにある' + name, sold: '売却済', detail: '詳しく見る',
          ask: 'お問い合わせください', gone: 'お渡し済み',
          note: 'すべて一点ものです。オンラインでの販売は行っておりません。',
          disc: '銘は当店による創作で、伝来の銘ではございません。'
              + '説明にも推測で記した事項が含まれます。' },
    en: { head: 'In the Yusando Gallery', sold: 'SOLD', detail: 'View details',
          ask: 'Enquire', gone: 'No longer available',
          note: 'Each piece is one of a kind. Online ordering is not yet available.',
          disc: 'The names we give are our own, not inherited ones, and our notes '
              + 'include informed judgements rather than established fact.' },
    fr: { head: 'À la galerie Yusando', sold: 'VENDU', detail: 'Voir la fiche',
          ask: 'Nous écrire', gone: 'Plus disponible',
          note: 'Chaque pièce est unique. La vente en ligne n’est pas encore ouverte.',
          disc: 'Les noms que nous donnons sont les nôtres, non des noms transmis, '
              + 'et nos notes comportent des jugements plutôt que des faits établis.' },
    'zh-Hant': { head: '悠三堂藝廊所藏', sold: '已售出', detail: '查看詳情',
          ask: '歡迎詢問', gone: '已交付',
          note: '每件皆為一點物。目前尚未開放線上販售。',
          disc: '各器物的銘由本店所取，並非傳世之銘；說明中亦含推測的部分。' }
  };
  var T = STR[lang] || STR.ja;

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
      + '<p class="st-note">' + esc(T.note) + '</p>'
      + '<p class="st-disc">' + esc(T.disc) + '</p>';
    return items.length;
  }).then(function (n) {
    if (DBG) note('在庫 ' + n + ' 件を表示しました (' + cat + ')');
  }).catch(function (e) {
    // 取得できないときは「準備中」のまま残す。?debug=1 で理由を表示。
    console.warn('[stock] 在庫を取得できませんでした:', e);
    note('在庫を取得できませんでした: ' + (e && e.message ? e.message : e));
  });
})();

// ---- 新入荷カルーセル ------------------------------------------------------
// トップの「準備中」の枠に、登録したばかりの道具を横並びで出す。
// 在庫が0件のとき・取得できないときは、準備中の文面に戻す（空の棚を見せない）。
(function () {
  var slot = document.querySelector('[data-arrivals] .ar-slot');
  if (!slot) return;
  var sec = slot.closest('[data-arrivals]');
  var root = sec.getAttribute('data-ec-root') || '';
  var lang = document.documentElement.lang || 'ja';
  var en = lang === 'en';
  var MAX = 12;

  var S = {
    ja: { all: 'すべての道具を見る', ask: 'お問い合わせください', gone: 'お渡し済み',
          none: 'ただいま準備中です。まもなくご案内します。',
          prev: '前へ', next: '次へ', unnamed: '無銘' },
    en: { all: 'See all pieces', ask: 'Please enquire', gone: 'No longer available',
          none: 'Pieces will appear here shortly.',
          prev: 'Previous', next: 'Next', unnamed: 'Unnamed' },
    fr: { all: 'Voir toutes les pièces', ask: 'Nous écrire', gone: 'Plus disponible',
          none: 'Les pièces paraîtront ici sous peu.',
          prev: 'Précédent', next: 'Suivant', unnamed: 'Sans nom' },
    'zh-Hant': { all: '查看全部茶道具', ask: '歡迎詢問', gone: '已交付',
          none: '目前準備中，近期將為您呈上。',
          prev: '上一個', next: '下一個', unnamed: '無銘' }
  };
  var T = S[lang] || S.ja;

  var esc = function (v) {
    return String(v == null ? '' : v).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };
  var quiet = function (msg) {
    slot.innerHTML = '<p class="ar-none">' + esc(msg) + '</p>';
  };

  var EP = (window.CHADOGU_EC && window.CHADOGU_EC.endpoint) || '';
  if (!EP) { quiet(T.none); return; }

  fetch(EP + '/api/items').then(function (r) {
    if (!r.ok) throw new Error(r.status);
    return r.json();
  }).then(function (all) {
    // API は新しい順に返す。売却済みも「こういうものが入ります」の見本になるので残す。
    var items = (all || []).filter(function (i) { return i.status !== 'hidden'; }).slice(0, MAX);
    if (!items.length) { quiet(T.none); return; }

    var cards = items.map(function (i) {
      var sold = i.status === 'sold';
      var photo = (i.photos && i.photos[0])
        ? '<img loading="lazy" alt="' + esc(i.mei) + '" src="'
          + EP + '/photos/' + esc(i.photos[0]) + '">'
        : '<span class="st-nophoto"></span>';
      // 種別は、漢字が読める言語（日本語・繁体字）はそのまま、
      // 読めない言語（英語・仏語）はローマ字表記に置き換える。
      var roman = lang === 'en' || lang === 'fr';
      var cat = i.category
        ? ((roman && window.CHADOGU_EC && CHADOGU_EC.catEn
            && CHADOGU_EC.catEn[i.category]) || i.category) : '';
      // 銘は訳さない。英語ページではローマ字を主に
      var mei = (en && i.mei_romaji) ? i.mei_romaji : (i.mei || T.unnamed);
      var sub = en ? i.mei : i.mei_romaji;
      return '<a class="ar-card' + (sold ? ' sold' : '') + '" href="'
        + root + 'item.html?id=' + encodeURIComponent(i.id) + '">'
        + '<span class="st-frame">' + photo
        + (sold ? '<span class="st-badge">' + esc(T.gone) + '</span>' : '') + '</span>'
        + '<span class="ar-body">'
        + (i.sku ? '<span class="ar-sku">' + esc(i.sku) + '</span>' : '')
        + '<span class="ar-mei">' + esc(mei) + '</span>'
        + (sub ? '<span class="ar-sub">' + esc(sub) + '</span>' : '')
        + (cat ? '<span class="ar-cat">' + esc(cat) + '</span>' : '')
        + '<span class="ar-ask">' + esc(sold ? T.gone : T.ask) + '</span>'
        + '</span></a>';
    }).join('');

    slot.innerHTML =
      '<div class="ar-wrap">'
      + '<button class="ar-nav prev" type="button" aria-label="' + esc(T.prev) + '"></button>'
      + '<div class="ar-track" tabindex="0">' + cards + '</div>'
      + '<button class="ar-nav next" type="button" aria-label="' + esc(T.next) + '"></button>'
      + '</div>'
      + '<p class="ar-more"><a href="' + root + 'stock.html">' + esc(T.all) + ' →</a></p>';

    var track = slot.querySelector('.ar-track');
    var prev = slot.querySelector('.ar-nav.prev');
    var next = slot.querySelector('.ar-nav.next');

    // 1カード分だけ送る。端では矢印を消す（押せるのに動かない状態を作らない）
    var step = function () {
      var c = track.querySelector('.ar-card');
      return c ? c.getBoundingClientRect().width + 18 : track.clientWidth * 0.8;
    };
    prev.addEventListener('click', function () {
      track.scrollBy({ left: -step(), behavior: 'smooth' });
    });
    next.addEventListener('click', function () {
      track.scrollBy({ left: step(), behavior: 'smooth' });
    });
    var sync = function () {
      var max = track.scrollWidth - track.clientWidth - 2;
      prev.hidden = track.scrollLeft <= 2;
      next.hidden = track.scrollLeft >= max;
    };
    track.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  }).catch(function (e) {
    console.warn('[arrivals] 新入荷を取得できませんでした:', e);
    quiet(T.none);
  });
})();


// ---- 抹茶／煎茶の切り替え（道具一覧） --------------------------------------
// 状態は <html data-tea>。URL の #sencha / #matcha が最優先、次に前回の選択、
// どちらも無ければ抹茶。#sencha という id は置かない（置くとそこへ跳ぶ）。
(function () {
  var sw = document.querySelector('.tea-sw');
  if (!sw) return;
  var html = document.documentElement, KEY = 'yusando_tea';
  function fromHash() {
    var h = (location.hash || '').replace('#', '');
    return h === 'sencha' || h === 'matcha' ? h : '';
  }
  function saved() { try { return localStorage.getItem(KEY) || ''; } catch (e) { return ''; } }
  function apply(pick, writeHash) {
    html.setAttribute('data-tea', pick);
    sw.querySelectorAll('[data-tea-pick]').forEach(function (a) {
      if (a.getAttribute('data-tea-pick') === pick) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
    try { localStorage.setItem(KEY, pick); } catch (e) { /* ignore */ }
    if (writeHash && history.replaceState) history.replaceState(null, '', '#' + pick);
    // 言語を変えても同じ側を見せる
    document.querySelectorAll('.lang-sw a.l-row, a[data-tea-link]').forEach(function (a) {
      a.href = a.href.replace(/#.*$/, '') + '#' + pick;
    });
    // 隠れていた札の reveal を起こす
    document.querySelectorAll('[data-tea="' + pick + '"] .reveal').forEach(function (el) {
      el.classList.add('on');
    });
  }
  apply(fromHash() || saved() || 'matcha', false);
  sw.addEventListener('click', function (e) {
    var a = e.target.closest('[data-tea-pick]');
    if (!a) return;
    e.preventDefault();
    apply(a.getAttribute('data-tea-pick'), true);
  });
  window.addEventListener('hashchange', function () {
    var h = fromHash(); if (h) apply(h, false);
  });
})();
