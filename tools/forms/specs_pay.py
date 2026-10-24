"""Forms: bills and payments."""
from engine import T
from specs_people import PERSON, address, CONTACT, DECL, STD_INS, OFFICIAL_STD

FORMS = {}

FORMS["TS-14"] = {
    "ink": "#1b1b1b", "mark": "gov", "rev": "rev. 12/2022 (for the tax year 2026)",
    "approved": "Approved by Order of the Ministry of Finance No. 212 of 28 December 2022 under the Tax Code, articles 341–356",
    "to": T("District tax inspectorate at the location of the property", "Mülk jaylashkan jerdegi aymaktık salık inspektsiyası", "Районная налоговая инспекция по месту нахождения имущества"),
    "instructions": STD_INS + [
        T("File one return for each property, by 1 April of the year following the tax year. Property held in common is declared by each co-owner for his or her share. Amounts are in som without tyiyn, rounded down.", "Ar bir mülk üchün bir deklaratsiyanı salık jılınan kiyinki jıldın 1-aprelıne cheyin beriñiz. Jalpı mülktü ar bir birge ee öz ülüshü boyuncha deklaratsiyalayt. Summalar tyiynsız som menen, tömön tegerektelip jazılat.", "Подавайте одну декларацию на каждый объект до 1 апреля года, следующего за налоговым. Общее имущество декларирует каждый сособственник за свою долю. Суммы в сомах без тыйынов, с округлением вниз."),
        T("The cadastral value is taken from the Technical Inventory Bureau passport. If the passport is older than 2009, the value is multiplied by the coefficient in Note 2 before the rate is applied.", "Kadastrdık baası Tekhnikalık inventarizatsiya byurosunun pasportunan alınat. Eger pasport 2009-jıldan eski bolso, baa stavka koldonulğanğa cheyin 2-eskertüüdögü koeffitsientke koböytülöt.", "Кадастровая стоимость берётся из паспорта Бюро технической инвентаризации. Если паспорт выдан до 2009 года, стоимость умножается на коэффициент из примечания 2 до применения ставки."),
    ],
    "sections": [
        dict(PERSON, rows=PERSON["rows"] + [[{"k": "boxes", "l": "tin", "n": 14, "w": 1.6}, {"k": "check", "l": T("Return", "Deklaratsiya", "Декларация"), "opts": [T("first", "alğachkı", "первичная"), T("corrective No.", "tüzötüü No.", "корректирующая №")], "cols": 2, "w": 1.4}]]),
        {"t": T("Property", "Mülk", "Имущество"), "rows": [
            {"k": "check", "l": T("Type of property", "Mülktün türü", "Вид имущества"), "opts": [T("flat", "batir", "квартира"), T("house", "üy", "жилой дом"), T("summer house (dacha)", "dacha", "дача"), T("garage", "garaj", "гараж"), T("non-residential premises", "turak emes jay", "нежилое помещение"), T("unfinished construction", "bütpögön kuruluş", "незавершённое строительство")], "cols": 3},
            [{"k": "boxes", "l": T("Cadastral number", "Kadastrdık nomeri", "Кадастровый номер"), "n": 16, "w": 1.8}, {"k": "boxes", "l": T("Technical Inventory Bureau passport No.", "Tekhnikalık inventarizatsiya byurosunun pasport No.", "№ паспорта БТИ"), "n": 10, "w": 1.2}],
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "street", "w": 1.6}, {"k": "boxes", "l": "house", "n": 4, "w": .45}],
            [{"k": "boxes", "l": T("Total area, m²", "Jalpı aymagı, m²", "Общая площадь, м²"), "n": 6, "w": 1}, {"k": "boxes", "l": T("Year built", "Kurulgan jılı", "Год постройки"), "n": 4, "w": .8}, {"k": "boxes", "l": T("Share held (e.g. 1/2)", "Ülüshü (mısalı 1/2)", "Доля (напр. 1/2)"), "n": 5, "w": .9}, {"k": "check", "l": T("Walls", "Dubalları", "Стены"), "opts": [T("brick", "kırpıch", "кирпич"), T("concrete panel", "beton panel", "панель"), T("adobe", "kerpich", "саман")], "cols": 3, "w": 1.6}],
        ]},
        {"t": T("Calculation of the tax", "Salıktı esepteö", "Расчёт налога"), "rows": [
            {"k": "table", "cols": [(T("Line", "Sap", "Строка"), .8), (T("Item", "Körsötküch", "Показатель"), 5.5), (T("Amount, som", "Summa, som", "Сумма, сом"), 2)], "rows": 9, "numbered": False},
            {"k": "text", "t": T("Lines: 010 cadastral value; 020 coefficient (Note 2); 030 value after coefficient (010 × 020); 040 share; 050 taxable value (030 × 040); 060 rate (Note 3); 070 tax (050 × 060); 080 relief (Note 4); 090 tax payable (070 − 080). If line 090 is less than 50 som, no tax is payable but the return must still be filed.", "Saptar: 010 kadastrdık baa; 020 koeffitsient (2-eskertüü); 030 koeffitsientten kiyinki baa (010 × 020); 040 ülüsh; 050 salık salınuuchu baa (030 × 040); 060 stavka (3-eskertüü); 070 salık (050 × 060); 080 jeñildik (4-eskertüü); 090 tölönüüchü salık (070 − 080). Eger 090-sap 50 somdon az bolso, salık tölönböyt, birok deklaratsiya baarıbir beriliş kerek.", "Строки: 010 кадастровая стоимость; 020 коэффициент (прим. 2); 030 стоимость с коэффициентом (010 × 020); 040 доля; 050 налоговая база (030 × 040); 060 ставка (прим. 3); 070 налог (050 × 060); 080 льгота (прим. 4); 090 налог к уплате (070 − 080). Если строка 090 меньше 50 сомов, налог не уплачивается, но декларация подаётся.")},
            {"k": "check", "l": T("Relief claimed", "Suralgan jeñildik", "Заявленная льгота"), "opts": [T("pensioner (one dwelling)", "pensioner (bir turak jay)", "пенсионер (одно жильё)"), T("disability group I or II", "I je II top mümkünchülügü chektelgen", "инвалид I или II группы"), T("veteran of 1992", "1992-jıldın ardageri", "ветеран 1992 года"), T("family with four or more children", "tört je andan köp baldu üy-bülö", "семья с четырьмя и более детьми"), T("none", "jok", "нет")], "cols": 3},
        ]},
        {"t": T("Contact details", "Baylanısh maalımatı", "Контактные данные"), "rows": [CONTACT]},
    ],
    "declaration": DECL,
    "official": OFFICIAL_STD,
    "counterfoil": {"t": T("Receipt for a tax return", "Salık deklaratsiyasın kabıl alğanı tuuraluu tilkat", "Квитанция о приёме налоговой декларации"), "rows": [[{"k": "line", "l": "fullname", "w": 2}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.3}, {"k": "date", "l": T("Date received", "Kabıl alıngan kün", "Дата приёма"), "w": 1.2}]]},
    "notes": [
        T("Coefficients for passports issued before 2009: 1993–1999, 3.10; 2000–2004, 2.35; 2005–2008, 1.68. Passports issued in Soviet times are not accepted; order a new one from the Technical Inventory Bureau.", "2009-jılğa cheyin berilgen pasporttor üchün koeffitsientter: 1993–1999, 3,10; 2000–2004, 2,35; 2005–2008, 1,68. Sovettik mezgilde berilgen pasporttor kabıl alınbayt; Tekhnikalık inventarizatsiya byurosunan jañısın buyurtuñuz.", "Коэффициенты для паспортов до 2009 года: 1993–1999 — 3,10; 2000–2004 — 2,35; 2005–2008 — 1,68. Паспорта советского времени не принимаются; закажите новый в БТИ."),
        T("Rates: dwellings 0.35% of the taxable value (0.5% in Talas and Nurzhan within the ring roads); non-residential premises 0.8%; unfinished construction older than five years 1.5%.", "Stavkalar: turak jaylar salık salınuuchu baanın 0,35% (Talas jana Nurzhanda aylanma joldordun ichinde 0,5%); turak emes jaylar 0,8%; besh jıldan eski bütpögön kuruluş 1,5%.", "Ставки: жильё 0,35% налоговой базы (0,5% в Таласе и Нуржане в пределах кольцевых дорог); нежилые помещения 0,8%; незавершённое строительство старше пяти лет 1,5%."),
        T("Relief: 100% for one dwelling of up to 80 m² for the persons listed in Section C; documents proving entitlement must be attached every year.", "Jeñildik: C bölümündö atalgandar üchün 80 m²ğa cheyinki bir turak jayğa 100%; ukuktu dalildegen dokumentter ar jılı tirkeliş kerek.", "Льгота: 100% на одно жильё до 80 м² для лиц, указанных в разделе C; подтверждающие документы прикладываются ежегодно."),
    ],
}

