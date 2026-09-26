'use strict';
// 追跡防止のための純粋関数群（Electronに依存しないのでNodeだけでテストできる）

const { getDomain, getHostname } = require('tldts');

// URLに付けられる追跡用パラメータ（完全一致）
const TRACKING_PARAMS = new Set([
  'fbclid', 'gclid', 'gclsrc', 'dclid', 'gbraid', 'wbraid', 'msclkid', 'yclid',
  'twclid', 'ttclid', 'igshid', 'igsh', 'li_fat_id', 'mc_cid', 'mc_eid', 'mkt_tok',
  '_ga', '_gl', '_hsenc', '_hsmi', '__hssc', '__hstc', '__hsfp', 'hsctatracking',
  'oly_anon_id', 'oly_enc_id', 'vero_id', 'vero_conv', 'wickedid', 'rb_clickid',
  's_cid', 'srsltid', 'epik', 'sccid', '_openstat', 'ncid', 'cmpid', 'sms_click',
  'sms_source', 'sms_uph', 'ref_src', 'ref_url', 'si', 'spm', 'scm', 'trk', 'trkcampaign',
]);

// 接頭辞で判定する追跡用パラメータ
const TRACKING_PREFIXES = ['utm_', 'pk_', 'mtm_', 'matomo_', 'hsa_', 'itm_', 'stm_'];

function isTrackingParam(name) {
  const k = name.toLowerCase();
  return TRACKING_PARAMS.has(k) || TRACKING_PREFIXES.some((p) => k.startsWith(p));
}

// 追跡パラメータを取り除いたURLを返す。変更がなければ null
function stripTrackingParams(url) {
  let u;
  try { u = new URL(url); } catch { return null; }
  if (u.protocol !== 'http:' && u.protocol !== 'https:') return null;
  const keys = [...new Set(u.searchParams.keys())].filter(isTrackingParam);
  if (keys.length === 0) return null;
  for (const k of keys) u.searchParams.delete(k);
  return u.toString();
}

// 登録ドメイン（example.co.jp 等）。IPやlocalhostはホスト名そのもの
function siteOf(url) {
  return getDomain(url, { allowPrivateDomains: true }) || getHostname(url) || null;
}

function isThirdParty(requestUrl, firstPartyUrl) {
  if (!firstPartyUrl) return false;
  const a = siteOf(requestUrl);
  const b = siteOf(firstPartyUrl);
  if (!a || !b) return false;
  return a !== b;
}

function findHeader(headers, name) {
  const lower = name.toLowerCase();
  return Object.keys(headers).find((k) => k.toLowerCase() === lower);
}

function deleteHeader(headers, name) {
  const key = findHeader(headers, name);
  if (key !== undefined) delete headers[key];
}

// 送信ヘッダーの整形。headers は書き換えて返す
function sanitizeRequestHeaders(headers, requestUrl, firstPartyUrl) {
  headers['DNT'] = '1';
  headers['Sec-GPC'] = '1';
  deleteHeader(headers, 'X-Client-Data');

  const thirdParty = isThirdParty(requestUrl, firstPartyUrl);
  if (thirdParty) deleteHeader(headers, 'Cookie');

  // 他サイトへはリファラーをオリジンだけに縮める（閲覧中のページのパスを漏らさない）
  const refKey = findHeader(headers, 'Referer');
  if (refKey !== undefined && isThirdParty(requestUrl, headers[refKey])) {
    try {
      headers[refKey] = new URL(headers[refKey]).origin + '/';
    } catch {
      delete headers[refKey];
    }
  }
  return { headers, thirdParty };
}

// 受信ヘッダーの整形：第三者のCookie設定を捨てる。変更したら true
function sanitizeResponseHeaders(headers, requestUrl, firstPartyUrl) {
  if (!isThirdParty(requestUrl, firstPartyUrl)) return false;
  const key = findHeader(headers, 'Set-Cookie');
  if (key === undefined) return false;
  delete headers[key];
  return true;
}

// ページ内に残すと送信されてしまう種類のリクエスト（ビーコン・<a ping>・CSPレポート）
const ALWAYS_BLOCKED_TYPES = new Set(['ping', 'cspReport']);

// フィルターリストが読み込めなかったとき用の最小限の遮断リスト
const FALLBACK_BLOCKED_SITES = new Set([
  'doubleclick.net', 'googlesyndication.com', 'googleadservices.com', 'google-analytics.com',
  'googletagmanager.com', 'googletagservices.com', 'adservice.google.com', 'app-measurement.com',
  'facebook.net', 'scorecardresearch.com', 'quantserve.com', 'criteo.com', 'criteo.net',
  'taboola.com', 'outbrain.com', 'adnxs.com', 'rubiconproject.com', 'pubmatic.com',
  'openx.net', 'casalemedia.com', 'amazon-adsystem.com', 'adsrvr.org', 'hotjar.com',
  'mixpanel.com', 'segment.io', 'segment.com', 'clarity.ms', 'bat.bing.com',
  'ads-twitter.com', 'analytics.tiktok.com', 'yimg.jp', 'microad.jp', 'i-mobile.co.jp',
  'adingo.jp', 'impact-ad.jp', 'logly.co.jp', 'popin.cc', 'fout.jp', 'socdm.com',
]);

function isFallbackBlocked(url) {
  const host = getHostname(url);
  if (!host) return false;
  const parts = host.split('.');
  for (let i = 0; i < parts.length - 1; i++) {
    if (FALLBACK_BLOCKED_SITES.has(parts.slice(i).join('.'))) return true;
  }
  return false;
}

// アドレスバーの入力をURLに変換する（URLでなければ検索）
function toNavigableUrl(input, searchBase = 'https://duckduckgo.com/?q=') {
  const text = input.trim();
  if (!text) return null;
  if (/^[a-z][a-z0-9+.-]*:\/\//i.test(text) || /^(about|data|file):/i.test(text)) return text;
  if (!/\s/.test(text) && (/^localhost(:\d+)?(\/|$)/.test(text) || /^[^/\s]+\.[a-z]{2,}(:\d+)?(\/.*)?$/i.test(text) || /^\d{1,3}(\.\d{1,3}){3}(:\d+)?(\/.*)?$/.test(text))) {
    return 'https://' + text;
  }
  return searchBase + encodeURIComponent(text);
}

module.exports = {
  isTrackingParam,
  stripTrackingParams,
  siteOf,
  isThirdParty,
  sanitizeRequestHeaders,
  sanitizeResponseHeaders,
  ALWAYS_BLOCKED_TYPES,
  isFallbackBlocked,
  toNavigableUrl,
};
