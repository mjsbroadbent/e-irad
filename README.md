# e-irad.org

e-Irad, the public services portal of the Irad Special Economic Zone (Irad ARG; lore in
`mjsbroadbent/irad_persona_skill`, see `canon.md`). The site itself is fully in-world; this README is not. Sister
site: iradgov.org (the Office of the Governor).

Domain: **e-irad.org** (`CNAME`). Address shown on the site: `help@e-irad.org`.
DNS: apex A records 185.199.108.153, .109.153, .110.153, .111.153 (AAAA 2606:50c0:8000::153, 8001::153, 8002::153,
8003::153) and `www` CNAME to `mjsbroadbent.github.io`. GitHub Pages: branch `main`, root, custom domain e-irad.org.

## Safety rules (keep them)

- Nothing is collected. There is no `fetch`, no form `action`, no analytics, no password field anywhere. Every form
  is handled in `assets/app.js` in the browser and its result is worked out from the input (a hash), so the same
  number always gives the same answer.
- The only thing stored is the passport queue numbers a visitor takes (`localStorage` `eirad_tickets`, at most six)
  and the language (`eirad_lang`).
- Services stop before anything sensitive: payments end at "Online payment is available to Talasbank card holders
  only; the gateway is being upgraded" (no card fields), sign-in ends at "Sign-in by Tulpar ID is suspended pending
  review" or "e-Irad cards are not yet issued" (no fields), registrations end at "visit your district office with
  originals". Never ask for real ID, card or password data.
- No real government branding. Look: teal, Manrope and Noto Sans; the national emblem appears only small, as a link
  to iradgov.org.

## Structure

No build step. Every page is a stub (`index.html`, `service.html?id=…`, `status.html`, `faq.html`,
`accessibility.html`, `contact.html`, `login.html`, `404.html`) rendered by `assets/app.js`.

- `assets/i18n.js`: interface strings in en / ir / ru.
- `assets/services.js`: the catalogue (`list`: id, category, status `ok|limited|maint|off|soon`, names, agency) and
  the passport offices (queue size `base` and numbers served a week `rate`).
- `assets/app.js`: the flows (`FLOWS.<id>`), their help texts (`HELP.<id>`), the status page (`SYS`, `INC`) and the
  FAQ. To add a service: an entry in `services.js`, a `FLOWS` function (and optional `HELP`) in `app.js`, and a
  line in `sitemap.xml`.

## Checking

`python3 -m http.server` here; try every service in all three languages at desktop and phone widths, and confirm
in the browser's network panel that nothing but the site's own files and Google Fonts is requested.
