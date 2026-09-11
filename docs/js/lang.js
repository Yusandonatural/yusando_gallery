// 言語切替 — <details> が開閉そのものを持つので、足すのは離脱時の始末だけ。
(function () {
  var d = document.querySelector('details.lang-sw');
  if (!d) return;
  document.addEventListener('click', function (e) {
    if (d.open && !d.contains(e.target)) d.open = false;
  });
  d.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' || !d.open) return;
    d.open = false;
    var s = d.querySelector('summary');
    if (s) s.focus();
  });
})();
