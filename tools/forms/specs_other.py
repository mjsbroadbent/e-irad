"""Forms: other services (hunting, gatherings, the Feast pass, archives, appeals, dogs, the line)."""
from engine import T
from specs_people import PERSON, address, CONTACT, DECL, STD_INS, OFFICIAL_STD

NONE_INS = T("Write NONE in every field that does not apply. Fields left blank are treated as not completed and the form is returned without consideration.",
             "Tiyeshelüü emes ar bir talaaga JOK dep jazıñız. Bosh kaltırılgan talaalar tolturulbagan dep eseptelip, forma karalbay kaytarılat.",
             "Во всех неприменимых полях пишите НЕТ. Незаполненные поля считаются незаполненными, и форма возвращается без рассмотрения.")

DATE_RECVD = T("Date received", "Kabıl alıngan kün", "Дата приёма")
SIGN_OFF = T("Signature of the official", "Kızmatkerdin kolu", "Подпись должностного лица")
YES = T("yes", "ooba", "да")
NO = T("no", "jok", "нет")


def short_person(title):
    """Name, identity card and personal number only (no place of birth)."""
    return {"t": title, "rows": [
        {"k": "boxes", "l": "surname"},
        {"k": "boxes", "l": "first"},
        {"k": "boxes", "l": "patr"},
        [{"k": "date", "l": "dob", "w": 1.1}, {"k": "boxes", "l": "idser", "n": 2, "w": .55}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.25}, {"k": "boxes", "l": "pin", "n": 14, "w": 2.1}],
    ]}


def split_tables(forms):
    """The engine reserves too little height for a table's label, so a labelled table that stands alone in a row
    touches the next row. Draw the label as an option-less check field (a bare label row) and the table without one."""
    for spec in forms.values():
        groups = [sec["rows"] for sec in spec["sections"]] + [spec.get("official", [])]
        for rows in groups:
            out = []
            for r in rows:
                if isinstance(r, dict) and r["k"] == "table" and r.get("l"):
                    out.append({"k": "check", "l": r["l"], "opts": [], "cols": 1})
                    t = dict(r)
                    del t["l"]
                    out.append(t)
                else:
                    out.append(r)
            rows[:] = out


FORMS = {}

# ---------------------------------------------------------------- AGR-11
FORMS["AGR-11"] = {
    "ink": "#24452b", "mark": "gov", "rev": "rev. 03/2019",
    "approved": "Approved by Order of the Talas Basin Agricultural Directorate No. 17 of 4 March 2019 under the Hunting and Fisheries Regulations № 09-14",
    "to": T("Head of the Hunting and Fisheries Section, Talas Basin Agricultural Directorate", "Talas basseyninin aylı charba direktsiyasının Añchılık jana balık charba bölümünün bashchısına", "Начальнику отдела охоты и рыболовства Таласского бассейнового управления сельского хозяйства"),
    "instructions": STD_INS[:2] + [NONE_INS,
        T("Submit the application in person, in two copies, with: a copy of the identity card; the hunter's ticket; the firearm permit issued by the Republican Gendarmerie (original shown, copy attached); two photographs 3 × 4 cm; the receipt for the licence fee. Fishing-only applicants do not submit a hunter's ticket or firearm permit.",
          "Arızdı özüñüz eki nuskada tapshırasız, tirkelet: jeke kuböölüktün köchürmösü; añchınin bileti; Respublikalık jandarmeriya bergen kural uruksatı (originalı körsötülöt, köchürmösü tirkelet); 3 × 4 sm eki süröt; litsenziya akısın tölögön kvitantsiya. Balık uloo üchün gana arız bergender añchı biletin jana kural uruksatın tapshırbayt.",
          "Заявление подаётся лично в двух экземплярах с приложением: копии удостоверения личности; охотничьего билета; разрешения на оружие Республиканской жандармерии (оригинал предъявляется, копия прилагается); двух фотографий 3 × 4 см; квитанции об уплате сбора. Заявители только на рыболовство охотничий билет и разрешение на оружие не представляют."),
    ],
    "sections": [
        short_person(T("Applicant", "Arız beruuchu", "Заявитель")),
        {"t": T("Photograph and address", "Süröt jana darek", "Фотография и адрес"), "rows": [
            [{"k": "photo", "w": .75}, {"k": "text", "w": 2.6, "t": T("Glue one photograph here with paper glue (no staples). The second photograph is attached to the licence on issue. Photographs in headwear, dark glasses or uniform are not accepted.",
                                                                 "Bir süröttü bul jerge kagaz jelimi menen chaplañız (skrepkasız). Ekinchi süröt litsenziya berilgende aga chaplanat. Bash kiyimchen, kara köz aynekchen je formachan sürötter kabıl alınbayt.",
                                                                 "Одну фотографию наклейте здесь бумажным клеем (без скрепок). Вторая наклеивается на лицензию при выдаче. Фотографии в головном уборе, тёмных очках или форменной одежде не принимаются.")}],
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "district", "w": 1}],
            [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
            CONTACT,
        ]},
        {"t": T("Hunter's ticket and firearms", "Añchınin bileti jana kural", "Охотничий билет и оружие"), "rows": [
            [{"k": "boxes", "l": T("Hunter's ticket No.", "Añchı biletinin No.", "№ охотничьего билета"), "n": 8, "w": 1.2}, {"k": "date", "l": "idate", "w": 1}, {"k": "line", "l": T("Issued by (examining commission)", "Kim bergen (sınak komissiyası)", "Кем выдан (экзаменационная комиссия)"), "w": 1.5}],
            {"k": "table", "l": T("Firearms to be used (each must be entered in a valid Gendarmerie permit)", "Koldonula turgan kural (ar biri Jandarmeriyanın jaraktuu uruksatına jazılgan boluşu kerek)", "Используемое оружие (каждое должно быть вписано в действующее разрешение жандармерии)"),
             "cols": [(T("Type (smoothbore, rifled, combined)", "Türü (jılmakay, nareztüü, aralash)", "Вид (гладкоств., нарезное, комбинир.)"), 2.4), (T("Make and model", "Markası jana modeli", "Марка и модель"), 2.2), (T("Calibre", "Kalibri", "Калибр"), 1), (T("Serial No.", "Seriyalık No.", "Заводской №"), 1.6), (T("Permit No. and valid until", "Uruksat No. jana möönötü", "№ разрешения и срок"), 2.2)], "rows": 2},
        ]},
        {"t": T("Licence requested", "Suralgan litsenziya", "Запрашиваемая лицензия"), "rows": [
            {"k": "check", "l": T("Kind of licence (one per form)", "Litsenziyanın türü (bir formaga bireö)", "Вид лицензии (одна на бланк)"), "opts": [
                T("seasonal licence, small game", "mezgildik litsenziya, mayda añ", "сезонная, мелкая дичь"), T("waterfowl licence", "suu kushtarına litsenziya", "на водоплавающую дичь"), T("quota licence, large game", "kvota litsenziyası, iri añ", "квотная, крупная дичь"),
                T("amateur fishing licence", "ışkıboz balık uloo litsenziyası", "любительское рыболовство"), T("fishing with nets (cooperatives only)", "tor menen (kooperativder gana)", "сетями (только кооп.)"), T("combined (small game and fishing)", "aralash (mayda añ jana balık)", "комбинированная (мелкая дичь и рыба)"),
            ], "cols": 3},
            {"k": "check", "l": T("Season", "Mezgil", "Сезон"), "opts": [T("spring (waterfowl only)", "jazgı (suu kushtarı gana)", "весенний (только водоплавающая)"), T("autumn and winter", "küzgü jana kıshkı", "осенне-зимний"), T("calendar year (fishing only)", "kalendardık jıl (balık gana)", "календарный год (только рыба)")], "cols": 3},
            [{"k": "boxes", "l": T("Hunting ground No. in the Register of Hunting Grounds", "Añchılık jerlerinin reestrindegi añchılık jerinin No.", "№ угодья в Реестре охотничьих угодий"), "n": 4, "w": 1.3, "note": T("Hunting with firearms is prohibited in the restricted-weapons zone 12 km either side of the Qara-Chik line. Hunting grounds lying in the zone, wholly or in part, are open for fishing only, and licences for them are issued without the right to carry a firearm.",
                                                                                                                                                                               "Kara-Chik liniyasınan eki tarapka 12 km kural chektelgen zonada kural menen añ uloo tıyuu salınat. Bul zonada tolugu menen je bölügü jatkan añchılık jerleri balık uloo üchün gana achık, alarga litsenziya kural kötörüü ukugusuz berilet.",
                                                                                                                                                                               "Охота с огнестрельным оружием запрещена в зоне ограничения оружия по 12 км по обе стороны линии Кара-Чик. Угодья, полностью или частично лежащие в зоне, открыты только для рыболовства, и лицензии на них выдаются без права ношения оружия.")},
             {"k": "line", "l": T("Name of the hunting ground and district", "Añchılık jerinin atı jana aymagı", "Название угодья и район"), "w": 2}],
            {"k": "table", "l": T("Species and quantities requested (game). Do not enter species not permitted for hunting: see note at the end", "Suralgan añ türlörü jana sanı. Uloogo uruksat berilbegen türlördü jazbañız: akırındagı tüshündürmönü karañız", "Запрашиваемые виды и количество (дичь). Не вписывайте виды, охота на которые запрещена: см. примечание"),
             "cols": [(T("Species", "Türü", "Вид"), 3), (T("Season dates", "Mezgildin datası", "Сроки сезона"), 2), (T("Quantity requested", "Suralgan sanı", "Запрошено"), 1.4), (T("Daily bag limit", "Kündük chegi", "Дневная норма"), 1.4), (T("Quota No. (official)", "Kvota No. (kızmattık)", "№ квоты (служ.)"), 1.6), (T("Allowed (official)", "Uruksat (kızmattık)", "Разрешено (служ.)"), 1.4)], "rows": 5},
        ]},
        {"t": T("Fishing", "Balık uloo", "Рыболовство"), "rows": [
            {"k": "check", "l": T("Waters", "Suular", "Водоёмы"), "opts": [
                T("Kyzyl-Adyr Reservoir", "Kızıl-Adır suu saktagıchı", "Кызыл-Адырское вдхр."), T("Talas river", "Talas daryası", "река Талас"), T("Kara-Buura river, lower course", "Kara-Buura daryası, tömönkü agımı", "река Кара-Буура, нижнее течение"),
                T("irrigation canals and ponds", "sugat aryktarı jana kölmötter", "оросительные каналы и пруды"), T("other (state)", "bashka (körsötüñüz)", "иное (укажите)"),
            ], "cols": 3},
            {"k": "check", "l": T("Fishing gear", "Balık uloo shaymandarı", "Орудия лова"), "opts": [
                T("float or ledger rod (2 rods, 2 hooks each)", "kalkıgıchtuu je tüp karmak", "поплавочная или донная удочка"), T("spinning rod (1 lure)", "spinning (1 aldamchı)", "спиннинг (1 приманка)"), T("fly rod", "nakhlıstı karmak", "нахлыстовая удочка"),
                T("landing net", "sachok", "подсачек"), T("fish trap (cooperatives only)", "balık tuzagı (kooperativder gana)", "верша (только кооперативы)"), T("gill net (cooperatives only)", "jabıshkak tor (kooperativ)", "ставная сеть (кооп.)"),
            ], "cols": 3},
            [{"k": "line", "l": T("Fishing cooperative and its register No. (net licences only)", "Balık uloochu kooperativ jana anın reestr No. (tor litsenziyası üchün gana)", "Рыболовецкий кооператив и его № в реестре (только сети)"), "w": 2}, {"k": "boxes", "l": T("Number of nets, total length (m)", "Torlordun sanı, jalpı uzundugu (m)", "Число сетей, общая длина (м)"), "n": 6, "w": 1}],
        ]},
        {"t": T("Previous licences and offences", "Murdagı litsenziyalar jana ukuk buzuular", "Прежние лицензии и правонарушения"), "rows": [
            {"k": "check", "l": T("Have you been fined for a hunting or fishing offence, or had a licence or firearm permit withdrawn, in the last three years?", "Akırkı üch jılda añ je balık uloo boyuncha ukuk buzuu üchün ayıp tölödüñüzbü, je litsenziyañız je kural uruksatıñız alındıbı?", "Привлекались ли вы за последние три года к ответственности за нарушение правил охоты или рыболовства, изымались ли лицензия или разрешение на оружие?"), "opts": [YES, NO], "cols": 4},
            [{"k": "boxes", "l": T("Previous licence No. (last season)", "Murdagı litsenziya No. (akırkı mezgil)", "№ прежней лицензии (прошлый сезон)"), "n": 9, "w": 1.3}, {"k": "line", "l": T("If fined: date, article, authority, penalty", "Ayıp salınsa: kün, berene, organ, jaza", "Если да: дата, статья, орган, взыскание"), "w": 2}],
        ]},
    ],
    "declaration": T("I declare that the information given is true and complete. I undertake to observe the closed seasons, bag limits and rules of the hunting ground; to carry the licence, hunter's ticket and firearm permit while hunting or fishing and show them to a game warden on request; and to return the licence with the completed record of game taken within 10 days of its expiry. A licence not returned bars a new one for the next season.",
                     "Berilgen maalımattın tuura jana toluk ekenin tastıktaym. Tıyuu mezgilderin, uloo chegin jana añchılık jerinin erejelerin saktoogo; añ je balık ulooda litsenziyanı, añchı biletin jana kural uruksatın janımda alıp jürüp, añ küzötchüsü suraganda körsötüügö; litsenziyanı möönötü bütkön soñ 10 kündün ichinde alıngan añ esebi menen kaytaruuga mildettenem. Kaytarılbagan litsenziya kiyinki mezgilge jañı litsenziya aluuga jol berbeyt.",
                     "Подтверждаю достоверность и полноту сведений. Обязуюсь соблюдать сроки запрета, нормы добычи и правила угодья; иметь при себе лицензию, охотничий билет и разрешение на оружие и предъявлять их егерю по требованию; сдать лицензию с заполненным учётом добычи в течение 10 дней после окончания её срока. Несданная лицензия лишает права на новую в следующем сезоне."),
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "boxes", "l": T("Order of receipt (quota)", "Kelgen tartibi (kvota)", "Очерёдность (квота)"), "n": 5, "w": .9}],
        [{"k": "boxes", "l": T("Licence No. issued", "Berilgen litsenziya No.", "№ выданной лицензии"), "n": 9, "w": 1.2}, {"k": "money", "l": T("Licence fee paid", "Tölöngön litsenziya akısı", "Уплачен сбор"), "n": 7, "w": 1.2}, {"k": "date", "l": T("Valid until", "Möönötü", "Действительна до"), "w": 1}],
        {"k": "check", "l": "decision", "opts": ["granted", "refused", T("waiting list (quota exhausted)", "kütüü tizmesi (kvota bütkön)", "лист ожидания (квота)")], "cols": 3},
        {"k": "sign", "l": ["recvd", SIGN_OFF]},
    ],
    "notes": [
        T("Not permitted for hunting at any time, and no licence is issued for them: Siberian ibex, argali, snow leopard, Menzbier's marmot, Tien Shan brown bear, lynx, stone marten, saker falcon, golden eagle and all other birds of prey, black stork, demoiselle crane. Taking, keeping, transporting or selling these animals, their meat, horns, skins or eggs is an offence; horns and skins found are handed to the Section.",
          "Bul jırtkıchtarga jana añdarga ech kachan uruksat berilbeyt jana litsenziya berilbeyt: Sibir teke, arkar, ilbirs, Menzbir suuru, Tyan-Shan küröñ ayuusu, silöösün, tash suusar, ılaachın, bürküt jana bashka bardık jırtkıch kushtar, kara leylek, turna. Bul janıbarlardı, alardın etin, müyüzün, terisin je jumurtkasın aluu, saktoo, tashuu je satuu ukuk buzuu bolup sanalat; tabılgan müyüz jana teriler bölümgö tapshırılat.",
          "Охота запрещена всегда, лицензии не выдаются: сибирский горный козёл (теке), архар, снежный барс, сурок Мензбира, тяньшанский бурый медведь, рысь, каменная куница, балобан, беркут и все другие хищные птицы, чёрный аист, журавль-красавка. Добыча, содержание, перевозка или продажа этих животных, их мяса, рогов, шкур или яиц являются правонарушением; найденные рога и шкуры сдаются в отдел."),
        T("Closed seasons: waterfowl 1 February – 31 March and 1 May – 14 August; pheasant, chukar partridge and quail 1 February – 30 September; tolai hare 1 February – 31 October; wild boar 1 March – 30 June (sows with young protected all year); fox and wolf no closed season (firearms only on a valid licence). Fishing: spawning ban on all waters 1 April – 31 May; trout and marinka of the Talas and its tributaries, rod only, 1 June – 30 September; Aral barbel not to be taken.",
          "Tıyuu mezgilderi: suu kushtarı 1-fevral – 31-mart jana 1-may – 14-avgust; kırgoool, kekilik jana bödönö 1-fevral – 30-sentyabr; tolay koyonu 1-fevral – 31-oktyabr; kaban 1-mart – 30-iyun (balası bar urgaachısı jıl boyu korgolot); tülkü jana karışkır tıyuu mezgili jok (kural jaraktuu litsenziya menen gana). Balık: bardık suularda uuldoo mezgilindegi tıyuu 1-aprel – 31-may; Talas jana anın kuymalarının forel jana marinkası, karmak menen gana, 1-iyun – 30-sentyabr; Aral muruttuu balıgın karmoogo bolboyt.",
          "Сроки запрета: водоплавающая дичь 1 февраля – 31 марта и 1 мая – 14 августа; фазан, кеклик и перепел 1 февраля – 30 сентября; заяц-толай 1 февраля – 31 октября; кабан 1 марта – 30 июня (самки с приплодом охраняются круглый год); лиса и волк без запрета (оружие только по действующей лицензии). Рыба: нерестовый запрет на всех водоёмах 1 апреля – 31 мая; форель и маринка Таласа и его притоков только удочкой, 1 июня – 30 сентября; аральский усач лову не подлежит."),
        T("Daily bag limits per licence holder: waterfowl 5, pheasant 2, chukar 5, quail 10, hare 1; fish 5 kg (trout 3 fish). Quota licences for large game are allocated by the commission of the Section in order of receipt of complete applications; applications for the autumn and winter season are accepted from 1 to 31 August only. Licence fees are set by the price list of the Directorate in force on the date of issue and are not refunded if the licence is not used.",
          "Bir litsenziya eesine kündük chek: suu kushtarı 5, kırgoool 2, kekilik 5, bödönö 10, koyon 1; balık 5 kg (forel 3 dana). Iri añ üchün kvota litsenziyaların bölümdün komissiyası toluk arızdar kelgen tartip boyuncha bölüştüröt; küzgü jana kıshkı mezgilge arızdar 1–31-avgustta gana kabıl alınat. Litsenziya akısı berilgen kündö küchündö bolgon direktsiyanın baa tizmesi boyuncha belgilenet jana litsenziya paydalanılbasa kaytarılbayt.",
          "Дневные нормы на владельца лицензии: водоплавающая 5, фазан 2, кеклик 5, перепел 10, заяц 1; рыба 5 кг (форель 3 шт.). Квотные лицензии на крупную дичь распределяются комиссией отдела в порядке поступления полных заявлений; заявления на осенне-зимний сезон принимаются только с 1 по 31 августа. Сборы устанавливаются прейскурантом управления на дату выдачи и при неиспользовании лицензии не возвращаются."),
    ],
}

