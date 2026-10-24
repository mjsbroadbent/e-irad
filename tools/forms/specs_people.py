"""Forms: documents and residence."""
from engine import T

INK = "#1b1b1b"

PERSON = {"t": T("Applicant", "Arız beruuchu", "Заявитель"), "rows": [
    {"k": "boxes", "l": "surname"},
    {"k": "boxes", "l": "first"},
    {"k": "boxes", "l": "patr"},
    [{"k": "date", "l": "dob", "w": 1.1}, {"k": "check", "l": "sex", "opts": ["male", "female"], "cols": 2, "w": 1}, {"k": "boxes", "l": "pin", "n": 14, "w": 2.1, "note": T("The personal number is printed on the reverse of the identity card under the photograph. Persons born before 1 January 1994 who have not been assigned a personal number write 00000000000000.", "Jeke nomer jeke kuböölüktün arka betinde süröttün astında basılgan. 1994-jıldın 1-yanvarına cheyin tuulup, jeke nomer berilbegender 00000000000000 dep jazat.", "Персональный номер напечатан на обороте удостоверения под фотографией. Лица, родившиеся до 1 января 1994 года и не получившие персонального номера, пишут 00000000000000.")}],
    {"k": "line", "l": "pob"},
    [{"k": "boxes", "l": "idser", "n": 2, "w": .55}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.25}, {"k": "date", "l": "idate", "w": 1.1}, {"k": "line", "l": "issued", "w": 1.6}],
]}


def address(title):
    return {"t": title, "rows": [
        [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "district", "w": 1}],
        [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
    ]}


CONTACT = [{"k": "boxes", "l": "phone", "n": 13, "w": 1}, {"k": "line", "l": "email", "w": 1}]

DECL = T("I declare that the information given in this form is true and complete. I understand that knowingly giving false information to a state body is an offence under the Code of Administrative Offences and that this form, once accepted, is kept for 75 years.",
         "Bul formada berilgen maalımat tuura jana toluk ekenin tastıktaym. Mamlekettik organga bile tura jalgan maalımat berüü Administrativdik ukuk buzuular kodeksi boyuncha ukuk buzuu ekenin jana kabıl alıngan bul forma 75 jıl saktaların tüshünöm.",
         "Подтверждаю, что сведения, указанные в настоящей форме, достоверны и полны. Мне известно, что заведомо ложные сведения, представленные государственному органу, являются правонарушением по Кодексу об административных правонарушениях и что принятая форма хранится 75 лет.")

STD_INS = [
    T("Complete this form in BLOCK CAPITALS in black or dark blue ink, one character per box, leaving one empty box between words.", "Bul formanı BASMA TAMGALAR menen kara je kara-kök siya menen, ar bir kutuchaga bir belgi, sözdördün arasına bir bosh kutucha kaltırıp tolturuñuz.", "Заполняйте ПЕЧАТНЫМИ БУКВАМИ чёрными или тёмно-синими чернилами, по одному знаку в клетке, оставляя между словами одну пустую клетку."),
    T("Names are written as in the identity card, in Latin letters. Do not abbreviate. Corrections, erasures and correction fluid make the form invalid; a new form must be completed.", "Attar jeke kuböölüktögüdöy latın tamgaları menen jazılat. Kıskartpañız. Onduular, öchürüülör jana tüzötkuch suyuktuk formanı jaraksız kılat; jañı forma tolturuluşu kerek.", "Имена пишутся как в удостоверении личности, латиницей. Не сокращайте. Исправления, подчистки и корректор делают форму недействительной; необходимо заполнить новую."),
    T("Sections marked “For official use only” are completed by the official. Do not sign the form until asked to do so by the official receiving it.", "“Kızmattık paydalanuu üchün gana” dep belgilengen bölümdördü kızmatker tolturat. Formanı kabıl alğan kızmatker suramayınça kol koybоñuz.", "Разделы «Только для служебного пользования» заполняются должностным лицом. Не подписывайте форму до просьбы принимающего её должностного лица."),
]

