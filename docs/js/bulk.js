// 茶器のまとめて登録 — 悠三堂
// 写真をファイル名（1・1_top・1_bottom）か撮影時刻で組に分け、下書きとして登録してから1点ずつ解析する。
const API = "https://yusando-gallery.isozaki-f67.workers.dev";
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g,
  (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

const CATEGORIES = ["茶碗","茶入","棗","水指","建水","蓋置","茶杓","花入","香合",
  "釜・風炉","急須・宝瓶","湯冷まし","湯呑・茶托","菓子器","掛物","その他"];
const MAX_PER_ITEM = 5;
const CONCURRENCY = 3;     // Anthropic 側を詰まらせない程度に抑える
const LAST_BATCH = "yusando_last_batch";

let photos = [];   // {file, url, time, hasExif, gi}
let groups = [];   // {photos:[idx], category:"", tier:""}

/* ================================================================ EXIF == */
// 撮影時刻は File.lastModified では当てにならない（コピーや同期で書き換わる）。
// JPEG の APP1 から DateTimeOriginal を読み、無いときだけ lastModified に落とす。
async function exifTime(file) {
  try {
    const buf = await file.slice(0, 131072).arrayBuffer();
    const v = new DataView(buf);
    if (v.byteLength < 4 || v.getUint16(0) !== 0xffd8) return null;
    let off = 2;
    while (off + 4 < v.byteLength) {
      if (v.getUint8(off) !== 0xff) return null;
      const marker = v.getUint8(off + 1);
      if (marker === 0xda || marker === 0xd9) return null;   // 画像本体に入った
      const size = v.getUint16(off + 2);
      if (marker === 0xe1 && off + 10 < v.byteLength && v.getUint32(off + 4) === 0x45786966)
        return readTiff(v, off + 10);
      off += 2 + size;
    }
  } catch (e) { console.warn("EXIF読み取り失敗", file.name, e); }
  return null;
}

function readTiff(v, base) {
  if (base + 8 > v.byteLength) return null;
  const le = v.getUint16(base) === 0x4949;
  const u16 = (o) => v.getUint16(o, le), u32 = (o) => v.getUint32(o, le);
  if (u16(base + 2) !== 42) return null;
  const entry = (dir, tag) => {
    if (dir + 2 > v.byteLength) return 0;
    const n = u16(dir);
    for (let i = 0; i < n; i++) {
      const e = dir + 2 + i * 12;
      if (e + 12 > v.byteLength) return 0;
      if (u16(e) === tag) return e;
    }
    return 0;
  };
  const ifd0 = base + u32(base + 4);
  const ptr = entry(ifd0, 0x8769);                       // Exif IFD
  const dir = ptr ? base + u32(ptr + 8) : ifd0;
  const e = entry(dir, 0x9003) || entry(dir, 0x9004) || entry(ifd0, 0x0132);
  if (!e) return null;
  const count = u32(e + 4);
  const at = count > 4 ? base + u32(e + 8) : e + 8;
  if (at + count > v.byteLength) return null;
  let s = "";
  for (let i = 0; i < count - 1; i++) s += String.fromCharCode(v.getUint8(at + i));
  const m = s.match(/^(\d{4}):(\d{2}):(\d{2})[ T](\d{2}):(\d{2}):(\d{2})/);
  if (!m) return null;
  return new Date(+m[1], +m[2] - 1, +m[3], +m[4], +m[5], +m[6]).getTime();
}

/* ============================================================= 写真選択 == */
$("drop").addEventListener("click", () => $("files").click());
["dragenter", "dragover"].forEach((n) => $("drop").addEventListener(n, (e) => {
  e.preventDefault(); $("drop").classList.add("over");
}));
["dragleave", "drop"].forEach((n) => $("drop").addEventListener(n, (e) => {
  e.preventDefault(); $("drop").classList.remove("over");
}));
$("drop").addEventListener("drop", (e) => take([...e.dataTransfer.files]));
$("files").addEventListener("change", (e) => { take([...e.target.files]); e.target.value = ""; });

async function take(list) {
  const imgs = list.filter((f) => f.type.startsWith("image/"));
  if (!imgs.length) return;
  $("drop").querySelector("p").textContent = "読み込んでいます…";
  const added = [];
  for (const file of imgs) {
    const t = await exifTime(file);
    added.push({ file, url: URL.createObjectURL(file), time: t ?? file.lastModified, hasExif: t != null });
  }
  // 選んだ順ではなく撮った順に並べる。まとめて選ぶと順序は当てにならない。
  photos = photos.concat(added).sort((a, b) => a.time - b.time);
  $("count").textContent = photos.length + " 枚";
  $("drop").querySelector("p").textContent = "ここをタップして写真をまとめて選ぶ";

  const noExif = photos.filter((p) => !p.hasExif).length;
  if ($("mode").value !== "name") $("exifnote").innerHTML = noExif
    ? `${noExif} 枚に撮影時刻が入っていませんでした（ファイルの更新日時で代用しています）。組がずれていたら下で直してください。`
    : "すべての写真から撮影時刻を読みました。";
  syncMode();
  step(2);
}

/* ============================================================ ファイル名 == */
// 「1.jpg」= 正面、「1_top.jpg」= 上面、「1_bottom.jpg」= 裏面 の付け方。
// 拡張子を外し、最初の _ か - の前を「番号」、後ろを「面」とみなす。
// 面の語は多少ゆるく受ける（top/ue/上、bottom/back/ura/裏 など）。
const FACE_RANK = { "": 0, front: 0, f: 0, "正面": 0,
  top: 1, ue: 1, "上": 1, "上面": 1,
  bottom: 2, back: 2, ura: 2, "裏": 2, "裏面": 2, "下": 2, "下面": 2,
  box: 3, hako: 3, "箱": 3, "共箱": 3 };
const FACE_LABEL = ["正面", "上面", "裏面", "箱"];
function parseName(name) {
  const stem = name.replace(/\.[^.]+$/, "").trim();
  const m = stem.match(/^(.*?)[\s_\-]+([^\s_\-]+)$/);
  let key = stem, face = "";
  if (m && (m[2].toLowerCase() in FACE_RANK)) { key = m[1]; face = m[2].toLowerCase(); }
  const rank = FACE_RANK[face] ?? 9;
  return { key: key.trim().toLowerCase(), face, rank };
}
// 番号の並びは「1, 2, 10」の順にしたい（文字列順だと 1, 10, 2 になる）
const natural = new Intl.Collator("ja", { numeric: true, sensitivity: "base" }).compare;

/* ========================================================== グループ分け == */
// 分け方は2通り。決まった枚数（正面・上面・下面の3枚など）で機械的に切るか、
// 器を入れ替えるときに自然に空く間で切るか。
function regroup() {
  groups = [];
  if ($("mode").value === "name") return regroupByName();
  const byCount = $("mode").value === "count";
  const per = +$("per").value;
  const gap = +$("gap").value * 1000;
  let cur = null;

  photos.forEach((p, i) => {
    const gapHere = i > 0 && p.time - photos[i - 1].time > gap;
    const full = cur && cur.photos.length >= (byCount ? per : MAX_PER_ITEM);
    if (!cur || full || (!byCount && gapHere)) {
      cur = { photos: [], category: "", tier: "", odd: false };
      groups.push(cur);
    } else if (byCount && gapHere) {
      // 枚数で切っているのに、組の途中で間が空いた。撮り忘れか撮り足しの合図。
      cur.odd = true;
    }
    cur.photos.push(i);
  });

  // 逆に、組の変わり目なのに間が空いていないところも怪しい。
  // ただし1枚ずつのときは、すべての写真が組の変わり目なので見ても意味がない。
  if (byCount && per > 1) {
    let idx = 0;
    groups.forEach((g, gi) => {
      idx += g.photos.length;
      const next = photos[idx];
      if (gi < groups.length - 1 && next && next.time - photos[idx - 1].time <= gap)
        g.odd = groups[gi + 1].odd = true;
    });
    // 最後の組が半端なら、どこかで枚数がずれている
    const last = groups[groups.length - 1];
    if (last && last.photos.length !== per && groups.length > 1) last.odd = true;
  }
  drawGroups();
}

// ファイル名で分ける。同じ番号を1組にし、正面→上面→裏面→箱の順に並べる。
// 正面（番号だけの名前）が無い組は印を付ける。表紙が裏面になってしまうため。
function regroupByName() {
  const map = new Map();
  photos.forEach((p, i) => {
    const n = parseName(p.file.name);
    if (!map.has(n.key)) map.set(n.key, []);
    map.get(n.key).push({ i, rank: n.rank, name: p.file.name });
  });
  const keys = [...map.keys()].sort(natural);
  let missingFront = 0;
  for (const k of keys) {
    const list = map.get(k).sort((a, b) => a.rank - b.rank || natural(a.name, b.name));
    const hasFront = list[0].rank === 0;
    if (!hasFront) missingFront++;
    groups.push({ photos: list.slice(0, MAX_PER_ITEM).map((x) => x.i), category: "", tier: "",
      odd: !hasFront, oddText: hasFront ? "" : "正面（番号だけの名前）がありません" });
  }
  $("exifnote").textContent = `ファイル名から ${groups.length} 点に分けました。`
    + (missingFront ? `　正面の無い組が ${missingFront} 件あります。` : "");
  drawGroups();
}

function syncMode() {
  const mode = $("mode").value;
  $("modeCount").hidden = mode !== "count";
  $("modeTime").hidden = mode !== "time";
  $("modeName").hidden = mode !== "name";
  regroup();
}
$("mode").addEventListener("change", syncMode);
$("per").addEventListener("change", regroup);
$("gap").addEventListener("input", () => {
  $("gapv").textContent = $("gap").value + " 秒";
  regroup();
});

function drawGroups() {
  const odd = groups.filter((g) => g.odd).length;
  $("gcount").textContent = `${groups.length} 点 / 写真 ${photos.length} 枚`
    + (odd ? `　確認 ${odd} 件` : "");
  $("groups").innerHTML = groups.map((g, gi) => {
    const cells = g.photos.map((pi, k) => {
      const p = photos[pi];
      return `<div class="ph${k === 0 ? " cover" : ""}">
        <img src="${p.url}" alt="" loading="lazy">
        <span class="no">${$("mode").value === "name"
          ? (FACE_LABEL[parseName(p.file.name).rank] || p.file.name.replace(/\.[^.]+$/, ""))
          : (k === 0 ? "表紙" : k + 1)}</span>
        <div class="bar">
          <button data-act="prev" data-g="${gi}" data-k="${k}" ${gi === 0 && k === 0 ? "disabled" : ""} title="前の組へ">←</button>
          <button data-act="split" data-g="${gi}" data-k="${k}" ${k === 0 ? "disabled" : ""} title="ここから新しい組にする">分</button>
          <button data-act="drop" data-g="${gi}" data-k="${k}" title="この写真を外す">×</button>
          <button data-act="next" data-g="${gi}" data-k="${k}" ${gi === groups.length - 1 && k === g.photos.length - 1 ? "disabled" : ""} title="次の組へ">→</button>
        </div></div>`;
    }).join("");
    const opts = (sel) => CATEGORIES.map((c) =>
      `<option value="${c}"${c === sel ? " selected" : ""}>${c}</option>`).join("");
    return `<div class="group${g.odd ? " odd" : ""}">
      <div class="g-head">
        <b>${gi + 1} 点目</b><span class="n">写真 ${g.photos.length} 枚</span>
        ${g.odd ? `<span class="g-flag">${esc(g.oddText || "撮影の間隔とずれています")}</span>` : ""}
        <span class="sp">
          <button class="mini" data-act="merge" data-g="${gi}" ${gi === 0 ? "disabled" : ""}>前の組と合わせる</button>
          <button class="mini warn" data-act="rmgroup" data-g="${gi}">この組を外す</button>
        </span>
      </div>
      <div class="g-body">${cells}</div>
      <div class="g-opts">
        <select data-act="cat" data-g="${gi}"><option value="">種別はAIにまかせる</option>${opts(g.category)}</select>
        <select data-act="tier" data-g="${gi}">
          <option value="">等級はAIにまかせる</option>
          <option value="1"${g.tier === "1" ? " selected" : ""}>等級1</option>
          <option value="2"${g.tier === "2" ? " selected" : ""}>等級2</option>
          <option value="3"${g.tier === "3" ? " selected" : ""}>等級3</option>
          <option value="4"${g.tier === "4" ? " selected" : ""}>等級4</option>
        </select>
      </div></div>`;
  }).join("");
  estimate();
}

$("groups").addEventListener("click", (e) => {
  const b = e.target.closest("button[data-act]");
  if (!b) return;
  const gi = +b.dataset.g, k = +b.dataset.k, act = b.dataset.act;
  if (act === "merge") {
    groups[gi - 1].photos = groups[gi - 1].photos.concat(groups[gi].photos);
    groups.splice(gi, 1);
  } else if (act === "rmgroup") {
    groups[gi].photos.forEach((pi) => URL.revokeObjectURL(photos[pi].url));
    groups.splice(gi, 1);
  } else if (act === "split") {
    const tail = groups[gi].photos.splice(k);
    groups.splice(gi + 1, 0, { photos: tail, category: "", tier: "" });
  } else if (act === "drop") {
    groups[gi].photos.splice(k, 1);
    if (!groups[gi].photos.length) groups.splice(gi, 1);
  } else if (act === "prev") {
    const [pi] = groups[gi].photos.splice(k, 1);
    if (gi === 0) groups.unshift({ photos: [], category: "", tier: "", odd: false });
    const to = gi === 0 ? 0 : gi - 1;
    groups[to].photos.push(pi);
    if (groups[gi + (gi === 0 ? 1 : 0)] && !groups[gi + (gi === 0 ? 1 : 0)].photos.length)
      groups.splice(gi + (gi === 0 ? 1 : 0), 1);
  } else if (act === "next") {
    const [pi] = groups[gi].photos.splice(k, 1);
    if (gi === groups.length - 1) groups.push({ photos: [], category: "", tier: "", odd: false });
    groups[gi + 1].photos.unshift(pi);
    if (!groups[gi].photos.length) groups.splice(gi, 1);
  } else return;
  groups = groups.filter((g) => g.photos.length);
  if (gi < groups.length) groups[gi].odd = false;   // 手で直した組は疑わない
  drawGroups();
});

$("groups").addEventListener("change", (e) => {
  const s = e.target.closest("select[data-act]");
  if (!s) return;
  groups[+s.dataset.g][s.dataset.act === "cat" ? "category" : "tier"] = s.value;
});

function estimate() {
  // 1点あたり 写真4枚で入力約11,000トークン・出力約1,200トークン。
  // claude-sonnet-5 は入力 $2 / 出力 $10（100万トークンあたり）。
  const px = +$("px").value;
  const perPhoto = Math.ceil(px / 28) * Math.ceil(px * 0.75 / 28);
  const inTok = groups.reduce((s, g) => s + g.photos.length * perPhoto, 0) + groups.length * 1000;
  const outTok = groups.length * 1200;
  const usd = inTok / 1e6 * 2 + outTok / 1e6 * 10;
  $("estimate").textContent = groups.length
    ? `${groups.length} 点の解析費用はおよそ $${usd.toFixed(2)}（約${Math.round(usd * 150)}円）。写真は下書きとして保存され、確認してから公開します。`
    : "";
}
$("px").addEventListener("change", estimate);

/* ================================================================ 送信 == */
function step(n) {
  [1, 2, 3].forEach((i) => {
    $("step" + i).hidden = i !== n;
    const s = $("s" + i);
    s.classList.toggle("on", i === n);
    s.classList.toggle("done", i < n);
  });
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// 送る前にこの端末で縮小する。原寸のままだと通信も解析費用も無駄に増える。
async function shrink(file, max) {
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

async function sha256(file) {
  const buf = await file.arrayBuffer();
  const d = await crypto.subtle.digest("SHA-256", buf);
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function logLine(mark, text, cls) {
  const d = document.createElement("div");
  d.innerHTML = `<span class="st ${cls || ""}">${mark}</span><span class="${cls || ""}">${esc(text)}</span>`;
  $("log").prepend(d);
}

let done = 0, total = 0;
function tick(label) {
  const pct = total ? Math.round(done / total * 100) : 0;
  $("pbar").style.width = pct + "%";
  $("ppct").textContent = pct + "%";
  $("pnow").textContent = label;
  $("pcount").textContent = `${done} / ${total}`;
}

$("go").addEventListener("click", run);

async function run() {
  const token = $("token").value.trim();
  if (!token) { alert("合言葉を入れてください"); return; }
  if (!groups.length) { alert("登録する組がありません"); return; }
  const max = +$("px").value;
  const batch = "b" + Date.now().toString(36);
  try { localStorage.setItem(LAST_BATCH, batch); } catch (e) { /* 使えなくても続行 */ }

  step(3);
  $("log").innerHTML = "";
  done = 0; total = groups.length * 2;   // 写真の保存と解析で2工程
  tick("写真を保存しています…");

  const created = [];
  // 保存は1点ずつ順に。まとめて投げると大きな本文が並列に走り、
  // 回線の細いところで軒並み時間切れになる。
  for (const [gi, g] of groups.entries()) {
    try {
      const files = [];
      for (const pi of g.photos) files.push(await shrink(photos[pi].file, max));
      const fd = new FormData();
      files.forEach((f) => fd.append("photos", f));
      fd.append("batch", batch);
      fd.append("cover_hash", await sha256(files[0]));
      if (g.category) fd.append("category", g.category);
      if (g.tier) fd.append("tier", g.tier);
      const res = await fetch(API + "/api/draft", {
        method: "POST", headers: { "x-upload-token": token }, body: fd,
      });
      const j = await res.json();
      if (!res.ok) throw new Error(j.error || "エラー " + res.status);
      if (j.duplicate_of) {
        logLine("=", `${gi + 1} 点目：同じ写真が既に登録されています（${j.sku || j.duplicate_of}）。とばしました`, "warn");
        total -= 2;      // この点は解析もしない
      } else {
        created.push(j.id);
        logLine("·", `${gi + 1} 点目：${j.sku} として写真 ${files.length} 枚を保存しました`);
        done++;
      }
      tick("写真を保存しています…");
    } catch (e) {
      logLine("×", `${gi + 1} 点目：保存できませんでした — ${e.message}`, "ng");
      total -= 2;
      tick("写真を保存しています…");
    }
  }

  if (!created.length) { finish(batch, 0, 0, 0); return; }
  await analyseAll(created, token, batch);
}

// 解析は同時 CONCURRENCY 本まで。1本ずつだと遅く、増やしすぎると 429 を招く。
async function analyseAll(ids, token, batch) {
  tick("内容を読み取っています…");
  let okCount = 0, warnCount = 0, ngCount = 0;
  const queue = ids.slice();

  const worker = async () => {
    while (queue.length) {
      const id = queue.shift();
      const r = await analyseOne(id, token);
      if (r.ok) { okCount++; if (r.warn) warnCount++; } else ngCount++;
      done++;
      tick("内容を読み取っています…");
    }
  };
  await Promise.all(Array.from({ length: Math.min(CONCURRENCY, queue.length) }, worker));
  finish(batch, okCount, warnCount, ngCount);
}

async function analyseOne(id, token, attempt = 1) {
  try {
    const res = await fetch(`${API}/api/items/${id}/analyze`, {
      method: "POST", headers: { "x-upload-token": token },
    });
    const j = await res.json();
    if (!res.ok) {
      // 混み合っているだけなら間を置いて試す。3回で諦め、下書きは残す。
      if (j.retryable && attempt < 3) {
        await new Promise((r) => setTimeout(r, attempt * 4000));
        return analyseOne(id, token, attempt + 1);
      }
      throw new Error(j.error || "エラー " + res.status);
    }
    if (j.same_object === false) {
      logLine("!", `${j.sku ? j.sku + "　" : ""}${j.mei || id}：${j.group_warning || "写真が同一の器に見えません"}`, "warn");
      return { ok: true, warn: true };
    }
    logLine("○", `${j.sku ? j.sku + "　" : ""}${j.mei || id}（${j.category || "種別不明"}・等級${j.tier}）`);
    return { ok: true, warn: false };
  } catch (e) {
    logLine("×", `${id}：読み取れませんでした — ${e.message}`, "ng");
    return { ok: false };
  }
}

function finish(batch, ok, warn, ng) {
  tick("終わりました");
  $("pnow").textContent = "終わりました";
  const parts = [`${ok} 点を下書きにしました`];
  if (warn) parts.push(`うち ${warn} 点は写真の組み合わせに注意が必要です`);
  if (ng) parts.push(`${ng} 点は読み取りに失敗しました（下書きには残っています）`);
  $("after").hidden = false;
  $("after").className = "msg " + (ng ? "err" : "ok");
  $("after").innerHTML = esc(parts.join("。")) + "。<br>"
    + `<a href="/drafts.html?batch=${encodeURIComponent(batch)}">下書きを確認して公開する →</a>`;
}

/* ============================================================== 再開 == */
// 解析の途中でタブを閉じても、下書きは D1 に残っている。写真を選び直さなくても
// 続きから解析できるよう、前回の batch に未処理があれば知らせる。
(async function checkResume() {
  let batch;
  try { batch = localStorage.getItem(LAST_BATCH); } catch (e) { return; }
  if (!batch) return;
  const token = sessionStorage.getItem("yusando_token");
  if (!token) {
    $("resume").hidden = false;
    $("resume").innerHTML = `前回の登録（${esc(batch)}）があります。`
      + `<a href="/drafts.html?batch=${encodeURIComponent(batch)}">下書きを見る →</a>`;
    return;
  }
  try {
    const res = await fetch(`${API}/api/items?batch=${encodeURIComponent(batch)}`,
      { headers: { "x-upload-token": token } });
    if (!res.ok) return;
    const items = await res.json();
    const left = items.filter((i) => i.analysis_status !== "done");
    if (!left.length) return;
    $("resume").hidden = false;
    $("resume").innerHTML = `前回の登録に、まだ読み取っていない茶器が ${left.length} 点あります。`
      + `<button class="btn" id="resumeGo" style="margin-left:10px;padding:7px 18px">続きから読み取る</button>`;
    $("resumeGo").addEventListener("click", () => {
      $("resume").hidden = true;
      step(3);
      $("log").innerHTML = "";
      done = 0; total = left.length;
      analyseAll(left.map((i) => i.id), token, batch);
    });
  } catch (e) { console.warn("再開の確認に失敗", e); }
})();

$("token").addEventListener("change", () => {
  try { sessionStorage.setItem("yusando_token", $("token").value.trim()); } catch (e) { /* ignore */ }
});