# ---------------------------------------------------------------- CH-50
FORMS["CH-50"] = {
    "ink": "#26324a", "mark": "gov", "rev": "rev. 11/2015",
    "approved": "Approved by joint Order of the City Halls of Talas, Nurzhan and Iyık Janyl No. 3/15 of 16 November 2015",
    "to": T("Mayor of the city, through the General Department of City Hall", "Shaardın merine, meriyanın Jalpı bölümü arkıluu", "Мэру города через Общий отдел мэрии"),
    "instructions": STD_INS[:2] + [NONE_INS,
        T("The notification is lodged in person by an organiser, in two copies, no earlier than 30 and no later than 10 days before the gathering. One copy is returned to the organiser with the incoming number. Notifications sent by post, fax or e-mail are not accepted.",
          "Bildirmeni uyushturuuchu özü eki nuskada, chogulushtan 30 kündön erte emes jana 10 kündön kech emes tapshırat. Bir nuskası kiruuchu nomeri menen uyushturuuchuga kaytarılat. Pochta, faks je e-pochta arkıluu jiberilgen bildirmeler kabıl alınbayt.",
          "Уведомление подаётся организатором лично в двух экземплярах не ранее чем за 30 и не позднее чем за 10 дней до собрания. Один экземпляр возвращается организатору с входящим номером. Уведомления по почте, факсу или электронной почте не принимаются."),
        T("A gathering may be held only at a place on the List of places designated for public gatherings approved by the city council. The List is displayed at City Hall (General Department) and may be read there on working days.",
          "Chogulush shaardık keñesh bekitken Kogomduk chogulushtar üchün belgilengen jerlerdin tizmesindegi jerde gana ötkörülüşü mümkün. Tizme meriyada (Jalpı bölüm) ilinip turat jana anı ish künderü ushul jerde okuuga bolot.",
          "Собрание может проводиться только в месте из Перечня мест, специально отведённых для публичных собраний, утверждённого городским советом. Перечень вывешен в мэрии (Общий отдел) и доступен для ознакомления в рабочие дни."),
        T("Posters, banners, placards and leaflets to be used, and the text of any address to be read aloud, are submitted with the notification, one specimen of each, listed in Section D. Materials not submitted may not be displayed at the gathering.",
          "Koldonula turgan afishalar, banerler, plakattar jana barakchalar, oshondoy ele ün chıgarıp okula turgan kayrıluunun tekstı bildirme menen birge ar birinen bir nuska tapshırılat jana D bölümündö tizmelenet. Tapshırılbagan materialdardı chogulushta körsötüügö bolboyt.",
          "Плакаты, транспаранты, лозунги и листовки, а также текст обращений, зачитываемых вслух, представляются с уведомлением по одному образцу каждого и перечисляются в разделе D. Непредставленные материалы на собрании не используются."),
    ],
    "sections": [
        {"t": T("Organisers", "Uyushturuuchular", "Организаторы"), "rows": [
            {"k": "check", "l": T("The organiser is", "Uyushturuuchu", "Организатор"), "opts": [T("one or more individuals", "bir je bir neche jeke adam", "одно или несколько физических лиц"), T("a registered association", "kattalgan birikme", "зарегистрированное объединение"), T("a business entity", "charbalık subyekt", "хозяйствующий субъект"), T("a registered religious community", "kattalgan dindik jamaat", "зарегистрированная религиозная община")], "cols": 2},
            {"k": "table", "l": T("Organisers (the first named is responsible for the gathering; persons under 18 may not be organisers)", "Uyushturuuchular (birinchi atalgan adam chogulush üchün jooptuu; 18 jashka tolbogondor uyushturuuchu bolo albayt)", "Организаторы (первый указанный отвечает за собрание; лица до 18 лет организаторами быть не могут)"),
             "cols": [("fullname", 4), ("idno", 1.8), (T("Address of residence", "Jashagan dareki", "Адрес проживания"), 3.4), ("phone", 1.8)], "rows": 3},
            [{"k": "line", "l": "orgname", "w": 2}, {"k": "boxes", "l": "regnum", "n": 10, "w": 1.1}],
        ]},
        {"t": T("Purpose and form of the gathering", "Chogulushtun maksatı jana türü", "Цель и форма собрания"), "rows": [
            {"k": "check", "l": T("Form", "Türü", "Форма"), "opts": [T("meeting", "jıyın", "митинг"), T("assembly", "chogulush", "собрание"), T("picket", "piket", "пикетирование"), T("procession", "jürüsh", "шествие"), T("other (state)", "bashka (körsötüñüz)", "иное (укажите)")], "cols": 5},
            {"k": "area", "l": T("Purpose of the gathering (state it in full; slogans are not a purpose)", "Chogulushtun maksatı (toluk jazıñız; uraan maksat bolup sanalbayt)", "Цель собрания (указывается полностью; лозунг целью не является)"), "lines": 3},
        ]},
        {"t": T("Place and time", "Ordu jana ubaktısı", "Место и время"), "rows": [
            [{"k": "check", "l": "city", "opts": [T("Talas", "Talas", "Талас"), T("Nurzhan", "Nurzhan", "Нуржан"), T("Iyık Janyl", "Iyık Janıl", "Ийык-Джаныл")], "cols": 3, "w": 1.6},
             {"k": "boxes", "l": T("Place No. in the List", "Tizmedegi jerdin No.", "№ места в Перечне"), "n": 3, "w": .8}],
            {"k": "line", "l": T("Name of the designated place as written in the List", "Belgilengen jerdin tizmede jazılgan atı", "Наименование отведённого места, как в Перечне")},
            {"k": "area", "l": T("Route (processions only): place of assembly, streets in order, place of dispersal", "Jürüshtün jolu (jürüsh üchün gana): chogulgan jer, köchölör tartibi menen, tarkagan jer", "Маршрут (только для шествий): место сбора, улицы по порядку, место окончания"), "lines": 3,
             "note": T("A procession must begin and end at places on the List and may use only the streets named in the notification. Movement on the carriageway is permitted only where the Highway Patrol Corps or the city police has agreed it; otherwise participants keep to the pavement.",
                       "Jürüsh tizmedegi jerlerde bashtalıp, ushul jerlerde ayaktalıshı kerek jana bildirmede atalgan köchölördü gana paydalanat. Jol bölügü menen jürüügö Avtojol patrul korpusu je shaar politsiyası makuldashkan jerde gana uruksat; kalgan jerlerde katıshuuchular jöö jol menen jürüshöt.",
                       "Шествие начинается и заканчивается в местах из Перечня и проходит только по улицам, указанным в уведомлении. Движение по проезжей части допускается лишь по согласованию с Корпусом дорожного патруля или городской полицией; в остальных случаях участники идут по тротуару.")},
            [{"k": "date", "l": T("Date of the gathering", "Chogulushtun künü", "Дата собрания"), "w": 1.1}, {"k": "boxes", "l": T("Assembly from (hh mm)", "Chogulup bashtoo (saat min)", "Сбор с (ч мин)"), "n": 4, "w": .9}, {"k": "boxes", "l": T("Start (hh mm)", "Bashtalışı (saat min)", "Начало (ч мин)"), "n": 4, "w": .9}, {"k": "boxes", "l": T("End (hh mm)", "Ayaktalışı (saat min)", "Окончание (ч мин)"), "n": 4, "w": .9}],
        ]},
        {"t": T("Participants, stewards and materials", "Katıshuuchular, tartip saktoochular jana materialdar", "Участники, распорядители и материалы"), "rows": [
            [{"k": "boxes", "l": T("Expected number of participants", "Kütülgön katıshuuchulardın sanı", "Предполагаемое число участников"), "n": 6, "w": 1}, {"k": "boxes", "l": T("Number of stewards (at least 1 per 50 participants)", "Tartip saktoochulardın sanı (50 katıshuuchuga keminde 1)", "Число распорядителей (не менее 1 на 50 участников)"), "n": 4, "w": 1.3}],
            {"k": "table", "l": T("Stewards (they wear a white armband with the word TARTIP and are present from assembly to dispersal)", "Tartip saktoochular (TARTIP dep jazılgan ak bilerik takat jana chogulgandan tarkaganga cheyin katısat)", "Распорядители (носят белую повязку с надписью TARTIP и присутствуют от сбора до окончания)"),
             "cols": [("fullname", 4.4), ("idno", 2), ("phone", 2), (T("Signature", "Kolu", "Подпись"), 1.6)], "rows": 4},
            [{"k": "check", "l": T("Sound equipment", "Ün küchötküch", "Звукоусилительная аппаратура"), "opts": [T("none", "jok", "нет"), T("hand megaphone", "kol megafonu", "мегафон"), T("amplifier and loudspeakers", "küchötkuch jana dinamikter", "усилитель и динамики"), T("vehicle with loudspeakers", "dinamiktüü unaa", "автомобиль с динамиком")], "cols": 2, "w": 3},
             {"k": "boxes", "l": T("Total power (W)", "Jalpı kubattuulugu (Vt)", "Общая мощность (Вт)"), "n": 4, "w": .8}],
            {"k": "table", "l": T("Materials submitted with this notification (one specimen each)", "Bul bildirme menen tapshırılgan materialdar (ar birinen bir nuska)", "Материалы, представленные с уведомлением (по одному образцу)"),
             "cols": [(T("Item (poster, banner, leaflet, text of address)", "Buyum (afisha, baner, barakcha, kayrıluu teksti)", "Предмет (плакат, транспарант, листовка, текст)"), 4), (T("Size", "Ölchömü", "Размер"), 1.4), (T("Copies to be used", "Koldonula turgan nuskalar", "Кол-во экз."), 1.4), (T("Language", "Tili", "Язык"), 1.4), (T("Sheets", "Barak", "Листов"), 1)], "rows": 4},
        ]},
    ],
    "declaration": T("I, the responsible organiser, confirm that the information given is true. I am aware that the organiser keeps order together with the stewards; that participants may not carry weapons or objects that may be used as weapons, alcohol, pyrotechnics or face coverings; that the gathering ends at the time stated; and that City Hall may within 3 working days propose another place on the List or another time.",
                     "Men, jooptuu uyushturuuchu, berilgen maalımattın tuura ekenin tastıktaym. Uyushturuuchu tartip saktoochular menen birge tartipti saktaarın; katıshuuchular kural je kural katarı koldonulushu mümkün bolgon buyumdardı, spirt ichimdikterin, pirotekhnikanı je betin jabuuchu nerselerdi alıp jürböstügün; chogulush körsötülgön ubakta ayaktalaarın; meriya 3 ish kündün ichinde tizmedegi bashka jerdi je bashka ubakıttı sunushu mümkün ekenin bilem.",
                     "Я, ответственный организатор, подтверждаю достоверность сведений. Мне известно, что организатор обеспечивает порядок вместе с распорядителями; что участникам запрещено иметь оружие и предметы, которые могут быть использованы как оружие, алкоголь, пиротехнику и средства сокрытия лица; что собрание заканчивается в указанное время; и что мэрия в течение 3 рабочих дней может предложить другое место из Перечня или другое время."),
    "signs": [T("Signature of the responsible organiser", "Jooptuu uyushturuuchunun kolu", "Подпись ответственного организатора"), "date"],
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "boxes", "l": T("Materials received (sheets)", "Kabıl alıngan materialdar (barak)", "Принято материалов (листов)"), "n": 3, "w": .9}],
        {"k": "check", "l": "decision", "opts": [T("noted without objection", "karshılıksız esepke alındı", "принято к сведению без возражений"), T("another place or time proposed", "bashka jer je ubakıt sunuldu", "предложено иное место или время"), T("not accepted: not on the List or late", "kabıl alınbadı: tizmede jok je kech", "не принято: вне Перечня или поздно")], "cols": 3},
        {"k": "sign", "l": ["recvd", SIGN_OFF]},
    ],
    "counterfoil": {"t": T("Receipt for a notification of a public gathering", "Kogomduk chogulush tuuraluu bildirmeni kabıl alganı tuuraluu tilkat", "Расписка в приёме уведомления о публичном собрании"), "rows": [
        [{"k": "line", "l": T("Responsible organiser", "Jooptuu uyushturuuchu", "Ответственный организатор"), "w": 1.4}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.4}, {"k": "date", "l": DATE_RECVD, "w": 1.1}, {"k": "line", "l": "recvd", "w": 1.2}],
    ]},
    "notes": [
        T("The receipt below is not a permit. A gathering for which another place or time has been proposed may be held only at the place and time proposed by City Hall, if the organiser accepts them in writing within 2 working days; otherwise the notification is considered withdrawn.",
          "Tömöndögü tilkat uruksat emes. Bashka jer je ubakıt sunulgan chogulush uyushturuuchu alardı 2 ish kündün ichinde jazuu jüzündö kabıl alsa gana meriya sungan jerde jana ubakta ötkörülüşü mümkün; antpese bildirme kaytarılıp alındı dep eseptelet.",
          "Расписка ниже не является разрешением. Собрание, для которого предложено иное место или время, может проводиться только в месте и время, предложенные мэрией, если организатор письменно согласится с ними в течение 2 рабочих дней; иначе уведомление считается отозванным."),
        T("Concerts, fairs, parades and other public events are not notified on this form: apply for a municipal permit on Form CH-31.",
          "Konsertter, yarmarkalar, paraddar jana bashka kogomduk ish-charalar bul forma menen bildirilbeyt: CH-31 forması boyuncha shaardık uruksatka arız beriñiz.",
          "Концерты, ярмарки, парады и иные публичные мероприятия этой формой не заявляются: подайте заявление на муниципальное разрешение по форме CH-31."),
    ],
}