OFFICIAL_STD = [
    [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": T("Date received", "Kabıl alıngan kün", "Дата приёма"), "w": 1}],
    {"k": "check", "l": "decision", "opts": ["granted", "refused", "returned"], "cols": 3},
    {"k": "sign", "l": ["recvd", T("Signature of the official", "Kızmatkerdin kolu", "Подпись должностного лица")]},
]

FORMS = {}

FORMS["PRS-3"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 05/2016",
    "approved": "Approved by Order of the Ministry of Internal Security No. 41 of 17 May 2016 (as amended 2019, 2022)",
    "to": T("Head of the Passport and Residence Service office at the place of residence", "Jashagan jerdegi Pasport jana jashoo jayı kızmatı bölümünün bashchısına", "Начальнику отдела Службы паспортов и регистрации по месту жительства"),
    "instructions": STD_INS + [
        T("Notify the change within 10 calendar days of moving. The owner of the dwelling (or every co-owner) must countersign Section E in the presence of the official or have the signature certified by a notary.", "Köchköndön kiyin 10 kalendardık kündün ichinde bildiriñiz. Turak jaydın eesi (je ar bir birge ee) E bölümünö kızmatkerdin aldında kol koyushu je kolun notariuska tastıktatıshı kerek.", "Уведомите о переезде в течение 10 календарных дней. Собственник жилья (или каждый сособственник) подписывает раздел E в присутствии должностного лица или заверяет подпись у нотариуса."),
    ],
    "sections": [
        PERSON,
        address(T("Previous address", "Murdaңkı dareki", "Прежний адрес")),
        address(T("New address of residence", "Jashoonun jañı dareki", "Новый адрес места жительства")),
        {"t": T("Grounds for residence", "Jashoonun negizi", "Основание проживания"), "rows": [
            {"k": "check", "l": T("I live at the new address as", "Jañı darekte men tömönküdöy jashaym", "Я проживаю по новому адресу как"), "opts": [
                T("owner", "eesi", "собственник"), T("co-owner", "birge eesi", "сособственник"), T("tenant under a registered lease", "kattalgan ijara boyuncha ijarachı", "наниматель по зарегистрированному договору"),
                T("family member of the owner", "eesinin üy-bülö müchösü", "член семьи собственника"), T("tenant of municipal housing", "shaardık turak jaydın ijarachısı", "наниматель муниципального жилья"), T("other (state in Section F)", "bashka (F bölümündö körsötüñüz)", "иное (укажите в разделе F)"),
            ], "cols": 3},
            [{"k": "boxes", "l": T("Title deed or lease registration No.", "Menchik kübölügünün je ijaranın kattoo nomeri", "№ правоустанавливающего документа или договора"), "n": 16, "w": 1.6}, {"k": "date", "l": T("Date of moving", "Köchkön kün", "Дата переезда"), "w": 1}],
            {"k": "table", "l": T("Persons moving with the applicant (children under 16 are entered here, not on separate forms)", "Arız beruuchu menen birge köchköndör (16 jashka cheyinki baldar bul jerge jazılat)", "Лица, переезжающие вместе с заявителем (дети до 16 лет вписываются сюда)"),
             "cols": [("fullname", 4), ("dob", 1.6), (T("Relationship", "Tuuganchılıgı", "Степень родства"), 1.6), ("pin", 2)], "rows": 4},
        ]},
        {"t": T("Consent of the owner of the dwelling", "Turak jaydın eesinin makuldugu", "Согласие собственника жилья"), "rows": [
            {"k": "text", "t": T("I, the owner of the dwelling named in Section C, consent to the registration of the applicant and the persons listed above at this address. This consent does not create any right of ownership or use of the dwelling.", "Men, C bölümündö körsötülgön turak jaydın eesi, arız beruuchunu jana jogoruda atalgandardı bul darekke kattoogo makulmun. Bul makulduk turak jayğa menchik je paydalanuu ukugun tüzböyt.", "Я, собственник жилья, указанного в разделе C, согласен на регистрацию заявителя и перечисленных лиц по этому адресу. Согласие не порождает права собственности или пользования жильём.")},
            [{"k": "line", "l": T("Owner: surname, first name", "Eesi: familiyası, atı", "Собственник: фамилия, имя"), "w": 1.5}, {"k": "boxes", "l": "idno", "n": 9, "w": 1}],
            {"k": "sign", "l": [T("Signature of the owner", "Eesinin kolu", "Подпись собственника"), "date"], "seal": "Notary / Notarius / Нотариус"},
        ]},
        {"t": T("Contact details", "Baylanısh maalımatı", "Контактные данные"), "rows": [CONTACT,
            {"k": "area", "l": T("Remarks (other grounds for residence, temporary absence, military registration)", "Eskertüülör (jashoonun bashka negizi, ubaktıluu jok boluu, askeriy kattoo)", "Примечания (иные основания, временное отсутствие, воинский учёт)"), "lines": 2}]},
    ],
    "declaration": DECL,
    "official": OFFICIAL_STD + [[{"k": "line", "l": T("Stamp of registration placed in the identity card on page", "Kattoo möörü jeke kuböölüktün ushul betine koyuldu", "Штамп о регистрации проставлен в удостоверении на стр."), "w": 1}, {"k": "line", "l": T("Address card sent to the Records Department (No., date)", "Darek kartochkası Esepke aluu departamentine jönötüldü (No., kün)", "Адресный листок направлен в Учётный департамент (№, дата)"), "w": 1.4}]],
    "counterfoil": {"t": T("Receipt for a notification of change of address", "Darekti özgörtüü bildirmesin kabıl alğanı tuuraluu tilkat", "Расписка в приёме уведомления о смене адреса"), "rows": [
        [{"k": "line", "l": "fullname", "w": 2}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.3}, {"k": "date", "l": T("Date received", "Kabıl alıngan kün", "Дата приёма"), "w": 1.2}],
        [{"k": "line", "l": "recvd", "w": 1}, {"k": "line", "l": T("The registration stamp may be collected after (date)", "Kattoo möörün ushul künden kiyin alsa bolot", "Штамп о регистрации можно получить после (дата)"), "w": 1}],
    ]},
    "notes": [
        T("A person who does not notify a change of address within 10 days is liable to a warning or a fine of 2 to 5 calculation units. Moving within the same flat or house is not a change of address.", "Darekti 10 kündün ichinde bildirbegen adamğa eskertüü je 2den 5ke cheyin eseptik birdik ayıp salınat. Bir batirdin je üydün ichinde köchüü darekti özgörtüü bolup sanalbayt.", "Неуведомление о смене адреса в течение 10 дней влечёт предупреждение или штраф от 2 до 5 расчётных единиц. Переезд в пределах одной квартиры или дома сменой адреса не является."),
        T("Residents of the ATR moving to the ISEZ apply first to the Republican Gendarmerie for a residence clearance (Form RG-9 is not used for this purpose).", "ATRden IAEZge köchköndör adegende Respublikalık jandarmeriyağa jashoo uruksatı üchün kayrılat (RG-9 forması bul maksatta koldonulbayt).", "Жители АТР, переезжающие в ОЭЗИ, сначала обращаются в Республиканскую жандармерию за разрешением на проживание (форма RG-9 для этого не используется)."),
    ],
}


def off(extra=None):
    return OFFICIAL_STD + (extra or [])


DUTY = {"t": T("State duty", "Mamlekettik bajı", "Государственная пошлина"), "rows": [
    [{"k": "money", "l": T("Amount paid", "Tölöngön summa", "Уплаченная сумма"), "n": 7, "w": 1.3}, {"k": "boxes", "l": T("Bank payment order No. (Form BI-0401)", "Bank tölöm tapshırmasının No. (BI-0401 forması)", "№ платёжного поручения (форма BI-0401)"), "n": 12, "w": 1.6}, {"k": "date", "l": T("Date of payment", "Tölöngön kün", "Дата оплаты"), "w": 1.1}],
    [{"k": "text", "t": T("Attach the original bank receipt to this form with a paper clip. Do not staple. Receipts older than 30 days, photocopies and receipts showing payment to an account other than the one named in the notes are not accepted.", "Bankın tölöm kvitantsiyasının originalın bul formağa kıskıch menen tirkeñiz. Stepler menen bekitpeñiz. 30 kündön eski kvitantsiyalar, köchürmölör jana eskertüülördö körsötülbögön esepke tölöngön kvitantsiyalar kabıl alınbayt.", "Приложите оригинал банковской квитанции скрепкой. Не сшивайте степлером. Квитанции старше 30 дней, копии и квитанции об оплате на счёт, отличный от указанного в примечаниях, не принимаются."), "w": 2.4}, {"k": "stamp", "w": 1}],
]}

