// 下書きの確認とまとめて公開 — 悠三堂
const API = "https://yusando-gallery.isozaki-f67.workers.dev";
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g,
  (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const CATEGORIES = ["茶碗","茶入","棗","水指","建水","蓋置","茶杓","花入","香合",
  "釜・風炉","急須・宝瓶","湯冷まし","湯呑・茶托","菓子器","掛物","その他"];

const batch = new URLSearchParams(location.search).get("batch") || "";
let items = [];
const picked = new Set();

function token() { return $("token").value.trim(); }
function note(text, cls) {
  $("msg").hidden = !text;
  $("msg").className = "msg " + (cls || "");
  $("msg").innerHTML = text;
}

/* ============================================================== 読み込み == */
async function load() {
  if (!token()) { note("合言葉を入れてください", "err"); return; }
  try { sessionStorage.setItem("yusando_token", token()); } catch (e) { /* ignore */ }
  note("読み込んでいます…");
  const q = new URLSearchParams();
  if (batch) q.set("batch", batch);
  if ($("filter").value) q.set("status", $("filter").value);
  try {
    const res = await fetch(`${API}/api/items?${q}`, { headers: { "x-upload-token": token() } });
    if (res.status === 401) { note("合言葉が違います", "err"); return; }
    if (!res.ok) throw new Error("エラー " + res.status);
    items = await res.json();
    picked.clear();
    note(batch ? `まとめて登録した分（${esc(batch)}）を表示しています。` : "");
    draw();
  } catch (e) {
    note("読み込めませんでした — " + esc(e.message), "err");
  }
}

function draw() {
  if (!items.length) {
    $("list").innerHTML = `<p class="hint" style="margin-top:24px">該当する茶器はありません。</p>`;
    $("footbar").hidden = true;
    return;
  }
  $("list").innerHTML = items.map(card).join("");
  $("footbar").hidden = false;
  updateSel();
}

function card(i) {
  const failed = i.analysis_status === "failed";
  const pending = i.analysis_status === "pending";
  const warn = i.same_object === 0;
  // 赤は「失敗」だけに使う。未読み取りはまだ何も起きていないので金茶で示す。
  const cls = failed ? " failed" : (warn || pending ? " warn" : "");
  const photo = (i.photos && i.photos[0])
    ? `<img src="${API}/photos/${encodeURIComponent(i.photos[0])}" alt="" loading="lazy">`
    : `<div style="aspect-ratio:1;background:var(--paper-deep)"></div>`;
  const opt = (sel) => CATEGORIES.map((c) =>
    `<option value="${c}"${c === sel ? " selected" : ""}>${c}</option>`).join("");

  let flag = "";
  if (failed) flag = `<span class="flag failed">読み取りに失敗 — ${esc(i.analysis_error || "")}</span>`;
  else if (pending) flag = `<span class="flag warn">まだ読み取っていません</span>`;
  else if (warn) flag = `<span class="flag warn">写真の組み合わせに注意 — ${esc(i.group_warning || "")}</span>`;

  return `<div class="card${cls}" data-id="${i.id}">
    <div class="shot">
      <input type="checkbox" class="pick" data-id="${i.id}"${picked.has(i.id) ? " checked" : ""}>
      ${photo}
    </div>
    <div class="body">
      <div class="top">
        ${i.sku ? `<span class="sku">${esc(i.sku)}</span>` : ""}
        <span class="mei">${esc(i.mei || "（未読み取り）")}</span>
        ${i.mei_romaji ? `<span class="romaji">${esc(i.mei_romaji)}</span>` : ""}
        <span class="id">${esc(i.id)}　${esc(i.status)}</span>
      </div>
      ${i.description ? `<p class="desc">${esc(i.description)}</p>` : ""}
      ${flag}
      <div class="meta">
        <select data-f="category" data-id="${i.id}"><option value="">種別なし</option>${opt(i.category)}</select>
        <select data-f="tier" data-id="${i.id}">
          ${[1, 2, 3, 4].map((t) => `<option value="${t}"${i.tier === t ? " selected" : ""}>等級${t}　${(i.price && i.tier === t) ? "¥" + i.price.toLocaleString() : ""}</option>`).join("")}
        </select>
      </div>
      <div class="acts">
        <a class="mini" href="/item.html?id=${encodeURIComponent(i.id)}" target="_blank" rel="noopener">詳細を見る</a>
        <button class="mini" data-act="analyze" data-id="${i.id}"${pending || failed ? "" : " disabled"}>もう一度読み取る</button>
      </div>
    </div></div>`;
}

/* ================================================================ 操作 == */
$("list").addEventListener("change", async (e) => {
  const cb = e.target.closest("input.pick");
  if (cb) {
    cb.checked ? picked.add(cb.dataset.id) : picked.delete(cb.dataset.id);
    updateSel();
    return;
  }
  const sel = e.target.closest("select[data-f]");
  if (!sel) return;
  const id = sel.dataset.id, field = sel.dataset.f;
  const body = field === "tier" ? { tier: +sel.value } : { category: sel.value };
  sel.disabled = true;
  try {
    const res = await fetch(`${API}/api/items/${id}`, {
      method: "PATCH",
      headers: { "x-upload-token": token(), "content-type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error("エラー " + res.status);
    const it = items.find((x) => x.id === id);
    if (it) Object.assign(it, body);
    note("保存しました", "ok");
    setTimeout(() => note(""), 1600);
  } catch (err) {
    note("保存できませんでした — " + esc(err.message), "err");
  } finally { sel.disabled = false; }
});

$("list").addEventListener("click", async (e) => {
  const b = e.target.closest("button[data-act='analyze']");
  if (!b) return;
  const id = b.dataset.id;
  b.disabled = true; b.textContent = "読み取っています…";
  try {
    const res = await fetch(`${API}/api/items/${id}/analyze`, {
      method: "POST", headers: { "x-upload-token": token() },
    });
    const j = await res.json();
    if (!res.ok) throw new Error(j.error || "エラー " + res.status);
    await load();
  } catch (err) {
    note("読み取れませんでした — " + esc(err.message), "err");
    b.disabled = false; b.textContent = "もう一度読み取る";
  }
});

function updateSel() {
  const ready = items.filter((i) => picked.has(i.id) && i.analysis_status === "done").length;
  const n = picked.size;
  $("sel").textContent = n
    ? `${n} 点を選択中${n > ready ? `（うち公開できるのは ${ready} 点。残りは未読み取りです）` : ""}`
    : "0 点を選択中";
  $("pub").disabled = !ready;
  $("del").disabled = !n;
}

$("all").addEventListener("click", () => {
  items.forEach((i) => picked.add(i.id));
  document.querySelectorAll("input.pick").forEach((c) => { c.checked = true; });
  updateSel();
});
$("none").addEventListener("click", () => {
  picked.clear();
  document.querySelectorAll("input.pick").forEach((c) => { c.checked = false; });
  updateSel();
});

async function bulk(action, confirmText) {
  if (!picked.size) return;
  if (confirmText && !confirm(confirmText)) return;
  const ids = [...picked];
  $("pub").disabled = $("del").disabled = true;
  try {
    const res = await fetch(`${API}/api/items/bulk`, {
      method: "POST",
      headers: { "x-upload-token": token(), "content-type": "application/json" },
      body: JSON.stringify({ ids, action }),
    });
    const j = await res.json();
    if (!res.ok) throw new Error(j.error || "エラー " + res.status);
    note(`${j.changed} 点を${action === "publish" ? "公開" : "削除"}しました。`, "ok");
    await load();
  } catch (e) {
    note("処理できませんでした — " + esc(e.message), "err");
    updateSel();
  }
}

$("pub").addEventListener("click", () => bulk("publish"));
$("del").addEventListener("click", () =>
  bulk("delete", `${picked.size} 点を削除します。写真も消え、元に戻せません。よろしいですか。`));
$("load").addEventListener("click", load);
$("filter").addEventListener("change", () => { if (items.length) load(); });
$("token").addEventListener("keydown", (e) => { if (e.key === "Enter") load(); });

// 直前の画面から合言葉を引き継いでいれば、そのまま読み込む
try {
  const t = sessionStorage.getItem("yusando_token");
  if (t) { $("token").value = t; load(); }
} catch (e) { /* ignore */ }