# ---------------------------------------------------------------- IJ-3
FORMS["IJ-3"] = {
    "ink": "#1d3766", "mark": "gov", "rev": "rev. 07/2018",
    "approved": "Approved by Order of the Mayor of Iyık Janyl No. 64 of 12 July 2018, agreed with the Archbishopric",
    "to": T("Transport Department, City Hall of Iyık Janyl", "Iyık Janıl meriyasının Transport bölümünö", "Отделу транспорта мэрии Ийык-Джаныла"),
    "instructions": STD_INS[:2] + [NONE_INS,
        T("On the Feast of St. Janyl (24 August) the Cathedral Hill road is closed to motor vehicles from 18:00 on 23 August to 22:00 on 24 August. Only vehicles with a pass issued on this form may enter, and only by the lower barrier.",
          "Iyık Janıl mayramında (24-avgust) Sobor dobosunun jolu 23-avgust saat 18:00dön 24-avgust saat 22:00gö cheyin unaalar üchün jabık. Bul forma boyuncha berilgen ötkörmösü bar unaalar gana, tömönkü shlagbaum arkıluu gana kire alat.",
          "В праздник Святой Джаныл (24 августа) дорога на Соборный холм закрыта для транспорта с 18:00 23 августа до 22:00 24 августа. Въезд разрешён только транспорту с пропуском по этой форме и только через нижний шлагбаум."),
        T("One application per vehicle. The pass is valid only for the vehicle, driver and passengers named in it and only for the year stated. Passes are collected in person by the applicant from window 4 of City Hall from 15 August.",
          "Bir unaaga bir arız. Ötkörmö anda atalgan unaa, aydoochu jana jürgünchülör üchün, körsötülgön jılga gana jaraktuu. Ötkörmölördü arız beruuchu 15-avgusttan tartıp meriyanın 4-terezesinen özü alat.",
          "Одно заявление на одно транспортное средство. Пропуск действителен только для указанных в нём транспорта, водителя и пассажиров на указанный год. Получение лично, окно 4 мэрии, с 15 августа."),
    ],
    "sections": [
        short_person(T("Applicant", "Arız beruuchu", "Заявитель")),
        {"t": T("Address and category", "Darek jana kategoriya", "Адрес и категория"), "rows": [
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "district", "w": 1}],
            [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
            CONTACT,
            {"k": "check", "l": T("Category of pass (one only)", "Ötkörmönün kategoriyası (biröö gana)", "Категория пропуска (только одна)"), "opts": [
                T("pilgrim with reduced mobility and escort", "kıymıldoosu chektelgen ziyaratchı jana jandoochu", "паломник с огранич. подвижностью и сопровожд."), T("clergy", "dinkızmatchılar", "духовенство"),
                T("supplier to the cathedral precinct", "sobor korusuna jetkirüüchü", "поставщик соборного двора"), T("press", "basma söz", "пресса"),
            ], "cols": 2},
            [{"k": "line", "l": T("Supporting document (see note)", "Tastıktoochu dokument (tüshündürmönü karañız)", "Подтверждающий документ (см. примечание)"), "w": 2, "note": T("Supporting documents: for pilgrims with reduced mobility, the certificate of the medical and social commission (disability group I or II) or a hospital certificate issued after 1 June of the current year; for clergy, a letter of the Chancellery of the Archbishopric; for suppliers, the supply contract with the administration of the cathedral precinct; for the press, the accreditation card of the Department of Public Information valid on 24 August.",
                                                                                                                                                                         "Tastıktoochu dokumentter: kıymıldoosu chektelgen ziyaratchılar üchün — meditsinalık-sotsialdık komissiyanın kuböölügü (I je II toptogu mümkünchülük chektöö) je uchurdagı jıldın 1-iyununan kiyin berilgen oorukana malımatnaması; dinkızmatchılar üchün — Arkhiyepiskopiya keñsesinin katı; jetkirüüchülör üchün — sobor korusunun administratsiyası menen jetkirüü kelishimi; basma söz üchün — 24-avgustta jaraktuu Kogomduk maalımat departamentinin akkreditatsiya kartochkası.",
                                                                                                                                                                         "Подтверждающие документы: для паломников с ограниченной подвижностью — справка медико-социальной комиссии (инвалидность I или II группы) или справка больницы, выданная после 1 июня текущего года; для духовенства — письмо Канцелярии архиепископии; для поставщиков — договор поставки с администрацией соборного двора; для прессы — аккредитационная карточка Департамента общественной информации, действительная на 24 августа.")},
             {"k": "boxes", "l": T("Document No.", "Dokumenttin No.", "№ документа"), "n": 8, "w": 1}, {"k": "date", "l": "idate", "w": 1}],
        ]},
        {"t": T("Vehicle and driver", "Unaa jana aydoochu", "Транспортное средство и водитель"), "rows": [
            [{"k": "boxes", "l": T("Registration plate", "Kattoo belgisi", "Гос. номер"), "n": 9, "w": 1.1}, {"k": "line", "l": T("Make and model", "Markası jana modeli", "Марка и модель"), "w": 1.3}, {"k": "line", "l": T("Colour", "Tüsü", "Цвет"), "w": .8}],
            [{"k": "check", "l": T("Type of vehicle", "Unaanın türü", "Тип транспортного средства"), "opts": [T("passenger car", "jeñil unaa", "легковой"), T("minibus up to 16 seats", "16 orunga cheyinki mikroavtobus", "микроавтобус до 16 мест"), T("van or lorry up to 3.5 t", "3,5 tga cheyinki furgon je jük unaa", "фургон или грузовик до 3,5 т"), T("ambulance", "tez jardam", "скорая помощь")], "cols": 2, "w": 3}, {"k": "boxes", "l": T("Seats", "Orundar", "Мест"), "n": 2, "w": .5}],
            [{"k": "line", "l": T("Driver: surname, first name", "Aydoochu: familiyası, atı", "Водитель: фамилия, имя"), "w": 1.6}, {"k": "boxes", "l": T("Driving licence No.", "Aydoochuluk kuböölügünün No.", "№ водительского удостоверения"), "n": 9, "w": 1.1}, {"k": "boxes", "l": T("Iradstrakh policy No.", "Iradstrakh polisinin No.", "№ полиса «Ирадстрах»"), "n": 10, "w": 1.2}],
        ]},
        {"t": T("Passengers", "Jürgünchülör", "Пассажиры"), "rows": [
            {"k": "table", "l": T("Passengers (not more than the seats entered above; children are entered)", "Jürgünchülör (jogoruda körsötülgön orundardan ashpayt; baldar da jazılat)", "Пассажиры (не более указанного числа мест; дети вписываются)"),
             "cols": [("fullname", 4.2), ("dob", 1.5), ("idno", 1.8), (T("Reduced mobility (yes / no)", "Kıymıldoosu chektelgen (ooba / jok)", "Огранич. подвижность (да / нет)"), 1.6), (T("Wheelchair", "Arabacha", "Коляска"), 1)], "rows": 6},
            [{"k": "check", "l": T("Drop-off point requested", "Suralgan tüshürüü jeri", "Запрашиваемое место высадки"), "opts": [T("north door (reduced mobility only)", "tündük eshik (chektelgender gana)", "северные двери (огранич. подвижн.)"), T("cloister gate (clergy)", "monastır darbazası (dinkızmatchılar)", "ворота клуатра (духовенство)"), T("supply yard (suppliers)", "jetkirüü koroosu (jetkirüüchülör)", "хозяйственный двор (поставщики)"), T("press area", "basma söz ayantı", "площадка прессы")], "cols": 2, "w": 2.6},
             {"k": "boxes", "l": T("Arrival at the barrier (hh mm)", "Shlagbaumga keluu (saat min)", "Прибытие к шлагбауму (ч мин)"), "n": 4, "w": .9}],
            {"k": "area", "l": T("Assistance needed at the drop-off point (wheelchair, stretcher, escort by a steward of the precinct)", "Tüshürüü jerinde kerek bolgon jardam (arabacha, zambil, sobor korusunun tartip saktoochusunun jandashı)", "Необходимая помощь у места высадки (коляска, носилки, сопровождение распорядителем двора)"), "lines": 2},
        ]},
    ],
    "declaration": T("I confirm that the information given is true. I understand that vehicles and persons are inspected at the barrier; that no arms may be carried into the precinct; that the vehicle may stand only at the drop-off point for as long as needed to set down and take up passengers, and is then directed to the parking area named on the pass; and that a pass used by another vehicle or person is withdrawn.",
                     "Berilgen maalımattın tuura ekenin tastıktaym. Shlagbaumda unaalar jana adamdar tekshirilerin; sobor korusuna kural alıp kirüügö bolboostugun; unaa tüshürüü jerinde jürgünchülördü tüshürüp-aluuga kerek ubakıt gana turup, andan kiyin ötkörmödö atalgan toktotuuchu jayga jönötülörün; bashka unaa je adam paydalangan ötkörmö alınıp koyuları tüshünöm.",
                     "Подтверждаю достоверность сведений. Мне известно, что транспорт и люди досматриваются у шлагбаума; что в соборный двор запрещено проносить оружие; что транспорт стоит у места высадки только для посадки и высадки пассажиров и затем направляется на стоянку, указанную в пропуске; и что пропуск, использованный другим транспортом или лицом, изымается."),
    "official": [
        [{"k": "boxes", "l": T("Order of receipt No.", "Kelgen tartibi No.", "№ очерёдности"), "n": 5, "w": 1}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "boxes", "l": T("Pass No.", "Ötkörmö No.", "№ пропуска"), "n": 6, "w": 1}],
        [{"k": "check", "l": "decision", "opts": [T("pass issued", "ötkörmö berildi", "пропуск выдан"), T("refused: quota exhausted", "baş tartıldı: kvota bütkön", "отказ: квота исчерпана"), T("refused: documents", "baş tartıldı: dokumentter", "отказано: документы")], "cols": 3, "w": 3}, {"k": "line", "l": T("Parking area", "Toktotuuchu jay", "Стоянка"), "w": 1}],
        {"k": "sign", "l": ["recvd", SIGN_OFF]},
    ],
    "counterfoil": {"t": T("Receipt for an application for a Feast vehicle pass", "Mayram unaa ötkörmösünö arızdı kabıl alganı tuuraluu tilkat", "Расписка в приёме заявления на пропуск транспорта в праздник"), "rows": [
        [{"k": "boxes", "l": T("Registration plate", "Kattoo belgisi", "Гос. номер"), "n": 9, "w": 1.2}, {"k": "boxes", "l": T("Order of receipt No.", "Kelgen tartibi No.", "№ очерёдности"), "n": 5, "w": .9}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "line", "l": "recvd", "w": 1.2}],
    ]},
    "notes": [
        T("Passes are issued from 1 August in order of receipt of complete applications, within the number of passes fixed for each category by the Mayor in agreement with the Archbishopric. When the number for a category is reached, further applications in that category are not considered; they are not returned and the fee is not charged.",
          "Ötkörmölör 1-avgusttan tartıp toluk arızdar kelgen tartip boyuncha, mer Arkhiyepiskopiya menen makuldashıp ar bir kategoriyaga belgilegen san cheginde berilet. Kategoriya boyuncha san jetkende, ushul kategoriyadagı kiyinki arızdar karalbayt; alar kaytarılbayt jana akı alınbayt.",
          "Пропуска выдаются с 1 августа в порядке поступления полных заявлений в пределах числа, установленного для каждой категории мэром по согласованию с архиепископией. По достижении числа заявления этой категории не рассматриваются; они не возвращаются, плата не взимается."),
        T("Passes issued for a previous year are not valid. Pilgrims from the tribal regions travel under the arrangements agreed each year through the Joint Liaison Committee of the United Nations Mission in Irad; this form is not used for crossing the line.",
          "Murdagı jılga berilgen ötkörmölör jaraksız. Tooluu aymaktardan kelgen ziyaratchılar Iraddagı BUU missiyasının Birgeleshken baylanısh komiteti arkıluu ar jılı makuldashılgan tartip menen kelet; bul forma liniyadan ötüü üchün koldonulbayt.",
          "Пропуска прошлых лет недействительны. Паломники из племенных районов следуют в порядке, ежегодно согласуемом через Совместный комитет связи Миссии ООН в Ираде; эта форма для пересечения линии не используется."),
    ],
}

