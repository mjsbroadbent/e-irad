# e-irad.org

e-Irad, the public services portal of the Irad Special Economic Zone (Irad ARG; lore in
`mjsbroadbent/irad_persona_skill`, see `canon.md`). The site itself is fully in-world; this README is not. Sister
site: iradgov.org (the Office of the Governor).

Domain: **e-irad.org** (`CNAME`). Address shown on the site: `help@e-irad.org`.
DNS: apex A records 185.199.108.153, .109.153, .110.153, .111.153 (AAAA 2606:50c0:8000::153, 8001::153, 8002::153,
8003::153) and `www` CNAME to `mjsbroadbent.github.io`. GitHub Pages: branch `main`, root, custom domain e-irad.org.

## Safety rules (keep them)

- Nothing typed into the site is collected. There is no form `action` and no password field anywhere. The site's own
  scripts make one network request, a GET of `data/procedures.json` (`assets/guide.js`). Every form is handled in
  `assets/app.js` in the browser and its result is worked out from the input (a hash), so the same number always gives
  the same answer. No external fonts: the page uses system fonts.
- The outside scripts are the shared GoatCounter page counter (irad.goatcounter.com) and Google Analytics
  (G-QTS2XFLJD7), as on every Irad site (Oct 2026). They record the page address, referrer, browser, screen size and
  country, never anything typed into a form; e-Irad's form results never go into the address. Google Analytics sets
  cookies; GoatCounter doesn't.
- The only thing stored is the passport queue numbers a visitor takes (`localStorage` `eirad_tickets`, at most six)
  and the language (`eirad_lang`).
- Services stop before anything sensitive: payments end at "Online payment is available to Talasbank card holders
  only; the gateway is being upgraded" (no card fields), sign-in ends at "Sign-in by Tulpar ID is suspended pending
  review" or "e-Irad cards are not yet issued" (no fields), registrations end at "visit your district office with
  originals". Never ask for real ID, card or password data.
- No real government branding, and nothing copied from real trade portals: no other portal's name, logo or wording.
  The guide's in-world credit is "developed with the support of the UNMI trade facilitation programme".
- Look (Oct 2026 rework): a deliberately dated institutional portal, grey page, white header, blue nav bar and blue
  panel headers, small system type, a three-slide hero (photos in `assets/img/hero-*.jpg`, 1536×512, with a dark gradient on the left for the text) with a
  pill search bar, four blue tabs, and a crimson rule at the top as the only nod to iradgov.org.
- Logo and icons: the product logo is `assets/logo.svg` (Oct 2026): a blue tile with a crimson base, a drawn white
  "e" and the gold Polaris star from the flag; header (42 px) and footer (30 px). It is also every site icon:
  `favicon.ico`, `favicon-32.png`, the SVG icon link, `apple-touch-icon.png` (square-cornered), `assets/logo-192.png`
  and `logo-512.png` (`manifest.webmanifest`) and the share image (`og:image`, logo-512).
- Government mark: the horse and star cut from the flag (crimson `#aa0000`; `assets/mark.svg`, `mark-white.svg`), as
  on iradgov.org, used only as the link to iradgov.org, like a federal signature: the crimson mark plus "Government
  of the Irad Special Economic Zone" in the header and the white mark in the footer. The circular seal is not used on e-Irad.

## Structure

No build step. Every page is a stub rendered by `assets/app.js` (header, footer, landing page, citizens home,
citizen services) and `assets/guide.js` (business home and the guide). The site has two halves under a landing page:

- `index.html`: landing page. Header, welcome line, two big tiles **For businesses** and **For citizens** (pictogram,
  one-line description, Enter button, example links), a strip with Service availability / Help / Contact us /
  Accessibility, the pilot banner and the footer. Old links `/#services` and `/#how` redirect to `citizens.html` and
  `business.html#how`.
