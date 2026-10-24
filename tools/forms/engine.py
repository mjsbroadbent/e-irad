"""Draws printed state forms as PDF (A4) from a small spec, in the manner of real post-Soviet application forms:
one ink colour, the issuing body's mark, a form number with the approving order, three languages on every label,
character boxes for block capitals, numbered notes, a shaded "for official use" block and, where a form has one,
a tear-off counterfoil.

Shared by e-irad.org (tools/forms/build.py) and post.iradgov.org (a copy in irad-post/tools/forms/).

Spec: see build.py. Every text is a triple {"en", "ir", "ru"} (or a key into COMMON).
"""
import hashlib
from pathlib import Path

from PIL import Image
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
FD = "/usr/share/fonts/truetype/crosextra/"
pdfmetrics.registerFont(TTFont("F", FD + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(TTFont("FB", FD + "Carlito-Bold.ttf"))
pdfmetrics.registerFont(TTFont("FI", FD + "Carlito-Italic.ttf"))
pdfmetrics.registerFont(TTFont("FBI", FD + "Carlito-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("S", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))

PW, PH = 210 * mm, 297 * mm
ML, MR, MT, MB = 13 * mm, 13 * mm, 11 * mm, 14 * mm
CW = PW - ML - MR
BOX = 4.4 * mm                       # character box width
BOXH = 5.4 * mm


def T(en, ir, ru):
    return {"en": en, "ir": ir, "ru": ru}


# labels used on many forms
COMMON = {
    "surname": T("Surname", "Familiyası", "Фамилия"),
    "first": T("First name", "Atı", "Имя"),
    "patr": T("Patronymic (if any)", "Atasının atı (bar bolso)", "Отчество (при наличии)"),
    "dob": T("Date of birth", "Tuulgan kün", "Дата рождения"),
    "pob": T("Place of birth (settlement, district)", "Tuulgan jeri (kalk konush, aymak)", "Место рождения (населённый пункт, район)"),
    "sex": T("Sex", "Jınısı", "Пол"),
    "male": T("male", "erkek", "муж."),
    "female": T("female", "ayal", "жен."),
    "idno": T("Identity card number", "Jeke kuböölüktün nomeri", "Номер удостоверения личности"),
    "idser": T("Series", "Seriyası", "Серия"),
    "issued": T("Issued by (authority)", "Kim bergen (organ)", "Кем выдано (орган)"),
    "idate": T("Date of issue", "Berilgen kün", "Дата выдачи"),
    "pin": T("Personal number (14 digits)", "Jeke nomer (14 sanarip)", "Персональный номер (14 цифр)"),
    "city": T("City / settlement", "Shaar / kalk konush", "Город / населённый пункт"),
    "district": T("District", "Aymak", "Район"),
    "street": T("Street, microdistrict", "Köchö, mikrorayon", "Улица, микрорайон"),
    "house": T("House", "Üy", "Дом"),
    "flat": T("Flat", "Batir", "Кв."),
    "phone": T("Telephone", "Telefon", "Телефон"),
    "email": T("E-mail (optional)", "E-pochta (kaalasañız)", "Эл. почта (по желанию)"),
    "sign": T("Signature of the applicant", "Arız beruuchunun kolu", "Подпись заявителя"),
    "date": T("Date", "Kün", "Дата"),
    "fullname": T("Surname, first name, patronymic", "Familiyası, atı, atasının atı", "Фамилия, имя, отчество"),
    "nat": T("Citizenship / status", "Jarandıgı / statusu", "Гражданство / статус"),
    "official": T("FOR OFFICIAL USE ONLY", "KIZMATTIK PAYDALANUU ÜCHÜN GANA", "ТОЛЬКО ДЛЯ СЛУЖЕБНОГО ПОЛЬЗОВАНИЯ"),
    "recvd": T("Received by (name, position)", "Kabıl alğan (atı, kızmatı)", "Принял (Ф.И.О., должность)"),
    "regno": T("Registration No.", "Kattoo nomeri", "Рег. №"),
    "decision": T("Decision", "Chechim", "Решение"),
    "granted": T("granted", "berildi", "удовлетворено"),
    "refused": T("refused", "baş tartıldı", "отказано"),
    "returned": T("returned for correction", "onduuga kaytarıldı", "возвращено на доработку"),
    "mp": T("Seal", "Möör", "М.П."),
    "regaddr": T("Registered address", "Kattalgan dareki", "Адрес регистрации"),
    "orgname": T("Full name of the entity", "Subyekttin toluk atı", "Полное наименование субъекта"),
    "regnum": T("Register of Firms number", "Firmalar reestrindegi nomeri", "Номер в Реестре фирм"),
    "tin": T("Taxpayer number", "Salık töloochünün nomeri", "ИНН"),
    "head": T("Head of the entity (name)", "Subyekttin jetekchisi (atı)", "Руководитель (Ф.И.О.)"),
}

for k, v in COMMON.items():
    for lang in ("ir",):
        v[lang] = v[lang].replace("ğ", "g")


def tx(v):
    if isinstance(v, str):
        return COMMON[v]
    return v


class Form:
    def __init__(self, path, spec):
        self.spec = spec
        self.ink = HexColor(spec.get("ink", "#111111"))
        self.tint = Color(self.ink.red, self.ink.green, self.ink.blue, alpha=0.10)
        self.c = canvas.Canvas(str(path), pagesize=(PW, PH), pageCompression=1)
        self.c.setTitle(f'{spec["code"]}: {spec["title"]["en"]}')
        self.c.setAuthor(spec["agency"]["en"])
        self.c.setSubject(spec["title"]["en"])
        self.c.setCreator("")
        self.c.setProducer("")
        self.page = 1
        self.pages = spec.get("_pages", 1)
        self.y = PH - MT
        self.notes = []

    # -- primitives
    def font(self, f, s):
        self.c.setFont(f, s)

    def text(self, x, y, s, f="F", size=7, color=None, anchor="l"):
        self.c.setFillColor(color or self.ink)
        self.c.setFont(f, size)
        if anchor == "c":
            self.c.drawCentredString(x, y, s)
        elif anchor == "r":
            self.c.drawRightString(x, y, s)
        else:
            self.c.drawString(x, y, s)

    def wrap(self, s, f, size, width):
        words, lines, cur = s.split(" "), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(t, f, size) <= width:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, s, f, size, width, lead=None, color=None):
        lead = lead or size * 1.18
        for ln in self.wrap(s, f, size, width):
            self.text(x, y, ln, f, size, color)
            y -= lead
        return y

    def grey(self):
        return Color(self.ink.red * .55 + .45 * .35, self.ink.green * .55 + .45 * .35, self.ink.blue * .55 + .45 * .35)

    def label(self, x, y, lab, width, sup=None):
        """Three-language label: English, then Iradi / Russian small. Returns height used."""
        lab = tx(lab)
        en = lab["en"] + (f" {sup}" if sup else "")
        self.text(x, y, en, "FB", 7)
        small = lab["ir"] + "  /  " + lab["ru"]
        lines = self.wrap(small, "FI", 5.6, width)
        yy = y - 6.4
        for ln in lines[:2]:
            self.text(x, yy, ln, "FI", 5.6, self.grey())
            yy -= 6.2
        return 7 + 6.3 * min(2, len(lines)) + 1.5

    def boxes(self, x, y, n, h=BOXH):
        self.c.setStrokeColor(self.ink)
        self.c.setLineWidth(0.5)
        for i in range(n):
            self.c.rect(x + i * BOX, y - h, BOX, h, stroke=1, fill=0)

    def checkbox(self, x, y, s=3.2 * mm):
        self.c.setLineWidth(0.6)
        self.c.setStrokeColor(self.ink)
        self.c.rect(x, y - s, s, s, stroke=1, fill=0)

    def rule(self, x1, y, x2, w=0.4, dash=None):
        self.c.setStrokeColor(self.ink)
        self.c.setLineWidth(w)
        if dash:
            self.c.setDash(*dash)
        self.c.line(x1, y, x2, y)
        self.c.setDash()

    # -- page furniture
    def mark_image(self):
        key = self.spec.get("mark", "gov")
        p = HERE / "marks" / f"{key}.png"
        out = HERE / "marks" / f".{key}-{self.spec.get('ink', '#111111').strip('#')}.png"
        if not out.exists():
            im = Image.open(p).convert("RGBA")
            a = im.split()[3]
            if not self.spec.get("mark_colour"):
                r, g, b = int(self.ink.red * 255), int(self.ink.green * 255), int(self.ink.blue * 255)
                lum = im.convert("L")
                # keep light parts light: tint by darkness so a one-ink mark keeps its detail
                solid = Image.new("RGBA", im.size, (r, g, b, 255))
                white = Image.new("RGBA", im.size, (255, 255, 255, 255))
                mask = lum.point(lambda v: 255 - int(v * 0.85))
                im = Image.composite(solid, white, mask)
                im.putalpha(a)
            im.save(out)
        return str(out)

    def barcode(self, x, y, w, h):
        hsh = hashlib.sha1(self.spec["code"].encode()).digest() * 4
        xx = x
        i = 0
        self.c.setFillColor(HexColor("#111111"))
        while xx < x + w - 1:
            bw = (1 + hsh[i] % 3) * 0.32 * mm
            if i % 2 == 0:
                self.c.rect(xx, y, bw, h, stroke=0, fill=1)
            xx += bw
            i += 1
        num = "".join(str(b % 10) for b in hsh[:13])
        self.text(x + w / 2, y - 6, num, "F", 5.5, HexColor("#111111"), "c")

    def header(self):
        s = self.spec
        c = self.c
        top = PH - MT
        mh = 17 * mm
        img = self.mark_image()
        iw, ih = Image.open(img).size
        if iw / ih > 1.4:                      # a wide logotype: give it width, not height
            mw = min(46 * mm, 11 * mm * iw / ih)
            c.drawImage(img, ML, top - 4 * mm - mw * ih / iw, mw, mw * ih / iw, mask="auto")
            x = ML + mw + 4 * mm
        else:
            c.drawImage(img, ML, top - mh, mh, mh, mask="auto", preserveAspectRatio=True)
            x = ML + mh + 3 * mm
        ag = s["agency"]
        self.text(x, top - 4.2 * mm, ag["en"].upper(), "FB", 8.2)
        self.text(x, top - 8.0 * mm, ag["ir"], "F", 6.8, self.grey())
        self.text(x, top - 11.2 * mm, ag["ru"], "F", 6.8, self.grey())
        if s.get("subagency"):
            self.text(x, top - 14.6 * mm, s["subagency"], "FI", 6.4, self.grey())
        # form number box
        bw, bh = 52 * mm, 17 * mm
        bx = PW - MR - bw
        c.setStrokeColor(self.ink)
        c.setLineWidth(0.9)
        c.rect(bx, top - bh, bw, bh)
        self.text(bx + bw / 2, top - 5.6 * mm, f"Form {s['code']}", "FB", 12, anchor="c")
        self.text(bx + bw / 2, top - 8.9 * mm, f"Forma {s['code']} · Форма {s['code']}", "F", 6.4, self.grey(), "c")
        y = top - 11.6 * mm
        for ln in self.wrap(s.get("approved", ""), "F", 5.4, bw - 4 * mm)[:2]:
            self.text(bx + bw / 2, y, ln, "F", 5.4, anchor="c")
            y -= 6
        self.y = top - bh - 3.2 * mm
        # incoming number line + barcode
        self.text(ML, self.y - 2, "Incoming No. / Kiruuchu No. / Вх. №", "F", 6.2)
        self.rule(ML + 41 * mm, self.y - 3, ML + 72 * mm, .4)
        self.text(ML + 74 * mm, self.y - 2, "of / ·  / от", "F", 6.2)
        self.rule(ML + 84 * mm, self.y - 3, ML + 108 * mm, .4)
        self.barcode(PW - MR - 42 * mm, self.y - 6.5 * mm, 42 * mm, 7 * mm)
        self.y -= 13 * mm

    def footer(self):
        s = self.spec
        y = MB - 6 * mm
        self.rule(ML, y + 4.2 * mm, PW - MR, .5)
        self.text(ML, y + 1.2 * mm, f"Form {s['code']} ({s.get('rev', 'rev. 2019')})", "FB", 6.2)
        self.text(PW / 2, y + 1.2 * mm, f"Page {self.page} of {self.pages}  ·  {self.page}-bet / {self.pages}  ·  Стр. {self.page} из {self.pages}", "F", 6.2, anchor="c")
        self.text(PW - MR, y + 1.2 * mm, s.get("printnote", "Free of charge. Sale of this form is prohibited."), "F", 6.2, anchor="r")
        self.text(PW / 2, y - 1.8 * mm, s.get("printnote2", "Photocopies are accepted only on white A4 paper, one side, at 100% scale. Forms completed in pencil, red or green ink are not accepted."), "FI", 5.4, self.grey(), "c")

    def new_page(self):
        self.footer()
        self.c.showPage()
        self.page += 1
        self.y = PH - MT
        s = self.spec
        self.text(ML, self.y - 3, f"Form {s['code']}", "FB", 9)
        self.text(ML + 22 * mm, self.y - 3, s["title"]["en"], "F", 7.5)
        self.text(PW - MR, self.y - 3, "(continued) / (ulanması) / (продолжение)", "FI", 6.5, anchor="r")
        self.rule(ML, self.y - 5.5, PW - MR, .7)
        self.y -= 11 * mm

    def need(self, h):
        if self.y - h < MB + (14 * mm if self.page == 1 and self.spec.get("counterfoil") else 0):
            self.new_page()

    # -- blocks
    def title(self):
        s = self.spec["title"]
        lines = self.wrap(s["en"].upper(), "FB", 12.5, CW - 10 * mm)
        for ln in lines:
            self.text(PW / 2, self.y, ln, "FB", 12.5, anchor="c")
            self.y -= 14
        self.text(PW / 2, self.y + 1, s["ir"], "FI", 8.4, self.grey(), "c")
        self.y -= 10
        self.text(PW / 2, self.y + 1, s["ru"], "FI", 8.4, self.grey(), "c")
        self.y -= 9
        if self.spec.get("to"):
            to = self.spec["to"]
            self.text(PW - MR, self.y, "To: " + to["en"], "F", 7, anchor="r")
            self.y -= 8
            self.text(PW - MR, self.y, to["ir"] + " / " + to["ru"], "FI", 5.8, self.grey(), "r")
            self.y -= 10

    def instructions(self):
        ins = self.spec.get("instructions") or []
        if not ins:
            return
        x, w = ML + 2.5 * mm, CW - 5 * mm
        # measure
        h = 0
        for i in ins:
            h += len(self.wrap(i["en"], "F", 6.6, w)) * 7.6 + len(self.wrap(i["ir"] + " / " + i["ru"], "FI", 5.5, w)) * 6.3 + 2.5
        h += 12
        self.need(h)
        top = self.y
        self.c.setFillColor(self.tint)
        self.c.setStrokeColor(self.ink)
        self.c.setLineWidth(0.6)
        self.c.rect(ML, top - h, CW, h, stroke=1, fill=1)
        y = top - 9
        self.text(x, y, "HOW TO COMPLETE THIS FORM · FORMANI TOLTURUU TARTIBI · ПОРЯДОК ЗАПОЛНЕНИЯ", "FB", 6.8)
        y -= 9
        for n, i in enumerate(ins, 1):
            y = self.para(x, y, f"{n}. " + i["en"], "F", 6.6, w, 7.6)
            y = self.para(x + 3 * mm, y, i["ir"] + " / " + i["ru"], "FI", 5.5, w - 3 * mm, 6.3, self.grey())
            y -= 2.5
        self.y = top - h - 4 * mm

    def section(self, sec):
        t = tx(sec["t"])
        first = sec["rows"][0] if sec["rows"] else None
        fh = max(self.field_h(f) for f in (first if isinstance(first, list) else [first])) if first else 0
        self.need(9 * mm + min(fh, 120 * mm))
        self.c.setFillColor(self.ink)
        self.c.rect(ML, self.y - 5.2 * mm, CW, 5.2 * mm, stroke=0, fill=1)
        lab = f'{sec["n"]}. {t["en"].upper()}'
        self.text(ML + 2 * mm, self.y - 3.7 * mm, lab, "FB", 7.6, HexColor("#ffffff"))
        self.text(PW - MR - 2 * mm, self.y - 3.7 * mm, t["ir"] + " / " + t["ru"], "FI", 6.2, HexColor("#ffffff"), "r")
        self.y -= 7.6 * mm
        for row in sec["rows"]:
            self.row(row)
        self.y -= 2 * mm

    def row(self, row):
        if isinstance(row, dict):
            row = [row]
        hs = [self.field_h(f) for f in row]
        h = max(hs)
        self.need(h + 2)
        x = ML
        ws = [f.get("w", 1) for f in row]
        tot = sum(ws)
        for f, wgt in zip(row, ws):
            w = CW * wgt / tot
            self.field(f, x, self.y, w - (2.5 * mm if f is not row[-1] else 0))
            x += w
        self.y -= h + 1.6 * mm

    def field_h(self, f):
        k = f["k"]
        if k in ("boxes", "date", "line", "money"):
            return 13 + 6.3 * 2 + BOXH if k != "line" else 13 + 6.3 * 2 + 5 * mm
        if k == "check":
            n = len(f["opts"])
            per = f.get("cols", 3)
            return 22 + ((n + per - 1) // per) * 15
        if k == "table":
            return 16 + 7 * mm + f["rows"] * 6.2 * mm
        if k == "text":
            t = tx(f["t"])
            return len(self.wrap(t["en"], "F", 6.6, CW * 0.98)) * 7.6 + len(self.wrap(t["ir"] + " / " + t["ru"], "FI", 5.5, CW * .98)) * 6.3 + 4
        if k == "area":
            return 20 + f.get("lines", 3) * 6.5 * mm
        if k == "sign":
            return 26 * mm
        if k == "photo":
            return 44 * mm
        if k == "stamp":
            return 30 * mm
        return 14 * mm

    def field(self, f, x, y, w):
        k = f["k"]
        sup = f.get("note")
        if sup:
            self.notes.append(sup)
            sup = f"({len(self.notes)})"
        if k == "boxes":
            lh = self.label(x, y - 7, f["l"], w, sup)
            n = f.get("n") or int(w // BOX)
            n = min(n, int(w // BOX))
            self.boxes(x, y - 7 - lh + 2, n)
        elif k == "money":
            lh = self.label(x, y - 7, f["l"], w, sup)
            n = min(f.get("n", 10), int((w - 12 * mm) // BOX))
            self.boxes(x, y - 7 - lh + 2, n)
            self.text(x + n * BOX + 1.2 * mm, y - 7 - lh - 2.2 * mm, "som · tyiyn", "F", 6.4)
        elif k == "date":
            lh = self.label(x, y - 7, f["l"], w, sup)
            yy = y - 7 - lh + 2
            xx = x
            for n, cap in ((2, "DD"), (2, "MM"), (4, "YYYY")):
                self.boxes(xx, yy, n)
                self.text(xx + n * BOX / 2, yy - BOXH - 5.5, cap, "F", 4.8, self.grey(), "c")
                xx += n * BOX + 1.6 * mm
        elif k == "line":
            lh = self.label(x, y - 7, f["l"], w, sup)
            self.rule(x, y - 7 - lh - 3 * mm, x + w, .5)
        elif k == "check":
            lh = self.label(x, y - 7, f["l"], w, sup)
            per = f.get("cols", 3)
            cw = w / per
            yy = y - 7 - lh
            for i, o in enumerate(f["opts"]):
                o = tx(o)
                cx = x + (i % per) * cw
                cy = yy - (i // per) * 15
                self.checkbox(cx, cy + 1)
                self.text(cx + 4.4 * mm, cy - 6.4, o["en"], "F", 6.8)
                small = o["ir"] + " / " + o["ru"]
                small = self.wrap(small, "FI", 5.2, cw - 5 * mm)[0]
                self.text(cx + 4.4 * mm, cy - 12.2, small, "FI", 5.2, self.grey())
        elif k == "table":
            lh = self.label(x, y - 7, f["l"], w, sup) if f.get("l") else 0
            yy = y - 7 - lh
            cols = f["cols"]
            tw = sum(cc[1] for cc in cols)
            hh = 7 * mm
            self.c.setLineWidth(.5)
            self.c.setStrokeColor(self.ink)
            self.c.setFillColor(self.tint)
            self.c.rect(x, yy - hh, w, hh, fill=1, stroke=1)
            xx = x
            for name, cwt in cols:
                name = tx(name)
                ww = w * cwt / tw
                self.c.line(xx, yy, xx, yy - hh - f["rows"] * 6.2 * mm)
                ln = self.wrap(name["en"], "FB", 6.2, ww - 2 * mm)
                ty = yy - 6
                for l_ in ln[:2]:
                    self.text(xx + 1 * mm, ty, l_, "FB", 6.2)
                    ty -= 6.6
                self.text(xx + 1 * mm, yy - hh + 2.2, self.wrap(name["ru"], "FI", 5, ww - 2 * mm)[0], "FI", 5, self.grey())
                xx += ww
            self.c.line(x + w, yy, x + w, yy - hh - f["rows"] * 6.2 * mm)
            for r in range(f["rows"] + 1):
                self.c.line(x, yy - hh - r * 6.2 * mm, x + w, yy - hh - r * 6.2 * mm)
            if f.get("numbered", True):
                for r in range(f["rows"]):
                    self.text(x + 1 * mm, yy - hh - (r + 1) * 6.2 * mm + 2.2 * mm, f"{r + 1}.", "F", 6, self.grey())
        elif k == "text":
            t = tx(f["t"])
            yy = self.para(x, y - 7, t["en"], "F", 6.6, w, 7.6)
            self.para(x, yy, t["ir"] + " / " + t["ru"], "FI", 5.5, w, 6.3, self.grey())
        elif k == "area":
            lh = self.label(x, y - 7, f["l"], w, sup)
            yy = y - 7 - lh - 1 * mm
            for i in range(f.get("lines", 3)):
                yy -= 6.5 * mm
                self.rule(x, yy, x + w, .4)
        elif k == "sign":
            labs = f.get("l", ["sign", "date"])
            n = len(labs)
            cw = (w - 30 * mm) / n
            for i, lab in enumerate(labs):
                xx = x + i * cw
                self.rule(xx, y - 13 * mm, xx + cw - 4 * mm, .5)
                self.label(xx, y - 13 * mm - 9, lab, cw - 4 * mm)
            # seal circle
            cx, cy = x + w - 14 * mm, y - 11 * mm
            self.c.setDash(1.5, 1.5)
            self.c.setLineWidth(.5)
            self.c.circle(cx, cy, 10 * mm)
            self.c.setDash()
            self.text(cx, cy - 2, f.get("seal", "M.P. / Möör / М.П."), "FI", 6, self.grey(), "c")
        elif k == "photo":
            self.c.setLineWidth(.6)
            self.c.setDash(2, 1.5)
            self.c.rect(x, y - 42 * mm, 30 * mm, 40 * mm)
            self.c.setDash()
            yy = y - 12 * mm
            for ln in ["PHOTOGRAPH", "3 × 4 cm", "matt paper,", "taken within", "the last", "6 months", "SÜRÖT · ФОТО"]:
                self.text(x + 15 * mm, yy, ln, "F", 6.2, self.grey(), "c")
                yy -= 7.5
        elif k == "stamp":
            self.c.setLineWidth(.6)
            self.c.setDash(2, 1.5)
            self.c.rect(x, y - 28 * mm, min(w, 42 * mm), 26 * mm)
            self.c.setDash()
            t = tx(f.get("l", T("Place the state duty stamp here", "Mamlekettik bajı markasın bul jerge chaplañız", "Место для марки государственной пошлины")))
            yy = y - 11 * mm
            for ln in self.wrap(t["en"], "F", 6.4, min(w, 42 * mm) - 4 * mm):
                self.text(x + min(w, 42 * mm) / 2, yy, ln, "F", 6.4, self.grey(), "c")
                yy -= 7.4
            self.text(x + min(w, 42 * mm) / 2, yy - 2, self.wrap(t["ru"], "FI", 5.4, min(w, 42 * mm) - 4 * mm)[0], "FI", 5.4, self.grey(), "c")

    def official(self, rows):
        self.need(40 * mm)
        top = self.y
        self.y -= 3 * mm
        start = self.y
        o = COMMON["official"]
        self.text(ML + 2 * mm, self.y - 3, f'{o["en"]}  ·  {o["ir"]}  ·  {o["ru"]}', "FB", 7)
        self.y -= 6 * mm
        for r in rows:
            self.row(r)
        h = top - self.y + 1 * mm
        self.c.setFillColor(Color(0, 0, 0, alpha=0.06))
        self.c.setStrokeColor(self.ink)
        self.c.setLineWidth(1.1)
        self.c.setDash(4, 2)
        self.c.rect(ML - 1 * mm, self.y - 1 * mm, CW + 2 * mm, h, stroke=1, fill=1)
        self.c.setDash()
        self.y -= 4 * mm

    def counterfoil(self, cf):
        y = MB + 2 * mm + 30 * mm
        self.rule(ML - 6 * mm, y, PW - MR + 6 * mm, .6, (3, 2))
        self.c.setFont("S", 9)
        self.c.setFillColor(self.ink)
        self.c.drawString(ML - 5 * mm, y - 1.4 * mm, "✂")
        self.text(PW / 2, y + 1.6 * mm, "Cut here · Bu jerden kesiñiz · Линия отреза", "FI", 5.8, self.grey(), "c")
        t = tx(cf["t"])
        self.text(ML, y - 5.5 * mm, f'{t["en"].upper()} (Form {self.spec["code"]})', "FB", 8)
        self.text(ML, y - 8.6 * mm, t["ir"] + " / " + t["ru"], "FI", 6, self.grey())
        save = self.y
        self.y = y - 11 * mm
        for r in cf["rows"]:
            hs = max(self.field_h(f) for f in (r if isinstance(r, list) else [r]))
            x = ML
            fs = r if isinstance(r, list) else [r]
            tot = sum(f.get("w", 1) for f in fs)
            for f in fs:
                w = CW * f.get("w", 1) / tot
                self.field(f, x, self.y, w - (2.5 * mm if f is not fs[-1] else 0))
                x += w
            self.y -= hs + 1 * mm
        self.y = save

    def notes_page(self):
        notes = self.spec.get("notes", [])
        allnotes = self.notes + notes
        if not allnotes:
            return
        self.need(40 * mm)
        self.text(ML, self.y, "NOTES · TÜSHÜNDÜRMÖLÖR · ПРИМЕЧАНИЯ", "FB", 8)
        self.y -= 10
        for i, n in enumerate(allnotes, 1):
            n = tx(n)
            h = len(self.wrap(n["en"], "F", 6.6, CW - 6 * mm)) * 7.6 + len(self.wrap(n["ir"] + " / " + n["ru"], "FI", 5.5, CW - 6 * mm)) * 6.3 + 4
            self.need(h)
            self.text(ML, self.y, f"({i})", "FB", 6.6)
            yy = self.para(ML + 6 * mm, self.y, n["en"], "F", 6.6, CW - 6 * mm, 7.6)
            self.y = self.para(ML + 6 * mm, yy, n["ir"] + " / " + n["ru"], "FI", 5.5, CW - 6 * mm, 6.3, self.grey()) - 3

    def build(self):
        s = self.spec
        self.header()
        self.title()
        self.instructions()
        for i, sec in enumerate(s["sections"]):
            sec = dict(sec)
            sec.setdefault("n", chr(65 + i))
            self.section(sec)
        if s.get("declaration"):
            self.need(self.field_h({"k": "text", "t": s["declaration"]}) + 30 * mm)
            self.row({"k": "text", "t": s["declaration"]})
            self.row({"k": "sign", "l": s.get("signs", ["sign", "date"])})
        if s.get("official"):
            self.official(s["official"])
        self.notes_page()
        if s.get("counterfoil"):
            # the counterfoil goes at the foot of the last page
            if self.y < MB + 46 * mm:
                self.new_page()
            self.counterfoil(s["counterfoil"])
        self.footer()
        self.c.showPage()
        return self.page


def render(path, spec):
    # two passes so "Page n of N" is right
    tmp = dict(spec)
    n = Form(path, tmp).build()
    tmp["_pages"] = n
    f = Form(path, tmp)
    f.build()
    f.c.save()
    return n