# ---------------------------------------------------------------- SA-4
FORMS["SA-4"] = {
    "ink": "#4a3321", "mark": "gov", "rev": "rev. 02/2017",
    "approved": "Approved by Order of the Director of the State Archives of Irad No. 9 of 2 February 2017",
    "to": T("Director, State Archives of Irad, 16 University Street (TSU campus), Talas", "Irad mamlekettik arkhivinin direktoruna, Universitet köchösü 16 (TMU kampusu), Talas", "Директору Государственного архива Ирада, ул. Университетская, 16 (кампус ТГУ), Талас"),
    "instructions": STD_INS[:2] + [NONE_INS,
        T("One request per fond, not more than 10 files per request. The archival cipher (fond, inventory, file, sheets) is taken from the published guide to the fonds, the inventories in the reading room, or a previous reply of the Archives. A request without a cipher is treated as a thematic enquiry and answered within 60 days.",
          "Bir fondgo bir suroo, bir suroodo 10 isten ashpayt. Arkhivdik shifr (fond, opis, ish, baraktar) fonddordun basılıp chıkkan jetekchisinen, okuu zalındagı opisterden je Arkhivdin murdagı joobunan alınat. Shifrsiz suroo temalık suroo katarı karalıp, 60 kündün ichinde joop berilet.",
          "Один запрос на один фонд, не более 10 дел в запросе. Архивный шифр (фонд, опись, дело, листы) берётся из опубликованного путеводителя по фондам, описей в читальном зале или прежнего ответа архива. Запрос без шифра рассматривается как тематический, ответ — в течение 60 дней."),
        T("Copies are sent by post only. Enclose a stamped addressed envelope of size C4 (for copies not folded) with postage for a registered letter of the expected weight. Copies are not handed over in the reading room or at the Archives' entrance. Requests received without an envelope are kept for 3 months and then destroyed without reply.",
          "Köchürmölör pochta arkıluu gana jiberilet. Kütülgön salmaktagı buyurtma kat üchün markası chaplangan, darek jazılgan C4 ölchömdögü konvert (büktölbögön köchürmölör üchün) tirkeñiz. Köchürmölör okuu zalında je Arkhivdin kireberishinde berilbeyt. Konvertsiz kelgen suroolor 3 ay saktalıp, andan kiyin joopsuz joyuluuga tiyish.",
          "Копии высылаются только по почте. Приложите конверт формата C4 (для копий без сгиба) с марками на заказное письмо ожидаемого веса и с адресом. В читальном зале и у входа в архив копии не выдаются. Запросы без конверта хранятся 3 месяца и затем уничтожаются без ответа."),
    ],
    "sections": [
        {"t": T("Applicant", "Arız beruuchu", "Заявитель"), "rows": [
            {"k": "boxes", "l": "surname"},
            {"k": "boxes", "l": "first"},
            [{"k": "boxes", "l": "patr", "w": 2.4}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.1}],
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "district", "w": 1}],
            [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
            CONTACT,
            [{"k": "boxes", "l": T("Earlier request or reply of the Archives: registration No.", "Arkhivge murdagı suroo je anın joobu: kattoo No.", "Прежний запрос или ответ архива: рег. №"), "n": 10, "w": 1.6}, {"k": "date", "l": "date", "w": 1}, {"k": "check", "l": T("Reader's ticket held", "Okurmandın bileti bar", "Читательский билет"), "opts": [YES, NO], "cols": 2, "w": 1}],
            {"k": "line", "l": T("Institution and position (researchers only); attach the institution's letter", "Mekeme jana kızmatı (izildöööchülör gana); mekemenin katın tirkeñiz", "Учреждение и должность (только исследователи); приложите письмо учреждения")},
        ]},
        {"t": T("Documents requested", "Suralgan dokumentter", "Запрашиваемые документы"), "rows": [
            [{"k": "boxes", "l": T("Fond No.", "Fond No.", "№ фонда"), "n": 4, "w": .8}, {"k": "line", "l": T("Name of the fond", "Fonddun atı", "Название фонда"), "w": 3}],
            {"k": "table", "l": T("Files and sheets (enter sheet numbers as foliated in the file, e.g. 12–14 rev.)", "Ishter jana baraktar (barak nomerlerin ishte nomerlengendey jazıñız, mısalı 12–14 ark.)", "Дела и листы (номера листов по листажу дела, напр. 12–14 об.)"),
             "cols": [(T("Inventory (opis)", "Opis", "Опись"), 1.2), (T("File No.", "Ish No.", "Дело №"), 1.2), (T("Sheets from – to", "Baraktar – cheyin", "Листы с – по"), 1.6), (T("Title of the file and dates", "Ishtin atı jana datası", "Заголовок дела и даты"), 4.4), (T("Number of sheets", "Baraktardın sanı", "Кол-во листов"), 1.2), (T("Copy: P or C", "Köchürmö: P je C", "Копия: P или C"), 1)], "rows": 10},
        ]},
        {"t": T("Purpose and kind of copies", "Maksatı jana köchürmölördün türü", "Цель и вид копий"), "rows": [
            {"k": "check", "l": T("Purpose of the request", "Suroonun maksatı", "Цель запроса"), "opts": [
                T("length of service, pension", "ish stajı, pensiya", "трудовой стаж, пенсия"), T("property or land rights", "mülk je jer ukugu", "права на имущество или землю"), T("genealogy (sanjyra)", "sanjıra", "генеалогия (санжыра)"),
                T("academic research", "ilimiy izildöö", "научное исследование"), T("court proceedings", "sot ishi", "судебное разбирательство"), T("publication or exhibition", "basıp chıgaruu je körgözmö", "публикация или выставка"),
            ], "cols": 3},
            {"k": "check", "l": T("Kind of copy (P = plain, C = certified, as marked in the table)", "Köchürmönün türü (P = jönököy, C = tastıktalgan, tablitsada belgilengendey)", "Вид копии (P — простая, C — заверенная, как отмечено в таблице)"), "opts": [
                T("plain photocopy (P)", "jönököy fotoköchürmö (P)", "простая ксерокопия (P)"), T("certified archival copy with seal (C)", "möör menen tastıktalgan arkhivdik köchürmö (C)", "заверенная архивная копия с печатью (C)"),
                T("archival extract", "arkhivdik köchürmö-üzündü", "архивная выписка"), T("archival certificate", "arkhivdik malımatnama", "архивная справка"),
            ], "cols": 2},
            [{"k": "check", "l": T("Paper size", "Kagazdın ölchömü", "Формат"), "opts": [T("A4", "A4", "A4"), T("A3", "A3", "A3"), T("photographic print", "foto basma", "фотоотпечаток")], "cols": 3, "w": 2}, {"k": "boxes", "l": T("Sets of copies", "Köchürmö toptomu", "Комплектов"), "n": 2, "w": .8}],
            {"k": "line", "l": T("Authority to which certified copies will be presented", "Tastıktalgan köchürmölör tapshırıla turgan organ", "Орган, в который представляются заверенные копии")},
        ]},
        {"t": T("Delivery by post", "Pochta arkıluu jetkirüü", "Доставка по почте"), "rows": [
            {"k": "text", "t": T("Copies are sent only to the address in Section A, by registered letter, in the envelope enclosed by the applicant. An invoice for the copying fee is sent first; the copies are dispatched within 10 working days of receipt of payment.",
                                 "Köchürmölör A bölümündögü darekke gana, buyurtma kat menen, arız beruuchu tirkegen konvertte jiberilet. Adegende köchürüü akısına esep jiberilet; köchürmölör tölöm kelgenden kiyin 10 ish kündün ichinde jönötülöt.",
                                 "Копии направляются только по адресу в разделе A заказным письмом в приложенном заявителем конверте. Сначала высылается счёт за изготовление копий; копии отправляются в течение 10 рабочих дней после поступления оплаты.")},
            [{"k": "check", "l": T("Envelope enclosed", "Tirkelgen konvert", "Приложен конверт"), "opts": [T("C4", "C4", "C4"), T("C5", "C5", "C5"), T("two or more", "eki je andan köp", "два и более")], "cols": 3, "w": 2}, {"k": "money", "l": T("Value of stamps on the envelope", "Konverttegi markalardın narkı", "Стоимость марок на конверте"), "n": 5, "w": 1.4}],
        ]},
    ],
    "declaration": T("I confirm that the information given is true and that the copies are requested for the purpose stated. I undertake not to publish or reproduce the copies without the written consent of the Archives and, where consent is given, to cite the archival cipher in full. I understand that the Archives may refuse copies of documents whose condition does not allow copying or whose use is restricted.",
                     "Berilgen maalımattın tuura ekenin jana köchürmölör körsötülgön maksat üchün suralganın tastıktaym. Köchürmölördü Arkhivdin jazuu jüzündögü makuldugusuz basıp chıgarboogo je köböytpöögö, makulduk berilse arkhivdik shifrdi toluk körsötüügö mildettenem. Abalı köchürüügö mümkünchülük berbegen je paydalanuusu chektelgen dokumentterdin köchürmösünön Arkhiv baş tartıshı mümkün ekenin tüshünöm.",
                     "Подтверждаю достоверность сведений и то, что копии запрашиваются для указанной цели. Обязуюсь не публиковать и не воспроизводить копии без письменного согласия архива, а при согласии указывать архивный шифр полностью. Мне известно, что архив может отказать в копировании документов, состояние которых не позволяет копирование, или доступ к которым ограничен."),
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "check", "l": T("Envelope", "Konvert", "Конверт"), "opts": [T("enclosed", "tirkelgen", "приложен"), T("missing", "jok", "нет")], "cols": 2, "w": 1}],
        [{"k": "line", "l": T("Files issued from the stack by (archivist)", "Ishterdi saktoochu jaydan bergen (arkhivist)", "Дела выданы из хранилища (архивист)"), "w": 1.4}, {"k": "boxes", "l": T("Sheets copied", "Köchürülgön baraktar", "Скопировано листов"), "n": 4, "w": .8}, {"k": "money", "l": T("Fee due", "Tölönö turgan akı", "К оплате"), "n": 6, "w": 1.2}],
        [{"k": "boxes", "l": T("Invoice No.", "Esep No.", "№ счёта"), "n": 7, "w": 1}, {"k": "date", "l": T("Payment received", "Tölöm keldi", "Оплата получена"), "w": 1}, {"k": "date", "l": T("Copies sent", "Köchürmölör jiberildi", "Копии отправлены"), "w": 1}],
        {"k": "check", "l": "decision", "opts": [T("copies made", "köchürmölör jasaldı", "копии изготовлены"), T("refused: restricted access", "baş tartıldı: chektelgen paydalanuu", "отказано: ограниченный доступ"), T("refused: condition of the document", "baş tartıldı: dokumenttin abalı", "отказано: состояние документа")], "cols": 3},
        {"k": "sign", "l": [T("Head of the Reading Room and Copying Section", "Okuu zalı jana köchürüü bölümünün bashchısı", "Заведующий читальным залом и отделом копирования"), SIGN_OFF]},
    ],
    "notes": [
        T("The reading room accepts researchers by written appointment only; places are allocated one month in advance and the waiting list is displayed at the entrance. Researchers working in the reading room order copies on this form like other applicants.",
          "Okuu zalı izildöööchülördü jazuu jüzündögü jazılıu boyuncha gana kabıl aladı; orundar bir ay murun bölünöt jana kütüü tizmesi kireberishte ilinip turat. Okuu zalında ishtegen izildöööchülör köchürmölördü bashka arız beruuchular sıyaktuu ele bul forma boyuncha buyurtat.",
          "Читальный зал принимает исследователей только по письменной записи; места распределяются на месяц вперёд, лист ожидания вывешен у входа. Исследователи, работающие в зале, заказывают копии по этой форме, как и другие заявители."),
        T("Records of the ISEZ period (from 2007) are subject to classification review and are not copied. Copies of personal files and of documents naming living persons are issued only to the person concerned or on a court's request.",
          "IAEZ mezgilinin jazuuları (2007-jıldan) kupuyalık kayra karoogo tiyish jana köchürülböyt. Jeke ishterdin jana tirüü adamdardın atı atalgan dokumentterdin köchürmölörü tiyeshelüü adamdın özünö je sottun suranıchı boyuncha gana berilet.",
          "Документы периода ОЭЗИ (с 2007 г.) подлежат пересмотру грифа секретности и не копируются. Копии личных дел и документов с именами живых лиц выдаются только самому лицу или по запросу суда."),
        T("Copying fees are charged under the price list of the State Archives in force on the date of the invoice. Certified copies of documents in Russian, Persian or Chagatai are issued with the text as written; translations are not made.",
          "Köchürüü akısı esep berilgen kündö küchündö bolgon Mamlekettik arkhivdin baa tizmesi boyuncha alınat. Orus, pars je chagatay tilindegi dokumentterdin tastıktalgan köchürmölörü tekst jazılganday berilet; kotormo jasalbayt.",
          "Плата взимается по прейскуранту Государственного архива на дату счёта. Заверенные копии документов на русском, персидском или чагатайском языках выдаются с текстом в подлиннике; переводы не выполняются."),
    ],
}

