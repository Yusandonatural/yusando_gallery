// AIが書いた内容を人が直すための編集フォーム。
// 1点ずつ登録（upload.html）と下書き確認（drafts.html）の両方から使う。
// 画面ごとに作ると必ず食い違うので、フォームの定義は1か所に置く。
(function () {
  const API = "https://yusando-gallery.isozaki-f67.workers.dev";
  const CATEGORIES = ["茶碗","茶入","棗","水指","建水","蓋置","茶杓","花入","香合",
    "釜・風炉","急須・宝瓶","湯冷まし","湯呑・茶托","菓子器","掛物","その他"];
  const SEKKI = ["立春","雨水","啓蟄","春分","清明","穀雨","立夏","小満","芒種","夏至",
    "小暑","大暑","立秋","処暑","白露","秋分","寒露","霜降","立冬","小雪","大雪","冬至",
    "小寒","大寒"];

  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // 欄の定義。ここに1行足せば両方の画面に出る。
  const FIELDS = [
    { g: "銘", f: [
      ["mei", "銘", "text"],
      ["mei_yomi", "読み（ひらがな）", "text"],
      ["mei_romaji", "ローマ字", "text"],
      ["mei_reason", "銘の由来", "area2"],
    ]},
    { g: "説明", f: [
      ["description", "説明（日本語）", "area"],
    ]},
    { g: "所見", f: [
      ["technique", "技法", "text"],
      ["glaze", "釉・土", "text"],
      ["kiln", "産地", "text"],
      ["era", "時代", "text"],
      ["condition", "状態", "area2"],
    ]},
    { g: "英語", fold: true, f: [
      ["mei_en", "銘の英訳（表示には使いません）", "text"],
      ["mei_reason_en", "由来（英）", "area2"],
      ["description_en", "説明（英）", "area"],
      ["technique_en", "技法（英）", "text"],
      ["glaze_en", "釉・土（英）", "text"],
      ["kiln_en", "産地（英）", "text"],
      ["era_en", "時代（英）", "text"],
      ["condition_en", "状態（英）", "text"],
    ]},
  ];

  const CSS = `
.ed{display:flex;flex-direction:column;gap:22px;font-family:var(--sans,sans-serif)}
.ed-grp{border:1px solid var(--line,#d8cfba);border-radius:4px;background:var(--paper,#f7f3ea)}
.ed-grp > summary,.ed-grp > .ed-head{
  padding:11px 16px;font-size:11.5px;letter-spacing:.16em;color:var(--matcha,#4a5d3a);
  border-bottom:1px solid var(--line,#d8cfba);background:var(--paper-deep,#efe8d8);
  cursor:default;list-style:none}
.ed-grp > summary{cursor:pointer}
.ed-grp > summary::-webkit-details-marker{display:none}
.ed-grp > summary::after{content:"＋";float:right;color:var(--rikyu,#8a8c78)}
.ed-grp[open] > summary::after{content:"−"}
.ed-body{padding:16px;display:flex;flex-direction:column;gap:14px}
.ed-f{display:flex;flex-direction:column;gap:5px}
.ed-f label{font-size:11px;letter-spacing:.1em;color:var(--ink-soft,#5a564c)}
.ed-f input,.ed-f textarea,.ed-f select{
  width:100%;font-family:inherit;font-size:14px;line-height:1.8;padding:10px 12px;
  border:1px solid var(--line,#d8cfba);border-radius:3px;
  background:#fff;color:var(--ink,#2b2a26)}
.ed-f textarea{resize:vertical;min-height:92px}
.ed-f textarea.s{min-height:54px}
.ed-f input:focus,.ed-f textarea:focus,.ed-f select:focus{outline:0;border-color:var(--matcha,#4a5d3a)}
.ed-f.changed input,.ed-f.changed textarea,.ed-f.changed select{
  border-color:var(--gold,#b0965a);background:#fffdf7}
.ed-two{display:flex;gap:12px;flex-wrap:wrap}
.ed-two > *{flex:1;min-width:150px}
.ed-sekki{display:flex;flex-wrap:wrap;gap:6px}
.ed-sekki label{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;
  border:1px solid var(--line,#d8cfba);border-radius:999px;padding:5px 11px;
  cursor:pointer;background:#fff;color:var(--ink-soft,#5a564c)}
.ed-sekki input{accent-color:var(--matcha,#4a5d3a);margin:0}
.ed-sekki label:has(input:checked){border-color:var(--matcha,#4a5d3a);
  color:var(--matcha,#4a5d3a);background:#f2f4ee}
.ed-bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;
  position:sticky;bottom:0;background:rgba(247,243,234,.97);padding:14px 0;
  border-top:1px solid var(--line,#d8cfba);z-index:5}
.ed-note{font-size:11.5px;color:var(--rikyu,#8a8c78);margin-right:auto;line-height:1.7}
.ed-note b{color:var(--gold,#b0965a);font-weight:400}
`;

  function injectCss() {
    if (document.getElementById("ed-css")) return;
    const st = document.createElement("style");
    st.id = "ed-css"; st.textContent = CSS;
    document.head.appendChild(st);
  }

  function field(key, label, kind, val) {
    const v = esc(val == null ? "" : val);
    if (kind === "area")
      return `<div class="ed-f" data-k="${key}"><label>${label}</label>`
        + `<textarea data-in="${key}">${v}</textarea></div>`;
    if (kind === "area2")
      return `<div class="ed-f" data-k="${key}"><label>${label}</label>`
        + `<textarea class="s" data-in="${key}">${v}</textarea></div>`;
    return `<div class="ed-f" data-k="${key}"><label>${label}</label>`
      + `<input type="text" data-in="${key}" value="${v}"></div>`;
  }

  // item.sekki は配列でも JSON 文字列でも来る（D1 の TEXT 列のため）
  function sekkiOf(item) {
    let s = item.sekki;
    if (typeof s === "string") { try { s = JSON.parse(s); } catch (e) { s = []; } }
    return Array.isArray(s) ? s : [];
  }

  function build(item) {
    const sk = sekkiOf(item);
    let html = '<div class="ed">';
    for (const grp of FIELDS) {
      const inner = grp.f.map(([k, l, t]) => field(k, l, t, item[k])).join("");
      html += grp.fold
        ? `<details class="ed-grp"><summary>${grp.g}</summary><div class="ed-body">${inner}</div></details>`
        : `<div class="ed-grp"><div class="ed-head">${grp.g}</div><div class="ed-body">${inner}</div></div>`;
    }
    // 分類は選ぶ欄なので別立て
    html += '<div class="ed-grp"><div class="ed-head">分類</div><div class="ed-body">'
      + '<div class="ed-two">'
      + `<div class="ed-f" data-k="category"><label>種別</label><select data-in="category">`
      + '<option value="">（未設定）</option>'
      + CATEGORIES.map((c) => `<option value="${c}"${c === item.category ? " selected" : ""}>${c}</option>`).join("")
      + '</select></div>'
      + `<div class="ed-f" data-k="tier"><label>等級</label><select data-in="tier">`
      + [1, 2, 3, 4].map((t) => `<option value="${t}"${item.tier === t ? " selected" : ""}>等級 ${t}</option>`).join("")
      + '</select></div></div>'
      + '<div class="ed-f" data-k="sekki"><label>節気（取り合わせの目安。無理に選ばなくて構いません）</label>'
      + '<div class="ed-sekki">'
      + SEKKI.map((s) => `<label><input type="checkbox" data-sekki value="${s}"${sk.indexOf(s) >= 0 ? " checked" : ""}>${s}</label>`).join("")
      + '</div></div>'
      + `<div class="ed-f" data-k="sekki_reason"><label>節気を選んだ理由</label>`
      + `<textarea class="s" data-in="sekki_reason">${esc(item.sekki_reason || "")}</textarea></div>`
      + '</div></div>';
    html += '</div>';
    return html;
  }

  // 変えた欄だけ送る。触っていない欄を送ると、他の画面での編集を
  // 古い値で上書きしてしまう。
  function collect(root, item) {
    const out = {};
    root.querySelectorAll("[data-in]").forEach((el) => {
      const k = el.dataset.in;
      let v = el.value;
      if (k === "tier") v = +v;
      const was = item[k] == null ? "" : item[k];
      if (String(v) !== String(was)) out[k] = v === "" && k !== "tier" ? null : v;
    });
    const sk = [...root.querySelectorAll("[data-sekki]:checked")].map((c) => c.value);
    const wasSk = sekkiOf(item);
    if (JSON.stringify(sk) !== JSON.stringify(wasSk)) out.sekki = sk;
    return out;
  }

  function markChanged(root, item) {
    const diff = collect(root, item);
    root.querySelectorAll(".ed-f").forEach((f) => {
      f.classList.toggle("changed", f.dataset.k in diff);
    });
    return Object.keys(diff).length;
  }

  /**
   * container に編集フォームを描く。
   *   onSaved(updatedItem) … 保存できたら呼ぶ
   *   extraButtons … [{label, cls, onClick(diffCount)}] を操作列に足す
   */
  function render(container, item, opts) {
    opts = opts || {};
    injectCss();
    container.innerHTML = build(item)
      + '<div class="ed-bar">'
      + '<span class="ed-note" data-note>AIが書いた内容です。直したところは<b>枠が金</b>に変わります。</span>'
      + '<button class="btn" data-save>保存する</button>'
      + (opts.extraHtml || "")
      + "</div>";

    const note = container.querySelector("[data-note]");
    const save = container.querySelector("[data-save]");
    const sync = () => {
      const n = markChanged(container, item);
      save.disabled = n === 0;
      note.innerHTML = n
        ? `${n} 箇所を直しました。保存するまで反映されません。`
        : "AIが書いた内容です。直したところは<b>枠が金</b>に変わります。";
    };
    container.addEventListener("input", sync);
    container.addEventListener("change", sync);
    sync();

    save.addEventListener("click", async () => {
      const diff = collect(container, item);
      if (!Object.keys(diff).length) return;
      save.disabled = true; save.textContent = "保存しています…";
      try {
        const res = await fetch(`${API}/api/items/${item.id}`, {
          method: "PATCH",
          headers: { "x-upload-token": opts.token(), "content-type": "application/json" },
          body: JSON.stringify(diff),
        });
        const j = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(j.error || "エラー " + res.status);
        Object.assign(item, diff);
        if (diff.sekki) item.sekki = diff.sekki;
        sync();
        note.textContent = "保存しました。";
        if (opts.onSaved) opts.onSaved(item);
      } catch (e) {
        note.textContent = "保存できませんでした — " + (e && e.message ? e.message : e);
        save.disabled = false;
      } finally { save.textContent = "保存する"; }
    });

    return { item, sync, hasChanges: () => Object.keys(collect(container, item)).length };
  }

  window.YSD_EDIT = { render, sekkiOf, CATEGORIES };
})();
