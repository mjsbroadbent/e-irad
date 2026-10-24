"""The catalogue of printed forms: code, file, titles, issuing body, the portal service it belongs to.
Written to data/forms.json by build.py; the Permits and forms page and the service pages read that file.
Post forms live on post.iradgov.org (site "post"); everything else on e-irad.org/forms/."""

def T(en, ir, ru):
    return {"en": en, "ir": ir, "ru": ru}

AG = {
    "prs": T("Passport and Residence Service, Ministry of Internal Security", "Pasport jana jashoo jayı kızmatı, Ichki koopsuzduk ministrligi", "Служба паспортов и регистрации, Министерство внутренней безопасности"),
    "hpc": T("Highway Patrol Corps, Republican Gendarmerie", "Avtojol patrul korpusu, Respublikalık jandarmeriya", "Корпус дорожного патруля, Республиканская жандармерия"),
    "cr": T("District civil registry offices", "Aymaktık JAAK bölümdörü", "Районные отделы ЗАГС"),
    "mis": T("Ministry of Internal Security, Records Department", "Ichki koopsuzduk ministrligi, Esepke aluu departamenti", "Министерство внутренней безопасности, Учётный департамент"),
    "sf": T("Social Fund of the ISEZ", "IAEZdin Sotsialdık fondu", "Социальный фонд ОЭЗИ"),
    "tax": T("Tax Service, Ministry of Finance", "Salık kızmatı, Finans ministrligi", "Налоговая служба, Министерство финансов"),
    "bank": T("Talasbank (form approved by the Bank of Irad)", "Talasbank (Irad Bankı bekitken forma)", "«Таласбанк» (форма утверждена Банком Ирада)"),
    "dic": T("Department of Infrastructure and Communications", "Infrastruktura jana baylanısh departamenti", "Департамент инфраструктуры и связи"),
    "rf": T("Register of Firms, Ministry of Economy", "Firmalar reestri, Ekonomika ministrligi", "Реестр фирм, Министерство экономики"),
    "me": T("Licensing Division, Ministry of Economy", "Litsenziyaloo bölümü, Ekonomika ministrligi", "Отдел лицензирования, Министерство экономики"),
    "city": T("City Halls of Talas, Nurzhan and Iyık Janyl", "Talas, Nurzhan jana Iyık Janıl meriyaları", "Мэрии Таласа, Нуржана и Ийык-Джаныла"),
    "arch": T("Architecture and Planning Department, City Hall", "Arkhitektura jana shaar kuruluşu bölümü, meriya", "Управление архитектуры и градостроительства, мэрия"),
    "fte": T("Irad Foreign Trade Escrow Authority", "Irad tashkı sooda eskrou organı", "Орган эскроу внешней торговли Ирада"),
    "tso": T("Territorial Statistics Office", "Aymaktık statistika keñsesi", "Территориальное статистическое управление"),
    "agr": T("Talas Basin Agricultural Directorate, Hunting and Fisheries Section", "Talas basseyninin aylı charba direktsiyası, Añchılık jana balık charba bölümü", "Таласское бассейновое управление сельского хозяйства, отдел охоты и рыболовства"),
    "ij": T("City Hall of Iyık Janyl", "Iyık Janıl meriyası", "Мэрия Ийык-Джаныла"),
    "sa": T("State Archives of Irad", "Irad mamlekettik arkhivi", "Государственный архив Ирада"),
    "og": T("Office of the Governor, Letters and Appeals Section", "Gubernator keñsesi, Kattar jana kayrıluular bölümü", "Канцелярия Губернатора, отдел писем и обращений"),
    "taz": T("Tazalık Municipal Sanitation Enterprise", "Tazalık shaardık tazaloo ishkanası", "МП «Тазалык»"),
    "rg": T("Republican Gendarmerie, Line Command", "Respublikalık jandarmeriya, Liniya komandovaniyesi", "Республиканская жандармерия, командование линии"),
    "post": T("Irad Pochtasy, State Postal Enterprise", "Irad Pochtası, Mamlekettik pochta ishkanası", "ГП «Ирадпочта»"),
}