# ---------------------------------------------------------------- OG-1
FORMS["OG-1"] = {
    "ink": "#6e0f16", "mark": "emblem", "rev": "rev. 03/2019",
    "approved": "Approved by Order of the Head of the Office of the Governor No. 22 of 1 March 2019 on the procedure for considering appeals",
    "to": T("Office of the Governor, Letters and Appeals Section, Government House, Talas", "Gubernator keñsesine, Kattar jana kayrıluular bölümü, Ökmöt üyü, Talas", "Канцелярия Губернатора, отдел писем и обращений, Дом Правительства, Талас"),
    "instructions": [
        T("Write clearly in black or dark blue ink. The text of the appeal may be handwritten or typed; continue on plain A4 sheets if necessary, numbering and signing each sheet.",
          "Kara je kara-kök siya menen aykın jazıñız. Kayrıluunun tekstin kol menen je mashinkada jazsa bolot; kerek bolso jönököy A4 baraktarda ulantıp, ar bir baraktı nomerlep, kol koyuñuz.",
          "Пишите разборчиво чёрными или тёмно-синими чернилами. Текст обращения может быть рукописным или машинописным; при необходимости продолжите на листах A4, пронумеровав и подписав каждый."),
        T("Anonymous appeals, and appeals without a postal address for the reply, are not considered. Appeals containing obscene or insulting language or threats are left without consideration and the author is informed.",
          "Anonimdik kayrıluular jana joop üchün pochta dareki jok kayrıluular karalbayt. Uyatsız je kordoochu sözdör, korkutuular bar kayrıluular karalbay kaltırılıp, avtorgo kabarlanat.",
          "Анонимные обращения и обращения без почтового адреса для ответа не рассматриваются. Обращения с нецензурными или оскорбительными выражениями либо угрозами оставляются без рассмотрения, о чём сообщается автору."),
        T("An appeal is answered within 30 days of its registration. Where the question is within the competence of another body, the appeal is forwarded to it within 7 days and the author is informed. The time limit may be extended once by 30 days with notice to the author.",
          "Kayrıluuga kattalgan kündön tartıp 30 kündün ichinde joop berilet. Masele bashka organdın ıygarım ukugunda bolso, kayrıluu aga 7 kündün ichinde jiberilip, avtorgo kabarlanat. Möönöt avtorgo kabarlap, bir jolu 30 küngö uzartılıshı mümkün.",
          "Ответ даётся в течение 30 дней со дня регистрации. Если вопрос относится к компетенции другого органа, обращение направляется туда в течение 7 дней с уведомлением автора. Срок может быть однократно продлён на 30 дней с уведомлением автора."),
        T("Do not enclose original documents: attach copies only. Copies are not returned. Appeals sent by e-mail to letters@iradgov.org are registered only if this form, signed, is attached as a scanned image.",
          "Original dokumentterdi tirkebeñiz: köchürmölördü gana tirkeñiz. Köchürmölör kaytarılbayt. letters@iradgov.org darekine e-pochta menen jiberilgen kayrıluular bul kol koyulgan forma skanerlengen süröt katarı tirkelse gana kattalat.",
          "Не прилагайте подлинники документов, только копии. Копии не возвращаются. Обращения по эл. почте на letters@iradgov.org регистрируются, только если приложен скан подписанной формы."),
    ],
    "sections": [
        {"t": T("Author of the appeal", "Kayrıluunun avtoru", "Автор обращения"), "rows": [
            {"k": "boxes", "l": "surname"},
            {"k": "boxes", "l": "first"},
            [{"k": "boxes", "l": "patr", "w": 2.4}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.1}],
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": "district", "w": 1}],
            [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
            CONTACT,
            {"k": "check", "l": T("The appeal is made", "Kayrıluu berilet", "Обращение подаётся"), "opts": [T("on my own behalf", "öz atımdan", "от своего имени"), T("for a group (list of signatures attached)", "top atınan (kol tizmesi tirkelgen)", "от группы (список подписей)"), T("on behalf of an organisation", "uyum atınan", "от имени организации")], "cols": 3},
        ]},
        {"t": T("Addressee and subject", "Darektöö jana tema", "Адресат и тема"), "rows": [
            {"k": "check", "l": T("The appeal is addressed to", "Kayrıluu kimge darektelgen", "Обращение адресовано"), "opts": [
                T("the Governor", "Gubernatorgo", "Губернатору"), T("the Lieutenant Governor", "Vitse-gubernatorgo", "Вице-губернатору"), T("Ministry of Internal Security", "Ichki koopsuzduk ministrligine", "Мин. внутренней безопасности"),
                T("Ministry of Finance", "Finans ministrligine", "Министерству финансов"), T("Ministry of Economy", "Ekonomika ministrligine", "Министерству экономики"), T("Dept. of Infrastructure and Communications", "Infrastruktura jana baylanısh dep.", "Деп. инфраструктуры и связи"),
                T("Department of Public Information", "Kogomduk maalımat dep.", "Деп. общественной информации"), T("Social Fund", "Sotsialdık fondgo", "Социальному фонду"), T("City Hall (state which)", "Meriyaga (kaysı ekenin körsötüñüz)", "Мэрии (укажите какой)"),
                T("district administration (state which)", "aymaktık administratsiyaga", "районной администрации"), T("other state body (state)", "bashka mamlekettik organga (körsötüñüz)", "иному органу (укажите)"),
            ], "cols": 3},
            {"k": "line", "l": T("Name of the City Hall, district administration or other body", "Meriyanın, aymaktık administratsiyanın je bashka organdın atı", "Наименование мэрии, районной администрации или иного органа")},
            {"k": "check", "l": T("Subject (one only)", "Tema (biröö gana)", "Тематика (только одна)"), "opts": [
                T("housing and utilities", "turak jay jana kommunaldık kızmattar", "жильё и коммунальные услуги"), T("pensions and allowances", "pensiyalar jana jöölökpuldar", "пенсии и пособия"), T("land and property", "jer jana mülk", "земля и имущество"),
                T("employment and wages", "ish jana emgek akı", "трудоустройство и зарплата"), T("health care", "salamattık saktoo", "здравоохранение"), T("education", "bilim berüü", "образование"),
                T("public order, courts", "kogomduk tartip, sottor", "общественный порядок, суды"), T("transport and roads", "transport jana joldor", "транспорт и дороги"), T("taxes and duties", "salıktar jana bajılar", "налоги и пошлины"),
                T("documents and registration", "dokumentter jana kattoo", "документы и регистрация"), T("trade and business", "sooda jana biznes", "торговля и предпринимательство"), T("other", "bashka", "иное"),
            ], "cols": 3},
            [{"k": "check", "l": T("Have you appealed on this question before?", "Bul masele boyuncha murda kayrıldıñızbı?", "Обращались ли вы по этому вопросу ранее?"), "opts": [YES, NO], "cols": 2, "w": 1.2},
             {"k": "boxes", "l": T("If yes: registration No. of the earlier appeal or reply", "Ooba bolso: murdagı kayrıluunun je jooptun kattoo No.", "Если да: рег. № прежнего обращения или ответа"), "n": 10, "w": 1.4}, {"k": "date", "l": "date", "w": 1}],
        ]},
        {"t": T("Text of the appeal", "Kayrıluunun teksti", "Текст обращения"), "rows": [
            {"k": "area", "l": T("State the facts, the action or decision you complain of, the body or official concerned, and what you ask for", "Faktılardı, dattangan aragettı je chechimdi, tiyeshelüü organdı je kızmatkerdi jana emne suraganıñızdı jazıñız", "Изложите факты, обжалуемое действие или решение, орган или должностное лицо и вашу просьбу"), "lines": 18},
        ]},
        {"t": T("Attachments and reply", "Tirkemeler jana joop", "Приложения и ответ"), "rows": [
            {"k": "table", "l": T("Attachments (copies only)", "Tirkemeler (köchürmölör gana)", "Приложения (только копии)"),
             "cols": [(T("Document", "Dokument", "Документ"), 6), (T("Date and No.", "Kün jana No.", "Дата и №"), 2.2), (T("Sheets", "Barak", "Листов"), 1)], "rows": 5},
            [{"k": "boxes", "l": T("Total sheets including attachments", "Tirkemeler menen jalpı barak", "Всего листов с приложениями"), "n": 3, "w": 1}, {"k": "check", "l": T("Reply to be sent", "Joop jiberilsin", "Ответ направить"), "opts": [T("by post to the address in Section A", "A bölümündögü darekke pochta menen", "по почте по адресу в разделе A"), T("by e-mail (and by post)", "e-pochta menen (jana pochta menen)", "по эл. почте (и по почте)")], "cols": 2, "w": 2.6}],
        ]},
    ],
    "declaration": T("I confirm that the facts stated in this appeal are true. I consent to the processing of the personal data given in it and to the forwarding of the appeal and its attachments to the state body competent to consider it.",
                     "Bul kayrıluuda körsötülgön faktılardın tuura ekenin tastıktaym. Andagı jeke maalımattardı ishtetüügö jana kayrıluunu tirkemeleri menen anı karoogo ıygarımı bar mamlekettik organga jiberüügö makulmun.",
                     "Подтверждаю достоверность изложенных фактов. Согласен на обработку персональных данных и на направление обращения с приложениями в государственный орган, компетентный его рассмотреть."),
    "signs": [T("Signature of the author", "Avtordun kolu", "Подпись автора"), "date"],
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": T("Date registered", "Kattalgan kün", "Дата регистрации"), "w": 1}, {"k": "date", "l": T("Reply due by", "Joop möönötü", "Срок ответа"), "w": 1}],
        {"k": "check", "l": T("Action", "Arakettenüü", "Движение"), "opts": [T("for consideration by the Office", "Keñsenin karoosuna", "на рассмотрение Канцелярии"), T("forwarded to the competent body", "ıygarımduu organga jiberildi", "направлено по компетенции"), T("left without consideration", "karalbay kaltırıldı", "оставлено без рассмотрения")], "cols": 3},
        [{"k": "line", "l": T("Forwarded to (body, outgoing No., date)", "Jiberildi (organ, chıguuchu No., kün)", "Направлено (орган, исх. №, дата)"), "w": 1.6}, {"k": "line", "l": T("Author informed (outgoing No., date)", "Avtorgo kabarlandı (chıguuchu No., kün)", "Автор уведомлён (исх. №, дата)"), "w": 1.2}],
        {"k": "sign", "l": [T("Officer of the Letters and Appeals Section", "Kattar jana kayrıluular bölümünün kızmatkeri", "Сотрудник отдела писем и обращений"), SIGN_OFF]},
    ],
    "notes": [
        T("Complaints against a court judgment are not considered under this procedure: they are made to the higher court in the manner set by the procedural codes. Appeals on questions of pensions and allowances are forwarded to the Social Fund of the ISEZ, on questions of documents and registration to the Passport and Residence Service.",
          "Sottun chechimine dattanuular bul tartip menen karalbayt: alar protsessualdık kodeksterde belgilengen tartipte jogorku sotko berilet. Pensiya jana jöölökpul maseleleri boyuncha kayrıluular IAEZdin Sotsialdık fonduna, dokumentter jana kattoo maseleleri boyuncha Pasport jana jashoo jayı kızmatına jiberilet.",
          "Жалобы на судебные решения в этом порядке не рассматриваются: они подаются в вышестоящий суд в порядке, установленном процессуальными кодексами. Обращения по пенсиям и пособиям направляются в Социальный фонд ОЭЗИ, по документам и регистрации — в Службу паспортов и регистрации."),
        T("Personal reception of citizens by officials of the Office of the Governor is held by appointment made through the Letters and Appeals Section; the appointment is requested on this form, stating the request in Section C.",
          "Gubernator keñsesinin kızmatkerleri jarandardı jeke kabıl aluusu Kattar jana kayrıluular bölümü arkıluu jazılıu boyuncha ötkörülöt; jazılıu bul forma menen suralat, suranıch C bölümündö jazılat.",
          "Личный приём граждан должностными лицами Канцелярии Губернатора ведётся по записи через отдел писем и обращений; запись запрашивается по этой форме с изложением просьбы в разделе C."),
    ],
}