FORMS["PRS-1"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 11/2021",
    "approved": "Approved by Order of the Ministry of Internal Security No. 7 of 12 January 2009 (as amended 2014, 2018, 2021)",
    "to": T("Passport and Residence Service, Ministry of Internal Security", "Pasport jana jashoo jayı kızmatı, Ichki koopsuzduk ministrligi", "Служба паспортов и регистрации, Министерство внутренней безопасности"),
    "instructions": STD_INS + [
        T("Bring the completed form in person, with a queue number for your passport office (e-irad.org), two photographs, the receipt for the state duty and the originals listed in Section F. Applications by post or through another person are not accepted, except under Note 4.", "Tolturulgan formanı özüñüz, pasport bölümünün kezek nomeri (e-irad.org), eki süröt, mamlekettik bajı kvitantsiyası jana F bölümündö atalgan originaldar menen alıp keliñiz. Pochta je bashka adam arkıluu arızdar kabıl alınbayt, 4-eskertüüdön tıshkarı.", "Принесите заполненную форму лично, с номером очереди в паспортный стол (e-irad.org), двумя фотографиями, квитанцией об уплате пошлины и оригиналами, перечисленными в разделе F. Заявления по почте или через другое лицо не принимаются, кроме случая, указанного в примечании 4."),
    ],
    "sections": [
        {"t": T("Document applied for", "Suralgan dokument", "Запрашиваемый документ"), "rows": [
            [{"k": "check", "l": T("Type", "Türü", "Вид"), "opts": [T("identity card", "jeke kuböölük", "удостоверение личности"), T("passport for travel abroad", "chet elge chıguu pasportu", "паспорт для выезда за рубеж"), T("both", "ekööñ teñ", "оба")], "cols": 3, "w": 2}, {"k": "photo", "w": .75}],
            {"k": "check", "l": T("Reason", "Sebebi", "Причина"), "opts": [T("first issue (age 16)", "alğachkı ret (16 jash)", "впервые (16 лет)"), T("expiry", "möönötü bütkön", "истечение срока"), T("change of name", "attın özgörüshü", "перемена имени"), T("pages used up", "barakları bütkön", "заполнены страницы"), T("lost or stolen (attach Form PRS-7)", "joğolgon je uurdalgan (PRS-7 formasın tirkeñiz)", "утерян или похищен (приложите форму PRS-7)"), T("damaged", "buzulgan", "повреждён")], "cols": 3},
            {"k": "check", "l": T("Urgency", "Shashılıshtıgı", "Срочность"), "opts": [T("ordinary (up to 30 working days)", "jönököy (30 ish künügö cheyin)", "обычный (до 30 рабочих дней)"), T("urgent (10 working days, double duty)", "shashılısh (10 ish kün, eki esse bajı)", "срочный (10 рабочих дней, двойная пошлина)")], "cols": 2, "note": T("Urgent issue is available only at the Talas City and Nurzhan City passport offices and only for travel for medical treatment, study or the funeral of a close relative, supported by documents.", "Shashılısh berüü Talas jana Nurzhan shaardık pasport bölümdöründö gana, dalildüü dokumentter menen daryılanuu, okuu je jakın tuugandın soögu üchün jol jürüügö gana mümkün.", "Срочное оформление возможно только в паспортных столах Таласа и Нуржана и только для поездки на лечение, учёбу или похороны близкого родственника при наличии документов.")},
        ]},
        PERSON,
        address(T("Address of residence (as registered)", "Jashoo dareki (kattalgandaй)", "Адрес места жительства (по регистрации)")),
        {"t": T("Family and previous names", "Üy-bülösü jana murdaңkı attarı", "Семья и прежние имена"), "rows": [
            [{"k": "check", "l": T("Marital status", "Üy-bülölük abalı", "Семейное положение"), "opts": [T("single", "boydok", "холост / не замужем"), T("married", "üylöngön / turmushta", "женат / замужем"), T("divorced", "ajırashkan", "разведён(а)"), T("widowed", "jesir", "вдовец / вдова")], "cols": 4}],
            {"k": "table", "l": T("All previous surnames and first names, with dates of change", "Murdaңkı bardık familiyalar jana attar, özgörgön künü menen", "Все прежние фамилии и имена с датами изменения"), "cols": [(T("Previous surname, first name", "Murdaңkı familiyası, atı", "Прежние фамилия, имя"), 4), (T("Changed on", "Özgörgön kün", "Дата изменения"), 1.6), (T("Civil registry office", "JAAK bölümü", "Отдел ЗАГС"), 3)], "rows": 3},
            {"k": "table", "l": T("Children under 16 to be entered in the passport for travel abroad", "Chet elge chıguu pasportuna jazıla turgan 16 jashka cheyinki baldar", "Дети до 16 лет, вписываемые в паспорт для выезда за рубеж"), "cols": [("fullname", 4), ("dob", 1.6), ("pin", 2.4)], "rows": 3},
        ]},
        {"t": T("Employment and travel", "Ish jana jol jürüü", "Работа и поездки"), "rows": [
            {"k": "line", "l": T("Place of work or study, position", "Ish je okuu ordu, kızmatı", "Место работы или учёбы, должность")},
            {"k": "check", "l": T("Do you have, or have you had, access to state secrets?", "Mamlekettik sırga jetkiliktüülügüñüz barbı je bolgonbu?", "Имеете ли вы (имели ли) допуск к государственной тайне?"), "opts": [T("no", "jok", "нет"), T("yes (attach the clearance from the employer)", "ooba (ish beruuchunun uruksatın tirkeñiz)", "да (приложите разрешение работодателя)")], "cols": 2},
            {"k": "table", "l": T("Countries visited in the last five years", "Akırkı besh jılda barılgan ölkölör", "Страны, посещённые за последние пять лет"), "cols": [(T("Country", "Ölkö", "Страна"), 3), (T("From", "Kachandan", "С"), 1.5), (T("To", "Kachanğa cheyin", "По"), 1.5), (T("Purpose", "Maksatı", "Цель"), 3)], "rows": 4},
        ]},
        DUTY,
        {"t": T("Documents enclosed (tick and bring the originals)", "Tirkelgen dokumentter (belgilep, originaldardı alıp keliñiz)", "Прилагаемые документы (отметьте и принесите оригиналы)"), "rows": [
            {"k": "check", "l": T("Enclosed", "Tirkelgen", "Приложено"), "opts": [T("old identity card or passport", "eski jeke kuböölük je pasport", "старое удостоверение или паспорт"), T("birth certificate", "tuuluu kuböölügü", "свидетельство о рождении"), T("marriage certificate", "nike kuböölügü", "свидетельство о браке"), T("two photographs 3×4 cm", "3×4 sm eki süröt", "две фотографии 3×4 см"), T("military registration document (men 18–27)", "askeriy kattoo dokumenti (18–27 jashtağı erkekter)", "документ воинского учёта (мужчины 18–27)"), T("address card (Form PRS-3 receipt)", "darek kartochkası (PRS-3 tilkatı)", "адресный листок (расписка PRS-3)"), T("duty receipt", "bajı kvitantsiyası", "квитанция об уплате пошлины"), T("Form PRS-7 (if lost)", "PRS-7 forması (joğolso)", "форма PRS-7 (при утере)"), T("other (list)", "bashka (tizmeleñiz)", "иное (перечислите)")], "cols": 3},
        ]},
    ],
    "declaration": DECL,
    "official": off([[{"k": "boxes", "l": T("Document series and No. issued", "Berilgen dokumenttin seriyası jana No.", "Серия и № выданного документа"), "n": 11, "w": 1.5}, {"k": "date", "l": T("Date of issue", "Berilgen kün", "Дата выдачи"), "w": 1}], {"k": "sign", "l": [T("Document received by the applicant (signature)", "Dokumentti arız beruuchu aldı (kolu)", "Документ получил (подпись)"), "date"]}]),
    "counterfoil": {"t": T("Receipt for documents accepted", "Kabıl alıngan dokumentter tuuraluu tilkat", "Расписка в приёме документов"), "rows": [
        [{"k": "line", "l": "fullname", "w": 2}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.3}, {"k": "date", "l": T("Collect on or after", "Ushul künü je andan kiyin alıñız", "Получить не ранее"), "w": 1.2}],
        [{"k": "line", "l": "recvd", "w": 1}, {"k": "line", "l": T("Bring this receipt and your old document when collecting", "Alğanda bul tilkattı jana eski dokumentiñizdi ala keliñiz", "При получении предъявите расписку и старый документ"), "w": 1}],
    ]},
    "notes": [
        T("The state duty is set by the schedule of state duties (see the State duty calculator on e-irad.org) and is paid only to the account of the Treasury at Talasbank, Ak Bata Bank or Chuy Commercial Bank. Payment at an Irad Pochtasy counter is accepted only for the identity card.", "Mamlekettik bajı mamlekettik bajılar tizmesi boyuncha belgilenet (e-irad.org saytındağı Mamlekettik bajı kalkulyatorun karañız) jana Talasbank, Ak Bata Bank je Chüy Kommertsiyalık Bankındağı Kaznachılıktın esebine gana tölönöt. Irad Pochtasının kassasındağı tölöm jeke kuböölük üchün gana kabıl alınat.", "Пошлина установлена перечнем государственных пошлин (см. калькулятор на e-irad.org) и уплачивается только на счёт Казначейства в «Таласбанке», «Ак Бата Банке» или «Чуйском коммерческом банке». Оплата в отделениях «Ирадпочты» принимается только за удостоверение личности."),
        T("Photographs: 3×4 cm, colour, matt paper, light grey background, taken within the last six months, without headwear except for religious reasons (face from chin to forehead visible), without glasses with tinted lenses. Photographs from booths are not accepted.", "Sürötter: 3×4 sm, tüstüü, küñgürt kağaz, ak-boz fon, akırkı altı aydın ichinde tartılgan, diniy sebepterden tıshkarı bash kiyimsiz (betı iyekten mañdayğa cheyin körünsün), boyolgon aynek koz aynegisiz. Avtomattan alınğan sürötter kabıl alınbayt.", "Фотографии: 3×4 см, цветные, матовые, светло-серый фон, сделаны в последние шесть месяцев, без головного убора, кроме как по религиозным причинам (лицо от подбородка до лба открыто), без тонированных очков. Фото из автоматов не принимаются."),
        T("A person who cannot attend because of illness or disability may apply through a representative holding a notarised power of attorney; an official of the office will visit the applicant to take the photograph and signature within 60 days.", "Ooruu je mümkünchülügü chektelgendikten kele albağan adam notarialdık ışenim katı bar ökül arkıluu kayrıla alat; bölümdün kızmatkeri 60 kündün ichinde arız beruuchügö barıp süröt jana kolun alat.", "Лицо, которое не может явиться по болезни или инвалидности, может обратиться через представителя с нотариальной доверенностью; сотрудник посетит заявителя для фото и подписи в течение 60 дней."),
    ],
}