FORMS["BI-0401"] = {
    "ink": "#0f5a3a", "mark": "talasbank", "mark_colour": True, "rev": "Bank of Irad form 0401060",
    "approved": "Form 0401060 approved by Bank of Irad Notice 2011/3; accepted at all licensed banks",
    "printnote": "Completed in one copy; the bank returns the stamped counterfoil.",
    "printnote2": "Payment orders with corrections, or with the amount in words not matching the amount in figures, are returned unpaid.",
    "instructions": [],
"sections": [
        {"t": T("Payment order", "Tölöm tapshırması", "Платёжное поручение"), "rows": [
            [{"k": "boxes", "l": T("No.", "No.", "№"), "n": 6, "w": .8}, {"k": "date", "l": "date", "w": 1}, {"k": "check", "l": T("Type of payment", "Tölömdün türü", "Вид платежа"), "opts": [T("cash", "nakta", "наличными"), T("from account", "esepten", "со счёта")], "cols": 2, "w": 1.3}],
            {"k": "money", "l": T("Amount in figures", "Summa sandar menen", "Сумма цифрами"), "n": 10},
            {"k": "line", "l": T("Amount in words", "Summa söz menen", "Сумма прописью")},
            [{"k": "line", "l": T("Payer (full name)", "Tölööchü (toluk atı)", "Плательщик (Ф.И.О.)"), "w": 2}, {"k": "boxes", "l": "pin", "n": 14, "w": 1.6}],
            [{"k": "line", "l": T("Payer's bank", "Tölööchünün bankı", "Банк плательщика"), "w": 2}, {"k": "boxes", "l": T("Account No. (if from account)", "Esep No. (esepten bolso)", "№ счёта (если со счёта)"), "n": 16, "w": 1.6}],
            [{"k": "line", "l": T("Recipient", "Aluuchu", "Получатель"), "w": 2}, {"k": "boxes", "l": T("Treasury account No.", "Kaznachılıktın esep No.", "№ счёта Казначейства"), "n": 16, "w": 1.6}],
            [{"k": "line", "l": T("Recipient's bank", "Aluuchunun bankı", "Банк получателя"), "w": 2}, {"k": "boxes", "l": T("Bank code", "Bank kodu", "Код банка"), "n": 6, "w": .9}, {"k": "boxes", "l": T("Purpose code (24)", "Maksat kodu (24)", "Код назначения (24)"), "n": 6, "w": .9}],
            {"k": "line", "l": T("Purpose of payment (name of the duty, the body and the applicant)", "Tölömdün maksatı (bajının, organdın jana arız beruuchunun atı)", "Назначение платежа (наименование пошлины, органа и заявителя)")},
            {"k": "text", "t": T("Treasury accounts: Talasbank 4001 0000 0000 1993; Ak Bata Bank 4001 0024 0000 0001; Chuy Commercial Bank 4001 0016 0000 0001. Bank codes and purpose codes are listed in the schedule of state duties (e-irad.org, State duty calculator).", "Kaznachılıktın esepteri: Talasbank 4001 0000 0000 1993; Ak Bata Bank 4001 0024 0000 0001; Chüy Kommertsiyalık Bankı 4001 0016 0000 0001. Bank kodtoru jana maksat kodtoru mamlekettik bajılar tizmesinde (e-irad.org, Mamlekettik bajı kalkulyatoru).", "Счета Казначейства: «Таласбанк» 4001 0000 0000 1993; «Ак Бата Банк» 4001 0024 0000 0001; «Чуйский коммерческий банк» 4001 0016 0000 0001. Коды банков и назначения — в перечне госпошлин (e-irad.org, калькулятор пошлин).")},
            {"k": "sign", "l": [T("Payer's signature", "Tölööchünün kolu", "Подпись плательщика"), T("Teller", "Kassir", "Кассир"), T("Controller", "Kontroler", "Контролёр")], "seal": "Bank stamp / Bank möörü / Штамп банка"},
        ]},
    ],
    "counterfoil": {"t": T("Counterfoil for the payer", "Tölööchü üchün kvitantsiya", "Квитанция плательщику"), "rows": [
        [{"k": "boxes", "l": T("No.", "No.", "№"), "n": 6, "w": .7}, {"k": "money", "l": T("Amount", "Summa", "Сумма"), "n": 8, "w": 1.6}, {"k": "boxes", "l": T("Purpose code", "Maksat kodu", "Код назначения"), "n": 6, "w": .9}, {"k": "line", "l": T("Teller (signature, stamp)", "Kassir (kolu, möör)", "Кассир (подпись, штамп)"), "w": 1.2}],
    ]},
}