# ---------------------------------------------------------------- TZ-61
OWNER = dict(PERSON, t=T("Owner of the dog", "Ittin eesi", "Владелец собаки"))

FORMS["TZ-61"] = {
    "ink": "#2c4a3b", "mark": "gov", "rev": "rev. 04/2014",
    "approved": "Approved by Decision of the City Council of Talas No. 87 of 14 April 2014 on the keeping of dogs and cats in the city",
    "to": T("Tazalık Municipal Sanitation Enterprise, Animal Registration Point", "Tazalık shaardık tazaloo ishkanası, Janıbarlardı kattoo punktu", "МП «Тазалык», пункт регистрации животных"),
    "instructions": STD_INS[:2] + [NONE_INS,
        T("Every dog over 3 months old kept in the city is registered within 30 days of acquisition, and re-registered every year in January. Bring the dog's veterinary passport with the current rabies vaccination; the dog itself need not be brought.",
          "Shaarda karalgan 3 aydan ashkan ar bir it alıngandan kiyin 30 kündün ichinde kattalat jana ar jılı yanvarda kayra kattalat. Ittin uchurdagı kuturmaga karshı emdöösü bar veterinardık pasportun ala keliñiz; ittin özün alıp keluu shart emes.",
          "Каждая собака старше 3 месяцев, содержащаяся в городе, регистрируется в течение 30 дней после приобретения и перерегистрируется ежегодно в январе. Принесите ветеринарный паспорт собаки с действующей прививкой от бешенства; саму собаку приводить не нужно."),
        T("The registration tag issued must be worn on the dog's collar at all times outside the owner's dwelling or yard. A lost tag is replaced for a fee on this form, marking the box in Section C.",
          "Berilgen kattoo jetonu it eesinin üyünön je koroosunan tıshkarı ar dayım ittin moynuna tagılıp jürüşü kerek. Jogolgon jeton akı menen ushul forma boyuncha, C bölümündögü kutuchanı belgilep almashtırılat.",
          "Выданный регистрационный жетон должен постоянно находиться на ошейнике собаки вне жилья или двора владельца. Утерянный жетон заменяется платно по этой форме с отметкой в разделе C."),
    ],
    "sections": [
        OWNER,
        dict(address(T("Address where the dog is kept", "It karalgan darek", "Адрес содержания собаки")), rows=address(None)["rows"] + [CONTACT]),
        {"t": T("The dog", "It", "Собака"), "rows": [
            [{"k": "boxes", "l": T("Name of the dog", "Ittin atı", "Кличка"), "w": 2}, {"k": "check", "l": "sex", "opts": [T("male", "erkek", "кобель"), T("female", "urgaachı", "сука"), T("neutered", "pıchılgan", "кастрир.")], "cols": 3, "w": 1.6}],
            [{"k": "line", "l": T("Breed (or MIXED)", "Tukumu (je ARALASH)", "Порода (или ПОМЕСЬ)"), "w": 1.6}, {"k": "line", "l": T("Colour and coat", "Tüsü jana jünü", "Окрас и шерсть"), "w": 1.4}, {"k": "date", "l": T("Date of birth (or estimated)", "Tuulgan kün (je bolzol menen)", "Дата рождения (или примерно)"), "w": 1.1}],
            [{"k": "boxes", "l": T("Height at withers (cm)", "Jalınan biyiktigi (sm)", "Рост в холке (см)"), "n": 3, "w": 1}, {"k": "boxes", "l": T("Weight (kg)", "Salmagı (kg)", "Вес (кг)"), "n": 3, "w": .8}, {"k": "boxes", "l": T("Veterinary passport No.", "Veterinardık pasport No.", "№ ветеринарного паспорта"), "n": 9, "w": 1.6}],
            {"k": "area", "l": T("Distinguishing marks (spots, scars, cropped ears or tail, brand or tattoo)", "Özgöchö belgileri (tak, tırtık, kesilgen kulak je kuyruk, tamga je tatuirovka)", "Особые приметы (пятна, шрамы, купированные уши или хвост, клеймо или татуировка)"), "lines": 2},
            {"k": "check", "l": T("Kept as", "Emne üchün karalat", "Назначение"), "opts": [T("companion", "üy iti", "компаньон"), T("guard dog", "küzötchü it", "сторожевая"), T("shepherd dog (alabai, töbet)", "chaban iti (alabay, töbet)", "пастушья (алабай, тобет)"), T("hunting dog (taigan, tazy)", "tazı (taygan)", "охотничья (тайган, тазы)"), T("service dog (state body)", "kızmattık it (mamlekettik organ)", "служебная (гос. орган)"), T("other", "bashka", "иное")], "cols": 3},
            {"k": "check", "l": T("Origin", "Kayda alıngan", "Происхождение"), "opts": [T("bought", "satıp alıngan", "куплена"), T("born to the owner's dog", "eesinin itinen tuulgan", "от собаки владельца"), T("gift", "belek", "подарок"), T("found or taken from the shelter", "tabılgan je bashpanadan alıngan", "найдена или взята из приюта"), T("from abroad (veterinary certificate)", "chet elden (vet. kübölük)", "из-за рубежа (вет. свидет.)")], "cols": 3},
        ]},
        {"t": T("Vaccinations, treatments and tag", "Emdöölör, darıloolor jana jeton", "Прививки, обработки и жетон"), "rows": [
            {"k": "table", "l": T("Vaccinations against rabies (copied from the veterinary passport; the last must be less than 12 months old)", "Kuturmaga karshı emdöölör (veterinardık pasporttan köchürülöt; akırkısı 12 aydan az boluşu kerek)", "Прививки против бешенства (из ветеринарного паспорта; последняя — не старше 12 месяцев)"),
             "cols": [(T("Date", "Kün", "Дата"), 1.4), (T("Vaccine, series", "Vaktsina, seriyası", "Вакцина, серия"), 2.6), (T("Veterinary station or clinic", "Veterinardık stantsiya je klinika", "Ветстанция или клиника"), 3), (T("Veterinarian", "Veterinar", "Ветврач"), 2), (T("Next due", "Kiyinkisi", "Следующая"), 1.4)], "rows": 4},
            {"k": "table", "l": T("Treatments against echinococcosis (every 3 months for shepherd and guard dogs)", "Ekhinokokkozgo karshı darıloolor (chaban jana küzötchü itterge ar 3 ayda)", "Обработки против эхинококкоза (раз в 3 месяца для пастушьих и сторожевых)"),
             "cols": [(T("Date", "Kün", "Дата"), 1.4), (T("Preparation", "Preparat", "Препарат"), 3), (T("Veterinary station or clinic", "Veterinardık stantsiya je klinika", "Ветстанция или клиника"), 3), (T("Veterinarian", "Veterinar", "Ветврач"), 2.6)], "rows": 3},
            [{"k": "check", "l": T("Registration", "Kattoo", "Регистрация"), "opts": [T("first registration", "birinchi kattoo", "первичная"), T("annual re-registration", "jıldık kayra kattoo", "перерегистрация"), T("replacement of a lost tag", "jetondu almashtıruu", "замена жетона")], "cols": 3, "w": 3}, {"k": "boxes", "l": T("Previous tag No.", "Murdagı jeton No.", "№ прежнего жетона"), "n": 7, "w": 1.2}],
            {"k": "text", "t": T("In public places the dog is kept on a lead not longer than 1.5 m. Dogs over 40 cm at the withers, and dogs of the shepherd and guard breeds whatever their size, are also muzzled. Dogs may not be walked in children's playgrounds, school yards, hospital grounds, markets or parks marked with the sign of the City Hall, and may not be left unattended in the street.",
                                 "Kogomduk jerlerde it 1,5 mden uzun emes boo menen jetelenet. Jalınan 40 smden biyik itter jana ölchömünö karabay chaban jana küzötchü tukumdagı itter tumshuk kap menen da jürüşü kerek. Itterdi baldar ayantchalarında, mektep koroolorunda, oorukana aymaktarında, bazarlarda je meriyanın belgisi koyulgan parkrarda seyildetüügö jana köchödö karoosuz kaltıruuga bolboyt.",
                                 "В общественных местах собака на поводке не длиннее 1,5 м. Собаки выше 40 см в холке, а также пастушьих и сторожевых пород независимо от роста — дополнительно в наморднике. Запрещено выгуливать собак на детских площадках, школьных дворах, территориях больниц, рынках и в парках со знаком мэрии, а также оставлять без присмотра на улице.")},
        ]},
    ],
    "declaration": T("I confirm that I am the owner of the dog described, that the information given is true, and that the dog is vaccinated against rabies. I undertake to keep the dog in accordance with the city rules, to report its loss, sale or death to the Registration Point within 10 days and to return the tag; and I understand that the owner answers for damage and injury caused by the dog.",
                     "Süröttölgön ittin eesi ekenimdi, berilgen maalımattın tuura ekenin jana it kuturmaga karshı emdelgenin tastıktaym. Ittı shaardın erejelerine ılayık karoogo, anın jogolushu, satılışı je ölüşü tuuraluu Kattoo punktuna 10 kündün ichinde kabarlap, jetondu kaytaruuga mildettenem; it keltirgen zıyan jana jaraat üchün eesi joop bererin tüshünöm.",
                     "Подтверждаю, что являюсь владельцем описанной собаки, что сведения достоверны и собака привита от бешенства. Обязуюсь содержать собаку по городским правилам, сообщать о её пропаже, продаже или гибели в пункт регистрации в течение 10 дней и сдавать жетон; мне известно, что владелец отвечает за вред и увечья, причинённые собакой."),
    "signs": [T("Signature of the owner", "Eesinin kolu", "Подпись владельца"), "date"],
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "boxes", "l": T("Tag No. issued", "Berilgen jeton No.", "№ выданного жетона"), "n": 7, "w": 1}, {"k": "money", "l": T("Registration fee paid", "Tölöngön kattoo akısı", "Уплачен сбор"), "n": 5, "w": 1.1}],
        {"k": "sign", "l": [T("Registered by (name)", "Kattagan (atı)", "Зарегистрировал (Ф.И.О.)"), SIGN_OFF]},
    ],
    "counterfoil": {"t": T("Dog registration certificate (carry it when walking the dog)", "It kattoo kübölügü (itti seyildetkende alıp jürüñüz)", "Регистрационное свидетельство собаки (иметь при выгуле)"), "rows": [
        [{"k": "boxes", "l": T("Tag No.", "Jeton No.", "№ жетона"), "n": 7, "w": 1.1}, {"k": "line", "l": T("Name of the dog, breed", "Ittin atı, tukumu", "Кличка, порода"), "w": 1.6}, {"k": "line", "l": T("Owner", "Eesi", "Владелец"), "w": 1.6}, {"k": "date", "l": T("Valid until", "Möönötü", "Действительно до"), "w": 1.1}],
    ]},
    "notes": [
        T("A dog found in a public place without a tag, or unattended, is taken by the Tazalık catching service and kept at the municipal shelter for 10 days, during which the owner may reclaim it on payment of the catching and keeping charges. Dogs not reclaimed are dealt with under the City Council decision on the keeping of dogs and cats.",
          "Kogomduk jerde jetonsuz je karoosuz tabılgan itti Tazalıktın karmoo kızmatı alıp, shaardık bashpanada 10 kün saktayt; bul möönöttö eesi karmoo jana saktoo akısın tölöp, anı kaytarıp ala alat. Kaytarılıp alınbagan itter boyuncha Shaardık keñeshtin itterdi jana mushuktardı karoo tuuraluu chechimine ılayık chara körülöt.",
          "Собака, обнаруженная в общественном месте без жетона или без присмотра, отлавливается службой отлова «Тазалык» и содержится в муниципальном приюте 10 дней, в течение которых владелец может её забрать, оплатив отлов и содержание. С невостребованными собаками поступают согласно решению городского совета о содержании собак и кошек."),
        T("Dogs kept by state bodies, and dogs of the Republican Gendarmerie and the Highway Patrol Corps, are registered by those bodies and are not entered on this form.",
          "Mamlekettik organdar karagan itter, Respublikalık jandarmeriyanın jana Avtojol patrul korpusunun itteri ushul organdar tarabınan kattalat jana bul formaga jazılbayt.",
          "Собаки государственных органов, Республиканской жандармерии и Корпуса дорожного патруля регистрируются этими органами и в эту форму не вносятся."),
    ],
}

