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
  // 「写真が少ない」はサーバ側の status ではないので、取ってから絞る
  if ($("filter").value && $("filter").value !== "few") q.set("status", $("filter").value);
  try {
    const res = await fetch(`${API}/api/items?${q}`, { headers: { "x-upload-token": token() } });
    if (res.status === 401) { note("合言葉が違います", "err"); return; }
    if (!res.ok) throw new Error("エラー " + res.status);
    items = await res.json();
    picked.clear();
      if ($("filter").value === "few") items = items.filter((i) => (i.photos || []).length < 3);
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
  const n = (i.photos || []).length;
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
        <span class="shots${n < 3 ? " few" : ""}">写真 ${n} 枚${n < 3 ? "（正面のみ）" : ""}</span>
        <label class="mini add">写真を足す
          <input type="file" accept="image/*" multiple data-add="${i.id}" hidden>
        </label>
        <a class="mini" href="/item.html?id=${encodeURIComponent(i.id)}" target="_blank" rel="noopener">詳細を見る</a>
        <button class="mini" data-act="analyze" data-id="${i.id}">${pending || failed ? "読み取る" : "もう一度読み取る"}</button>
        <button class="mini" data-act="edit" data-id="${i.id}"${pending ? " disabled" : ""}>内容を直す</button>
      </div>
      <div class="editbox" data-editbox="${i.id}" hidden></div>
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

// 正面だけ先に登録しておいて、上面・下面をあとから足す進め方のための口。
// 足しただけでは読み直さない（費用がかかり、手で直した文章も消えるため）。
// 読み直したいときは、そのあと「もう一度読み取る」を押す。
$("list").addEventListener("change", async (e) => {
  const inp = e.target.closest("input[data-add]");
  if (!inp || !inp.files.length) return;
  const id = inp.dataset.add;
  const box = inp.closest(".acts").querySelector(".add");
  const was = box.firstChild.nodeValue;
  box.firstChild.nodeValue = "送っています…";
  try {
    const fd = new FormData();
    for (const f of [...inp.files].slice(0, 4)) fd.append("photos", await shrink(f));
    const res = await fetch(`${API}/api/items/${id}/photos`, {
      method: "POST", headers: { "x-upload-token": token() }, body: fd,
    });
    const j = await res.json();
    if (!res.ok) throw new Error(j.error || "エラー " + res.status);
    note(`${j.added} 枚を足しました（合計 ${j.photos} 枚）。内容に反映するには「もう一度読み取る」を押してください。`, "ok");
    await load();
  } catch (err) {
    note("足せませんでした — " + esc(err.message), "err");
    box.firstChild.nodeValue = was;
  } finally { inp.value = ""; }
});

// 送る前にこの端末で縮小する（bulk.js と同じ扱い）
async function shrink(file, max = 1600) {
  const img = await new Promise((res, rej) => {
    const i = new Image();
    i.onload = () => res(i); i.onerror = rej; i.src = URL.createObjectURL(file);
  });
  const s = Math.min(1, max / Math.max(img.width, img.height));
  const c = document.createElement("canvas");
  c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
  c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
  URL.revokeObjectURL(img.src);
  const blob = await new Promise((r) => c.toBlob(r, "image/jpeg", 0.85));
  return new File([blob], file.name.replace(/\.[^.]+$/, "") + ".jpg", { type: "image/jpeg" });
}

// AI が書いた銘・説明・所見を人が直す欄。カードの中で開く。
// 保存のたびに一覧を読み直すと編集欄が閉じてしまうので、再取得はせず、
// そのカードの見出しと抜粋だけ書き換える。
$("list").addEventListener("click", (e) => {
  const b = e.target.closest("button[data-act='edit']");
  if (!b) return;
  const id = b.dataset.id;
  const box = $("list").querySelector(`[data-editbox="${id}"]`);
  if (!box) return;
  if (!box.hidden) {
    box.hidden = true; box.innerHTML = "";
    b.classList.remove("on"); b.textContent = "内容を直す";
      return;
  }
  const item = items.find((x) => x.id === id);
  if (!item) return;
  if (!token()) { note("合言葉を入れてください", "err"); return; }
  box.hidden = false;
  b.classList.add("on"); b.textContent = "編集を閉じる";
  YSD_EDIT.render(box, item, {
    token,
    extraHtml: item.status === "draft"
      ? '<button class="btn solid" data-act="pub1" data-id="' + id + '" type="button">この1点を公開する</button>'
      : "",
    onSaved: (it) => {
      const card = box.closest(".card");
      card.querySelector(".mei").textContent = it.mei || "（未読み取り）";
      const desc = card.querySelector(".desc");
      if (desc) desc.textContent = it.description || "";
    },
  });
});

$("list").addEventListener("click", async (e) => {
  const b = e.target.closest("button[data-act='pub1']");
  if (!b) return;
  const id = b.dataset.id;
  b.disabled = true; b.textContent = "公開しています…";
  try {
    const res = await fetch(`${API}/api/items/${id}`, {
      method: "PATCH",
      headers: { "x-upload-token": token(), "content-type": "application/json" },
      body: JSON.stringify({ status: "published" }),
    });
    if (!res.ok) throw new Error("エラー " + res.status);
    note("公開しました。", "ok");
    await load();
  } catch (err) {
    note("公開できませんでした — " + esc(err.message), "err");
    b.disabled = false; b.textContent = "この1点を公開する";
  }
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