FORMS["PRS-7"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 03/2018",
    "approved": "Approved by Order of the Ministry of Internal Security No. 7 of 12 January 2009 (as amended 2018)",
    "to": T("Head of the Passport and Residence Service office at the place of residence", "Jashagan jerdegi Pasport jana jashoo jayı kızmatı bölümünün bashchısına", "Начальнику отдела Службы паспортов и регистрации по месту жительства"),
    "instructions": STD_INS + [T("If the card was stolen, first report the theft to the city police or the district police post and attach the certificate of report (talon). A card that is found after a replacement has been ordered must be handed in to any passport office within 3 days; it cannot be used.", "Eger kuböölük uurdalsa, adegende shaar politsiyasına je aymaktık politsiya postuna kabarlap, kabar talonun tirkeñiz. Almashtıruu buyurtulgandan kiyin tabılgan kuböölük 3 kündün ichinde kaalagan pasport bölümünö tapshırıluuğa tiyish; anı koldonuuğa bolboyt.", "При краже сначала заявите в городскую полицию или районный пост полиции и приложите талон-уведомление. Найденное после заказа замены удостоверение сдаётся в любой паспортный стол в течение 3 дней; пользоваться им нельзя.")],
    "sections": [
        PERSON,
        {"t": T("Circumstances", "Jagdaylar", "Обстоятельства"), "rows": [
            {"k": "check", "l": T("The identity card was", "Jeke kuböölük", "Удостоверение было"), "opts": [T("lost", "joğolgon", "утеряно"), T("stolen", "uurdalgan", "похищено"), T("damaged (attach the card)", "buzulgan (kuböölüktü tirkeñiz)", "повреждено (приложите)"), T("destroyed by fire, flood or earthquake", "örttön, suu kaptoodon je jer titirөödön joyulgan", "уничтожено при пожаре, наводнении или землетрясении"), T("withheld by a third party", "üchünchü jak karmap turat", "удерживается третьим лицом"), T("other", "bashka", "иное")], "cols": 3},
            [{"k": "date", "l": T("Date of loss or discovery", "Joğolgon je bilingen kün", "Дата утраты или обнаружения"), "w": 1}, {"k": "line", "l": T("Place (city, street, transport)", "Jeri (shaar, köchö, transport)", "Место (город, улица, транспорт)"), "w": 2}],
            {"k": "area", "l": T("Describe how the card was lost, stolen or damaged (in your own words, in block capitals)", "Kuböölük kantip joğolgonun, uurdalganın je buzulganın jazıñız (öz sözüñüz menen, basma tamgalar menen)", "Опишите, как удостоверение было утеряно, похищено или повреждено (своими словами, печатными буквами)"), "lines": 5},
            [{"k": "boxes", "l": T("Police report (talon) No.", "Politsiyağa kabar (talon) No.", "Талон-уведомление полиции №"), "n": 10, "w": 1.2}, {"k": "line", "l": T("Police unit", "Politsiya bölümü", "Подразделение полиции"), "w": 1.3}, {"k": "date", "l": "date", "w": 1}],
            {"k": "check", "l": T("Was the card replaced before?", "Kuböölük murda almashtırılganbı?", "Заменялось ли удостоверение ранее?"), "opts": [T("no", "jok", "нет"), T("once", "bir jolu", "один раз"), T("twice or more (see Note 2)", "eki je andan köp (2-eskertüünü karañız)", "два и более раз (см. примечание 2)")], "cols": 3},
        ]},
        DUTY,
    ],
    "declaration": T("I declare that the card described above is no longer in my possession or is damaged as described, and that I have not handed it to any other person as security, pledge or for safekeeping. I understand that the card will be entered in the register of invalid documents.", "Jogoruda körsötülgön kuböölük menin kolumda jok je körsötülgöndöy buzulgan ekenin jana anı eч kimge kepil, garantiya je saktoo üchün bergen emesmin dep tastıktaym. Kuböölük jaraksız dokumentter reestrine kirgiziletin tüshünöm.", "Заявляю, что указанное удостоверение у меня отсутствует или повреждено, как описано, и что я не передавал его другим лицам в залог или на хранение. Мне известно, что удостоверение будет внесено в реестр недействительных документов."),
    "official": off([{"k": "line", "l": T("Entered in the register of invalid documents (No., date)", "Jaraksız dokumentter reestrine kirgizildi (No., kün)", "Внесено в реестр недействительных документов (№, дата)")}]),
    "notes": [
        T("The state duty for a replacement is three times the ordinary duty; for a second replacement within five years, five times. No duty is charged where the card was destroyed in a natural disaster confirmed by the district office.", "Almashtıruu üchün mamlekettik bajı jönököy bajıdan üch esse köp; besh jıldın ichinde ekinchi ret almashtıruu besh esse. Aymaktık keñse tastıktağan tabiyiy kırsıkta joyulgan kuböölük üchün bajı alınbayt.", "Пошлина за замену в три раза выше обычной; за повторную замену в течение пяти лет — в пять раз. Пошлина не взимается при утрате в результате стихийного бедствия, подтверждённого районным отделом."),
        T("A third replacement within five years is considered only after an interview with the head of the office and a check by the Records Department, which may take up to 90 days.", "Besh jıldın ichinde üchünchü almashtıruu bölüm bashchısı menen süylöshüüdön jana Esepke aluu departamentinin tekshiruusünön kiyin gana karalat, al 90 küngö cheyin sozuluşu mümkün.", "Третья замена в течение пяти лет рассматривается только после собеседования с начальником отдела и проверки Учётным департаментом, которая может занять до 90 дней."),
    ],
}