# code, agency, category, service id (e-Irad), title
FORMS = [
    # documents and residence
    ("PRS-1", "prs", "people", "passport", T("Application for a passport or identity card", "Pasportko je jeke kuböölükkö arız", "Заявление на выдачу паспорта или удостоверения личности")),
    ("PRS-3", "prs", "people", "address", T("Notification of change of address of residence", "Jashoo darekin özgörtüü tuuraluu bildirme", "Уведомление о смене адреса места жительства")),
    ("PRS-7", "prs", "people", "lostid", T("Application to replace a lost, stolen or damaged identity card", "Jogolgon, uurdalgan je buzulgan jeke kuböölüktü almashtıruu arızı", "Заявление о замене утерянного, похищенного или повреждённого удостоверения личности")),
    ("HPC-12", "hpc", "people", "licence", T("Application to exchange a foreign driving licence", "Chet eldik aydoochuluk kuböölügün almashtıruu arızı", "Заявление об обмене иностранного водительского удостоверения")),
    ("CR-9", "cr", "people", "namechange", T("Application to change a surname, first name or patronymic", "Familiyanı, attı je atasının atın özgörtüü arızı", "Заявление о перемене фамилии, имени или отчества")),
    ("CR-2", "cr", "people", "civil", T("Request for a duplicate civil registration certificate", "Jarandık abal aktısının kuböölügünün dublikatın suroo", "Запрос дубликата свидетельства о регистрации акта гражданского состояния")),
    ("MIS-22", "mis", "people", "conduct", T("Request for a certificate of good conduct", "Jakshı jürüsh-turush tuuraluu malımatnama suroo", "Запрос справки о благонадёжности")),
    ("SF-1", "sf", "people", "pension", T("Application for an old-age pension", "Karılık pensiyasına arız", "Заявление о назначении пенсии по старости")),
    # bills and payments
    ("TS-14", "tax", "pay", "proptax", T("Property tax return for individuals", "Jeke adamdardın mülk salıgı boyuncha deklaratsiya", "Декларация по налогу на имущество физических лиц")),
    ("BI-0401", "bank", "pay", "duty", T("Payment order for state duty", "Mamlekettik bajı üchün tölöm tapshırması", "Платёжное поручение на уплату государственной пошлины")),
    ("DIC-5", "dic", "pay", "roadcharge", T("Declaration for the annual road-use charge", "Jıldık jol akısı boyuncha deklaratsiya", "Декларация на уплату годового сбора за пользование дорогами")),
    # permits and business
    ("RF-1", "rf", "biz", "business", T("Application for registration of a business entity", "Charbalık subyektti kattoo arızı", "Заявление о регистрации хозяйствующего субъекта")),
    ("RF-8", "rf", "check", "firmcheck", T("Request for an extract from the Register of Firms", "Firmalar reestrinen köchürmö suroo", "Запрос выписки из Реестра фирм")),
    ("CH-31", "city", "biz", "event", T("Application for a municipal permit for a public event", "Kogomduk ish-chara üchün shaardık uruksatka arız", "Заявление на муниципальное разрешение на проведение мероприятия")),
    ("CH-40", "city", "biz", "stall", T("Application for a trading place at a municipal market", "Shaardık bazardan sooda orunun aluu arızı", "Заявление о предоставлении торгового места на муниципальном рынке")),
    ("CH-44", "city", "biz", "sign", T("Application for permission to place an outdoor sign", "Tışkı jarnama tablichkasın ornotuuga uruksat arızı", "Заявление на разрешение размещения наружной вывески")),
    ("CA-6", "arch", "biz", "building", T("Application for a building permit", "Kuruluşka uruksat arızı", "Заявление на разрешение на строительство")),
    ("DIC-3", "dic", "biz", "taxi", T("Application for a passenger taxi licence", "Jürgünchü taksi litsenziyasına arız", "Заявление на лицензию на перевозку пассажиров такси")),
    ("ME-17", "me", "biz", "alcohol", T("Application for a licence to sell alcoholic beverages", "Spirt ichimdikterin satuuga litsenziya arızı", "Заявление на лицензию на продажу алкогольной продукции")),
    ("FTE-2", "fte", "biz", "trader", T("Registration card of a foreign trade participant", "Tashkı sooda katıshuuchusunun kattoo kartochkası", "Регистрационная карточка участника внешнеторговой деятельности")),
    ("TSO-26", "tso", "biz", "census", T("Census questionnaire for business entities 2026", "2026-jılkı charbalık subyektterdin sanak suroo kagazı", "Переписной лист хозяйствующих субъектов 2026")),
    # other
    ("AGR-11", "agr", "other", "hunting", T("Application for a hunting and fishing licence", "Añchılık jana balık uloo litsenziyasına arız", "Заявление на лицензию на охоту и рыболовство")),
    ("CH-50", "city", "other", "gathering", T("Notification of a public gathering", "Kogomduk chogulush tuuraluu bildirme", "Уведомление о проведении публичного собрания")),
    ("IJ-3", "ij", "other", "feastpass", T("Application for a vehicle pass to Cathedral Hill for the Feast of St. Janyl", "Iyık Janıl mayramında Sobor dobosuna unaa ötkörmösünö arız", "Заявление на пропуск транспорта на Соборный холм в праздник Святой Джаныл")),
    ("SA-4", "sa", "other", "archive", T("Request for copies of archival documents", "Arkhiv dokumentterinin köchürmölörün suroo", "Запрос копий архивных документов")),
    ("OG-1", "og", "other", "appeal", T("Written appeal to a state body", "Mamlekettik organga jazuu jüzündögü kayrıluu", "Письменное обращение в государственный орган")),
    ("TZ-61", "taz", "other", "dog", T("Dog registration card", "It kattoo kartochkası", "Регистрационная карточка собаки")),
    ("RG-9", "rg", "other", "crossing", T("Application for a Qara-Chik line crossing pass", "Kara-Chik liniyasınan ötüü ötkörmösünö arız", "Заявление на пропуск через линию Кара-Чик")),
    # Irad Pochtasy
    ("P-2", "post", "post", "parcel", T("Customs declaration for postal items sent abroad", "Chet elge jönötülgön pochta jönötmölörü üchün bajı deklaratsiyası", "Таможенная декларация на международные почтовые отправления")),
    ("P-4", "post", "post", "parcel", T("Parcel dispatch note", "Posılka jönötüü kagazı", "Сопроводительный адрес к посылке")),
    ("P-11", "post", "post", None, T("Domestic money order", "Ölkö ichindegi akcha kotoruu", "Почтовый перевод по Ираду")),
    ("P-15", "post", "post", "parcel", T("Enquiry about a missing postal item", "Jogolgon pochta jönötmösü boyuncha suroo", "Заявление о розыске почтового отправления")),
    ("P-21", "post", "post", None, T("Subscription order for newspapers and periodicals, 2027", "2027-jılga gazeta jana jurnaldarga jazıluu buyurtması", "Абонемент на подписку на газеты и журналы, 2027")),
    ("P-27", "post", "post", "pension", T("Power of attorney to collect mail and pensions", "Pochtanı jana pensiyanı aluuga ışenim kat", "Доверенность на получение почты и пенсии")),
    ("P-30", "post", "post", None, T("Application to rent a post-office box", "Pochta yashıgın ijaraga aluu arızı", "Заявление на аренду абонентского ящика")),
]