- **For businesses** (`business.html` home: hero slider, pill search, four blue tabs, objective grid, "Business
  services" box `#services`): `procedures.html`, `procedure.html?id=…`, `laws.html`, and the services whose `sec`
  includes `b`. Breadcrumbs start "e-Irad › Business". The partners strip appears only in this section.
- **For citizens** (`citizens.html` home: blue heading band with a service filter, category boxes `#cat-people`,
  `#cat-pay`, `#cat-check`, `#cat-biz`, `#cat-other`, My e-Irad side box): the services whose `sec` includes `c`,
  and `login.html` (My e-Irad). Breadcrumbs start "e-Irad › Citizens".
- Shared: `status.html`, `faq.html`, `contact.html`, `accessibility.html`, `404.html` (neutral nav), plus the common
  footer.
- The nav bar changes with the section (`NAVS` in `app.js`), with a "Business | Citizens" switch at its right (always
  visible on phones); the e-Irad logo goes to the landing page. `service.html?id=…` takes its section from the
  service's `sec` (first letter is home); a service in both sections linked from its other section gets `&s=b|c`.

- `assets/i18n.js`: interface strings in en / ir / ru; `assets/i18n-guide.js` adds and overrides the strings of the
  portal layout and the guide.
- `assets/img/`: hero slides and the institution photo cards (`inst-<pic>.jpg`, 480×300: gov, office, post, lab, bank,
  kiosk, depot, yurt, warehouse, stable). Photos generated locally (FLUX.1 Krea + Amateur Photography LoRA 0.6, see
  irad_wiki `tools/comfyui/`); garbled lettering on signs, plates and posters pixelated, flags repainted crimson.
- `assets/services.js`: the catalogue (`list`: id, category, `sec` (`b`, `c` or both, e.g. `bc`), status `ok|limited|maint|off|soon`, names, agency) and
  the passport offices (queue size `base` and numbers served a week `rate`).
- `assets/app.js`: the flows (`FLOWS.<id>`), their help texts (`HELP.<id>`), the status page (`SYS`, `INC`) and the
  FAQ. To add a service: an entry in `services.js`, a `FLOWS` function (and optional `HELP`) in `app.js`, and a
  line in `sitemap.xml`. Every service page shows a "Forms for this service" box (`formBox(id)`, in the help column
  and in results that end at a counter) listing the entries of `window.E_FORMS` (`assets/forms.js`, loaded before
  `app.js` on every page) whose `service` is the page's id; no box if there are none.
- Services (41, Oct 2026). Documents: passport queue, address registration, lost ID card, foreign driving licence,
  change of name, certificate of good conduct, old-age pension, civil certificates. Bills: electricity, water, gas,
  heating (status `maint`: shows the last completed bill, September, so heating reads "outside the heating season"),
  property tax, road-use charge, kindergarten fees, traffic fines, and the state duty calculator (`DUTY` in
  `app.js`: the one table of state duties, used by every service that names one; prints a Talasbank payment order).
  Checks: parcels, motor policy, firm register, vehicle register (agrees with the motor policy check and the road
  charge for the same plate), permit and licence numbers, Supreme Court register of pending cases (hearing dates
  "not yet set" for most), Iradstandart certificates, school leaving examination results. Permits: event, business,
  census, market trading place, building pre-application (links the guide's Add a second storey), taxi, alcohol,
  outdoor sign (spelling check for the Toponymic Section: Cyrillic, letters not in Iradi, English-only text), foreign
  trade participant. Other: crossing the line, hunting and fishing, public gathering notification, Feast of St. Janyl
  vehicle pass (issued from 1 August), archive copies (ends at a stamped addressed envelope), written appeals
  (letters@iradgov.org; e-Irad sends nothing), dog registration. The same rule everywhere: lookups are worked out
  from a hash of the input; applications end at "download the form, block capitals, bring it with the originals";
  payments end at the Talasbank gateway message.

## Step-by-step guide to procedures (`data/procedures.json`)

A comically thorough, deadpan guide on the pattern of national trade-procedure portals: choose a type of operation
(Import, Export, Transit, Open a business, Hold an event, Build, Sell food, Livestock, Foreign worker) and a type of
product, and get every permit, stamp and window. The site takes it completely seriously; the comedy is in the quantity
and the logic. Pages: `procedures.html` (all objectives; `?op=import` an objective page with collapsible product
panels; `&p=<objective id>` opens one; `?q=` searches), `procedure.html?id=<procedure or objective id>` (an objective
id gives the **full procedure**, all its procedures chained; `&step=N` opens step N), `laws.html` (every law,
document and institution in the data, with anchors `#l-<law>` and `#i-<institution>`).

Everything is data. All text is `{"en", "ir", "ru"}` (Iradi in Latin orthography, no Cyrillic). Top-level keys:

- `operations`: `id`, `icon` (a key in `OPI` in `guide.js`), `name`, `desc`.
- `objectives`: one per operation + product. `id`, `op`, `product`, `productName`, `title`, `intro`, `context`,
  `inputs` (the cost estimator's quantities: `key`, `label`, `per` (unit text such as "per tray"), `default`,
  `step`), optional `perunit` (`key`, `mult`, `label`: e.g. cost per egg = total / (trays × 30)), `laws`
  (`[lawId, "articles …"]`), and `items`, the chain in order: `{"proc": id}` or a choice
  `{"title", "desc", "options": [id, id]}` (the full procedure uses the first option).
- `procedures`: `id → {objective, title, desc (one line naming the institution), inst, context?, laws?, steps}`.
  A step: `title`, `inst`, `optional` (shown ★, excluded from cost totals unless ticked), `note` (the detail where
  the bureaucracy lives), `who`, `where` and `hours` (override the institution's), `needs` and `gives` (document ids;
  the page works out "needed at step n" and "issued at step n"; `receipt`/`cashreceipt` are not counted as
  results), `cost` (list of `{amount, per: [input keys], times, label, cash (payable in cash som only), usd
  (converted at 8.40), bands: {by, bands: [[upTo, amount], …, [null, amount]], per}}`), `queue` and `counter`
  (minutes, `[min, max]`), `wait` (days until the next step, `[min, max]`). Durations are summed step by step.
- `institutions`: `id → {name, parent, address, hours, phone, pic, note?}` (`note` marks non-ISEZ bodies such as the
  El-Choro post and clan councils: "Not an institution of the ISEZ. Listed for information.").
- `documents`: `id → {name, valid? (days)}`. `laws`: `id → {no, title}`. Article references are written in English
  (`articles 4, 7`; `paragraph 2`; `section 5.2`; `annex`) and translated on the page.

Built so far (Oct 2026): Import table eggs (the showpiece: 32 procedures, 63 steps, 28 institutions, 35 documents
issued), Export walnuts, Export an Akyel horse, Import a used car, Hold a concert with performers from abroad, Open a
café, Sell kymyz from a roadside stand, Diesel in transit, Add a second storey, Move sheep across the Qara-Chik line,
Hire a foreign cook; added 23 Oct: Open a guesthouse (Konok Üy), Import spare parts by post, Film in Irad with a
foreign crew, Rent a stall at Bazar-i Kalan, Run a taxi, Hold a wedding for more than 300 guests; also added 23 Oct:
Import medicines for a pharmacy, Export dried apricots to Kazakhstan by rail, Open a bakery with a tandoor in a
courtyard, Bring a pet dog or cat from abroad, Register a newspaper, magazine or website, Open a private
kindergarten (ids prefixed `a-`). To add one: institutions, documents and laws first, then the procedures, then the objective;
keep institutions and laws consistent with the canon and iradgov.org (existing directive numbers: 2016 decree,
2022/14, 2026/24, 2026/31; Bank of Irad notices 2026/2, 2026/5), add the objective's `procedure.html?id=` to
`sitemap.xml`, and check that `ir` strings contain no Cyrillic.

Invented for the guide (also noted in the canon): Iradstandart (State Agency for Standards, Metrology and
Certification) and its IST standards; the State Veterinary Inspectorate of the Talas Basin Agricultural Directorate
and its cash desk on Tokmok Street; the Nurzhan Interdistrict Veterinary Laboratory (the only licensed candling
table); the Plant Quarantine Inspectorate; the State Fire Inspectorate; the Technical Inventory Bureau; the Toponymic
Section of the State Archives (window Tuesdays 10:00–11:30); the Foreign Labour Quota Section; Tazalık; the act
numbers (`No. YY-NN`), Regulation No. 77, DPI Regulation No. 12 and Executive Directives 2014/22, 2019/07, 2021/09
and 2024/11.

## Checking

`python3 -m http.server` here; try every service in all three languages at desktop and phone widths, and confirm
in the browser's network panel that nothing but the site's own files is requested. Look at a sample of procedures
(the eggs full procedure, a step view, a component procedure) and `laws.html` in all three languages.