FORMS["HPC-12"] = {
    "ink": "#1d2f5e", "mark": "gov", "rev": "rev. 08/2017",
    "approved": "Approved by Order of the Commander of the Republican Gendarmerie No. 112 of 3 August 2017",
    "to": T("Registration and Examination Section, Highway Patrol Corps", "Kattoo jana sınak bölümü, Avtojol patrul korpusu", "Отдел регистрации и экзаменов, Корпус дорожного патруля"),
    "instructions": STD_INS + [T("Licences issued in Kazakhstan, Kyrgyzstan, Uzbekistan and the Russian Federation are exchanged after a theory test only. All other licences require the theory test, a practical test on the Talas or Nurzhan circuit and a translation of the licence certified by a notary in Irad.", "Kazakstanda, Kırgızstanda, Özbekstanda jana Orusiya Federatsiyasında berilgen kuböölüktör teoriyalık sınaktan gana kiyin almashtırılat. Bashka bardık kuböölüktörgö teoriyalık sınak, Talas je Nurzhan avtodromunda praktikalık sınak jana kuböölüktün Iraddağı notarius tastıktağan kotormosu kerek.", "Удостоверения Казахстана, Кыргызстана, Узбекистана и Российской Федерации обмениваются после теоретического экзамена. Для остальных необходимы теоретический и практический экзамены на автодроме Таласа или Нуржана и нотариально заверенный в Ираде перевод удостоверения.")],
    "sections": [
        PERSON,
        address(T("Address of residence in the ISEZ", "IAEZdegi jashoo dareki", "Адрес места жительства в ОЭЗИ")),
        {"t": T("Foreign driving licence", "Chet eldik aydoochuluk kuböölügü", "Иностранное водительское удостоверение"), "rows": [
            [{"k": "line", "l": T("Issuing country", "Bergen ölkö", "Страна выдачи"), "w": 1.2}, {"k": "boxes", "l": T("Licence No.", "Kuböölüktün No.", "№ удостоверения"), "n": 12, "w": 1.6}],
            [{"k": "date", "l": T("Date of issue", "Berilgen kün", "Дата выдачи"), "w": 1}, {"k": "date", "l": T("Valid until", "Ushul künğö cheyin jaraktuu", "Действительно до"), "w": 1}, {"k": "date", "l": T("Date of first issue of any licence", "Kaalagan kuböölüktün alğach berilgen künü", "Дата первой выдачи любого удостоверения"), "w": 1}],
            {"k": "table", "l": T("Categories held", "Bar kategoriyalar", "Имеющиеся категории"), "cols": [(T("Category", "Kategoriya", "Категория"), 1), (T("Since", "Kachandan beri", "С"), 1.4), (T("Restrictions / codes", "Chekteöölör / kodtor", "Ограничения / коды"), 3), (T("To be exchanged for ISEZ category", "IAEZ kategoriyasına almashtırılat", "Заменить на категорию ОЭЗИ"), 2)], "rows": 5},
            {"k": "check", "l": T("Has the licence ever been suspended or withdrawn?", "Kuböölük kachan bolso toktotulganbı je alınganbı?", "Приостанавливалось ли удостоверение или изымалось?"), "opts": [T("no", "jok", "нет"), T("yes (attach details)", "ooba (maalımattı tirkeñiz)", "да (приложите сведения)")], "cols": 2},
        ]},
        {"t": T("Medical certificate", "Meditsinalık malımatnama", "Медицинская справка"), "rows": [
            [{"k": "boxes", "l": T("Driver's medical certificate No. (Form 083/u)", "Aydoochunun meditsinalık malımatnamasının No. (083/u forması)", "№ медицинской справки водителя (форма 083/у)"), "n": 10, "w": 1.5}, {"k": "date", "l": "date", "w": 1}, {"k": "line", "l": T("Issued by (clinic)", "Kim bergen (klinika)", "Выдана (поликлиника)"), "w": 1.5}],
            {"k": "check", "l": T("Vision correction", "Kordu tüzötüü", "Коррекция зрения"), "opts": [T("none", "jok", "нет"), T("glasses", "kozaynek", "очки"), T("contact lenses", "kontakttık linzalar", "контактные линзы")], "cols": 3},
        ]},
        {"t": T("Test appointments (filled in by the Section)", "Sınak möönöttörü (bölüm tolturat)", "Назначение экзаменов (заполняет отдел)"), "rows": [
            {"k": "table", "cols": [(T("Test", "Sınak", "Экзамен"), 2), (T("Date and time", "Kün jana saat", "Дата и время"), 2), (T("Circuit / room", "Avtodrom / bölmö", "Автодром / кабинет"), 2), (T("Result", "Natıyjası", "Результат"), 1.5), (T("Examiner", "Sınakchı", "Экзаменатор"), 2)], "rows": 3, "numbered": False},
        ]},
        DUTY,
    ],
    "declaration": DECL,
    "official": off([{"k": "line", "l": T("Foreign licence surrendered and sent to the issuing authority through the Ministry of Foreign Affairs (No., date)", "Chet eldik kuböölük tapshırıldı jana Tashkı ishter ministrligi arkıluu bergen organğa jönötüldü (No., kün)", "Иностранное удостоверение сдано и направлено выдавшему органу через МИД (№, дата)")}]),
    "notes": [T("The foreign licence is surrendered when the ISEZ licence is issued. Holders who need the foreign licence for travel may ask for it to be kept at the Section for up to 3 years instead; it is returned only against the ISEZ licence.", "IAEZ kuböölügü berilgende chet eldik kuböölük tapshırılat. Jol jürüü üchün chet eldik kuböölük kerek bolgondor anı 3 jılğa cheyin bölümdö saktoonu surasa bolot; al IAEZ kuböölügünö almashtırıp gana kaytarılat.", "Иностранное удостоверение сдаётся при выдаче удостоверения ОЭЗИ. Владельцы, которым оно нужно для поездок, могут оставить его на хранение в отделе до 3 лет; возвращается только в обмен на удостоверение ОЭЗИ.")],
}