FORMS["DIC-5"] = {
    "ink": "#1d2f5e", "mark": "gov", "rev": "rev. 01/2019",
    "approved": "Approved by Order of the Department of Infrastructure and Communications No. 3 of 9 January 2019 under Executive Directive 2019/07",
    "to": T("Road Fund Section, Department of Infrastructure and Communications", "Jol fondu bölümü, Infrastruktura jana baylanısh departamenti", "Отдел дорожного фонда, Департамент инфраструктуры и связи"),
    "instructions": STD_INS + [T("The road-use charge is paid once a year for every motor vehicle registered in the ISEZ, by 31 March. On payment the vehicle receives a windscreen sticker (vignette) for the calendar year; the sticker is placed in the lower right corner of the windscreen and is checked at the Highway Patrol Corps posts.", "Jol akısı IAEZde kattalgan ar bir avtounaa üchün jılına bir jolu, 31-martka cheyin tölönöt. Tölöngöndö unaa kalendardık jılğa aldıñkı aynekke chaplanuuchu belgi (vinyetka) alat; belgi aldıñkı aynektin oñ tömönkü burchuna chaplanat jana Avtojol patrul korpusunun postorunda tekshirilet.", "Сбор за пользование дорогами уплачивается раз в год за каждое транспортное средство, зарегистрированное в ОЭЗИ, до 31 марта. После оплаты выдаётся наклейка (виньетка) на календарный год; она клеится в правый нижний угол лобового стекла и проверяется на постах Корпуса дорожного патруля.")],
    "sections": [
        dict(PERSON, t=T("Owner of the vehicle", "Unaanın eesi", "Владелец транспортного средства")),
        {"t": T("Vehicle", "Unaa", "Транспортное средство"), "rows": [
            [{"k": "boxes", "l": T("Registration plate", "Mamlekettik nomeri", "Госномер"), "n": 9, "w": 1}, {"k": "boxes", "l": T("VIN / chassis No.", "VIN / shassi No.", "VIN / № шасси"), "n": 17, "w": 2}],
            [{"k": "line", "l": T("Make and model", "Markası jana modeli", "Марка и модель"), "w": 1.5}, {"k": "boxes", "l": T("Year", "Jılı", "Год"), "n": 4, "w": .6}, {"k": "boxes", "l": T("Engine, cm³", "Kıymıldatkıch, sm³", "Двигатель, см³"), "n": 5, "w": .8}, {"k": "boxes", "l": T("Gross weight, kg", "Toluk salmağı, kg", "Полная масса, кг"), "n": 6, "w": .9}],
            {"k": "check", "l": T("Category for the charge", "Akı üchün kategoriya", "Категория для сбора"), "opts": [T("motorcycle", "mototsikl", "мотоцикл"), T("car up to 2,000 cm³", "2 000 sm³ğa cheyinki jeñil unaa", "легковой до 2 000 см³"), T("car over 2,000 cm³", "2 000 sm³dan ashkan jeñil unaa", "легковой свыше 2 000 см³"), T("minibus (marshrutka)", "marshrutka", "маршрутка"), T("lorry up to 12 t", "12 tğa cheyinki jük unaası", "грузовик до 12 т"), T("lorry over 12 t (per axle, see Note 1)", "12 tdan ashkan jük unaası (ar bir ok, 1-eskertüü)", "грузовик свыше 12 т (за ось, прим. 1)"), T("tractor or farm machine", "traktor je aylı charba mashinası", "трактор или сельхозмашина"), T("vehicle of a person with disability (exempt)", "mümkünchülügü chektelgen adamdın unaası (boshotulgon)", "ТС инвалида (освобождено)")], "cols": 2},
            {"k": "check", "l": T("Period", "Mezgili", "Период"), "opts": [T("full year", "toluk jıl", "полный год"), T("from registration to 31 December (pro rata)", "kattoodon 31-dekabrğa cheyin (üleshtirip)", "с регистрации до 31 декабря (пропорционально)"), T("transit vehicle, 30 days", "tranzit unaa, 30 kün", "транзитное ТС, 30 дней")], "cols": 3},
        ]},
        {"t": T("Payment", "Tölöm", "Оплата"), "rows": [
            [{"k": "money", "l": T("Charge payable", "Tölönüüchü akı", "Сбор к уплате"), "n": 7, "w": 1.3}, {"k": "boxes", "l": T("Payment order No. (Form BI-0401)", "Tölöm tapshırmasının No. (BI-0401)", "№ платёжного поручения (BI-0401)"), "n": 12, "w": 1.6}, {"k": "boxes", "l": T("Vignette No. (filled in by the Section)", "Vinyetkanın No. (bölüm tolturat)", "№ виньетки (заполняет отдел)"), "n": 8, "w": 1.2}],
        ]},
    ],
    "declaration": DECL,
    "official": OFFICIAL_STD,
    "counterfoil": {"t": T("Vignette issue slip", "Vinyetka berüü kagazı", "Талон о выдаче виньетки"), "rows": [[{"k": "boxes", "l": T("Registration plate", "Mamlekettik nomeri", "Госномер"), "n": 9, "w": 1.2}, {"k": "boxes", "l": T("Vignette No.", "Vinyetka No.", "№ виньетки"), "n": 8, "w": 1.1}, {"k": "boxes", "l": T("Year", "Jılı", "Год"), "n": 4, "w": .6}, {"k": "line", "l": T("Issued by (signature)", "Bergen (kolu)", "Выдал (подпись)"), "w": 1.2}]]},
    "notes": [T("Charges for 2026 (som): motorcycle 120; car up to 2,000 cm³ 480; over 2,000 cm³ 960; minibus 1,800; lorry up to 12 t 3,600; over 12 t 1,500 per axle; tractor 240; transit vehicle 30 days 350, collected at the crossings. Late payment: 1% per day, up to the amount of the charge.", "2026-jılğa akılar (som): mototsikl 120; 2 000 sm³ğa cheyinki jeñil unaa 480; 2 000 sm³dan ashkan 960; marshrutka 1 800; 12 tğa cheyinki jük unaası 3 600; 12 tdan ashkan ar bir okko 1 500; traktor 240; tranzit unaa 30 kün 350, ötköldördö alınat. Kechiktirip tölöö: kününö 1%, akının summasına cheyin.", "Ставки на 2026 год (сом): мотоцикл 120; легковой до 2 000 см³ — 480; свыше 2 000 см³ — 960; маршрутка 1 800; грузовик до 12 т — 3 600; свыше 12 т — 1 500 за ось; трактор 240; транзит 30 дней — 350, взимается на переходах. Просрочка: 1% в день, но не более суммы сбора.")],
}