# ---------------------------------------------------------------- RG-9
FORMS["RG-9"] = {
    "ink": "#2f3a2b", "mark": "gov", "rev": "rev. 06/2019",
    "approved": "Approved by Order of the Republican Gendarmerie No. 47 of 30 September 2008 (as amended 2013, 2019)",
    "to": T("Commander of the Line, Republican Gendarmerie, through the district Gendarmerie office", "Respublikalık jandarmeriyanın Liniya komandirine, aymaktık jandarmeriya bölümü arkıluu", "Командиру линии Республиканской жандармерии через районный отдел жандармерии"),
    "instructions": [
        T("NOTICE: the issue of Qara-Chik line crossing passes is suspended until further notice. Applications continue to be accepted at the district Gendarmerie offices; they are registered and kept on file, and will be considered in order of registration when the issue of passes resumes. No reply is sent while the suspension is in force.",
          "KABARLANDIRUU: Kara-Chik liniyasınan ötüü ötkörmölörün berüü kiyinki kabarlandıruuga cheyin toktotuldu. Arızdar aymaktık jandarmeriya bölümdöründö kabıl alına beret; alar kattalıp, saktalat jana ötkörmö berüü kayra bashtalganda kattalgan tartibi boyuncha karalat. Toktotuu küchündö turganda joop jiberilbeyt.",
          "ВНИМАНИЕ: выдача пропусков через линию Кара-Чик приостановлена до особого распоряжения. Заявления по-прежнему принимаются в районных отделах жандармерии; они регистрируются, хранятся и будут рассмотрены в порядке регистрации после возобновления выдачи. На время приостановления ответы не направляются."),
        STD_INS[0], STD_INS[1], NONE_INS,
        T("Residents of the tribal regions coming to the ISEZ do not use this form: they travel with a permit of their clan council, registered by the Gendarmerie at the crossing point.",
          "IAEZge kelgen tooluu aymaktardın turgundarı bul formanı koldonboyt: alar öz uruk keñeshinin uruksatı menen kelet, anı ötkööl punktunda Jandarmeriya kattayt.",
          "Жители племенных районов, приезжающие в ОЭЗИ, эту форму не используют: они следуют по разрешению своего совета рода, которое регистрирует жандармерия на пункте пропуска."),
    ],
    "sections": [
        {"t": T("Notice: issue of passes suspended", "Kabarlandıruu: ötkörmö berüü toktotuldu", "Внимание: выдача пропусков приостановлена"), "rows": [
            {"k": "text", "t": T("The issue of passes is suspended until further notice. This application will be registered and kept on file. Lodging it does not give the right to cross the line, and the receipt is not a pass. Do not travel to a crossing point on the strength of this application.",
                                 "Ötkörmö berüü kiyinki kabarlandıruuga cheyin toktotuldu. Bul arız kattalıp, saktalat. Anı tapshıruu liniyadan ötüü ukugun berbeyt, tilkat ötkörmö emes. Bul arızga tayanıp ötkööl punktuna barbañız.",
                                 "Выдача пропусков приостановлена до особого распоряжения. Настоящее заявление будет зарегистрировано и оставлено на хранении. Его подача не даёт права пересекать линию, расписка пропуском не является. Не выезжайте на пункт пропуска на основании этого заявления.")},
        ]},
        PERSON,
        address(T("Address of residence in the ISEZ", "IAEZdegi jashagan dareki", "Адрес проживания в ОЭЗИ")),
        {"t": T("Journey", "Sapar", "Поездка"), "rows": [
            {"k": "check", "l": T("Purpose of crossing", "Ötüünün maksatı", "Цель пересечения"), "opts": [
                T("visiting relatives", "tuugandarga baruu", "посещение родственников"), T("funeral or memorial meal", "söök koyuu je eske aluu ashı", "похороны или поминки"), T("wedding or family event", "toy je üy-bülölük ish-chara", "свадьба или семейное событие"),
                T("seasonal pasture, livestock", "mezgildik jayıt, mal", "сезонный выпас, скот"), T("trade", "sooda", "торговля"), T("work under a state contract", "mamlekettik kelishim boyuncha ish", "работа по госконтракту"),
                T("medical (with a doctor's referral)", "dabaloo (darıgerdin jollomosu menen)", "лечение (по направлению врача)"), T("humanitarian, with UNMI", "gumanitardık, BUUMI menen", "гуманитарная, с МООНИ"), T("other (state)", "bashka (körsötüñüz)", "иное (укажите)"),
            ], "cols": 3},
            {"k": "check", "l": T("Crossing point", "Ötkööl punktu", "Пункт пропуска"), "opts": [
                T("Qara-Chik Border Checkpoint", "Kara-Chik chek ara postu", "КПП Кара-Чик"), T("Aksay", "Aksay", "Аксай"), T("Toguz-Bulak (Kök-Bel road)", "Toguz-Bulak (Kök-Bel jolu)", "Тогуз-Булак (дорога Кок-Бел)"),
                T("Kara-Bulak (Kenkol Pass road)", "Kara-Bulak (Kenkol jolu)", "Кара-Булак (дор. Кенкол)"), T("Suusamyr", "Suusamır", "Суусамыр"), T("Mailuu-Suu road", "Maylu-Suu jolu", "дорога Майлуу-Суу"),
                T("Arslanbob road", "Arstanbap jolu", "дорога Арсланбоб"), T("Kök-Kamar", "Kök-Kamar", "Кок-Камар"),
            ], "cols": 3},
            [{"k": "date", "l": T("Outward crossing on", "Barıp ötüü künü", "Выезд"), "w": 1}, {"k": "date", "l": T("Return crossing by", "Kaytıp ötüü künü", "Возвращение до"), "w": 1}, {"k": "check", "l": T("Pass", "Ötkörmö", "Пропуск"), "opts": [T("single", "bir jolku", "разовый"), T("multiple, up to 3 months", "köp jolku, 3 ay", "многократ., 3 мес.")], "cols": 2, "w": 1.5}],
            {"k": "line", "l": T("Destination: settlement, valley, clan territory", "Bara turgan jer: kalk konush, öröön, uruk jeri", "Пункт назначения: населённый пункт, долина, территория рода")},
            [{"k": "line", "l": T("Clan council issuing the invitation or consent", "Chakıruu je makulduk bergen uruk keñeshi", "Совет рода, выдавший приглашение или согласие"), "w": 1.6, "note": T("The written invitation or consent of the clan council of the destination is attached in the original, with a translation into Iradi or Russian if written otherwise. The Gendarmerie may verify it with the council through the El-Choro post of the crossing point named. Applications without it are registered but marked incomplete.",
                                                                                                                                                                                                    "Bara turgan jerdin uruk keñeshinin jazuu jüzündögü chakıruusu je makuldugu originalı menen, bashka tilde jazılgan bolso, Irad je orus tiline kotormosu menen tirkelet. Jandarmeriya anı atalgan ötkööl punktunun El-Choro postu arkıluu keñesh menen tekshirishi mümkün. Ansız arızdar kattalat, birok toluk emes dep belgilenet.",
                                                                                                                                                                                                    "Письменное приглашение или согласие совета рода пункта назначения прилагается в подлиннике, с переводом на ирадский или русский язык, если оно написано на ином языке. Жандармерия может проверить его у совета через пост Эль-Чоро указанного пункта пропуска. Заявления без него регистрируются с отметкой о неполноте.")},
             {"k": "boxes", "l": T("Reference No. of the council", "Keñeshtin No.", "№ документа совета"), "n": 6, "w": .9}, {"k": "date", "l": "date", "w": 1}],
        ]},
        {"t": T("Persons, vehicle and loads", "Adamdar, unaa jana jüktör", "Лица, транспорт и грузы"), "rows": [
            {"k": "table", "l": T("Persons travelling with the applicant (each adult also lodges a separate application)", "Arız beruuchu menen birge baruuchular (ar bir chong kishi özünchö arız da beret)", "Лица, следующие с заявителем (каждый взрослый подаёт также отдельное заявление)"),
             "cols": [("fullname", 4), ("dob", 1.5), ("idno", 1.8), (T("Relationship", "Tuuganchılıgı", "Степень родства"), 1.6)], "rows": 5},
            [{"k": "check", "l": T("Travelling", "Jol jürüü", "Способ передвижения"), "opts": [T("on foot", "jöö", "пешком"), T("on horseback, pack animals", "at menen, jük mal menen", "верхом, с вьюками"), T("by vehicle", "unaa menen", "на транспорте")], "cols": 3, "w": 2.6}, {"k": "boxes", "l": T("Registration plate", "Kattoo belgisi", "Гос. номер"), "n": 9, "w": 1.2}],
            {"k": "area", "l": T("Livestock and goods to be taken across (kind, number, weight)", "Ötkörülö turgan mal jana tovarlar (türü, sanı, salmagı)", "Перемещаемые скот и товары (вид, количество, вес)"), "lines": 2},
        ]},
    ],
    "declaration": T("I declare that the information given is true and complete. I understand that weapons may not be carried within 12 km of the line; that I and my belongings may be searched at the crossing point; that the information in this application may be checked with the records of the Ministry of Internal Security; and that the pass, if issued, may be withdrawn at any time without reasons being given.",
                     "Berilgen maalımattın tuura jana toluk ekenin tastıktaym. Liniyadan 12 km aralıkta kural kötörüügö bolboostugun; ötkööl punktunda meni jana buyumdarımdı tintüügö boloorun; bul arızdagı maalımat Ichki koopsuzduk ministrliginin esebi menen tekshirilishi mümkündügün; ötkörmö berilse, sebebi körsötülböy kaalagan ubakta alınıp koyulushu mümkündügün tüshünöm.",
                     "Подтверждаю достоверность и полноту сведений. Мне известно, что в пределах 12 км от линии запрещено иметь оружие; что я и мои вещи можем быть досмотрены на пункте пропуска; что сведения заявления могут быть проверены по учётам Министерства внутренней безопасности; и что пропуск, если он будет выдан, может быть изъят в любое время без объяснения причин."),
    "official": [
        [{"k": "boxes", "l": "regno", "n": 10, "w": 1.2}, {"k": "date", "l": DATE_RECVD, "w": 1}, {"k": "boxes", "l": T("File No. (on hold)", "Saktoo ishi No.", "№ дела хранения"), "n": 6, "w": 1}],
        [{"k": "check", "l": T("Checked against the records", "Esep boyuncha tekshirildi", "Проверено по учётам"), "opts": [T("no objection", "karshılık jok", "без возражений"), T("objection", "karshılık bar", "есть возражения")], "cols": 2, "w": 1.4}, {"k": "check", "l": "decision", "opts": [T("kept on file (suspension)", "saktalat (toktotuu)", "на хранении"), T("pass issued", "ötkörmö berildi", "пропуск выдан"), "refused"], "cols": 3, "w": 2.6}],
        {"k": "sign", "l": [T("Officer of the district Gendarmerie office", "Aymaktık jandarmeriya bölümünün kızmatkeri", "Сотрудник районного отдела жандармерии"), SIGN_OFF]},
    ],
    "counterfoil": {"t": T("Receipt for an application for a line crossing pass (not a pass)", "Liniyadan ötüü ötkörmösünö arızdı kabıl alganı tuuraluu tilkat (ötkörmö emes)", "Расписка в приёме заявления на пропуск через линию (не является пропуском)"), "rows": [
        [{"k": "line", "l": "fullname", "w": 2}, {"k": "boxes", "l": "regno", "n": 10, "w": 1.3}, {"k": "date", "l": DATE_RECVD, "w": 1.2}],
    ]},
    "notes": [
        T("When the issue of passes resumes, the date will be announced by the Republican Gendarmerie through IradOne and the district Gendarmerie offices. Applications on file are then considered in order of registration; applicants are notified by post and need not lodge a new application, unless the journey dates have passed, in which case new dates are given on Form RG-9 with the earlier registration number.",
          "Ötkörmö berüü kayra bashtalganda, anın künün Respublikalık jandarmeriya IradOne jana aymaktık jandarmeriya bölümdörü arkıluu jarıyalayt. Saktalgan arızdar ushul ubakta kattalgan tartibi boyuncha karalat; arız beruuchularga pochta arkıluu kabarlanat jana alar jañı arız berbeyt, eger sapar kündörü ötüp ketpese; ötüp ketse, jañı kündör RG-9 forması menen murdagı kattoo nomeri körsötülüp berilet.",
          "О возобновлении выдачи пропусков Республиканская жандармерия объявит через IradOne и районные отделы жандармерии. Хранящиеся заявления будут рассмотрены в порядке регистрации; заявители уведомляются по почте и новых заявлений не подают, если только сроки поездки не истекли — тогда новые сроки указываются по форме RG-9 с прежним регистрационным номером."),
        T("Crossing points are open in daylight only. Pilgrimages to Iyık Janyl for the Feast of St. Janyl are arranged each year through the Joint Liaison Committee of the United Nations Mission in Irad and do not require this pass.",
          "Ötkööl punkttarı kündüz gana achık. Iyık Janılga Iyık Janıl mayramına ziyarattar ar jılı Iraddagı BUU missiyasının Birgeleshken baylanısh komiteti arkıluu uyushturulat jana bul ötkörmönü talap kılbayt.",
          "Пункты пропуска открыты только в светлое время суток. Паломничество в Ийык-Джаныл на праздник Святой Джаныл ежегодно организуется через Совместный комитет связи Миссии ООН в Ираде и этого пропуска не требует."),
    ],
}


split_tables(FORMS)