FORMS["CR-9"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 01/2015",
    "approved": "Approved under the Civil Registration Act 1996, Regulation No. 31 of 9 January 2015",
    "to": T("Head of the civil registry office of the district (city) of residence", "Jashagan aymaktın (shaardın) JAAK bölümünün bashchısına", "Заведующему отделом ЗАГС района (города) по месту жительства"),
    "instructions": STD_INS + [T("A change of name is registered not earlier than one month after this application is filed. During that month the office publishes a notice of the intended change on its notice board. Objections may be lodged by any person.", "Attı özgörtüü bul arız berilgenden bir aydan kiyin gana kattalat. Ushul aydın ichinde bölüm pland­alğan özgörtüü tuuraluu bildirüünü öz taktasına ilet. Kaalagan adam karshı pikir bere alat.", "Перемена имени регистрируется не ранее чем через месяц после подачи заявления. В течение месяца отдел вывешивает объявление о предстоящей перемене. Возражения может подать любое лицо.")],
    "sections": [
        PERSON,
        {"t": T("Change requested", "Suralgan özgörtüü", "Запрашиваемая перемена"), "rows": [
            {"k": "check", "l": T("I wish to change my", "Men özgörtköm kelet", "Прошу изменить"), "opts": [T("surname", "familiyamdı", "фамилию"), T("first name", "atımdı", "имя"), T("patronymic", "atamdın atın", "отчество"), T("spelling only (Latin form)", "jazılışın gana (latın türü)", "только написание (латиница)")], "cols": 4},
            {"k": "boxes", "l": T("New surname", "Jañı familiya", "Новая фамилия")},
            {"k": "boxes", "l": T("New first name", "Jañı at", "Новое имя")},
            {"k": "boxes", "l": T("New patronymic or uulu / kyzy form", "Jañı atasının atı je uulu / kızı türü", "Новое отчество или форма уулу / кызы"), "note": T("The Iradi forms uulu (son of) and kyzy (daughter of) after the father's name may be chosen instead of a Russian-style patronymic. The spelling of the new name is checked against the official orthography; a name not conforming to it is refused.", "Atasının atınan kiyin uulu jana kızı irad türlörü orus türündögü atasının atının ordunda tandalışı mümkün. Jañı attın jazılışı rasmiy orfografiya boyuncha tekshirilet; ağa tuura kelbegen at kabıl alınbayt.", "Вместо отчества русского образца можно выбрать ирадские формы уулу (сын) и кызы (дочь) после имени отца. Написание нового имени проверяется по официальной орфографии; несоответствующее имя не принимается.")},
            {"k": "area", "l": T("Reasons for the change", "Özgörtüünün sebepteri", "Причины перемены"), "lines": 4},
        ]},
        {"t": T("Certificates to be reissued", "Kayra beriluuchü kuböölüktör", "Свидетельства, подлежащие замене"), "rows": [
            {"k": "table", "cols": [(T("Certificate (birth, marriage, children's birth)", "Kuböölük (tuuluu, nike, baldardın tuuluşu)", "Свидетельство (о рождении, браке, рождении детей)"), 4), (T("Record No.", "Jazuu No.", "№ записи"), 1.5), (T("Date", "Kün", "Дата"), 1.5), (T("Office that registered it", "Kattağan bölüm", "Отдел, зарегистрировавший"), 3)], "rows": 5},
        ]},
        {"t": T("Consents", "Makulduktar", "Согласия"), "rows": [
            {"k": "text", "t": T("If the applicant is married, the spouse's written consent is required for a change of surname. For a person aged 14 to 18, the consent of both parents, certified by a notary, is required.", "Eger arız beruuchu üylöngön bolso, familiyanı özgörtüügö jubayının jazuu jüzündögü makulduğu kerek. 14tön 18 jashka cheyinki adam üchün eki ata-enenin notarius tastıktağan makulduğu kerek.", "Если заявитель состоит в браке, для перемены фамилии нужно письменное согласие супруга. Для лиц 14–18 лет необходимо нотариально заверенное согласие обоих родителей.")},
            {"k": "sign", "l": [T("Spouse / parent (signature)", "Jubayı / ata-enesi (kolu)", "Супруг / родитель (подпись)"), T("Spouse / parent (signature)", "Jubayı / ata-enesi (kolu)", "Супруг / родитель (подпись)"), "date"], "seal": "Notary / Notarius / Нотариус"},
        ]},
        DUTY,
    ],
    "declaration": DECL,
    "official": off([[{"k": "date", "l": T("Notice posted on", "Bildirüü ilingen kün", "Объявление вывешено"), "w": 1}, {"k": "date", "l": T("Objection period ends", "Karshı pikir möönötü bütöt", "Срок возражений истекает"), "w": 1}, {"k": "line", "l": T("Record of change of name No.", "Attı özgörtüü jazuusunun No.", "№ записи о перемене имени"), "w": 1.3}]]),
}

