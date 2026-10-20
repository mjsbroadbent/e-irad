/* e-Irad portal script: header, footer, language, catalogue, and the service flows.
   No form on e-Irad sends anything: there is no network call in this file. */
(function () {
  "use strict";
  var I = window.E_I18N, S = window.E_SERVICES;
  var LANGS = ["en", "ir", "ru"], LANG = "en";
  try { var sv = localStorage.getItem("eirad_lang"); if (LANGS.indexOf(sv) >= 0) LANG = sv; } catch (e) {}
  var qs = new URLSearchParams(location.search);
  if (LANGS.indexOf(qs.get("lang")) >= 0) LANG = qs.get("lang");
  var PAGE = document.body.getAttribute("data-page");
  var GOV = "https://iradgov.org/";

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fill(s, v) { return String(s).replace(/\{(\w+)\}/g, function (m, k) { return v && v[k] != null ? v[k] : m; }); }
  function t(k, v) { var d = I.ui[LANG]; var s = d[k] != null ? d[k] : I.ui.en[k]; return v ? fill(s, v) : s; }
  function L(o, v) { if (o == null) return ""; var s = typeof o === "string" ? o : (o[LANG] != null ? o[LANG] : o.en); return v ? fill(s, v) : s; }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function hash(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function iradNow() { var n = new Date(); return new Date(n.getTime() + n.getTimezoneOffset() * 60000 + 6 * 3600000); }
  function today() { var d = iradNow(); return new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate())); }
  function addDays(d, n) { var x = new Date(d.getTime()); x.setUTCDate(x.getUTCDate() + n); return x; }
  function fmtD(d) { var M = I.ui[LANG].months; return LANG === "ir" ? d.getUTCDate() + "-" + M[d.getUTCMonth()] + " " + d.getUTCFullYear() : d.getUTCDate() + " " + M[d.getUTCMonth()] + " " + d.getUTCFullYear(); }
  function fmtN(x, dp) { var s = Number(x).toFixed(dp || 0); var p = s.split("."); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, LANG === "en" ? "," : " "); return p.join(LANG === "en" ? "." : ","); }
  function som(x) { return fmtN(x, 2) + " " + t("som"); }
  function norm(s) { return String(s || "").toUpperCase().replace(/[\s\-\.]/g, ""); }
  function svc(id) { for (var i = 0; i < S.list.length; i++) if (S.list[i].id === id) return S.list[i]; return null; }

  var ICONS = {
    id: '<path d="M4 5h16v14H4z"/><circle cx="9" cy="11" r="2.2"/><path d="M6 16c.6-1.6 1.7-2.4 3-2.4s2.4.8 3 2.4M14 10h4M14 13h3"/>',
    ticket: '<path d="M4 7h16v3a2 2 0 0 0 0 4v3H4v-3a2 2 0 0 0 0-4z"/><path d="M10 7v10" stroke-dasharray="2 2"/>',
    shop: '<path d="M4 9l1.5-4h13L20 9M4 9h16v2a2.5 2.5 0 0 1-5 0 2.5 2.5 0 0 1-5 0 2.5 2.5 0 0 1-5 0zM5 12v7h14v-7M10 19v-4h4v4"/>',
    chart: '<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>',
    bolt: '<path d="M13 3 5 14h6l-1 7 8-11h-6z"/>',
    drop: '<path d="M12 3c3.5 4.5 6 7.7 6 10.5A6 6 0 0 1 6 13.5C6 10.7 8.5 7.5 12 3z"/>',
    car: '<path d="M5 16V12l2-5h10l2 5v4M5 16h14M5 16v2M19 16v2"/><circle cx="8" cy="13.5" r="1"/><circle cx="16" cy="13.5" r="1"/>',
    box: '<path d="M4 8l8-4 8 4v8l-8 4-8-4zM4 8l8 4 8-4M12 12v8"/>',
    shield: '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="m9 12 2 2 4-4"/>',
    route: '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h6a3 3 0 0 0 0-6h-4a3 3 0 0 1 0-6h6"/>',
    doc: '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h7M9 16h5"/>'
  };
  function icon(k) { return '<svg class="sic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (ICONS[k] || ICONS.doc) + "</svg>"; }
  function badge(st) { return '<span class="badge b-' + st + '">' + esc(t("st_" + st)) + "</span>"; }

  /* ---------- chrome ---------- */
  var NAV = [["home", "/"], ["status", "/status.html"], ["faq", "/faq.html"], ["contact", "/contact.html"], ["login", "/login.html"]];
  function chrome() {
    var cur = PAGE === "service" ? "home" : PAGE;
    $("#top").innerHTML =
      '<a class="skip" href="#main">' + esc(t("skip")) + "</a>" +
      '<div class="govbar"><div class="wrap"><a href="' + GOV + '"><img src="/assets/emblem.svg" alt="" width="18" height="18"> ' + esc(t("gov")) + "</a>" +
      '<div class="langs" role="group" aria-label="' + esc(t("lang")) + '">' + LANGS.map(function (l) { return '<button type="button" data-lang="' + l + '" aria-pressed="' + (l === LANG) + '">' + esc(I.langs[l]) + "</button>"; }).join("") + "</div></div></div>" +
      '<header class="head"><div class="wrap"><a class="brand" href="/"><span class="logo" aria-hidden="true">e</span><span><b>e-Irad</b><small>' + esc(t("tag")) + "</small></span></a>" +
      '<button class="burger" type="button" aria-expanded="false">' + esc(t("menu")) + '</button><nav aria-label="e-Irad"><ul>' +
      NAV.map(function (n) { return '<li><a href="' + n[1] + '"' + (n[0] === cur ? ' aria-current="page"' : "") + (n[0] === "login" ? ' class="loginlink"' : "") + ">" + esc(t("nav_" + n[0])) + "</a></li>"; }).join("") +
      "</ul></nav></div></header>" +
      '<div class="banner" role="status"><div class="wrap"><span class="dot" aria-hidden="true"></span><span>' + t("banner") + ' <a href="/status.html">' + esc(t("bannerMore")) + "</a></span></div></div>";
    $(".burger").addEventListener("click", function () { var h = $(".head"); var o = !h.classList.contains("open"); h.classList.toggle("open", o); this.setAttribute("aria-expanded", o); });
    $$("[data-lang]").forEach(function (b) { b.addEventListener("click", function () { setLang(b.getAttribute("data-lang")); }); });
    $("#bottom").innerHTML = '<footer class="foot"><div class="wrap"><div class="fcols"><div><div class="brand small"><span class="logo">e</span><b>e-Irad</b></div><p>' + esc(t("footAbout")) + "</p></div>" +
      "<div><h4>" + esc(t("footLinks")) + '</h4><ul><li><a href="/status.html">' + esc(t("nav_status")) + '</a></li><li><a href="/faq.html">' + esc(t("nav_faq")) + '</a></li><li><a href="/accessibility.html">' + esc(t("footAcc")) + '</a></li><li><a href="/contact.html">' + esc(t("nav_contact")) + "</a></li></ul></div>" +
      "<div><h4>" + esc(t("gov")) + '</h4><ul><li><a href="' + GOV + '">' + esc(t("footGov")) + '</a></li><li><a href="' + GOV + 'holidays.html">iradgov.org</a></li></ul><p class="tiny">' + esc(t("noPw")) + "</p></div></div>" +
      '<div class="fine">' + esc(t("footCopy", { y: iradNow().getFullYear() })) + "</div></div></footer>";
  }
  function setLang(l) {
    if (l === LANG) return; LANG = l;
    try { localStorage.setItem("eirad_lang", l); } catch (e) {}
    var u = new URL(location.href); if (u.searchParams.has("lang")) { u.searchParams.delete("lang"); history.replaceState(null, "", u.pathname + u.search); }
    render();
  }

  /* ---------- texts used by the flows ---------- */
  var X = {
    office: { en: "Office", ir: "Bölüm", ru: "Отдел" },
    document: { en: "Document", ir: "Dokument", ru: "Документ" },
    docs: {
      P: { en: "Passport, first issue", ir: "Pasport, birinchi jolu", ru: "Паспорт, впервые" },
      R: { en: "Passport, renewal or replacement", ir: "Pasport, almashtıruu", ru: "Паспорт, замена" },
      I: { en: "ID card", ir: "ID-karta", ru: "ID-карта" },
      C: { en: "Residence card (foreign nationals)", ir: "Jashoo kartası (chet el jarandarı)", ru: "Вид на жительство (иностранцы)" }
    },
    take: { en: "Take a number", ir: "Kezek nomerin aluu", ru: "Взять номер" },
    yourNo: { en: "Your number", ir: "Siziñ nomeriñiz", ru: "Ваш номер" },
    place: { en: "Place in the queue", ir: "Kezektegi ordu", ru: "Место в очереди" },
    wait: { en: "Estimated wait", ir: "Boljoldoo kütüü", ru: "Ожидаемое ожидание" },
    weeks: { en: "{a}–{b} weeks", ir: "{a}–{b} juma", ru: "{a}–{b} нед." },
    calledBy: { en: "Numbers are called on the board at the office. Check your place here; the estimate is recalculated each week.", ir: "Nomerler bölümdögü tablodo chakırılat. Ordunuzdu bul jerden tekshiriñiz; boljol ar juma kayra eseptelet.", ru: "Номера вызываются на табло в отделе. Проверяйте место здесь; оценка пересчитывается каждую неделю." },
    bring: { en: "Bring to the counter", ir: "Kassaga ala kelüüchü dokumentter", ru: "Принести в окошко" },
    bringList: {
      en: ["Your ID card or old passport, and your birth certificate for a first passport", "Two photographs, 3.5 × 4.5 cm", "Your residence registration", "The receipt for the state fee (passport IS 120, ID card IS 60, residence card IS 300), paid at any Talasbank branch"],
      ir: ["Jeke kuböölügüñüz je eski pasportuñuz, birinchi pasport üchün tuuluu tuuraluu kübölük", "3,5 × 4,5 sm eki süröt", "Jashoo jayı boyuncha kattoo", "Mamlekettik alım tölöngönü tuuraluu kvitantsiya (pasport 120 som, ID-karta 60 som, jashoo kartası 300 som), Talasbanktın kaalagan filialında tölönöt"],
      ru: ["Удостоверение личности или старый паспорт; для первого паспорта свидетельство о рождении", "Две фотографии 3,5 × 4,5 см", "Регистрация по месту жительства", "Квитанция об оплате госпошлины (паспорт 120 сомов, ID-карта 60, вид на жительство 300) в любом отделении «Таласбанка»"]
    },
    myTickets: { en: "Your numbers on this device", ir: "Bul tüzmöktögü nomerleriñiz", ru: "Ваши номера на этом устройстве" },
    taken: { en: "taken {d}", ir: "{d} alıngan", ru: "получен {d}" },
    remove: { en: "Remove", ir: "Öchürüü", ru: "Удалить" },
    checkTicket: { en: "Check a number taken earlier", ir: "Murda alıngan nomerdi tekshirüü", ru: "Проверить ранее полученный номер" },
    ticketPh: { en: "e.g. TL-P-0417", ir: "mısalı: TL-P-0417", ru: "например, TL-P-0417" },
    ticketBad: { en: "Numbers look like TL-P-0417. Numbers given at the office counter can be checked only at that office.", ir: "Nomerler TL-P-0417 sıyaktuu bolot. Bölümdün kassasında berilgen nomerlerdi oshol bölümdö gana tekshirüügö bolot.", ru: "Номер выглядит как TL-P-0417. Номера, выданные в окошке отдела, проверяются только в этом отделе." },
    yourTurn: { en: "Your number is due to be called within a week. Come to the office with your documents.", ir: "Nomeriñiz bir jumanın ichinde chakırılat. Dokumentteriñiz menen bölümgö keliñiz.", ru: "Ваш номер вызовут в течение недели. Приходите в отдел с документами." }
  };

  /* ---------- catalogue ---------- */
  function card(s) {
    return '<a class="svc" href="/service.html?id=' + s.id + '" data-kw="' + esc((L(s.name) + " " + L(s.desc) + " " + s.keywords + " " + s.name.en).toLowerCase()) + '">' + icon(s.icon) +
      '<span class="sbody"><span class="sname">' + esc(L(s.name)) + '</span><span class="sdesc">' + esc(L(s.desc)) + "</span>" + badge(s.status) + "</span></a>";
  }
  function pageHome() {
    var main = $("#app");
    main.innerHTML = '<section class="hero"><div class="wrap"><h1>' + esc(t("heroH")) + "</h1><p>" + esc(t("heroP")) + '</p><label class="srch"><span>' + esc(t("search")) + '</span><input type="search" id="q" autocomplete="off" placeholder="' + esc(t("searchPh")) + '"></label></div></section>' +
      '<div class="wrap page">' + S.cats.map(function (c) {
        var items = S.list.filter(function (s) { return s.cat === c; });
        return '<section class="cat" data-cat="' + c + '"><h2>' + esc(t("cat" + c.charAt(0).toUpperCase() + c.slice(1))) + '</h2><div class="svcs">' + items.map(card).join("") + "</div></section>";
      }).join("") + '<p class="nomatch" hidden>' + esc(t("noMatch")) + '</p><p class="note">' + esc(t("officeHoursNote")) + "</p></div>";
    var q = $("#q");
    q.addEventListener("input", function () {
      var v = q.value.trim().toLowerCase(), any = false;
      $$(".svc").forEach(function (a) { var ok = !v || a.getAttribute("data-kw").indexOf(v) >= 0; a.hidden = !ok; if (ok) any = true; });
      $$(".cat").forEach(function (c) { c.hidden = !$$(".svc", c).some(function (a) { return !a.hidden; }); });
      $(".nomatch").hidden = any;
    });
  }

  /* ---------- service page ---------- */
  function field(id, label, html) { return '<div class="fld"><label for="' + id + '">' + esc(label) + "</label>" + html + '<span class="err" id="' + id + '-err" hidden>' + esc(t("required")) + "</span></div>"; }
  function sel(id, opts) { return '<select id="' + id + '">' + opts.map(function (o) { return '<option value="' + esc(o[0]) + '">' + esc(o[1]) + "</option>"; }).join("") + "</select>"; }
  function inp(id, ph, extra) { return '<input id="' + id + '" type="text" autocomplete="off" spellcheck="false" placeholder="' + esc(ph || "") + '"' + (extra || "") + ">"; }
  function need(id, test) { var el = $("#" + id), ok = test ? test(el.value) : el.value.trim() !== ""; $("#" + id + "-err").hidden = ok; el.setAttribute("aria-invalid", !ok); if (!ok) el.focus(); return ok; }
  function payBox() { return '<div class="paybox"><button type="button" class="btn ghost paybtn">' + esc(t("payBtn")) + '</button><div class="payinfo" hidden role="alert"><h4>' + esc(t("payH")) + "</h4><p>" + esc(t("payP")) + "</p></div></div>"; }
  function wirePay(root) { $$(".paybtn", root).forEach(function (b) { b.addEventListener("click", function () { b.nextElementSibling.hidden = false; b.disabled = true; }); }); }
  function result(html) { var r = $("#result"); r.innerHTML = html; r.hidden = false; wirePay(r); r.scrollIntoView({ block: "nearest" }); }
  function kv(rows) { return '<dl class="kvs">' + rows.map(function (r) { return "<dt>" + esc(r[0]) + "</dt><dd>" + r[1] + "</dd>"; }).join("") + "</dl>"; }
  function noForm(e) { e.preventDefault(); }

  var FLOWS = {};
  var HELP = {};

  /* passport */
  function loadTickets() { try { return JSON.parse(localStorage.getItem("eirad_tickets") || "[]"); } catch (e) { return []; } }
  function saveTickets(a) { try { localStorage.setItem("eirad_tickets", JSON.stringify(a.slice(-6))); } catch (e) {} }
  function officeBy(code) { for (var i = 0; i < S.offices.length; i++) if (S.offices[i].code === code) return S.offices[i]; return null; }
  function queueFor(no, takenISO) {
    var m = /^([A-Z]{2})-([PRIC])-(\d{4})$/.exec(no); if (!m) return null;
    var o = officeBy(m[1]); if (!o) return null;
    var h = hash(no);
    var start = takenISO ? o.base + (h % Math.round(o.base * 0.15)) : Math.round(o.base * (0.25 + (h % 80) / 100));
    var weeksGone = takenISO ? Math.max(0, Math.floor((today() - new Date(takenISO + "T00:00:00Z")) / 604800000)) : 0;
    var pos = Math.max(1, start - weeksGone * o.rate);
    var a = Math.max(1, Math.floor(pos / o.rate)), b = Math.max(a + 1, Math.ceil(pos * 1.18 / o.rate));
    return { office: o, doc: m[2], pos: pos, a: a, b: b };
  }
  function queueCard(no, q) {
    return '<div class="ticket"><div class="tno"><span>' + esc(L(X.yourNo)) + "</span><b>" + esc(no) + "</b></div>" +
      kv([[L(X.office), esc(L(q.office.name))], [L(X.document), esc(L(X.docs[q.doc]))], [L(X.place), "<b>" + fmtN(q.pos) + "</b>"], [L(X.wait), q.a <= 1 ? esc(L(X.yourTurn)) : esc(L(X.weeks, { a: q.a, b: q.b }))]]) + "</div>";
  }
  FLOWS.passport = function (box) {
    box.innerHTML = '<form class="flow" id="f1">' +
      field("office", L(X.office), sel("office", S.offices.map(function (o) { return [o.code, L(o.name)]; }))) +
      field("doc", L(X.document), sel("doc", ["P", "R", "I", "C"].map(function (k) { return [k, L(X.docs[k])]; }))) +
      '<button class="btn" type="submit">' + esc(L(X.take)) + "</button></form>" +
      '<div id="result" class="result" hidden aria-live="polite"></div>' +
      '<div id="mytickets"></div>' +
      '<form class="flow inline" id="f2"><h3>' + esc(L(X.checkTicket)) + "</h3>" + field("tno", L(X.yourNo), inp("tno", L(X.ticketPh), ' maxlength="12"')) + '<button class="btn ghost" type="submit">' + esc(t("check")) + "</button></form>" +
      '<div id="result2" class="result" hidden aria-live="polite"></div>';
    function drawMine() {
      var a = loadTickets(), el = $("#mytickets");
      if (!a.length) { el.innerHTML = ""; return; }
      el.innerHTML = "<h3>" + esc(L(X.myTickets)) + "</h3>" + a.slice().reverse().map(function (tk) {
        var q = queueFor(tk.no, tk.d); if (!q) return "";
        return '<div class="mine">' + queueCard(tk.no, q) + '<p class="tiny">' + esc(L(X.taken, { d: fmtD(new Date(tk.d + "T00:00:00Z")) })) + ' · <button type="button" class="linkbtn" data-rm="' + esc(tk.no) + '">' + esc(L(X.remove)) + "</button></p></div>";
      }).join("");
      $$("[data-rm]", el).forEach(function (b) { b.addEventListener("click", function () { saveTickets(loadTickets().filter(function (x) { return x.no !== b.getAttribute("data-rm"); })); drawMine(); }); });
    }
    $("#f1").addEventListener("submit", function (e) {
      noForm(e);
      var o = $("#office").value, d = $("#doc").value;
      var n = (hash(o + d + Date.now() + Math.random()) % 9000) + 1000;
      var no = o + "-" + d + "-" + n, td = today().toISOString().slice(0, 10);
      var a = loadTickets(); a.push({ no: no, d: td }); saveTickets(a);
      var q = queueFor(no, td);
      result(queueCard(no, q) + '<p class="tiny">' + esc(L(X.calledBy)) + "</p><h4>" + esc(L(X.bring)) + "</h4><ul>" + L(X.bringList).map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>");
      drawMine();
    });
    $("#f2").addEventListener("submit", function (e) {
      noForm(e);
      var no = $("#tno").value.toUpperCase().replace(/\s/g, "");
      if (!need("tno")) return;
      var mine = loadTickets().filter(function (x) { return x.no === no; })[0];
      var q = queueFor(no, mine ? mine.d : null), r = $("#result2");
      r.hidden = false;
      r.innerHTML = q ? queueCard(no, q) : '<p class="warn">' + esc(L(X.ticketBad)) + "</p>";
    });
    drawMine();
  };
  HELP.passport = {
    en: "<h3>Where is the passport accepted?</h3><p>The Republic of Irad passport is accepted for travel by the states that maintain recognition of the Republic of Irad. Before you travel, ask the consulate of the country of destination whether it accepts the passport and whether you need a visa. For travel to the neighbouring states, check the rules at the crossing in advance.</p><p>The ISEZ does not object to residents also holding the documents of other states.</p><h3>Residence cards</h3><p>Residence cards for foreign nationals are issued at the Talas City and Nurzhan City offices only. A long-term card can be requested after ten years of residence.</p><h3>Lost passport</h3><p>Report a lost or stolen passport to the police first; bring the police certificate with your application for a replacement.</p>",
    ir: "<h3>Pasport kayda kabıl alınat?</h3><p>Irad Respublikasının pasportu Irad Respublikasın taanıgan mamleketter tarabınan saparga kabıl alınat. Saparga chıgaardan murun barchu ölkönün konsulduguna pasportu kabıl aların jana viza kerekpi ekenin surañız. Koñshu mamleketterge barsañız, ötkööldögü erejelerdi aldın ala tekshiriñiz.</p><p>IAEZ turgundardın bashka mamleketterdin dokumentterin da karmashına karshı emes.</p><h3>Jashoo kartaları</h3><p>Chet el jarandarı üchün jashoo kartaları Talas jana Nurzhan shaardık bölümdörüündö gana berilet. Uzak möönöttük kartanı on jıl jashagandan kiyin surasa bolot.</p><h3>Jogolgon pasport</h3><p>Jogolgon je uurdalgan pasport tuuraluu adegende politsiyaga kabarlañız; almashtıruu arızına politsiyanın maalımkatın tirkeñiz.</p>",
    ru: "<h3>Где принимается паспорт?</h3><p>Паспорт Республики Ирад принимается для поездок государствами, которые сохраняют признание Республики Ирад. Перед поездкой уточните в консульстве страны назначения, принимает ли она паспорт и нужна ли виза. При поездке в соседние государства заранее проверьте правила на переходе.</p><p>ОЭЗИ не возражает против того, чтобы жители имели также документы других государств.</p><h3>Вид на жительство</h3><p>Вид на жительство для иностранцев выдаётся только в паспортных столах Таласа и Нуржана. Долгосрочную карту можно запросить после десяти лет проживания.</p><h3>Утерянный паспорт</h3><p>Сначала сообщите об утере или краже в полицию; приложите справку полиции к заявлению о замене.</p>"
  };

  /* event permit */
  var EV = {
    city: { en: "City", ir: "Shaar", ru: "Город" },
    cities: { tl: { en: "Talas", ir: "Talas", ru: "Талас" }, nz: { en: "Nurzhan", ir: "Nurzhan", ru: "Нуржан" }, ij: { en: "Iyık Janyl", ir: "Iyık Janıl", ru: "Ийык-Джаныл" } },
    kind: { en: "Type of event", ir: "Ish-charanın türü", ru: "Вид мероприятия" },
    kinds: [["concert", { en: "Concert", ir: "Konsert", ru: "Концерт" }], ["festival", { en: "Festival or fair", ir: "Festival je yarmarka", ru: "Фестиваль или ярмарка" }], ["parade", { en: "Parade or procession", ir: "Parad je jürüsh", ru: "Шествие или парад" }], ["sport", { en: "Sports event", ir: "Sport ish-charası", ru: "Спортивное мероприятие" }], ["gathering", { en: "Public gathering", ir: "Kogomduk chogulush", ru: "Публичное собрание" }]],
    venue: { en: "Venue or route", ir: "Ötkörülüüchü jer je marshrut", ru: "Место или маршрут" },
    date: { en: "Date", ir: "Kün", ru: "Дата" },
    aud: { en: "Expected audience", ir: "Kütülgön kishi sanı", ru: "Ожидаемое число участников" },
    foreign: { en: "Performers from abroad", ir: "Chet eldik atkaruuchular", ru: "Исполнители из-за рубежа" },
    prep: { en: "Prepare application", ir: "Arız dayardoo", ru: "Подготовить заявку" },
    ref: { en: "Pre-application reference", ir: "Aldın ala arızdın nomeri", ru: "Номер предварительной заявки" },
    saved: { en: "Online submission is not yet available in the pilot. Write down this reference and take it to the permits counter with the documents below.", ir: "Sınoo mezgilinde onlayn jönötüü azırınca jok. Bul nomerdi jazıp alıp, tömöndögü dokumentter menen uruksat kassasına barıñız.", ru: "Онлайн-подача в пилотном режиме пока недоступна. Запишите номер и принесите его в окошко разрешений вместе с документами ниже." },
    counter: { tl: { en: "Talas City Hall, Central Square, permits counter (room 104). Road closures are considered by the transport committee on Wednesdays.", ir: "Talas meriyası, Borborduk ayant, uruksat kassası (104-bölmö). Joldordu jabuu maselesin transport komiteti sharshembi künderi karayt.", ru: "Мэрия Таласа, Центральная площадь, окно разрешений (комната 104). Перекрытие улиц рассматривает транспортный комитет по средам." }, nz: { en: "Nurzhan City Administration, House of Soviets, Central Square, permits office.", ir: "Nurzhan shaar administratsiyası, Sovetter Üyü, Borborduk ayant, uruksat bölümü.", ru: "Администрация Нуржана, Дом Советов, Центральная площадь, отдел разрешений." }, ij: { en: "Iyık Janyl City Hall, Lower Town, permits office. Processions on Cathedral Hill are agreed with the cathedral rector.", ir: "Iyık Janıl meriyası, Tömönkü shaar, uruksat bölümü. Chirköö döbösündögü jürüshtör sobor rektoru menen makuldashılat.", ru: "Мэрия Ийык-Джаныла, Нижний город, отдел разрешений. Шествия на Соборном холме согласуются с настоятелем собора." } },
    docsH: { en: "Bring", ir: "Ala keliñiz", ru: "Принесите" },
    docs: { en: ["The organiser's ID card or company registration", "The venue owner's written consent, or the route on a city plan", "The programme and expected number of people", "For ticketed events: the state fee receipt (IS 250)"], ir: ["Uyushturuuchunun jeke kuböölügü je kompaniyanın kattoo kübölügü", "Jaydın eesinin jazuu jüzündögü makuldugu je shaar planındagı marshrut", "Programma jana kütülgön kishi sanı", "Bilettüü ish-charalar üchün: mamlekettik alımdın kvitantsiyası (250 som)"], ru: ["Удостоверение организатора или регистрация компании", "Письменное согласие владельца площадки или маршрут на плане города", "Программа и ожидаемое число участников", "Для платных мероприятий: квитанция госпошлины (250 сомов)"] },
    dpi: { en: "Performers from abroad also need a performance permit from the Department of Public Information. Apply at least six weeks before the event.", ir: "Chet eldik atkaruuchular üchün Kogomduk maalımat departamentinin konsert uruksatı da kerek. Ish-charaga keminde altı juma kalganda kayrılıñız.", ru: "Для зарубежных исполнителей нужно также разрешение на выступление от Департамента общественной информации. Подавайте не позднее чем за шесть недель." },
    big: { en: "Events for more than 500 people need a police and fire-safety inspection of the venue, arranged by the city.", ir: "500dön ashık kishilik ish-charalar üchün shaar uyushturgan politsiya jana ört koopsuzdugu tekshirüüsü kerek.", ru: "Для мероприятий более чем на 500 человек нужна проверка площадки полицией и пожарной охраной, которую организует город." },
    gathering: { en: "Notice of a public gathering must be lodged at least ten days in advance. The city may propose another place or time.", ir: "Kogomduk chogulush tuuraluu keminde on kün murun kabarlash kerek. Shaar bashka jerdi je ubakıttı sunushu mümkün.", ru: "Уведомление о публичном собрании подаётся не позднее чем за десять дней. Город может предложить другое место или время." },
    late: { en: "Fewer than 30 days remain before this date. The city may not be able to consider the application in time.", ir: "Bul küngö 30 kündön az kaldı. Shaar arızdı öz ubaktısında karay albashı mümkün.", ru: "До этой даты осталось меньше 30 дней. Город может не успеть рассмотреть заявку." },
    past: { en: "Choose a date in the future.", ir: "Kelechektegi kündü tandañız.", ru: "Выберите будущую дату." },
    permit: { en: "Every event is subject to municipal permit.", ir: "Ar bir ish-chara shaardık uruksatka baylanıshtuu.", ru: "Любое мероприятие проводится при наличии муниципального разрешения." }
  };
  FLOWS.event = function (box) {
    box.innerHTML = '<form class="flow" id="fe">' +
      field("city", L(EV.city), sel("city", [["tl", L(EV.cities.tl)], ["nz", L(EV.cities.nz)], ["ij", L(EV.cities.ij)]])) +
      field("kind", L(EV.kind), sel("kind", EV.kinds.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("venue", L(EV.venue), inp("venue", "", ' maxlength="80"')) +
      field("edate", L(EV.date), '<input id="edate" type="date">') +
      field("aud", L(EV.aud), '<input id="aud" type="number" min="1" max="100000" inputmode="numeric">') +
      '<div class="fld chk"><label><input id="foreign" type="checkbox"> ' + esc(L(EV.foreign)) + "</label></div>" +
      '<button class="btn" type="submit">' + esc(L(EV.prep)) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#fe").addEventListener("submit", function (e) {
      noForm(e);
      if (!need("venue") || !need("edate") || !need("aud", function (v) { return +v > 0; })) return;
      var d = new Date($("#edate").value + "T00:00:00Z"), days = Math.round((d - today()) / 86400000);
      if (days < 0) { $("#edate-err").textContent = L(EV.past); $("#edate-err").hidden = false; return; }
      var c = $("#city").value, k = $("#kind").value, aud = +$("#aud").value;
      var ref = c.toUpperCase() + "-EV-" + String(iradNow().getFullYear()).slice(2) + "-" + pad5(hash(c + k + $("#venue").value + $("#edate").value) % 100000);
      var notes = [];
      if (days < 30) notes.push('<p class="warn">' + esc(L(EV.late)) + "</p>");
      if ($("#foreign").checked) notes.push("<p>" + esc(L(EV.dpi)) + "</p>");
      if (aud > 500) notes.push("<p>" + esc(L(EV.big)) + "</p>");
      if (k === "gathering") notes.push("<p>" + esc(L(EV.gathering)) + "</p>");
      result('<div class="ticket"><div class="tno"><span>' + esc(L(EV.ref)) + "</span><b>" + esc(ref) + "</b></div>" + kv([[L(EV.date), esc(fmtD(d))], [L(EV.city), esc(L(EV.cities[c]))]]) + "</div><p>" + esc(L(EV.saved)) + "</p><p><b>" + esc(L(EV.counter[c])) + "</b></p><h4>" + esc(L(EV.docsH)) + "</h4><ul>" + L(EV.docs).map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" + notes.join("") + '<p class="tiny">' + esc(L(EV.permit)) + "</p>");
    });
  };
  function pad5(n) { return ("00000" + n).slice(-5); }
  HELP.event = {
    en: "<h3>Who issues the permit?</h3><p>Concerts, fairs, parades and gatherings in a city need a permit from the city council, issued through City Hall. Performances by foreign ensembles and public film screenings also need a permit from the Department of Public Information. Outside the cities, apply to the district administration.</p><h3>Tickets</h3><p>Tickets may be sold, and advertised as on sale, only after the permit has been issued.</p>",
    ir: "<h3>Uruksattı kim beret?</h3><p>Shaardagı konsertter, yarmarkalar, paraddar jana chogulushtar üchün meriya arkıluu berilüüchü shaar keñeshinin uruksatı kerek. Chet eldik ansambldardın chıguuları jana kinonu elge körsötüü üchün Kogomduk maalımat departamentinin uruksatı da kerek. Shaardan tıshkarı aymaktık administratsiyaga kayrılıñız.</p><h3>Biletter</h3><p>Biletterdi uruksat berilgenden kiyin gana satuuga jana jarnamaloogo bolot.</p>",
    ru: "<h3>Кто выдаёт разрешение?</h3><p>Для концертов, ярмарок, шествий и собраний в городе нужно разрешение городского совета, которое выдаётся через мэрию. Для выступлений зарубежных коллективов и публичных кинопоказов нужно также разрешение Департамента общественной информации. За пределами городов обращайтесь в районную администрацию.</p><h3>Билеты</h3><p>Продавать и рекламировать билеты можно только после выдачи разрешения.</p>"
  };

  /* business */
  var BZ = {
    form: { en: "Legal form", ir: "Uyushmanın forması", ru: "Организационная форма" },
    forms: [["st", { en: "Sole trader", ir: "Jeke ishker", ru: "Индивидуальный предприниматель" }], ["llc", { en: "Limited company", ir: "Joopkerchiligi chektelgen koom", ru: "Общество с ограниченной ответственностью" }], ["farm", { en: "Farm", ir: "Dıykan charbası", ru: "Фермерское хозяйство" }], ["coop", { en: "Cooperative", ir: "Kooperativ", ru: "Кооператив" }]],
    act: { en: "Main activity", ir: "Negizgi ish", ru: "Основной вид деятельности" },
    acts: [["trade", { en: "Shop or market stall", ir: "Dükön je bazar ordu", ru: "Магазин или торговое место" }], ["food", { en: "Café, canteen or bakery", ir: "Kafe, ashkana je nan bıshıruuchu jay", ru: "Кафе, столовая или пекарня" }], ["craft", { en: "Workshop or crafts", ir: "Ustakana je kol önörü", ru: "Мастерская или ремесло" }], ["transport", { en: "Transport or taxi", ir: "Transport je taksi", ru: "Транспорт или такси" }], ["agri", { en: "Farming or livestock", ir: "Dıykanchılık je mal charbası", ru: "Земледелие или животноводство" }], ["print", { en: "Publishing or printing", ir: "Basma je basmakana", ru: "Издательство или типография" }], ["it", { en: "Services, IT or consulting", ir: "Kızmattar, IT je konsalting", ru: "Услуги, ИТ или консалтинг" }]],
    district: { en: "District or city", ir: "Aymak je shaar", ru: "Район или город" },
    name: { en: "Proposed business name", ir: "Sunushtalgan at", ru: "Предлагаемое название" },
    checkName: { en: "Check name", ir: "Attı tekshirüü", ru: "Проверить название" },
    free: { en: "The name “{n}” is available. It is not reserved until registration is completed.", ir: "“{n}” degen at bosh. Kattoo bütkönchö al ech kimge bekitilbeyt.", ru: "Название «{n}» свободно. До завершения регистрации оно не закрепляется." },
    taken: { en: "A business with a similar name, “{n}”, is already registered in this district. Choose another name or add a distinguishing word.", ir: "Bul aymakta “{n}” degen okshosh attagı ishkana kattalgan. Bashka at tandañız je ayırmaluu söz koshuñuz.", ru: "В этом районе уже зарегистрировано предприятие с похожим названием «{n}». Выберите другое название или добавьте отличительное слово." },
    prot: { en: "Names containing words such as “Irad”, “State”, “National”, “Governor” or registered trademarks need the approval of the Ministry of Economy. Your application will take longer.", ir: "“Irad”, “Mamlekettik”, “Uluttuk”, “Gubernator” sıyaktuu sözdördü je kattalgan sooda belgilerin kamtıgan attar üchün Ekonomika ministrliginin makuldugu kerek. Arızıñız uzagıraak karalat.", ru: "Названия со словами «Ирад», «государственный», «национальный», «губернатор» или с зарегистрированными товарными знаками требуют согласования Министерства экономики. Рассмотрение займёт больше времени." },
    nextH: { en: "Next: visit your district office with originals", ir: "Kiyinki kadam: asıl dokumentter menen aymaktık keñsege barıñız", ru: "Дальше: обратитесь в районный отдел с оригиналами" },
    docs: {
      en: ["Your ID card and residence registration", "Proof of premises: lease, ownership certificate or the owner's letter", "Receipt for the state fee, paid at Talasbank: sole trader IS 150, company or cooperative IS 600, farm IS 100", "For a company or cooperative: the charter signed by all founders", "For a farm: the land-use certificate"],
      ir: ["Jeke kuböölügüñüz jana jashoo jayı boyuncha kattoo", "Jaydı tastıktagan dokument: ijara kelishimi, menchik kübölügü je eesinin katı", "Talasbankta tölöngön mamlekettik alımdın kvitantsiyası: jeke ishker 150 som, kompaniya je kooperativ 600 som, dıykan charbası 100 som", "Kompaniya je kooperativ üchün: bardık negizdööchülör kol koygon ustav", "Dıykan charbası üchün: jerdi paydaluu kübölügü"],
      ru: ["Удостоверение личности и регистрация по месту жительства", "Документ на помещение: договор аренды, свидетельство о собственности или письмо владельца", "Квитанция госпошлины, оплаченной в «Таласбанке»: ИП 150 сомов, компания или кооператив 600, ферма 100", "Для компании или кооператива: устав, подписанный всеми учредителями", "Для фермы: свидетельство о землепользовании"]
    },
    printNote: { en: "Publishers and printers must also register with the Department of Public Information before they publish.", ir: "Basma üylör jana basmakanalar basıp chıgaraardan murun Kogomduk maalımat departamentinde da kattalıshı kerek.", ru: "Издатели и типографии до начала выпуска должны также зарегистрироваться в Департаменте общественной информации." },
    foodNote: { en: "Food businesses need a sanitary certificate from the city health inspectorate before opening.", ir: "Tamak-ash ishkanalarına achılardan murun shaardık sanitardık inspektsiyanın kübölügü kerek.", ru: "Предприятиям питания до открытия нужно санитарное заключение городской санинспекции." },
    taxiNote: { en: "Taxi and passenger transport also need a carrier's licence from the Department of Infrastructure and Communications.", ir: "Taksi jana jürgünchü tashuu üchün Infrastruktura jana baylanısh departamentinin tashuuchu litsenziyası da kerek.", ru: "Для такси и пассажирских перевозок нужна также лицензия перевозчика Департамента инфраструктуры и связи." },
    oneVisit: { en: "If your documents are complete, registration is completed in one visit and the certificate is issued within five working days.", ir: "Dokumentteriñiz toluk bolso, kattoo bir barganda bütöt, kübölük besh ish kündün ichinde berilet.", ru: "Если документы в порядке, регистрация оформляется за одно посещение, свидетельство выдаётся в течение пяти рабочих дней." }
  };
  var DISTRICTS = [["tl", { en: "Talas (city)", ir: "Talas (shaar)", ru: "Талас (город)" }], ["nz", { en: "Nurzhan (city)", ir: "Nurzhan (shaar)", ru: "Нуржан (город)" }], ["ij", { en: "Iyık Janyl (city)", ir: "Iyık Janıl (shaar)", ru: "Ийык-Джаныл (город)" }], ["chu", { en: "Chu District", ir: "Chüy aymagı", ru: "Чуйский район" }], ["kb", { en: "Kara-Buura District", ir: "Kara-Buura aymagı", ru: "Кара-Бууринский район" }], ["td", { en: "Talas District", ir: "Talas aymagı", ru: "Таласский район" }], ["ln", { en: "Lower Naryn District", ir: "Tömönkü Narın aymagı", ru: "Нижненарынский район" }], ["tok", { en: "Toktogul District", ir: "Toktogul aymagı", ru: "Токтогульский район" }], ["sb", { en: "Sary-Bulak District", ir: "Sarı-Bulak aymagı", ru: "Сары-Булакский район" }]];
  FLOWS.business = function (box) {
    box.innerHTML = '<form class="flow" id="fb">' +
      field("bform", L(BZ.form), sel("bform", BZ.forms.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("bact", L(BZ.act), sel("bact", BZ.acts.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("bdist", L(BZ.district), sel("bdist", DISTRICTS.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("bname", L(BZ.name), inp("bname", "", ' maxlength="60"')) +
      '<button class="btn" type="submit">' + esc(L(BZ.checkName)) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#fb").addEventListener("submit", function (e) {
      noForm(e);
      if (!need("bname")) return;
      var n = $("#bname").value.trim().replace(/\s+/g, " "), low = n.toLowerCase(), h = hash(low + $("#bdist").value);
      var msg;
      if (/irad|state|national|govern|mamleket|uluttuk|gubern|tulpar|nurgaz|attelkom|государ|национ|ирад|губерн/.test(low)) msg = '<p class="warn">' + esc(L(BZ.prot)) + "</p>";
      else if (h % 5 === 0) msg = '<p class="warn">' + esc(L(BZ.taken, { n: n + (h % 2 ? " Plus" : "-" + (2 + h % 7)) })) + "</p>";
      else msg = '<p class="ok">' + esc(L(BZ.free, { n: n })) + "</p>";
      var act = $("#bact").value, extra = act === "print" ? BZ.printNote : act === "food" ? BZ.foodNote : act === "transport" ? BZ.taxiNote : null;
      var docs = L(BZ.docs).filter(function (x, i) { var f = $("#bform").value; return i < 3 || (i === 3 && (f === "llc" || f === "coop")) || (i === 4 && f === "farm"); });
      result(msg + "<h4>" + esc(L(BZ.nextH)) + "</h4><ul>" + docs.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" + (extra ? "<p>" + esc(L(extra)) + "</p>" : "") + '<p class="tiny">' + esc(L(BZ.oneVisit)) + "</p>");
    });
  };
  HELP.business = {
    en: "<h3>Why can't I register online?</h3><p>The register of firms requires the founder's signature on the application in front of a registrar and the original documents. Online registration with an e-Irad card is planned after the pilot.</p><h3>Census of business entities</h3><p>Registered and unregistered businesses are being counted until 30 November. Taking part in the census does not register a business, and registering does not replace the census questionnaire.</p>",
    ir: "<h3>Emne üchün onlayn kattala albaym?</h3><p>Firmalar reestri arızga negizdööchünün registratordun aldında kol koyushun jana asıl dokumentterdi talap kılat. e-Irad kartası menen onlayn kattoo sınoo mezgilinen kiyin plandashtırılgan.</p><h3>Ishkanalardın sanagı</h3><p>Kattalgan jana kattalbagan ishkanalar 30-noyabrga cheyin sanalat. Sanakka katıshuu ishkananı kattabayt, kattoo sanaktın suroo-joop kagazın almashtırbayt.</p>",
    ru: "<h3>Почему нельзя зарегистрироваться онлайн?</h3><p>Реестр фирм требует подписи учредителя на заявлении в присутствии регистратора и оригиналов документов. Онлайн-регистрация с картой e-Irad планируется после пилота.</p><h3>Перепись хозяйствующих субъектов</h3><p>До 30 ноября проходит учёт зарегистрированных и незарегистрированных предприятий. Участие в переписи не регистрирует предприятие, а регистрация не заменяет анкету переписи.</p>"
  };

  /* census (information) */
  FLOWS.census = function (box) {
    box.innerHTML = '<div class="flow">' + L({
      en: "<p>The census of business entities runs from 15 October to 30 November 2026. You can answer in one of three ways:</p><ol><li><b>When the enumerator visits.</b> Enumerators carry a Territorial Statistics Office card with a photograph and never ask for payment. The questionnaire takes about 25 minutes.</li><li><b>At an Attelkom service point,</b> on the terminal, with the help of the staff.</li><li><b>On e-Irad.</b> The online questionnaire will open here in November.</li></ol><p>Answers are used for statistics only and are not passed to tax inspectors.</p>",
      ir: "<p>Ishkanalardın sanagı 2026-jıldın 15-oktyabrınan 30-noyabrına cheyin ötöt. Üch jol menen joop berse bolot:</p><ol><li><b>Kattoochu kelgende.</b> Kattoochulardın süröttüü Aymaktık statistika keñsesinin kartası bolot, alar ech kachan akcha surabayt. Suroo-joop 25 minutaga jakın ubakıt alat.</li><li><b>Attelkomdun kızmat punktunda,</b> terminalda, kızmatkerlerdin jardamı menen.</li><li><b>e-Iradda.</b> Onlayn suroo-joop bul jerde noyabrda achılat.</li></ol><p>Jooptor statistika üchün gana koldonulat jana salık inspektorloruna berilbeyt.</p>",
      ru: "<p>Перепись хозяйствующих субъектов проходит с 15 октября по 30 ноября 2026 года. Ответить можно тремя способами:</p><ol><li><b>Когда придёт счётчик.</b> У счётчиков есть удостоверение Территориального статистического управления с фотографией; они никогда не просят денег. Анкета занимает около 25 минут.</li><li><b>В пункте обслуживания «Аттелкома»,</b> на терминале, с помощью сотрудников.</li><li><b>На e-Irad.</b> Онлайн-анкета откроется здесь в ноябре.</li></ol><p>Ответы используются только для статистики и не передаются налоговым инспекторам.</p>"
    }) + '<button class="btn" type="button" disabled>' + esc(L({ en: "Online questionnaire (opens in November)", ir: "Onlayn suroo-joop (noyabrda achılat)", ru: "Онлайн-анкета (откроется в ноябре)" })) + "</button></div>";
  };

  /* electricity and water */
  var BILL = {
    network: { en: "Network", ir: "Tarmak", ru: "Сеть" },
    nets: [["tl", { en: "Talas Electric Networks", ir: "Talas elektr tarmaktarı", ru: "Таласские электросети" }], ["nz", { en: "Nurzhan Electric Networks", ir: "Nurzhan elektr tarmaktarı", ru: "Нуржанские электросети" }], ["dist", { en: "Iradenergo district service (Iyık Janyl and the districts)", ir: "Iradenergonun aymaktık kızmatı (Iyık Janıl jana aymaktar)", ru: "Районная служба «Ирадэнерго» (Ийык-Джаныл и районы)" }]],
    acct: { en: "Personal account number", ir: "Jeke esep nomeri", ru: "Номер лицевого счёта" },
    acctPh: { en: "8 to 12 digits, from your last bill", ir: "8den 12ge cheyin sıfra, akırkı eseptten", ru: "от 8 до 12 цифр, с последней квитанции" },
    acctBad: { en: "The account number has 8 to 12 digits and is printed at the top of your bill.", ir: "Esep nomeri 8den 12ge cheyin sıfradan turat jana eseptin jogorkusunda basılgan.", ru: "Номер лицевого счёта состоит из 8–12 цифр и напечатан вверху квитанции." },
    period: { en: "Billing period", ir: "Esep mezgili", ru: "Расчётный период" },
    readings: { en: "Meter readings", ir: "Hisoochtun körsötküchü", ru: "Показания счётчика" },
    used: { en: "Consumption", ir: "Sarptalganı", ru: "Расход" },
    tariff: { en: "Household tariff", ir: "Turmushtuk tarif", ru: "Бытовой тариф" },
    arrears: { en: "Unpaid from earlier periods", ir: "Murdagı mezgilderden tölönbögönü", ru: "Задолженность за прошлые периоды" },
    due: { en: "Amount due", ir: "Tölönüüchü summa", ru: "К оплате" },
    dueBy: { en: "Pay by", ir: "Tölöö möönötü", ru: "Оплатить до" },
    show: { en: "Show bill", ir: "Esepti körsötüü", ru: "Показать счёт" },
    acctNo: { en: "Account", ir: "Esep", ru: "Лицевой счёт" },
    wcity: { en: "Water enterprise", ir: "Suu ishkanası", ru: "Водоканал" },
    wnets: [["tl", { en: "Talas City Water Enterprise", ir: "Talas shaardık suu ishkanası", ru: "Таласский городской водоканал" }], ["nz", { en: "Nurzhan Vodokanal", ir: "Nurzhan Vodokanalı", ru: "Нуржанский водоканал" }], ["ij", { en: "Iyık Janyl City Water Enterprise", ir: "Iyık Janıl shaardık suu ishkanası", ru: "Водоканал Ийык-Джаныла" }]],
    persons: { en: "Registered residents", ir: "Kattalgan turgundar", ru: "Зарегистрировано жильцов" },
    wrate: { en: "Water, per person a month", ir: "Suu, bir kishige aylık", ru: "Вода, на человека в месяц" },
    srate: { en: "Sewerage, per person a month", ir: "Kanalizatsiya, bir kishige aylık", ru: "Канализация, на человека в месяц" },
    winter: { en: "Heating is billed separately by the city heating enterprise.", ir: "Jılytuu üchün esepti shaardık jılytuu ishkanası öznchö chıgarat.", ru: "Отопление выставляет отдельно городское теплопредприятие." }
  };
  function lastMonth() { var d = today(); return new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - 1, 1)); }
  function monthName(d) { var M = I.ui[LANG].months, n = M[d.getUTCMonth()]; if (LANG === "ru") n = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"][d.getUTCMonth()]; return n.charAt(0).toUpperCase() + n.slice(1) + " " + d.getUTCFullYear(); }
  function dueDate() { var d = today(); return new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 25)); }
  function mask(a) { return "••••" + a.slice(-4); }
  FLOWS.electricity = function (box) {
    box.innerHTML = '<form class="flow" id="fel">' + field("net", L(BILL.network), sel("net", BILL.nets.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("acct", L(BILL.acct), inp("acct", L(BILL.acctPh), ' inputmode="numeric" maxlength="14"')) + '<button class="btn" type="submit">' + esc(L(BILL.show)) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#fel").addEventListener("submit", function (e) {
      noForm(e);
      var a = $("#acct").value.replace(/\D/g, "");
      if (!need("acct", function () { return a.length >= 8 && a.length <= 12; })) { $("#acct-err").textContent = L(BILL.acctBad); return; }
      var h = hash("el" + $("#net").value + a);
      if (h % 13 === 0) { result('<p class="warn">' + esc(t("notFound")) + "</p>"); return; }
      var prev = 10000 + (h % 80000), kwh = 140 + (h % 260), tariff = 0.32, arr = h % 7 === 0 ? Math.round((90 + h % 70) * tariff * 100) / 100 * 1 : 0;
      var amt = Math.round(kwh * tariff * 100) / 100, total = amt + arr;
      result(kv([[L(BILL.acctNo), esc(mask(a))], [L(BILL.period), esc(monthName(lastMonth()))], [L(BILL.readings), fmtN(prev) + " → " + fmtN(prev + kwh)], [L(BILL.used), fmtN(kwh) + " kWh"], [L(BILL.tariff), som(tariff) + " / kWh"]].concat(arr ? [[L(BILL.arrears), som(arr)]] : []).concat([[L(BILL.due), "<b>" + som(total) + "</b>"], [L(BILL.dueBy), esc(fmtD(dueDate()))]])) + payBox());
    });
  };
  FLOWS.water = function (box) {
    box.innerHTML = '<form class="flow" id="fw">' + field("wnet", L(BILL.wcity), sel("wnet", BILL.wnets.map(function (k) { return [k[0], L(k[1])]; }))) +
      field("acct", L(BILL.acct), inp("acct", L(BILL.acctPh), ' inputmode="numeric" maxlength="14"')) + '<button class="btn" type="submit">' + esc(L(BILL.show)) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#fw").addEventListener("submit", function (e) {
      noForm(e);
      var a = $("#acct").value.replace(/\D/g, "");
      if (!need("acct", function () { return a.length >= 8 && a.length <= 12; })) { $("#acct-err").textContent = L(BILL.acctBad); return; }
      var h = hash("wa" + $("#wnet").value + a);
      if (h % 11 === 0) { result('<p class="warn">' + esc(t("notFound")) + "</p>"); return; }
      var p = 1 + (h % 6), wr = 14.8, sr = 6.2, total = Math.round(p * (wr + sr) * 100) / 100;
      result(kv([[L(BILL.acctNo), esc(mask(a))], [L(BILL.period), esc(monthName(lastMonth()))], [L(BILL.persons), String(p)], [L(BILL.wrate), som(wr)], [L(BILL.srate), som(sr)], [L(BILL.due), "<b>" + som(total) + "</b>"], [L(BILL.dueBy), esc(fmtD(dueDate()))]]) + '<p class="tiny">' + esc(L(BILL.winter)) + "</p>" + payBox());
    });
  };
  HELP.electricity = {
    en: "<h3>Where else can I pay?</h3><p>At any Talasbank branch, at Irad Pochtasy counters and at the cash desks of Talas and Nurzhan Electric Networks. Keep the receipt until the next bill shows the payment.</p><h3>Meter readings</h3><p>Readings are taken by the network's inspectors once a month. If you think a reading is wrong, call the network's office with your account number.</p>",
    ir: "<h3>Dagı kayda tölösö bolot?</h3><p>Talasbanktın kaalagan filialında, Irad Pochtasının kassalarında jana Talas, Nurzhan elektr tarmaktarının kassalarında. Kiyinki esepte tölöm körüngönchö kvitantsiyanı saktañız.</p><h3>Hisoochtun körsötküchü</h3><p>Körsötküchtü tarmaktın inspektorloru ayına bir jolu alat. Kata bar dep oylosoñuz, esep nomeriñiz menen tarmaktın keñsesine chalıñız.</p>",
    ru: "<h3>Где ещё можно оплатить?</h3><p>В любом отделении «Таласбанка», в окошках «Ирадпочты» и в кассах Таласских и Нуржанских электросетей. Сохраняйте квитанцию, пока оплата не отразится в следующем счёте.</p><h3>Показания счётчика</h3><p>Показания снимают контролёры сети раз в месяц. Если вы считаете, что показания неверны, позвоните в отделение сети и назовите номер лицевого счёта.</p>"
  };
  HELP.water = HELP.electricity;

  /* plates: fines and motor policy */
  var PL = {
    plate: { en: "Registration plate", ir: "Mamlekettik nomer", ru: "Госномер" },
    platePh: { en: "as on the plate", ir: "nomerdegidey", ru: "как на номерном знаке" },
    plateBad: { en: "Enter the plate as it appears, 4 to 10 letters and digits.", ir: "Nomerdi 4tön 10go cheyin tamga jana sıfra menen jazıñız.", ru: "Введите номер как на знаке: от 4 до 10 букв и цифр." },
    none: { en: "No unpaid fines are recorded for {p}.", ir: "{p} üchün tölönbögön ayıp jok.", ru: "Неоплаченных штрафов по номеру {p} нет." },
    some: { en: "Unpaid fines for {p}", ir: "{p} üchün tölönbögön ayıptar", ru: "Неоплаченные штрафы по номеру {p}" },
    thD: { en: "Date", ir: "Kün", ru: "Дата" }, thO: { en: "Offence and place", ir: "Ukuk buzuu jana jer", ru: "Нарушение и место" }, thA: { en: "Amount", ir: "Summa", ru: "Сумма" },
    total: { en: "Total", ir: "Bardıgı", ru: "Итого" },
    half: { en: "Half the fine is waived if paid within 20 days of the notice. To dispute a fine, write to the Highway Patrol Corps within 10 days.", ir: "Bildirüüdön kiyin 20 kündün ichinde tölönsö, ayıptın jarımı kechilet. Ayıpka makul bolboso, 10 kündün ichinde Avtojol patrul korpusuna jazıñız.", ru: "При оплате в течение 20 дней с даты уведомления половина штрафа списывается. Обжаловать штраф можно письменно в Корпус дорожного патруля в течение 10 дней." },
    offs: [
      [{ en: "Speeding, camera: Trans-Talas Highway, km {k}", ir: "Ildamdıktı ashuu, kamera: Trans-Talas jolu, {k}-km", ru: "Превышение скорости, камера: Транс-Таласская трасса, {k} км" }, 150],
      [{ en: "Parking in a no-parking zone: Liberty Boulevard, Talas", ir: "Toktotuuga tıyuu salıngan jerde turuu: Erkindik bulvarı, Talas", ru: "Стоянка в запрещённом месте: бульвар Свободы, Талас" }, 50],
      [{ en: "Seat belt not worn: Kök-Bel road, Toguz-Bulak post", ir: "Koopsuzduk kurı takılgan emes: Kök-Bel jolu, Toguz-Bulak postu", ru: "Не пристёгнут ремень: дорога Кок-Бел, пост Тогуз-Булак" }, 75],
      [{ en: "Red light: Azatlık Prospect, Nurzhan", ir: "Kızıl jarık: Azattık prospekti, Nurzhan", ru: "Проезд на красный: проспект Азатлык, Нуржан" }, 200],
      [{ en: "Speeding, camera: Fergana Mountain Transit Highway, km {k}", ir: "Ildamdıktı ashuu, kamera: Fergana tooluu tranzit jolu, {k}-km", ru: "Превышение скорости, камера: Ферганская горная трасса, {k} км" }, 150],
      [{ en: "No technical inspection certificate: Talas–Nurzhan road", ir: "Tekhnikalık karoo kübölügü jok: Talas–Nurzhan jolu", ru: "Нет талона техосмотра: дорога Талас–Нуржан" }, 100]
    ],
    valid: { en: "Valid policy", ir: "Jaraktuu polis", ru: "Действующий полис" },
    expired: { en: "Policy expired", ir: "Polistin möönötü bütkön", ru: "Срок полиса истёк" },
    susp: { en: "Policy suspended: premium unpaid", ir: "Polis toktotulgan: tölöm jok", ru: "Полис приостановлен: взнос не оплачен" },
    noPol: { en: "No compulsory policy is recorded for {p}. Policies bought in the last five working days may not yet be on the register.", ir: "{p} üchün mildettüü polis kattalgan emes. Akırkı besh ish kündö satılıp alıngan polister reestrge ali kire elek bolushu mümkün.", ru: "Обязательный полис по номеру {p} не зарегистрирован. Полисы, купленные за последние пять рабочих дней, могут ещё не быть в реестре." },
    polNo: { en: "Policy number", ir: "Polistin nomeri", ru: "Номер полиса" },
    until: { en: "Valid until", ir: "Möönötü", ru: "Действует до" },
    ended: { en: "Expired on", ir: "Möönötü bütkön kün", ru: "Истёк" },
    office: { en: "Issued by", ir: "Bergen", ru: "Выдан" },
    offices: [{ en: "Iradstrakh, Talas head office", ir: "Iradstrakh, Talas bash keñsesi", ru: "«Ирадстрах», головной офис, Талас" }, { en: "Iradstrakh, Nurzhan office", ir: "Iradstrakh, Nurzhan keñsesi", ru: "«Ирадстрах», офис в Нуржане" }, { en: "Iradstrakh, Kyzyl-Adyr office", ir: "Iradstrakh, Kızıl-Adır keñsesi", ru: "«Ирадстрах», офис в Кызыл-Адыре" }, { en: "Iradstrakh, Tash-Kömür office", ir: "Iradstrakh, Tash-Kömür keñsesi", ru: "«Ирадстрах», офис в Таш-Кумыре" }, { en: "Iradstrakh agent, Chu Gate crossing", ir: "Iradstrakhtın agenti, Chüy darbazası ötköölü", ru: "Агент «Ирадстраха», переход Чуйские ворота" }],
    renew: { en: "Driving without a valid compulsory policy is an offence. A policy can be bought at any Iradstrakh office; the premium for a private car is IS 380 a year.", ir: "Jaraktuu mildettüü polissiz unaa aydoo ukuk buzuu bolup sanalat. Polisti Iradstrakhtın kaalagan keñsesinen satıp alsa bolot; jeke unaa üchün jılına 380 som.", ru: "Езда без действующего обязательного полиса является нарушением. Полис можно купить в любом офисе «Ирадстраха»; взнос для личного автомобиля 380 сомов в год." }
  };
  function plateOk(v) { var p = norm(v); return /^[A-Z0-9АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЭЮЯ]{4,10}$/.test(p); }
  function plateForm(box, id, cb) {
    box.innerHTML = '<form class="flow" id="' + id + '">' + field("plate", L(PL.plate), inp("plate", L(PL.platePh), ' maxlength="14" style="text-transform:uppercase"')) + '<button class="btn" type="submit">' + esc(t("check")) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#" + id).addEventListener("submit", function (e) {
      noForm(e);
      if (!need("plate", plateOk)) { $("#plate-err").textContent = L(PL.plateBad); return; }
      cb(norm($("#plate").value));
    });
  }
  FLOWS.fines = function (box) {
    plateForm(box, "ff", function (p) {
      var h = hash("fi" + p), n = h % 3 === 0 ? 0 : 1 + (h % 3);
      if (!n) { result('<p class="ok">' + esc(L(PL.none, { p: p })) + "</p>"); return; }
      var rows = [], sum = 0;
      for (var i = 0; i < n; i++) {
        var hh = hash(p + i), o = PL.offs[hh % PL.offs.length], d = addDays(today(), -(3 + hh % 55));
        sum += o[1];
        rows.push("<tr><td>" + esc(fmtD(d)) + "</td><td>" + esc(L(o[0], { k: 20 + hh % 170 })) + '</td><td class="num">' + som(o[1]) + "</td></tr>");
      }
      result("<h4>" + esc(L(PL.some, { p: p })) + '</h4><div class="tw"><table class="tbl"><thead><tr><th>' + esc(L(PL.thD)) + "</th><th>" + esc(L(PL.thO)) + '</th><th class="num">' + esc(L(PL.thA)) + "</th></tr></thead><tbody>" + rows.join("") + '</tbody><tfoot><tr><td></td><td>' + esc(L(PL.total)) + '</td><td class="num"><b>' + som(sum) + "</b></td></tr></tfoot></table></div><p class=\"tiny\">" + esc(L(PL.half)) + "</p>" + payBox());
    });
  };
  FLOWS.motor = function (box) {
    plateForm(box, "fm", function (p) {
      var h = hash("ms" + p), k = h % 10, office = L(PL.offices[(h >>> 4) % PL.offices.length]), pol = "ISM-" + String(26 - (k > 5 ? 1 : 0)) + "-" + ("000000" + (h % 1000000)).slice(-6);
      if (k <= 5) result('<p class="ok">' + esc(L(PL.valid)) + "</p>" + kv([[L(PL.plate), esc(p)], [L(PL.polNo), esc(pol)], [L(PL.until), esc(fmtD(addDays(today(), 12 + (h >>> 3) % 340)))], [L(PL.office), esc(office)]]));
      else if (k <= 7) result('<p class="warn">' + esc(L(PL.expired)) + "</p>" + kv([[L(PL.plate), esc(p)], [L(PL.polNo), esc(pol)], [L(PL.ended), esc(fmtD(addDays(today(), -(1 + (h >>> 3) % 90))))], [L(PL.office), esc(office)]]) + "<p>" + esc(L(PL.renew)) + "</p>");
      else if (k === 8) result('<p class="warn">' + esc(L(PL.susp)) + "</p>" + kv([[L(PL.plate), esc(p)], [L(PL.polNo), esc(pol)], [L(PL.office), esc(office)]]) + "<p>" + esc(L(PL.renew)) + "</p>");
      else result('<p class="warn">' + esc(L(PL.noPol, { p: p })) + "</p><p>" + esc(L(PL.renew)) + "</p>");
    });
  };
  HELP.motor = {
    en: "<h3>Compulsory motor insurance</h3><p>Every vehicle registered in the ISEZ must have a compulsory third-party policy from Iradstrakh (since 2009). The Highway Patrol Corps checks policies at its posts. Vehicles entering from Kazakhstan, Kyrgyzstan or Uzbekistan can buy a short-term policy at the main crossings.</p>",
    ir: "<h3>Mildettüü avtokamsızdandıruu</h3><p>IAEZde kattalgan ar bir unaada Iradstrakhtın mildettüü polisi bolushu kerek (2009-jıldan beri). Avtojol patrul korpusu polisterdi postoroundo tekshiret. Kazakstandan, Kırgızstandan je Özbekstandan kirgen unaalar negizgi ötkööldördö kıska möönöttük polis satıp ala alat.</p>",
    ru: "<h3>Обязательное автострахование</h3><p>Каждое транспортное средство, зарегистрированное в ОЭЗИ, должно иметь обязательный полис «Ирадстраха» (с 2009 года). Корпус дорожного патруля проверяет полисы на постах. Для въезжающих из Казахстана, Кыргызстана и Узбекистана краткосрочный полис продаётся на основных переходах.</p>"
  };
  HELP.fines = {
    en: "<h3>Where do fines come from?</h3><p>Fines issued by the Highway Patrol Corps on the highways and by the city police in Talas, Nurzhan and Iyık Janyl appear here within three working days. Fines issued on paper at a post may take longer.</p>",
    ir: "<h3>Ayıptar kaydan kelet?</h3><p>Avtojol patrul korpusu jana Talas, Nurzhan, Iyık Janıl shaar politsiyası salgan ayıptar bul jerde üch ish kündün ichinde payda bolot. Postto kagaz jüzündö jazılgan ayıptar uzagıraak bolushu mümkün.</p>",
    ru: "<h3>Откуда берутся штрафы?</h3><p>Штрафы Корпуса дорожного патруля на трассах и городской полиции Таласа, Нуржана и Ийык-Джаныла появляются здесь в течение трёх рабочих дней. Штрафы, выписанные на бумаге на посту, могут появиться позже.</p>"
  };

  /* parcel tracking */
  var PC = {
    no: { en: "Tracking number", ir: "Izdöö nomeri", ru: "Трек-номер" },
    noPh: { en: "e.g. RA123456789KZ or IP12345678", ir: "mısalı: RA123456789KZ je IP12345678", ru: "например, RA123456789KZ или IP12345678" },
    bad: { en: "Tracking numbers look like RA123456789KZ (from abroad) or IP12345678 (inside Irad).", ir: "Izdöö nomerleri RA123456789KZ (chet elden) je IP12345678 (Iraddın ichinde) sıyaktuu bolot.", ru: "Трек-номер выглядит как RA123456789KZ (из-за рубежа) или IP12345678 (внутри Ирада)." },
    places: ["Talas Central Post Office", "Post Office No. 14, Nurzhan", "Post Office No. 3, Iyık Janyl", "Post Office, Kyzyl-Adyr", "Post Office, Tash-Kömür", "Post Office, Bazar-Korgon", "Post Office, Toktogul", "Post Office No. 22, Talas (Semiz)"],
    placesRu: ["Таласский центральный почтамт", "Отделение № 14, Нуржан", "Отделение № 3, Ийык-Джаныл", "Отделение связи, Кызыл-Адыр", "Отделение связи, Таш-Кумыр", "Отделение связи, Базар-Коргон", "Отделение связи, Токтогул", "Отделение № 22, Талас (Семиз)"],
    placesIr: ["Talas borborduk pochtası", "14-pochta bölümü, Nurzhan", "3-pochta bölümü, Iyık Janıl", "Pochta bölümü, Kızıl-Adır", "Pochta bölümü, Tash-Kömür", "Pochta bölümü, Bazar-Korgon", "Pochta bölümü, Toktogul", "22-pochta bölümü, Talas (Semiz)"],
    ev: {
      acc: { en: "Accepted at {p}", ir: "{p} kabıl aldı", ru: "Принято: {p}" },
      sort: { en: "Sorted, Talas sorting centre", ir: "Talas sortirovka borborunda sortirovkalandı", ru: "Обработано, Таласский сортировочный центр" },
      disp: { en: "Dispatched to {p}", ir: "{p} karay jönötüldü", ru: "Отправлено в {p}" },
      arr: { en: "Arrived at {p}", ir: "{p} keldi", ru: "Прибыло: {p}" },
      wait: { en: "Awaiting collection at {p}. Bring your ID card; items are kept for 30 days.", ir: "{p} aluuga dayar. Jeke kuböölügüñüzdü ala keliñiz; jönötmölör 30 kün saktalat.", ru: "Ожидает получения: {p}. Возьмите удостоверение личности; отправления хранятся 30 дней." },
      deliv: { en: "Delivered", ir: "Tapshırıldı", ru: "Вручено" },
      abroad: { en: "Accepted for posting abroad ({c})", ir: "Chet elde jönötüügö kabıl alındı ({c})", ru: "Принято к пересылке за рубежом ({c})" },
      almaty: { en: "Received by the Kazakh postal service, Almaty international exchange", ir: "Kazakstan pochta kızmatı aldı, Almatı el aralık almashuu punktu", ru: "Получено казахстанской почтой, Алматинский международный пункт обмена" },
      handed: { en: "Handed over to Irad Pochtasy at the Chu Gate exchange", ir: "Chüy darbazasındagı almashuu punktunda Irad Pochtasına berildi", ru: "Передано «Ирадпочте» в пункте обмена Чуйские ворота" },
      customs: { en: "Customs inspection, Talas Customs Clearance Terminal", ir: "Bajı tekshirüüsü, Talas bajı tarıktoo terminalı", ru: "Таможенный досмотр, Таласский таможенный терминал" },
      held: { en: "Held by customs: a declaration is required. Bring the invoice and your ID card to the terminal's postal counter.", ir: "Bajı karmadı: deklaratsiya kerek. Esep-faktura jana jeke kuböölügüñüz menen terminaldın pochta kassasına keliñiz.", ru: "Задержано таможней: требуется декларация. Принесите счёт и удостоверение личности в почтовое окно терминала." },
      released: { en: "Released by customs", ir: "Bajıdan chıgarıldı", ru: "Выпущено таможней" }
    },
    intl: { en: "International items reach Irad through the Kazakh postal service, by way of Almaty. Allow three to six weeks.", ir: "Chet eldik jönötmölör Iradga Kazakstan pochtası arkıluu, Almatı arkıluu kelet. Üch-altı juma kütüñüz.", ru: "Международные отправления приходят в Ирад через казахстанскую почту, через Алматы. Срок три-шесть недель." },
    countries: { KZ: "KZ", RU: "RU", US: "US", CN: "CN", KG: "KG", UZ: "UZ", DE: "DE", TR: "TR", MX: "MX", GB: "GB" }
  };
  function place(i) { return (LANG === "ru" ? PC.placesRu : LANG === "ir" ? PC.placesIr : PC.places)[i % PC.places.length]; }
  FLOWS.parcel = function (box) {
    box.innerHTML = '<form class="flow" id="fp">' + field("tn", L(PC.no), inp("tn", L(PC.noPh), ' maxlength="20" style="text-transform:uppercase"')) + '<button class="btn" type="submit">' + esc(t("check")) + '</button></form><div id="result" class="result" hidden aria-live="polite"></div>';
    $("#fp").addEventListener("submit", function (e) {
      noForm(e);
      var n = norm($("#tn").value);
      var intl = /^[A-Z]{2}\d{9}[A-Z]{2}$/.test(n), dom = /^IP\d{8,10}$/.test(n);
      if (!intl && !dom) { if (!need("tn")) return; result('<p class="warn">' + esc(L(PC.bad)) + "</p>"); return; }
      var h = hash(n);
      if (h % 9 === 0) { result('<p class="warn">' + esc(t("notFound")) + "</p>"); return; }
      var dest = (h >>> 3) % PC.places.length, ev = [], day = 0, stage = h % 4, E = PC.ev;
      function push(o, v) { ev.push([day, L(o, v)]); day += 1 + ((h >>> (ev.length + 2)) % 3); }
      if (intl) {
        var c = n.slice(-2);
        push(E.abroad, { c: c }); day += 6; push(E.almaty); day += 4; push(E.handed); push(E.customs);
        if (stage === 0) push(E.held);
        else { push(E.released); push(E.disp, { p: place(dest) }); if (stage >= 2) push(E.arr, { p: place(dest) }); if (stage === 2) push(E.wait, { p: place(dest) }); if (stage === 3) push(E.deliv); }
      } else {
        var org = (h >>> 7) % PC.places.length; if (org === dest) org = (org + 1) % PC.places.length;
        push(E.acc, { p: place(org) }); push(E.sort); push(E.disp, { p: place(dest) });
        if (stage >= 1) push(E.arr, { p: place(dest) });
        if (stage === 1 || stage === 2) push(E.wait, { p: place(dest) });
        if (stage === 3) push(E.deliv);
      }
      var total = ev[ev.length - 1][0], start = addDays(today(), -total - (h % 2));
      result("<h4>" + esc(n) + '</h4><ol class="track">' + ev.slice().reverse().map(function (x, i) { return '<li class="' + (i === 0 ? "now" : "") + '"><span class="d">' + esc(fmtD(addDays(start, x[0]))) + "</span><span>" + esc(x[1]) + "</span></li>"; }).join("") + "</ol>" + (intl ? '<p class="tiny">' + esc(L(PC.intl)) + "</p>" : ""));
    });
  };
  HELP.parcel = {
    en: "<h3>Mail from abroad</h3><p>Irad Pochtasy exchanges international mail through the Kazakh postal service. Senders abroad should add “via Almaty, Kazakhstan” to the address. Parcels from abroad are inspected by customs at the Talas Customs Clearance Terminal. Irad Pochtasy stamps are valid for domestic mail only.</p>",
    ir: "<h3>Chet elden kelgen pochta</h3><p>Irad Pochtası el aralık pochtanı Kazakstan pochta kızmatı arkıluu almashat. Chet eldegi jönötüüchülör darekke “via Almaty, Kazakhstan” dep koshushu kerek. Chet elden kelgen posılkalardı Talas bajı tarıktoo terminalında bajı tekshiret. Irad Pochtasının markaları ölkö ichindegi pochta üchün gana jaraktuu.</p>",
    ru: "<h3>Почта из-за рубежа</h3><p>«Ирадпочта» обменивается международной почтой через казахстанскую почтовую службу. Отправителям за рубежом следует добавлять к адресу «via Almaty, Kazakhstan». Посылки из-за рубежа проходят таможенный досмотр на Таласском таможенном терминале. Марки «Ирадпочты» действительны только для внутренней почты.</p>"
  };

  /* crossing (information only) */
  FLOWS.crossing = function (box) {
    box.innerHTML = '<div class="flow">' + L({
      en: "<p class=\"warn\">Permits to cross the Qara-Chik line are not issued online.</p><h3>Visitors from the tribal regions</h3><p>Residents of the tribal regions travel to the ISEZ with a permit issued by their clan council. The permit is registered by the Republican Gendarmerie at the crossing point. Registration may take from a day to a week; bring the permit and an identity document.</p><h3>Crossing points</h3><p>Qara-Chik Border Checkpoint (main crossing, Kara-Buura District), Aksay, Toguz-Bulak (two posts on the Kök-Bel road), Kara-Bulak (Kenkol Pass road), Suusamyr, and the local crossings on the Mailuu-Suu road, the Arslanbob road and at Kök-Kamar. Crossings are open in daylight.</p><h3>Pilgrimages</h3><p>Arrangements for pilgrims travelling to Iyık Janyl for the Feast of St. Janyl are agreed each year through the Joint Liaison Committee of the United Nations Mission in Irad.</p><p>Weapons may not be carried within 12 km of the line.</p>",
      ir: "<p class=\"warn\">Kara-Chik liniyasınan ötüü uruksattarı onlayn berilbeyt.</p><h3>Tooluu aymaktardan kelgender</h3><p>Tooluu aymaktardın turgundarı IAEZge öz uruk keñeshi bergen uruksat menen kelet. Uruksattı ötkööl punktunda Respublikalık jandarmeriya kattayt. Kattoo bir kündön bir jumaga cheyin sozulushu mümkün; uruksattı jana ınyıktoochu dokumentti ala keliñiz.</p><h3>Ötkööl punkttarı</h3><p>Kara-Chik chek ara postu (negizgi ötkööl, Kara-Buura aymagı), Aksay, Toguz-Bulak (Kök-Bel jolunda eki post), Kara-Bulak (Kenkol ashuusunun jolu), Suusamır jana Maylu-Suu jolundagı, Arstanbap jolundagı, Kök-Kamardagı jergiliktüü ötkööldör. Ötkööldör kündüz achık.</p><h3>Ziyarattar</h3><p>Janıl Mayramına Iyık Janılga bargan ziyaratchılar üchün tartip ar jılı Iraddagı BUU missiyasının Birgeleshken baylanısh komiteti arkıluu makuldashılat.</p><p>Liniyadan 12 km aralıkta kural kötörüügö bolboyt.</p>",
      ru: "<p class=\"warn\">Разрешения на пересечение линии Кара-Чик онлайн не выдаются.</p><h3>Приезжающие из племенных районов</h3><p>Жители племенных районов приезжают в ОЭЗИ по разрешению своего совета рода. Разрешение регистрирует Республиканская жандармерия на пункте пропуска. Регистрация может занять от дня до недели; возьмите разрешение и документ, удостоверяющий личность.</p><h3>Пункты пропуска</h3><p>КПП Кара-Чик (основной, Кара-Бууринский район), Аксай, Тогуз-Булак (два поста на дороге Кок-Бел), Кара-Булак (дорога на перевал Кенкол), Суусамыр, а также местные переходы на дорогах Майлуу-Суу и Арсланбоб и у Кок-Камара. Переходы открыты в светлое время суток.</p><h3>Паломничество</h3><p>Порядок для паломников, едущих в Ийык-Джаныл на праздник Святой Джаныл, ежегодно согласуется через Совместный комитет связи Миссии ООН в Ираде.</p><p>Ношение оружия ближе 12 км от линии запрещено.</p>"
    }) + "</div>";
  };
  FLOWS.civil = function (box) {
    box.innerHTML = '<div class="flow">' + L({
      en: "<p>Copies of birth, marriage and death certificates are issued by the civil registry office of the district or city where the event was registered. Bring your ID card; the fee is IS 30 a copy. Online requests will open on e-Irad in 2027.</p><p>Records from before 1992 are held by the State Archives of Irad.</p>",
      ir: "<p>Tuuluu, nike jana ölüm kübölüktörünün köchürmölörün okuya kattalgan aymaktın je shaardın JAAK bölümü beret. Jeke kuböölügüñüzdü ala keliñiz; bir köchürmö 30 som. Onlayn arızdar e-Iradda 2027-jılı achılat.</p><p>1992-jılga cheyinki jazuular Irad mamlekettik arkhivinde saktalat.</p>",
      ru: "<p>Копии свидетельств о рождении, браке и смерти выдаёт отдел ЗАГС района или города, где было зарегистрировано событие. Возьмите удостоверение личности; пошлина 30 сомов за копию. Онлайн-запросы откроются на e-Irad в 2027 году.</p><p>Записи до 1992 года хранятся в Государственном архиве Ирада.</p>"
    }) + '<button class="btn" type="button" disabled>' + esc(L({ en: "Request online (2027)", ir: "Onlayn suroo (2027)", ru: "Запросить онлайн (2027)" })) + "</button></div>";
  };

  function pageService() {
    var id = new URLSearchParams(location.search).get("id"), s = svc(id), main = $("#app");
    if (!s) { pageNF(); return; }
    document.title = L(s.name) + " | e-Irad";
    main.innerHTML = '<div class="wrap page"><p class="crumbs"><a href="/">' + esc(t("back")) + "</a></p>" +
      '<div class="svchead">' + icon(s.icon) + "<div><h1>" + esc(L(s.name)) + "</h1><p>" + esc(L(s.desc)) + '</p><p class="agency"><span>' + esc(t("agency")) + ":</span> " + esc(L(s.agency)) + " " + badge(s.status) + "</p></div></div>" +
      '<div class="svcgrid"><div id="flowbox"></div><aside class="help">' + (HELP[id] ? L(HELP[id]) : "") + '<p class="tiny">' + esc(t("offline")) + "</p></aside></div></div>";
    FLOWS[id]($("#flowbox"));
  }

  /* ---------- status ---------- */
  var SYS = [
    [{ en: "Talasbank payment gateway", ir: "Talasbanktın tölöm shlyuzu", ru: "Платёжный шлюз «Таласбанка»" }, "maint", { en: "Upgrade in progress; online payments unavailable", ir: "Jañıloo jürüp jatat; onlayn tölöm jok", ru: "Идёт модернизация; онлайн-оплата недоступна" }],
    [{ en: "Sign-in by Tulpar ID", ir: "Tulpar ID arkıluu kirüü", ru: "Вход через Tulpar ID" }, "off", { en: "Suspended pending review", ir: "Tekshirüügö cheyin toktotuldu", ru: "Приостановлен до проверки" }],
    [{ en: "e-Irad cards", ir: "e-Irad kartaları", ru: "Карты e-Irad" }, "soon", { en: "After the pilot", ir: "Sınoodon kiyin", ru: "После пилота" }],
    [{ en: "Irad Pochtasy tracking", ir: "Irad Pochtasın izdöö", ru: "Отслеживание «Ирадпочты»" }, "ok", { en: "International items updated with a delay of up to three days", ir: "Chet eldik jönötmölör üch küngö cheyin kechigip jañılanat", ru: "Международные отправления обновляются с задержкой до трёх дней" }],
    [{ en: "Iradstrakh policy register", ir: "Iradstrakhtın polis reestri", ru: "Реестр полисов «Ирадстраха»" }, "ok", { en: "", ir: "", ru: "" }],
    [{ en: "Passport queue boards", ir: "Pasport kezeginin tabloloru", ru: "Табло очереди в паспортных столах" }, "limited", { en: "Iyık Janyl office: board under repair, numbers called aloud", ir: "Iyık Janıl bölümü: tablo oñdolup jatat, nomerler ün menen chakırılat", ru: "Ийык-Джаныл: табло в ремонте, номера объявляют голосом" }]
  ];
  var INC = [
    ["2026-10-19", { en: "Talasbank has informed us that the upgrade of its payment gateway will continue into November. Bills can be paid at Talasbank branches and Irad Pochtasy counters.", ir: "Talasbank tölöm shlyuzun jañıloo noyabrga cheyin ulanarın bildirdi. Esepterdi Talasbanktın filialdarında jana Irad Pochtasının kassalarında tölösö bolot.", ru: "«Таласбанк» сообщил, что модернизация платёжного шлюза продлится до ноября. Счета можно оплатить в отделениях «Таласбанка» и окошках «Ирадпочты»." }],
    ["2026-10-15", { en: "The census of business entities has begun. The online questionnaire will open on e-Irad in November.", ir: "Ishkanalardın sanagı bashtaldı. Onlayn suroo-joop e-Iradda noyabrda achılat.", ru: "Началась перепись хозяйствующих субъектов. Онлайн-анкета откроется на e-Irad в ноябре." }],
    ["2026-10-09", { en: "Sign-in by Tulpar ID has been suspended pending review. Services that do not need sign-in are not affected.", ir: "Tulpar ID arkıluu kirüü tekshirüügö cheyin toktotuldu. Kirüünü talap kılbagan kızmattarga tiyishpeyt.", ru: "Вход через Tulpar ID приостановлен до проверки. Услуги, не требующие входа, работают." }],
    ["2026-10-01", { en: "e-Irad opens in pilot. Services formerly on the ministries' id.gov pages are now listed here.", ir: "e-Irad sınoo rejiminde achıldı. Murda ministrlikterdin id.gov betterinde turgan kızmattar emi bul jerde.", ru: "e-Irad открыт в пилотном режиме. Услуги, ранее размещённые на страницах министерств в зоне id.gov, теперь здесь." }]
  ];
  function pageStatus() {
    $("#app").innerHTML = '<div class="wrap page"><h1>' + esc(t("statusH")) + "</h1><p class=\"lead\">" + esc(t("statusP")) + '</p><p class="tiny">' + esc(t("updated", { d: fmtD(new Date(INC[0][0] + "T00:00:00Z")) })) + "</p>" +
      '<div class="tw"><table class="tbl status"><tbody>' + S.list.map(function (s) { return '<tr><td><a href="/service.html?id=' + s.id + '">' + esc(L(s.name)) + "</a></td><td>" + badge(s.status) + "</td></tr>"; }).join("") +
      SYS.map(function (r) { return "<tr><td>" + esc(L(r[0])) + (L(r[2]) ? '<br><span class="tiny">' + esc(L(r[2])) + "</span>" : "") + "</td><td>" + badge(r[1]) + "</td></tr>"; }).join("") + "</tbody></table></div>" +
      "<h2>" + esc(t("incH")) + '</h2><ul class="inc">' + INC.map(function (x) { return '<li><span class="d">' + esc(fmtD(new Date(x[0] + "T00:00:00Z"))) + "</span><span>" + esc(L(x[1])) + "</span></li>"; }).join("") + "</ul></div>";
  }

  /* ---------- static pages ---------- */
  var FAQ = [
    [{ en: "Why does every service end at the district office?", ir: "Emne üchün ar bir kızmat aymaktık keñsede bütöt?", ru: "Почему каждая услуга заканчивается в районном отделе?" }, { en: "Most applications need your signature in front of an official, original documents or a state fee. During the pilot these steps are completed at the counter. e-Irad lets you prepare, take a number and check the status first, so that one visit is enough.", ir: "Arızdardın köbü kızmatkerdin aldında koluñuzdu, asıl dokumentterdi je mamlekettik alımdı talap kılat. Sınoo mezgilinde bul kadamdar kassada bütkörülöt. e-Irad aldın ala dayardanıp, kezek alıp, abaldı tekshirüügö jardam beret, oshondo bir barganıñız jetishtüü bolot.", ru: "Большинство заявлений требуют подписи в присутствии сотрудника, оригиналов документов или госпошлины. В пилотном режиме эти шаги выполняются в окошке. e-Irad помогает заранее подготовиться, взять номер и проверить статус, чтобы хватило одного визита." }],
    [{ en: "When will online payment work?", ir: "Onlayn tölöm kachan ishteyt?", ru: "Когда заработает онлайн-оплата?" }, { en: "When Talasbank completes the upgrade of its payment gateway. Online payment will be available to Talasbank card holders. Cards of other banks and Tulpar Pay are not accepted for state services.", ir: "Talasbank tölöm shlyuzun jañıloonu bütkörgöndö. Onlayn tölöm Talasbanktın kartasın karmagandar üchün achılat. Bashka banktardın kartaları jana Tulpar Pay mamlekettik kızmattar üchün kabıl alınbayt.", ru: "Когда «Таласбанк» завершит модернизацию платёжного шлюза. Онлайн-оплата будет доступна держателям карт «Таласбанка». Карты других банков и Tulpar Pay для государственных услуг не принимаются." }],
    [{ en: "Why can't I sign in with Tulpar?", ir: "Emne üchün Tulpar menen kire albaym?", ru: "Почему нельзя войти через Tulpar?" }, { en: "Sign-in by Tulpar ID is suspended pending a review of the service's compliance with the conditions for state services. Most e-Irad services do not need sign-in.", ir: "Tulpar ID arkıluu kirüü kızmattın mamlekettik kızmattar üchün shartarga ılayıktuulugu tekshirilgenge cheyin toktotuldu. e-Iraddın köp kızmattarı kirüünü talap kılbayt.", ru: "Вход через Tulpar ID приостановлен до проверки соответствия сервиса условиям для государственных услуг. Для большинства услуг e-Irad вход не нужен." }],
    [{ en: "Is my information sent anywhere?", ir: "Maalımatım bir jakka jönötülöbü?", ru: "Куда отправляются мои данные?" }, { en: "During the pilot, nothing you type on e-Irad leaves your device. Queue numbers you take are remembered by your browser so that you can check them later; you can remove them at any time.", ir: "Sınoo mezgilinde e-Iradga jazgan ech nerseñiz tüzmögüñüzdön chıkpayt. Algan kezek nomerleriñizdi kiyin tekshirüü üchün brauzeriñiz estep kaladı; alardı kaalagan ubakta öchürsöñüz bolot.", ru: "В пилотном режиме ничего из введённого на e-Irad не покидает ваше устройство. Полученные номера очереди запоминает ваш браузер, чтобы вы могли проверить их позже; их можно удалить в любой момент." }],
    [{ en: "I can't open e-Irad from abroad.", ir: "Chet elden e-Iraddı acha albay jatam.", ru: "Не открывается e-Irad из-за рубежа." }, { en: "e-Irad is available from abroad. If a page does not load, try again later or contact the e-Government Service Centre.", ir: "e-Irad chet elden da achılat. Bet jüktölbösö, kiyinireek kayra araket kılıñız je e-Ökmöt kızmat borboruna kayrılıñız.", ru: "e-Irad доступен из-за рубежа. Если страница не загружается, попробуйте позже или обратитесь в Центр услуг электронного правительства." }],
    [{ en: "Someone called me from “e-Irad” asking for my card number.", ir: "Maga “e-Irad” atınan chalıp, karta nomerimdi surashtı.", ru: "Мне позвонили «из e-Irad» и спросили номер карты." }, { en: "e-Irad never asks for passwords, card numbers or ID numbers by telephone, SMS or e-mail. Do not give them, and report the call to the police.", ir: "e-Irad ech kachan telefon, SMS je e-pochta arkıluu sırsöz, karta nomerin je jeke nomerdi surabayt. Berbeñiz jana chaluu tuuraluu politsiyaga kabarlañız.", ru: "e-Irad никогда не запрашивает пароли, номера карт или личные номера по телефону, SMS или электронной почте. Не сообщайте их и заявите о звонке в полицию." }]
  ];
  function pageFAQ() {
    $("#app").innerHTML = '<div class="wrap page narrow"><h1>' + esc(t("faqH")) + "</h1>" + FAQ.map(function (q) { return '<details class="faq"><summary>' + esc(L(q[0])) + "</summary><p>" + esc(L(q[1])) + "</p></details>"; }).join("") + "</div>";
  }
  function pageAcc() {
    $("#app").innerHTML = '<div class="wrap page narrow"><h1>' + esc(t("accH")) + "</h1>" + L({
      en: "<p>The Department of Infrastructure and Communications wants e-Irad to be usable by everyone, including people who use screen readers, keyboard navigation or large text.</p><h2>What we have done</h2><ul><li>Every page is available in English, Iradi and Russian.</li><li>Pages work with the keyboard alone, and the focus is always visible.</li><li>Text can be enlarged to 200% without loss of content.</li><li>Forms have labels and explain errors in words.</li><li>Pages are light enough for slow connections and older phones.</li></ul><h2>Known limitations</h2><ul><li>Some help texts are shorter in Iradi and Russian than in English.</li><li>The queue boards in the offices are not yet announced by voice in every office.</li></ul><h2>Tell us</h2><p>If something does not work for you, write to <a href=\"mailto:help@e-irad.org\">help@e-irad.org</a> or call +996-39-2-27-14-14. We answer within ten working days.</p><p class=\"tiny\">Statement prepared on 1 October 2026.</p>",
      ir: "<p>Infrastruktura jana baylanısh departamenti e-Iraddı bardıgı, anın ichinde ekran okuguchtardı, klaviaturanı je choñ tekstti koldongondor da paydalana alıshın kaalayt.</p><h2>Emne kıldık</h2><ul><li>Ar bir bet anglis, irad jana orus tilderinde.</li><li>Better klaviatura menen gana ishteyt, fokus ar dayım körünüp turat.</li><li>Tekstti mazmunu jogolboston 200%ga cheyin choñoytuuga bolot.</li><li>Formalardın belgileri bar, katalar söz menen tüshündürülöt.</li><li>Better jay internet jana eski telefondor üchün jeñil.</li></ul><h2>Belgilüü chekteöölör</h2><ul><li>Ayrım jardam teksterri irad jana orus tilderinde anglischesinen kıskaraak.</li><li>Bölümdördögü kezek tabloloru ar bir bölümdö ün menen jarıyalanbayt.</li></ul><h2>Bizge aytıñız</h2><p>Bir nerse ishtebese, <a href=\"mailto:help@e-irad.org\">help@e-irad.org</a> daregine jazıñız je +996-39-2-27-14-14 nomerine chalıñız. On ish kündün ichinde joop beribiz.</p><p class=\"tiny\">Bildirüü 2026-jıldın 1-oktyabrında dayardalgan.</p>",
      ru: "<p>Департамент инфраструктуры и связи стремится к тому, чтобы e-Irad был удобен для всех, в том числе для пользователей программ чтения с экрана, клавиатуры или крупного шрифта.</p><h2>Что сделано</h2><ul><li>Все страницы доступны на английском, ирадском и русском языках.</li><li>Страницы работают только с клавиатуры, фокус всегда виден.</li><li>Текст можно увеличить до 200% без потери содержания.</li><li>У полей форм есть подписи, ошибки объясняются словами.</li><li>Страницы рассчитаны на медленный интернет и старые телефоны.</li></ul><h2>Известные ограничения</h2><ul><li>Некоторые справочные тексты на ирадском и русском короче английских.</li><li>Табло очереди не во всех отделах дублируется голосом.</li></ul><h2>Сообщите нам</h2><p>Если что-то не работает, напишите на <a href=\"mailto:help@e-irad.org\">help@e-irad.org</a> или позвоните +996-39-2-27-14-14. Мы отвечаем в течение десяти рабочих дней.</p><p class=\"tiny\">Заявление подготовлено 1 октября 2026 года.</p>"
    }) + "</div>";
  }
  function pageContact() {
    $("#app").innerHTML = '<div class="wrap page narrow"><h1>' + esc(t("ctH")) + "</h1>" + L({
      en: "<p>The e-Government Service Centre answers questions about e-Irad and the services listed on it. It cannot process applications or take payments.</p><dl class=\"kvs\"><dt>Telephone</dt><dd>+996-39-2-27-14-14</dd><dt>E-mail</dt><dd><a href=\"mailto:help@e-irad.org\">help@e-irad.org</a></dd><dt>Hours</dt><dd>Monday to Friday 9:00–18:00, Saturday 9:00–13:00 (Irad Time)</dd><dt>Address</dt><dd>Department of Infrastructure and Communications, Liberty Boulevard 14, Talas</dd></dl><h2>Public Service Centres</h2><p>Help with e-Irad on a terminal, with staff on hand:</p><ul><li>Talas: Liberty Boulevard 14</li><li>Nurzhan: Azatlık Prospect 31</li><li>Iyık Janyl: City Hall, Lower Town</li></ul><p>Attelkom service points also have e-Irad terminals.</p>",
      ir: "<p>e-Ökmöt kızmat borboru e-Irad jana andagı kızmattar tuuraluu suroolorgo joop beret. Al arızdardı karabayt jana tölöm kabıl albayt.</p><dl class=\"kvs\"><dt>Telefon</dt><dd>+996-39-2-27-14-14</dd><dt>E-pochta</dt><dd><a href=\"mailto:help@e-irad.org\">help@e-irad.org</a></dd><dt>Ish saattarı</dt><dd>Düyshömbüdön jumaga cheyin 9:00–18:00, ishembi 9:00–13:00 (Irad ubaktısı)</dd><dt>Darek</dt><dd>Infrastruktura jana baylanısh departamenti, Erkindik bulvarı 14, Talas</dd></dl><h2>Kalkka kızmat körsötüü borborloru</h2><p>Terminalda e-Irad boyuncha jardam, kızmatkerler menen:</p><ul><li>Talas: Erkindik bulvarı 14</li><li>Nurzhan: Azattık prospekti 31</li><li>Iyık Janıl: Meriya, Tömönkü shaar</li></ul><p>Attelkomdun kızmat punkttarında da e-Irad terminaldarı bar.</p>",
      ru: "<p>Центр услуг электронного правительства отвечает на вопросы о e-Irad и размещённых на нём услугах. Он не рассматривает заявления и не принимает платежи.</p><dl class=\"kvs\"><dt>Телефон</dt><dd>+996-39-2-27-14-14</dd><dt>Эл. почта</dt><dd><a href=\"mailto:help@e-irad.org\">help@e-irad.org</a></dd><dt>Часы работы</dt><dd>Понедельник–пятница 9:00–18:00, суббота 9:00–13:00 (по Ирадскому времени)</dd><dt>Адрес</dt><dd>Департамент инфраструктуры и связи, бульвар Свободы, 14, Талас</dd></dl><h2>Центры обслуживания населения</h2><p>Помощь с e-Irad на терминале, с сотрудниками:</p><ul><li>Талас: бульвар Свободы, 14</li><li>Нуржан: проспект Азатлык, 31</li><li>Ийык-Джаныл: мэрия, Нижний город</li></ul><p>Терминалы e-Irad есть также в пунктах обслуживания «Аттелкома».</p>"
    }) + '<p class="tiny">' + esc(t("noPw")) + "</p></div>";
  }
  function pageLogin() {
    $("#app").innerHTML = '<div class="wrap page"><div class="login"><h1>' + esc(t("loginH")) + "</h1><p>" + esc(t("loginP")) + '</p><div class="lbtns"><button type="button" class="btn tulpar" data-m="tulpar">' + esc(t("tulparBtn")) + '</button><button type="button" class="btn ghost" data-m="card">' + esc(t("cardBtn")) + '</button></div><div id="lmsg" class="result" hidden role="alert"></div><p class="tiny">' + esc(t("noPw")) + "</p></div></div>";
    $$("[data-m]").forEach(function (b) {
      b.addEventListener("click", function () {
        var m = b.getAttribute("data-m"), el = $("#lmsg");
        el.innerHTML = '<p class="warn"><b>' + esc(t(m + "MsgH")) + "</b></p><p>" + esc(t(m + "Msg")) + "</p>"; el.hidden = false;
      });
    });
  }
  function pageNF() {
    $("#app").innerHTML = '<div class="wrap page narrow nf"><h1>' + esc(t("nfH")) + "</h1><p>" + esc(t("nfP")) + '</p><p><a class="btn" href="/">' + esc(t("nfHome")) + "</a></p></div>";
    document.title = t("nfH") + " | e-Irad";
  }

  var TITLES = { status: "nav_status", faq: "faqH", accessibility: "accH", contact: "ctH", login: "loginH" };
  function render() {
    document.documentElement.lang = I.htmlLang[LANG];
    chrome();
    if (TITLES[PAGE]) document.title = t(TITLES[PAGE]) + " | e-Irad"; else if (PAGE === "home") document.title = "e-Irad | " + t("tag");
    ({ home: pageHome, service: pageService, status: pageStatus, faq: pageFAQ, accessibility: pageAcc, contact: pageContact, login: pageLogin, nf: pageNF }[PAGE] || pageNF)();
  }
  render();
})();
