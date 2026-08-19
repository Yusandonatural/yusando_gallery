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