FORMS["CR-2"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 01/2015",
    "approved": "Approved under the Civil Registration Act 1996, Regulation No. 31 of 9 January 2015",
    "to": T("Head of the civil registry office holding the record", "Jazuunu saktağan JAAK bölümünün bashchısına", "Заведующему отделом ЗАГС, где хранится запись"),
    "instructions": STD_INS + [T("A duplicate is issued only to the person named in the record, a parent of a minor, or a person holding a notarised power of attorney. Records made before 1993 are held by the State Archives; for those, use Form SA-4.", "Dublikat jazuuda atalgan adamğa, jashı jete elek baldın ata-enesine je notarialdık ışenim katı bar adamğa gana berilet. 1993-jılğa cheyinki jazuular Mamlekettik arkhivde saktalat; alar üchün SA-4 formasın koldonuñuz.", "Дубликат выдаётся только лицу, указанному в записи, родителю несовершеннолетнего или лицу с нотариальной доверенностью. Записи до 1993 года хранятся в Государственном архиве; для них используйте форму SA-4.")],
    "sections": [
        PERSON,
        {"t": T("Certificate requested", "Suralgan kuböölük", "Запрашиваемое свидетельство"), "rows": [
            {"k": "check", "l": T("Type", "Türü", "Вид"), "opts": [T("birth", "tuuluu", "о рождении"), T("marriage", "nike", "о браке"), T("divorce", "ajırashuu", "о расторжении брака"), T("death", "ölüm", "о смерти"), T("change of name", "attı özgörtüü", "о перемене имени"), T("paternity", "atalıktı anıktoo", "об установлении отцовства")], "cols": 3},
            {"k": "line", "l": T("Full name of the person in the record", "Jazuudağı adamdın toluk atı", "Ф.И.О. лица, указанного в записи")},
            [{"k": "date", "l": T("Date of the event", "Okuyanın künü", "Дата события"), "w": 1}, {"k": "line", "l": T("Place of registration (office)", "Kattalgan jeri (bölüm)", "Место регистрации (отдел)"), "w": 2}],
            [{"k": "line", "l": T("Father's full name (for birth certificates)", "Atasının toluk atı (tuuluu kuböölügü üchün)", "Ф.И.О. отца (для свидетельства о рождении)"), "w": 1}, {"k": "line", "l": T("Mother's full name and maiden name", "Enesinin toluk atı jana kız kezindegi familiyası", "Ф.И.О. матери и девичья фамилия"), "w": 1}],
            {"k": "check", "l": T("Relationship of the applicant to the person in the record", "Arız beruuchunun jazuudağı adamğa tuuganchılıgı", "Отношение заявителя к лицу в записи"), "opts": [T("the person himself or herself", "özü", "само лицо"), T("parent", "ata-enesi", "родитель"), T("spouse", "jubayı", "супруг(а)"), T("child", "balası", "ребёнок"), T("heir (attach proof)", "murasker (dalil tirkeñiz)", "наследник (приложите)"), T("representative", "ökül", "представитель")], "cols": 3},
            {"k": "check", "l": T("Purpose", "Maksatı", "Цель"), "opts": [T("lost certificate", "joğolgon kuböölük", "утеря свидетельства"), T("damaged certificate", "buzulgan kuböölük", "повреждение"), T("for use abroad (apostille not available; see Note 1)", "chet elde koldonuu üchün (apostil jok; 1-eskertüünü karañız)", "для использования за рубежом (апостиль невозможен; см. прим. 1)"), T("pension or inheritance", "pensiya je muras", "пенсия или наследство")], "cols": 2},
        ]},
        DUTY,
    ],
    "declaration": DECL,
    "official": off([[{"k": "boxes", "l": T("Record No.", "Jazuu No.", "№ записи"), "n": 8, "w": 1}, {"k": "boxes", "l": T("Duplicate series and No.", "Dublikattın seriyası jana No.", "Серия и № дубликата"), "n": 10, "w": 1.3}]]),
    "notes": [T("The ISEZ is not a party to the Hague Apostille Convention. Certificates for use abroad are legalised by the Ministry of Foreign Affairs and then by the consulate of the country of destination, where one will accept them.", "IAEZ Gaaga apostil konventsiyasının katıshuuchusu emes. Chet elde koldonuluuchu kuböölüktördü Tashkı ishter ministrligi, andan kiyin, eger kabıl alsa, barıluuchu ölkönün konsuldugu legalizatsiyalayt.", "ОЭЗИ не участвует в Гаагской конвенции об апостиле. Свидетельства для использования за рубежом легализуются МИД, а затем консульством страны назначения, если оно их принимает.")],
}

FORMS["MIS-22"] = {
    "ink": INK, "mark": "gov", "rev": "rev. 06/2020",
    "approved": "Approved by Order of the Ministry of Internal Security No. 88 of 1 June 2020",
    "to": T("Records Department, Ministry of Internal Security", "Esepke aluu departamenti, Ichki koopsuzduk ministrligi", "Учётный департамент, Министерство внутренней безопасности"),
    "instructions": STD_INS + [T("The certificate states whether the Records Department holds information about the applicant that bars employment in the post or activity named in Section C. It is valid for 3 months and only for the purpose stated.", "Malımatnama Esepke aluu departamentinde arız beruuchu tuuraluu C bölümündö atalgan kızmatka je ishke tоskool bolo turgan maalımat bar-jogun körsötöt. Al 3 ay jana körsötülgön maksat üchün gana jaraktuu.", "В справке указывается, имеются ли в Учётном департаменте сведения о заявителе, препятствующие работе в должности или деятельности, указанной в разделе C. Действительна 3 месяца и только для указанной цели.")],
    "sections": [
        PERSON,
        address(T("Addresses during the last ten years (current first)", "Akırkı on jıldağı darekter (azırkısı birinchi)", "Адреса за последние десять лет (сначала текущий)")),
        {"t": T("Purpose", "Maksatı", "Цель"), "rows": [
            {"k": "check", "l": T("The certificate is required for", "Malımatnama kerek", "Справка требуется для"), "opts": [T("employment in a state body", "mamlekettik organğa ishke", "работы в государственном органе"), T("teaching or work with children", "sabak berüü je baldar menen ish", "преподавания или работы с детьми"), T("private security licence (Kalkan and others)", "jeke kuzot litsenziyası (Kalkan j.b.)", "лицензии частной охраны (Калкан и др.)"), T("taxi licence (Form DIC-3)", "taksi litsenziyası (DIC-3 forması)", "лицензии такси (форма DIC-3)"), T("foreign visa or residence", "chet eldik viza je jashoo", "иностранной визы или проживания"), T("adoption or guardianship", "asırap aluu je kamkordoo", "усыновления или опеки")], "cols": 2},
            [{"k": "line", "l": T("Name of the employer or authority requesting it", "Suragan ish beruuchunun je organdın atı", "Наименование запрашивающего работодателя или органа"), "w": 2}, {"k": "line", "l": T("Post or activity", "Kızmatı je ishi", "Должность или деятельность"), "w": 1.3}],
            {"k": "check", "l": T("Language of the certificate", "Malımatnamanın tili", "Язык справки"), "opts": [T("English", "Anglis", "английский"), T("Iradi", "Irad", "ирадский"), T("Russian", "Orus", "русский")], "cols": 3},
        ]},
        DUTY,
    ],
    "declaration": DECL,
    "official": off(),
    "counterfoil": {"t": T("Receipt", "Tilkat", "Расписка"), "rows": [[{"k": "line", "l": "fullname", "w": 2}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.3}, {"k": "date", "l": T("Collect after", "Ushul künden kiyin alıñız", "Получить после"), "w": 1.2}]]},
    "notes": [T("Certificates are issued within 30 days, or within 10 days for an additional duty. They are handed only to the applicant in person against the identity card; they are not sent by post or e-mail.", "Malımatnamalar 30 kündün ichinde, koshumcha bajı menen 10 kündün ichinde berilet. Alar arız beruuchunun özünö jeke kuböölük boyuncha gana berilet; pochta je e-pochta menen jönötülböyt.", "Справки выдаются в течение 30 дней, за дополнительную пошлину — 10 дней. Выдаются лично заявителю по удостоверению личности; по почте и электронной почте не направляются.")],
}

