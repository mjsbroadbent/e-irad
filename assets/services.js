/* e-Irad service catalogue. Every form runs in the browser only: nothing is sent, nothing is stored except the
   queue tickets a visitor takes (localStorage "eirad_tickets") and the language. Results are worked out from the
   input (deterministic), so the same number always gives the same answer. */
window.E_SERVICES = {
  offices: [
    { id: "tl", code: "TL", base: 1840, rate: 160, name: { en: "Talas City Passport Office, Liberty Boulevard", ir: "Talas shaardık pasport bölümü, Erkindik bulvarı", ru: "Паспортный стол города Таласа, бульвар Свободы" } },
    { id: "nz", code: "NZ", base: 1510, rate: 140, name: { en: "Nurzhan City Passport Office, Azatlık Prospect", ir: "Nurzhan shaardık pasport bölümü, Azattık prospekti", ru: "Паспортный стол города Нуржана, проспект Азатлык" } },
    { id: "ij", code: "IJ", base: 720, rate: 70, name: { en: "Iyık Janyl City Passport Office, Lower Town", ir: "Iyık Janıl shaardık pasport bölümü, Tömönkü shaar", ru: "Паспортный стол Ийык-Джаныла, Нижний город" } },
    { id: "ka", code: "KA", base: 410, rate: 45, name: { en: "Kara-Buura District office, Kyzyl-Adyr", ir: "Kara-Buura aymaktık keñsesi, Kızıl-Adır", ru: "Отдел Кара-Бууринского района, Кызыл-Адыр" } },
    { id: "kb", code: "KB", base: 300, rate: 40, name: { en: "Talas District office, Kara-Bulak", ir: "Talas aymaktık keñsesi, Kara-Bulak", ru: "Отдел Таласского района, Кара-Булак" } },
    { id: "mk", code: "MK", base: 280, rate: 30, name: { en: "Chu District office, Merke", ir: "Chüy aymaktık keñsesi, Merke", ru: "Отдел Чуйского района, Мерке" } },
    { id: "tk", code: "TK", base: 520, rate: 50, name: { en: "Lower Naryn District office, Tash-Kömür", ir: "Tömönkü Narın aymaktık keñsesi, Tash-Kömür", ru: "Отдел Нижненарынского района, Таш-Кумыр" } },
    { id: "bk", code: "BK", base: 460, rate: 35, name: { en: "Lower Naryn District office, Bazar-Korgon branch", ir: "Tömönkü Narın aymaktık keñsesi, Bazar-Korgon filialı", ru: "Отдел Нижненарынского района, филиал в Базар-Коргоне" } },
    { id: "to", code: "TO", base: 160, rate: 20, name: { en: "Toktogul District office, Toktogul", ir: "Toktogul aymaktık keñsesi, Toktogul", ru: "Отдел Токтогульского района, Токтогул" } },
    { id: "sb", code: "SB", base: 120, rate: 18, name: { en: "Sary-Bulak District office, Sary-Bulak", ir: "Sarı-Bulak aymaktık keñsesi, Sarı-Bulak", ru: "Отдел Сары-Булакского района, Сары-Булак" } }
  ],
  cats: ["people", "biz", "pay", "check", "other"],
  /* sec: the section(s) of the portal a service belongs to, first one is its home: b = For businesses, c = For citizens */
  list: [
    {
      id: "passport", cat: "people", sec: "c", status: "limited", icon: "id",
      name: { en: "Passport and ID card queue", ir: "Pasport jana ID-karta kezegi", ru: "Очередь на паспорт и ID-карту" },
      desc: { en: "Take a number for your passport office and see your place in the queue.", ir: "Pasport bölümünö kezek nomerin alıp, kezektegi ordunuzdu köruñüz.", ru: "Возьмите номер в паспортный стол и узнайте своё место в очереди." },
      agency: { en: "Passport and Residence Service, Ministry of Internal Security", ir: "Pasport jana jashoo jayı kızmatı, Ichki koopsuzduk ministrligi", ru: "Служба паспортов и регистрации, Министерство внутренней безопасности" },
      keywords: "passport id card pasport паспорт удостоверение residence kuböölük"
    },
    {
      id: "event", cat: "biz", sec: "bc", status: "limited", icon: "ticket",
      name: { en: "Event and concert permit", ir: "Ish-chara jana konsert uruksatı", ru: "Разрешение на мероприятие и концерт" },
      desc: { en: "Prepare an application for a municipal permit for a concert, festival, parade or gathering.", ir: "Konsert, festival, parad je chogulush üchün shaardık uruksatka arız dayardañız.", ru: "Подготовьте заявку на муниципальное разрешение на концерт, фестиваль, шествие или собрание." },
      agency: { en: "City halls of Talas, Nurzhan and Iyık Janyl; Department of Public Information", ir: "Talas, Nurzhan jana Iyık Janıl meriyaları; Kogomduk maalımat departamenti", ru: "Мэрии Таласа, Нуржана и Ийык-Джаныла; Департамент общественной информации" },
      keywords: "permit concert event festival uruksat konsert разрешение концерт мероприятие"
    },
    {
      id: "business", cat: "biz", sec: "b", status: "limited", icon: "shop",
      name: { en: "Small business registration", ir: "Chakan ishkanany kattoo", ru: "Регистрация малого предприятия" },
      desc: { en: "Check a business name and prepare the registration of a sole trader, company, farm or cooperative.", ir: "Ishkananın atın tekshirip, jeke ishkerdi, kompaniyanı, dıykan charbasın je kooperativdi kattoogo dayardanıñız.", ru: "Проверьте название и подготовьте регистрацию ИП, компании, фермы или кооператива." },
      agency: { en: "Register of Firms, Ministry of Economy, through the district offices", ir: "Firmalar reestri, Ekonomika ministrligi, aymaktık keñseler arkıluu", ru: "Реестр фирм, Министерство экономики, через районные отделы" },
      keywords: "business company register firm ishkana kattoo бизнес регистрация фирма ИП"
    },
    {
      id: "census", cat: "biz", sec: "bc", status: "soon", icon: "chart",
      name: { en: "Census of business entities 2026", ir: "2026-jılkı ishkanalardın sanagı", ru: "Перепись хозяйствующих субъектов 2026" },
      desc: { en: "How to answer the census questionnaire before 30 November.", ir: "Sanak suroo-joop kagazına 30-noyabrga cheyin kantip joop berüü kerek.", ru: "Как ответить на вопросы переписи до 30 ноября." },
      agency: { en: "Territorial Statistics Office", ir: "Aymaktık statistika keñsesi", ru: "Территориальное статистическое управление" },
      keywords: "census sanak перепись statistics"
    },
    {
      id: "electricity", cat: "pay", sec: "c", status: "limited", icon: "bolt",
      name: { en: "Electricity bill", ir: "Elektr energiyası üchün esep", ru: "Счёт за электроэнергию" },
      desc: { en: "See your Iradenergo bill and meter readings by personal account number.", ir: "Jeke esep nomeri boyuncha Iradenergo esebiñizdi jana hisoochtun körsötküchün köruñüz.", ru: "Счёт «Ирадэнерго» и показания счётчика по номеру лицевого счёта." },
      agency: { en: "Iradenergo: Talas Electric Networks and Nurzhan Electric Networks", ir: "Iradenergo: Talas jana Nurzhan elektr tarmaktarı", ru: "«Ирадэнерго»: Таласские и Нуржанские электросети" },
      keywords: "electricity power iradenergo bill elektr jarık электричество свет счёт"
    },
    {
      id: "water", cat: "pay", sec: "c", status: "limited", icon: "drop",
      name: { en: "Water bill", ir: "Suu üchün esep", ru: "Счёт за воду" },
      desc: { en: "Check your water and sewerage charges in Talas, Nurzhan and Iyık Janyl.", ir: "Talas, Nurzhan jana Iyık Janıldagı suu jana kanalizatsiya tölömüñüzdü tekshiriñiz.", ru: "Начисления за воду и канализацию в Таласе, Нуржане и Ийык-Джаныле." },
      agency: { en: "City water enterprises", ir: "Shaardık suu ishkanaları", ru: "Городские водоканалы" },
      keywords: "water sewer suu вода водоканал"
    },
    {
      id: "fines", cat: "pay", sec: "c", status: "limited", icon: "car",
      name: { en: "Traffic fines", ir: "Jol kıymıl ayıptarı", ru: "Штрафы ГИБДД" },
      desc: { en: "Look up unpaid traffic fines by registration plate.", ir: "Mamlekettik nomer boyuncha tölönbögön jol ayıptarın tabıñız.", ru: "Неоплаченные штрафы по госномеру." },
      agency: { en: "Highway Patrol Corps, Republican Gendarmerie; city police", ir: "Avtojol patrul korpusu, Respublikalık jandarmeriya; shaar politsiyası", ru: "Корпус дорожного патруля Республиканской жандармерии; городская полиция" },
      keywords: "fine traffic speeding ayıp штраф"
    },
    {
      id: "parcel", cat: "check", sec: "c", status: "ok", icon: "box",
      name: { en: "Parcel and letter tracking", ir: "Posılka jana kat izdöö", ru: "Отслеживание посылок и писем" },
      desc: { en: "Follow a registered item through Irad Pochtasy.", ir: "Kattalgan jönötmönü Irad Pochtası arkıluu baykañız.", ru: "Отслеживание регистрируемых отправлений «Ирадпочты»." },
      agency: { en: "Irad Pochtasy, State Postal Enterprise", ir: "Irad Pochtası, mamlekettik pochta ishkanası", ru: "«Ирадпочта», государственное почтовое предприятие" },
      keywords: "parcel post tracking pochta posılka посылка почта"
    },
    {
      id: "motor", cat: "check", sec: "c", status: "ok", icon: "shield",
      name: { en: "Motor policy check", ir: "Avtopolis tekshirüü", ru: "Проверка автополиса" },
      desc: { en: "Check whether a vehicle has a valid compulsory third-party policy.", ir: "Unaanın mildettüü kamsızdandıruu polisi jaraktuu ekenin tekshiriñiz.", ru: "Проверка действующего полиса обязательного страхования ответственности." },
      agency: { en: "Iradstrakh, State Insurance Company of Irad", ir: "Iradstrakh, Irad mamlekettik kamsızdandıruu kompaniyası", ru: "«Ирадстрах», Государственная страховая компания Ирада" },
      keywords: "insurance policy motor iradstrakh polis страховка осаго"
    },
    {
      id: "crossing", cat: "other", sec: "c", status: "off", icon: "route",
      name: { en: "Crossing the Qara-Chik line", ir: "Kara-Chik liniyasınan ötüü", ru: "Пересечение линии Кара-Чик" },
      desc: { en: "Rules for visitors from the tribal regions and for travel across the line.", ir: "Tooluu aymaktardan kelgender jana liniya arkıluu jol jürüü erejeleri.", ru: "Правила для приезжающих из племенных районов и для поездок через линию." },
      agency: { en: "Republican Gendarmerie", ir: "Respublikalık jandarmeriya", ru: "Республиканская жандармерия" },
      keywords: "line crossing checkpoint permit qara-chik kara-chik liniya линия пропуск"
    },
    {
      id: "civil", cat: "people", sec: "c", status: "soon", icon: "doc",
      name: { en: "Birth, marriage and death certificates", ir: "Tuuluu, nike jana ölüm kübölüktörü", ru: "Свидетельства о рождении, браке и смерти" },
      desc: { en: "Copies of civil registration certificates.", ir: "Jarandık abal aktılarının kübölüktörünün köchürmölörü.", ru: "Копии свидетельств о регистрации актов гражданского состояния." },
      agency: { en: "District civil registry offices", ir: "Aymaktık JAAK bölümdörü", ru: "Районные отделы ЗАГС" },
      keywords: "birth marriage certificate civil registry nike загс свидетельство"
    }
  ]
};
