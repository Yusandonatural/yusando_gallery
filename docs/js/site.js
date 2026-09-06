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
  }
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
    ? { head: 'Available Now', sold: ' (sold)', detail: 'View details',
        note: 'Prices include tax. Each piece is one of a kind.' }
    : { head: 'いま買える' + (stub.getAttribute('data-ec-name') || cat),
        sold: '(売却済)', detail: '詳しく見る',
        note: '価格は税込。すべて一点ものです。' };

  var esc = function (v) {
    return String(v == null ? '' : v).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };

  fetch(EC.endpoint + '/api/items').then(function (r) {
    if (!r.ok) throw new Error(r.status);
    return r.json();
  }).then(function (all) {
    var items = (all || []).filter(function (i) {
      return i.category === cat && i.status !== 'hidden';
    });
    if (!items.length) return;                        // 準備中の文面を残す

    var cards = items.map(function (i) {
      var sold = i.status === 'sold';
      var photo = (i.photos && i.photos[0])
        ? '<img class="st-photo" loading="lazy" alt="' + esc(i.mei) + '" src="'
          + EC.endpoint + '/photos/' + esc(i.photos[0]) + '">'
        : '<div class="st-photo st-nophoto"></div>';
      var sekki = (i.sekki && i.sekki.length)
        ? '<p class="st-sekki">' + i.sekki.map(esc).join('・') + '</p>' : '';
      return '<a class="stock-card' + (sold ? ' sold' : '') + '" href="'
        + root + 'item.html?id=' + encodeURIComponent(i.id) + '">'
        + photo
        + '<div class="st-body">'
        + '<h4 class="st-mei">' + esc(i.mei)
        + (i.mei_yomi ? '<span class="st-yomi">' + esc(i.mei_yomi) + '</span>' : '')
        + '</h4>'
        + (i.description ? '<p class="st-desc">' + esc(i.description) + '</p>' : '')
        + sekki
        + '<p class="st-price">¥' + Number(i.price || 0).toLocaleString('ja-JP')
        + (sold ? '<span class="st-sold">' + T.sold + '</span>' : '') + '</p>'
        + '<p class="st-more">' + T.detail + ' →</p>'
        + '</div></a>';
    }).join('');

    stub.classList.add('has-stock');
    stub.innerHTML = '<h3>' + esc(T.head) + '</h3>'
      + '<div class="stock-grid">' + cards + '</div>'
      + '<p class="st-note">' + esc(T.note) + '</p>';
  }).catch(function () {
    /* 取得できないときは「準備中」のまま静かに残す */
  });
})();