FORMS["SF-1"] = {
    "ink": "#22442c", "mark": "gov", "rev": "rev. 03/2008",
    "approved": "Approved by Resolution of the Board of the Social Fund No. 5 of 17 March 2008 (som amounts revised annually)",
    "to": T("District department of the Social Fund", "Sotsialdık fonddun aymaktık bölümü", "Районное отделение Социального фонда"),
    "instructions": STD_INS + [T("Apply not earlier than one month before reaching pensionable age (63 for men, 58 for women) and bring the employment record book (trudovaya knizhka), certificates of earnings for any 60 consecutive months, and the military record if applicable.", "Pensiyalık jashka (erkekter 63, ayaldar 58) jetkenge bir ay kalğanda gana kayrılıñız jana emgek kitepchesin, kaalagan 60 ay katarınan aylık tuuraluu malımatnamalardı jana kerek bolso askeriy dokumentti alıp keliñiz.", "Обращайтесь не ранее чем за месяц до достижения пенсионного возраста (63 года для мужчин, 58 для женщин) с трудовой книжкой, справками о заработке за любые 60 месяцев подряд и военным билетом, если применимо.")],
    "sections": [
        PERSON,
        address(T("Address of residence", "Jashoo dareki", "Адрес места жительства")),
        {"t": T("Work record", "Emgek stajı", "Трудовой стаж"), "rows": [
            {"k": "table", "l": T("Periods of employment, including in the Iradi SSR (continue on an annex sheet)", "Ishtegen mezgilder, Irad SSRinde da (koshumcha barakta ulantıñız)", "Периоды работы, включая Ирадскую ССР (продолжите на дополнительном листе)"), "cols": [(T("From", "Kachandan", "С"), 1.3), (T("To", "Kachanğa cheyin", "По"), 1.3), (T("Employer", "Ish beruuchu", "Работодатель"), 4), (T("Position", "Kızmatı", "Должность"), 2.4), (T("Record book entry No.", "Kitepchedegi jazuu No.", "№ записи в книжке"), 1.4)], "rows": 9},
            {"k": "check", "l": T("Special periods counted towards the record", "Stajğa kirüüchü atayın mezgilder", "Особые периоды, засчитываемые в стаж"), "opts": [T("military service", "askeriy kızmat", "военная служба"), T("child care (up to 3 years per child)", "bala karoo (ar bir balağa 3 jılğa cheyin)", "уход за ребёнком (до 3 лет на ребёнка)"), T("study at TSU or a technical school", "TMUda je tekhnikumda okuu", "учёба в ТГУ или техникуме"), T("work at the Mailuu-Suu or Sary-Bulak mines (reduced age)", "Mailuu-Suu je Sarı-Bulak kenderinde ish (jashı tömöndötülgön)", "работа на рудниках Майлуу-Суу или Сары-Булак (сниженный возраст)")], "cols": 2},
        ]},
        {"t": T("Payment", "Tölöm", "Выплата"), "rows": [
            {"k": "check", "l": T("I ask for the pension to be paid", "Pensiyanı tölöödü suranam", "Прошу выплачивать пенсию"), "opts": [T("at the counter of Irad Pochtasy (post office No.)", "Irad Pochtasının kassasında (pochta bölümü No.)", "в окне «Ирадпочты» (отделение №)"), T("delivered to the home by the postman (over 80 or disability group I)", "pochtalyon üygö jetkirsin (80den ashkan je I top)", "с доставкой почтальоном на дом (старше 80 лет или I группа)"), T("into an account at Talasbank", "Talasbanktağı esepke", "на счёт в «Таласбанке»"), T("into an account at Ak Bata Bank or Chuy Commercial Bank", "Ak Bata Bank je Chüy Kommertsiyalık Bankındağı esepke", "на счёт в «Ак Бата Банке» или «Чуйском коммерческом банке»")], "cols": 2},
            [{"k": "boxes", "l": T("Post office No. or bank account No.", "Pochta bölümü No. je bank esebinin No.", "№ отделения связи или счёта"), "n": 20, "w": 2}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.2}],
            {"k": "text", "t": T("Pensions are paid in som from the 10th of each month. A pension not collected for six months in a row is suspended; it is resumed on a written application with proof that the pensioner is alive (Form SF-1a, available at the district department).", "Pensiyalar ar aydın 10-kününön tartıp som menen tölönöt. Katarınan altı ay alınbağan pensiya toktotulat; al pensioner tirüü ekenin dalildöö menen jazuu jüzündögü arız boyuncha kayra bashtalat (SF-1a forması, aymaktık bölümdö).", "Пенсии выплачиваются в сомах с 10-го числа каждого месяца. Пенсия, не полученная шесть месяцев подряд, приостанавливается; возобновляется по письменному заявлению с подтверждением, что пенсионер жив (форма SF-1a, в районном отделении).")},
        ]},
    ],
    "declaration": DECL,
    "official": off([[{"k": "money", "l": T("Pension awarded per month", "Aylık belgilengen pensiya", "Назначенная пенсия в месяц"), "n": 7, "w": 1.3}, {"k": "date", "l": T("Payable from", "Ushul künden tölönöt", "Выплачивается с"), "w": 1}, {"k": "line", "l": T("Pension certificate No.", "Pensiya kuböölügünün No.", "№ пенсионного удостоверения"), "w": 1.2}]]),
}
