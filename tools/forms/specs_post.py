"""Forms: Irad Pochtasy (state post). Built here like the others; the PDFs are published on post.iradgov.org."""
from engine import T
from specs_people import STD_INS
from specs_other import NONE_INS, YES, NO, SIGN_OFF, short_person, split_tables

INK = "#0B6280"
MARK = "post"
RULES = "Postal Services Rules (Order of the Department of Infrastructure and Communications No. 18 of 2009)"
PRINT = "Supplied free of charge at post office counters."

COUNTER = T("Counter clerk (name)", "Kassachı (atı)", "Оператор (Ф.И.О.)")
OFFICE_STAMP = T("Date stamp of the office", "Bölümdün kalendardık möörü", "Календарный штемпель")
SENDER = T("Sender", "Jönötüüchü", "Отправитель")
ADDRESSEE = T("Addressee", "Aluuchu", "Получатель")
ADDR_LINE = T("Address: city or settlement, street, house, flat", "Darek: shaar je kalk konush, köchö, üy, batir", "Адрес: город или населённый пункт, улица, дом, квартира")
ITEM_NO = T("Item No.", "Jönötmönün No.", "№ отправления")
OFFICE_NO = T("Post office No.", "Pochta bölümünün No.", "№ отделения")

FORMS = {}

# ---------------------------------------------------------------- P-2
FORMS["P-2"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 03/2024", "printnote": PRINT,
    "subagency": "Talas Central Post Office · Pochtamt Street 2 · Talas",
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024; Customs Code of the ISEZ",
    "instructions": [
        T("Complete this form in Latin BLOCK CAPITALS in black or dark blue ink, in three copies: the first is attached to the item, the second is kept by the office of posting, the third travels with the dispatch list to ISEZ customs at the Chu Gate exchange.",
          "Bul formanı latın BASMA TAMGALARI menen kara je kara-kök siya menen üch nuskada tolturuñuz: birinchisi jönötmögö tirkelet, ekinchisi jönötkön bölümdö kalat, üchünchüsü jönötüü tizmesi menen Chüy darbazasındagı almashuu punktundagı IAEZ bajısına barat.",
          "Заполняйте латинскими ПЕЧАТНЫМИ БУКВАМИ чёрными или тёмно-синими чернилами в трёх экземплярах: первый прикрепляется к отправлению, второй остаётся в отделении приёма, третий следует с накладной в таможню ОЭЗИ в пункте обмена Чуйские ворота."),
        T("Items go abroad through the Kazakh postal service via Almaty under the bilateral arrangement and are subject to the customs rules of Kazakhstan and of the country of destination. Allow three to six weeks. Parcels of goods are not accepted for dispatch abroad: this declaration is completed for letters and small packets of printed matter or documents that contain anything other than written correspondence.",
          "Jönötmölör eki taraptuu kelishim boyuncha Kazakstan pochta kızmatı arkıluu Almatı aşa chet elge ketet jana Kazakstandın, oshondoy ele bara turgan ölkönün bajı erejelerine bagınat. Üch-altı juma kütüñüz. Tovar salıngan posılkalar chet elge kabıl alınbayt: bul deklaratsiya jazuu kattarınan bashka nerse salıngan kattar jana basma materialdar je dokumentter salıngan kichine banderoldor üchün tolturulat.",
          "Отправления уходят за рубеж через казахстанскую почтовую службу через Алматы по двустороннему соглашению и подчиняются таможенным правилам Казахстана и страны назначения. Срок — от трёх до шести недель. Посылки с товарами за рубеж не принимаются: декларация заполняется на письма и мелкие пакеты с печатными изданиями или документами, содержащие что-либо кроме письменной корреспонденции."),
        T("Bring the item to the counter unsealed. It is examined in your presence and closed by the counter clerk. Postage is paid at the counter and printed on a label: Irad Pochtasy stamps are not valid on mail abroad.",
          "Jönötmönü kassaga jabılbagan türdö alıp keliñiz. Al sizdin közüñüzchö tekshirilip, kassachı tarabınan jabılat. Akısı kassada tölönüp, etiketkaga basılat: Irad Pochtasının markaları chet elge pochtaga jaraktuu emes.",
          "Принесите отправление в окно незапечатанным. Оно проверяется в вашем присутствии и закрывается оператором. Оплата производится в окне и печатается на ярлыке: марки «Ирадпочты» на международной почте недействительны."),
        T("Irad Pochtasy is not liable for items detained or confiscated by the customs authorities of the ISEZ, Kazakhstan or the country of destination, nor for delays caused by customs examination. Enquiries about items sent abroad are made on Form P-15 not earlier than 30 days after posting.",
          "Irad Pochtası IAEZdin, Kazakstandın je bara turgan ölkönün bajı organdarı karmagan je kamakka algan jönötmölör üchün, oshondoy ele bajı tekshirüüsünön ulam bolgon kechigüülör üchün joop berbeyt. Chet elge jönötülgön jönötmölör boyuncha suroolor jönötkön kündön 30 kün ötkönsün P-15 forması menen berilet.",
          "«Ирадпочта» не отвечает за отправления, задержанные или конфискованные таможенными органами ОЭЗИ, Казахстана или страны назначения, и за задержки из-за таможенного досмотра. Розыск международных отправлений — по форме P-15 не ранее чем через 30 дней после приёма."),
        NONE_INS,
    ],
    "sections": [
        {"t": T("Sender", "Jönötüüchü", "Отправитель"), "rows": [
            {"k": "boxes", "l": "surname"},
            [{"k": "boxes", "l": "first", "w": 2.2}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.2}],
            [{"k": "line", "l": T("Address in the ISEZ: street, house, flat, city", "IAEZdegi dareki: köchö, üy, batir, shaar", "Адрес в ОЭЗИ: улица, дом, квартира, город"), "w": 2.2}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
        ]},
        {"t": T("Addressee abroad", "Chet eldegi aluuchu", "Получатель за рубежом"), "rows": [
            {"k": "line", "l": T("Name of the addressee (Latin letters)", "Aluuchunun atı (latın tamgaları menen)", "Имя получателя (латиницей)")},
            {"k": "area", "l": T("Address abroad in Latin letters: street, house, flat, city, postal code, region", "Chet eldegi darek latın tamgaları menen: köchö, üy, batir, shaar, pochta indeksi, oblus", "Адрес за рубежом латиницей: улица, дом, квартира, город, индекс, область"), "lines": 2},
            [{"k": "check", "l": T("Country of destination", "Bara turgan ölkö", "Страна назначения"), "opts": [T("Kazakhstan", "Kazakstan", "Казахстан"), T("Kyrgyzstan", "Kırgızstan", "Кыргызстан"), T("Uzbekistan", "Özbekstan", "Узбекистан"), T("Russia", "Orusiya", "Россия"), T("other", "bashka", "иная")], "cols": 5, "w": 2.6}, {"k": "line", "l": T("Other country", "Bashka ölkö", "Иная страна"), "w": .9}],
        ]},
        {"t": T("Item and contents", "Jönötmö jana anın ichindegisi", "Отправление и вложение"), "rows": [
            [{"k": "check", "l": T("Kind of item", "Jönötmönün türü", "Вид отправления"), "opts": [T("letter", "kat", "письмо"), T("small packet, printed matter", "banderol, basma", "пакет, печать"), T("small packet, documents", "banderol, dokument", "пакет, документы")], "cols": 3, "w": 2.6}, {"k": "boxes", "l": T("Gross weight (g)", "Jalpı salmagı (g)", "Вес брутто (г)"), "n": 4, "w": .9}],
            {"k": "check", "l": T("Category of item", "Jönötmönün kategoriyası", "Категория отправления"), "opts": [T("gift", "belek", "подарок"), T("documents", "dokumentter", "документы"), T("commercial sample", "soodalık ülgü", "образец"), T("returned goods", "kaytarılgan tovar", "возврат товара"), T("other (explain)", "bashka", "иное")], "cols": 5},
            {"k": "table", "l": T("Detailed description of contents (one line for each kind of article; general terms such as GIFT or SAMPLES are not accepted)", "Ichindegisinin toluk süröttölüshü (ar bir türgö bir sap; BELEK je ÜLGÜLÖR sıyaktuu jalpı sözdör kabıl alınbayt)", "Подробное описание вложения (строка на каждый вид предметов; общие слова «ПОДАРОК», «ОБРАЗЦЫ» не принимаются)"),
             "cols": [(T("Description of contents", "Ichindegisi", "Описание вложения"), 4), (T("Quantity", "Sanı", "Кол-во"), 1), (T("Net weight (g)", "Taza salmagı (g)", "Вес нетто (г)"), 1.2), (T("Value (som)", "Narkı (som)", "Стоимость (сом)"), 1.3), (T("Country of origin", "Chıkkan ölkösü", "Страна происхождения"), 1.6), (T("HS tariff No.", "TN VED kodu", "Код ТН ВЭД"), 1.5)], "rows": 5},
            [{"k": "boxes", "l": T("Total net weight (g)", "Jalpı taza salmagı (g)", "Общий вес нетто (г)"), "n": 5, "w": 1}, {"k": "money", "l": T("Total value", "Jalpı narkı", "Общая стоимость"), "n": 8, "w": 1.4, "note": T("The value is the price paid or, for gifts and documents, the replacement value in som. The 6-digit tariff number of the Harmonized System is required for commercial samples and returned goods; for gifts and documents write NONE. Items whose total value exceeds 2,000 som are presented with an export declaration at the Talas Customs Clearance Terminal before posting.",
                                                                                                                                                                                                                             "Nark — tölöngön baa je belek jana dokumentter üchün som menen almashtıruu narkı. Garmonizatsiyalangan sistemanın 6 sanaripten turgan tarifik nomeri soodalık ülgülör jana kaytarılgan tovarlar üchün talap kılınat; belek jana dokumentter üchün JOK dep jazıñız. Jalpı narkı 2000 somdon ashkan jönötmölör jönötüügö cheyin Talas bajı tarıktoo terminalında eksporttuk deklaratsiya menen körsötülöt.",
                                                                                                                                                                                                                             "Стоимость — уплаченная цена, для подарков и документов — восстановительная стоимость в сомах. Шестизначный код Гармонизированной системы обязателен для образцов и возвращаемых товаров; для подарков и документов пишите НЕТ. Отправления общей стоимостью свыше 2 000 сомов до приёма предъявляются с экспортной декларацией на Таласском таможенном терминале.")},
             {"k": "line", "l": T("Explanation (category OTHER)", "Tüshündürmö (BASHKA kategoriyası)", "Пояснение (категория «ИНОЕ»)"), "w": 1.4}],
            [{"k": "check", "l": T("Documents attached", "Tirkelgen dokumentter", "Прилагаемые документы"), "opts": [T("invoice", "esep-faktura", "счёт-фактура"), T("certificate of origin", "sertifikat", "сертификат"), T("export licence", "eksport litsenz.", "эксп. лицензия"), T("none", "jok", "нет")], "cols": 4, "w": 2.6}, {"k": "boxes", "l": T("Document No.", "Dokument No.", "№ документа"), "n": 8, "w": .9}],
            {"k": "check", "l": T("If the item cannot be delivered", "Jönötmö tapshırılbay kalsa", "При невозможности доставки"), "opts": [T("return to sender by the quickest route", "jönötüüchügö eñ tez jol menen kaytaruu", "вернуть кратчайшим путём"), T("return to sender by surface", "jönötüüchügö jer üstü jolu menen kaytaruu", "вернуть наземным путём"), T("treat as abandoned", "taştalgan dep eseptöö", "считать брошенным")], "cols": 3},
        ]},
    ],
    "declaration": T("I, the undersigned, whose name and address are given above, certify that the particulars given in this declaration are correct and that the item does not contain any article prohibited by the legislation of the ISEZ or by postal or customs regulations (see notes). I agree to the opening of the item for customs inspection and understand that the cost of returning an undeliverable item is charged to me.",
                     "Men, tömöndö kol koyuuchu, atım jana darekim jogoruda körsötülgön, bul deklaratsiyadagı maalımattın tuura ekenin jana jönötmödö IAEZdin myizamdarı je pochta jana bajı erejeleri menen tıyuu salıngan buyum jok ekenin tastıktaym (tüshündürmölördü karañız). Jönötmönü bajı tekshirüüsü üchün achuuga makulmun jana tapshırılbagan jönötmönü kaytaruu akısı menden alınarın tüshünöm.",
                     "Я, нижеподписавшийся, чьи имя и адрес указаны выше, удостоверяю, что сведения в декларации верны и что отправление не содержит предметов, запрещённых законодательством ОЭЗИ или почтовыми и таможенными правилами (см. примечания). Согласен на вскрытие отправления для таможенного досмотра; мне известно, что расходы по возврату недоставленного отправления взимаются с меня."),
    "signs": [T("Signature of the sender", "Jönötüüchünün kolu", "Подпись отправителя"), "date"],
    "official": [
        [{"k": "boxes", "l": ITEM_NO, "n": 13, "w": 1.5}, {"k": "money", "l": T("Postage paid", "Tölöngön akı", "Оплачено"), "n": 6, "w": 1.1}, {"k": "line", "l": COUNTER, "w": 1.2}],
        [{"k": "check", "l": T("Customs, Chu Gate exchange", "Bajı, Chüy darbazası almashuu punktu", "Таможня, пункт обмена Чуйские ворота"), "opts": [T("released without opening", "achılbay ötkörüldü", "выпущено без вскрытия"), T("opened and released", "achılıp ötkörüldü", "вскрыто и выпущено"), T("detained (act No.)", "karmaldı (akt No.)", "задержано (акт №)")], "cols": 3, "w": 3}, {"k": "boxes", "l": T("Customs seal No.", "Bajı plombası No.", "№ таможенной пломбы"), "n": 7, "w": 1}],
        {"k": "sign", "l": [T("Customs officer", "Bajı kızmatkeri", "Должностное лицо таможни"), SIGN_OFF], },
    ],
    "notes": [
        T("Prohibited in items sent abroad: som banknotes and coins and foreign currency, cheques and securities; precious metals and stones and articles made of them; weapons, their parts, ammunition and explosives; narcotic and psychotropic substances; medicines without a prescription and an export permit; ephedra and other plants, seeds and herbal preparations; foodstuffs and perishable goods; live animals, skins, horns and hunting trophies; cultural valuables without an export certificate; topographic maps at a scale larger than 1:100,000; printed matter not registered with the Department of Public Information.",
          "Chet elge jönötülgön jönötmölördö tıyuu salınat: som banknottoruna jana tıyındarına, chet el valyutasına, chekterge jana baalu kagazdarga; baalu metaldarga jana tashtarga, alardan jasalgan buyumdarga; kuralga, anın bölüktörünö, ok-darıga jana jarılguuchu zattarga; narkotikalık jana psikhotroptuk zattarga; retseptsiz jana eksport uruksatısız darılarga; chakandaga jana bashka ösümdüktörgö, urukhtarga jana chöp darılarga; azık-tülükkö jana tez buzuluuchu tovarlarga; tirüü janıbarlarga, terilerge, müyüzdörgö jana añchılık oljolorgo; eksport kuböölügü jok madaniy baalıktarga; 1:100 000den iri masshtabdagı topografiyalık kartalarga; Kogomduk maalımat departamentinde kattalbagan basma materialdarga.",
          "В международных отправлениях запрещены: банкноты и монеты сома и иностранная валюта, чеки и ценные бумаги; драгоценные металлы и камни и изделия из них; оружие, его части, боеприпасы и взрывчатые вещества; наркотические и психотропные вещества; лекарства без рецепта и разрешения на вывоз; эфедра и другие растения, семена и травяные сборы; продукты питания и скоропортящиеся товары; живые животные, шкуры, рога и охотничьи трофеи; культурные ценности без свидетельства на вывоз; топографические карты масштаба крупнее 1:100 000; печатные издания, не зарегистрированные в Департаменте общественной информации."),
    ],
}

# ---------------------------------------------------------------- P-4
FORMS["P-4"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 03/2024", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024 under the " + RULES,
    "sections": [
        {"t": T("Sender, addressee and parcel", "Jönötüüchü, aluuchu jana posılka", "Отправитель, получатель и посылка"), "rows": [
            [{"k": "line", "l": T("Sender: surname, first name, patronymic", "Jönötüüchü: familiyası, atı, atasının atı", "Отправитель: фамилия, имя, отчество"), "w": 2.1}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
            {"k": "line", "l": T("Sender's address: city or settlement, street, house, flat", "Jönötüüchünün dareki: shaar je kalk konush, köchö, üy, batir", "Адрес отправителя: город или населённый пункт, улица, дом, квартира")},
            [{"k": "line", "l": T("Addressee: surname, first name, patronymic", "Aluuchu: familiyası, atı, atasının atı", "Получатель: фамилия, имя, отчество"), "w": 2.1}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
            [{"k": "line", "l": T("Addressee's address: city or settlement, street, house, flat", "Aluuchunun dareki: shaar je kalk konush, köchö, üy, batir", "Адрес получателя: город или населённый пункт, улица, дом, квартира"), "w": 2.6}, {"k": "boxes", "l": T("Office of destination No.", "Bara turgan bölüm No.", "№ отделения назначения"), "n": 3, "w": .8}],
            [{"k": "boxes", "l": T("Weight (kg, g)", "Salmagı (kg, g)", "Вес (кг, г)"), "n": 5, "w": .9}, {"k": "money", "l": T("Declared value", "Jarıyalangan baa", "Объявленная ценность"), "n": 7, "w": 1.3},
             {"k": "money", "l": T("Cash on delivery", "Tapshıruuda tölöö", "Наложенный платёж"), "n": 7, "w": 1.3}],
            [{"k": "line", "l": T("Contents (write in full; no prohibited or dangerous articles)", "Ichindegisi (toluk jazıñız; tıyuu salıngan je korkunuchtuu buyumdar jok)", "Вложение (подробно; без запрещённых и опасных предметов)"), "w": 2.2},
             {"k": "check", "l": T("Delivery", "Jetkirüü", "Доставка"), "opts": [T("collect at office", "bölümdön aluu", "в отделении"), T("to the home", "üygö", "на дом")], "cols": 2, "w": 1.2}],
        ]},
    ],
    "declaration": T("I confirm that the parcel contains no articles prohibited for posting (weapons, ammunition, narcotics, flammable, toxic or perishable substances, money) and that the contents correspond to the description above. Declared value is charged at 1 som per 100 som; cash on delivery may not exceed it and is remitted to me by money order less the fee.",
                     "Posılkada pochta menen jönötüügö tıyuu salıngan buyumdar (kural, ok-darı, narkotikter, tez tutanuuchu, uuluu je tez buzuluuchu zattar, akcha) jok ekenin jana ichindegisi jogorudagı süröttölüshkö tuura kelerin tastıktaym. Jarıyalangan baa üchün ar 100 somgo 1 som alınat; tapshıruuda tölönüüchü summa andan ashpayt jana maga akısı karmalıp akcha kotoruu menen jiberilet.",
                     "Подтверждаю, что в посылке нет предметов, запрещённых к пересылке (оружие, боеприпасы, наркотики, легковоспламеняющиеся, ядовитые и скоропортящиеся вещества, деньги), и что вложение соответствует описанию. Объявленная ценность оплачивается по 1 сому за 100 сомов; наложенный платёж не может её превышать и переводится мне почтовым переводом за вычетом платы."),
    "signs": [T("Signature of the sender", "Jönötüüchünün kolu", "Подпись отправителя"), "date"],
    "official": [
        [{"k": "boxes", "l": T("Item No. (IP...)", "Jönötmö No. (IP...)", "№ отправления (IP...)"), "n": 10, "w": 1.3}, {"k": "money", "l": T("Postage and fees", "Akı jana jıyımdar", "Плата за пересылку"), "n": 6, "w": 1.1}, {"k": "line", "l": COUNTER, "w": 1.2}],
    ],
    "counterfoil": {"t": T("Coupon kept by the sender: needed for an enquiry", "Jönötüüchüdö kala turgan talon: suroo üchün kerek", "Талон, остающийся у отправителя: нужен для розыска"), "rows": [
        [{"k": "boxes", "l": T("Item No. (IP...)", "Jönötmö No. (IP...)", "№ отправления (IP...)"), "n": 10, "w": 1.3}, {"k": "line", "l": T("Addressee", "Aluuchu", "Получатель"), "w": 1.5}, {"k": "money", "l": T("Declared value", "Jarıyalangan baa", "Объявл. ценность"), "n": 6, "w": 1.2}, {"k": "date", "l": T("Date of posting", "Jönötülgön kün", "Дата приёма"), "w": 1}],
    ]},
}

# ---------------------------------------------------------------- P-11
FORMS["P-11"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 10/2026", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024 (as amended 2026)",
    "sections": [
        {"t": T("Amount, sender and recipient", "Summa, jönötüüchü jana aluuchu", "Сумма, отправитель и получатель"), "rows": [
            [{"k": "money", "l": T("Amount in figures", "Summa sanarip menen", "Сумма цифрами"), "n": 7, "w": 1.15}, {"k": "line", "l": T("Amount in words (som in words, tyiyn in figures)", "Summa jazuu menen (som jazuu menen, tıyın sanarip menen)", "Сумма прописью (сомы прописью, тыйыны цифрами)"), "w": 2.4}],
            [{"k": "line", "l": T("Sender: surname, first name, patronymic", "Jönötüüchü: familiyası, atı, atasının atı", "Отправитель: фамилия, имя, отчество"), "w": 2.2}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.2}],
            [{"k": "line", "l": T("Recipient: surname, first name, patronymic", "Aluuchu: familiyası, atı, atasının atı", "Получатель: фамилия, имя, отчество"), "w": 2.2}, {"k": "check", "l": T("Payment", "Tölöm", "Выплата"), "opts": [T("at the office", "bölümdö", "в отделении"), T("to the home", "üygö", "на дом")], "cols": 2, "w": 1.2}],
            [{"k": "line", "l": T("Recipient's address: city or settlement, street, house, flat", "Aluuchunun dareki: shaar je kalk konush, köchö, üy, batir", "Адрес получателя: город или населённый пункт, улица, дом, квартира"), "w": 2.6}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .8}],
        ]},
        {"t": T("Coupon for the recipient (cut off on payment)", "Aluuchuga talon (tölöndö kesilet)", "Отрезной талон получателю"), "rows": [
            [{"k": "line", "l": T("From: sender's name and address", "Kimden: jönötüüchünün atı jana dareki", "От кого: имя и адрес отправителя"), "w": 2.4}, {"k": "money", "l": T("Amount", "Summa", "Сумма"), "n": 7, "w": 1.15}],
            {"k": "area", "l": T("Message to the recipient (not more than 20 words; no abbreviations or figures in place of words)", "Aluuchuga bildirüü (20 sözdön ashpayt; kıskartuular je söz ordunda sanarip jok)", "Сообщение получателю (не более 20 слов; без сокращений и цифр вместо слов)"), "lines": 1},
        ]},
    ],
    "declaration": T("I confirm the particulars of this order. Fee 1.5% of the amount, at least 5 som; home delivery 10 som. Paid in cash at the counter or to a bank account only (Bank of Irad notice 2026/5).",
                     "Kotoruunun maalımatın tastıktaym. Akısı summanın 1,5%ı, keminde 5 som; üygö jetkirüü 10 som. Kassada nak akcha menen je bank esebine gana tölönöt (Irad Bankının 2026/5 bildirmesi).",
                     "Подтверждаю данные перевода. Плата 1,5% суммы, не менее 5 сомов; доставка на дом 10 сомов. Выплата только наличными в окне или на банковский счёт (уведомление Банка Ирада 2026/5)."),
    "signs": [T("Signature of the sender", "Jönötüüchünün kolu", "Подпись отправителя"), T("Paid: signature of the recipient", "Tölöndü: aluuchunun kolu", "Выплачено: подпись получателя")],
    "official": [
        [{"k": "boxes", "l": T("Order No.", "Kotoruu No.", "№ перевода"), "n": 8, "w": 1.1}, {"k": "money", "l": T("Fee", "Akısı", "Плата"), "n": 5, "w": 1}, {"k": "line", "l": T("Recipient's ID card (series, No.)", "Aluuchunun jeke kuböölügü (seriyası, No.)", "Удостоверение получателя (серия, №)"), "w": 1.3}, {"k": "line", "l": COUNTER, "w": 1}],
    ],
    "counterfoil": {"t": T("Receipt for the sender", "Jönötüüchügö tilkat", "Квитанция отправителю"), "rows": [
        [{"k": "boxes", "l": T("Order No.", "Kotoruu No.", "№ перевода"), "n": 8, "w": 1.1}, {"k": "money", "l": T("Amount", "Summa", "Сумма"), "n": 7, "w": 1.25}, {"k": "money", "l": T("Fee", "Akısı", "Плата"), "n": 5, "w": 1}, {"k": "line", "l": T("Recipient", "Aluuchu", "Получатель"), "w": 1.2}],
    ]},
}

# ---------------------------------------------------------------- P-15
FORMS["P-15"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 03/2024", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024 under the " + RULES,
    "to": T("Head of the post office, for the Enquiries Section, Talas Central Post Office", "Pochta bölümünün bashchısına, Talas borborduk pochtasının Izdöö bölümü üchün", "Начальнику отделения связи для отдела розыска Таласского центрального почтамта"),
    "instructions": [STD_INS[0], NONE_INS,
        T("An enquiry is lodged at any post office by the sender, the addressee or a person holding a power of attorney (Form P-27), within 6 months of the day after posting. Attach the original receipt or coupon; the office makes a copy and returns the original.",
          "Suroonu jönötkön kündün ertesinen tartıp 6 aydın ichinde jönötüüchü, aluuchu je ışenim katı bar adam (P-27 forması) kaalagan pochta bölümünö beret. Tilkattın je talondun originalın tirkeñiz; bölüm köchürmösün alıp, originalın kaytarat.",
          "Заявление о розыске подаётся в любое отделение отправителем, получателем или лицом по доверенности (форма P-27) в течение 6 месяцев со дня, следующего за днём приёма. Приложите подлинник квитанции или талона; отделение снимает копию и возвращает подлинник."),
        T("The result is notified within 30 days for items within Irad and within 90 days for items sent abroad or received from abroad, which are traced through the Kazakh postal service.",
          "Natıyjesi Irad ichindegi jönötmölör boyuncha 30 kündün ichinde, chet elge jönötülgön je chet elden kelgen jönötmölör boyuncha, alar Kazakstan pochta kızmatı arkıluu izdelgendikten, 90 kündün ichinde kabarlanat.",
          "О результате сообщается в течение 30 дней по отправлениям внутри Ирада и в течение 90 дней по международным отправлениям, розыск которых ведётся через казахстанскую почтовую службу."),
    ],
    "sections": [
        {"t": T("Applicant", "Arız beruuchu", "Заявитель"), "rows": [
            {"k": "boxes", "l": "surname"},
            [{"k": "boxes", "l": "first", "w": 2.2}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.2}],
            [{"k": "line", "l": ADDR_LINE, "w": 2.2}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
            {"k": "check", "l": T("The applicant is", "Arız beruuchu", "Заявитель является"), "opts": [T("the sender", "jönötüüchü", "отправителем"), T("the addressee", "aluuchu", "получателем"), T("an attorney (Form P-27 attached)", "ışenimdüü adam (P-27 tirkelgen)", "доверенным лицом (P-27)")], "cols": 3},
        ]},
        {"t": T("The item", "Jönötmö", "Отправление"), "rows": [
            {"k": "check", "l": T("Kind of item", "Jönötmönün türü", "Вид отправления"), "opts": [
                T("registered letter", "buyurtma kat", "заказное письмо"), T("small packet", "banderol", "бандероль"), T("parcel", "posılka", "посылка"),
                T("item with declared value", "jarıyalangan baası bar", "с объявленной ценностью"), T("cash-on-delivery item", "tapshıruuda tölönüüchü", "с наложенным платежом"), T("money order", "akcha kotoruu", "почтовый перевод"),
                T("item sent abroad", "chet elge jönötülgön", "отправлено за рубеж"), T("item received from abroad", "chet elden kelgen", "получено из-за рубежа"), T("advice of delivery", "tapshıruu bildirmesi", "уведомление о вручении"),
            ], "cols": 3},
            [{"k": "boxes", "l": T("Item or order No. (e.g. IP12345678, RA123456789KZ)", "Jönötmö je kotoruu No. (mısalı IP12345678, RA123456789KZ)", "№ отправления или перевода (напр. IP12345678, RA123456789KZ)"), "n": 13, "w": 1.9}, {"k": "date", "l": T("Date of posting", "Jönötülgön kün", "Дата приёма"), "w": 1}],
            [{"k": "line", "l": T("Office of posting (name, or country if posted abroad)", "Jönötkön bölüm (atı, chet elde bolso ölkösü)", "Отделение приёма (название или страна, если за рубежом)"), "w": 2.4}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .8}],
            [{"k": "line", "l": T("Sender: name and full address", "Jönötüüchü: atı jana toluk dareki", "Отправитель: имя и полный адрес"), "w": 1}, {"k": "line", "l": T("Addressee: name and full address", "Aluuchu: atı jana toluk dareki", "Получатель: имя и полный адрес"), "w": 1}],
            [{"k": "boxes", "l": T("Weight (kg, g)", "Salmagı (kg, g)", "Вес (кг, г)"), "n": 5, "w": .8}, {"k": "money", "l": T("Declared value", "Jarıyalangan baa", "Объявленная ценность"), "n": 7, "w": 1.2}, {"k": "money", "l": T("Cash on delivery / order amount", "Tapshıruuda tölöö / kotoruu summası", "Наложенный платёж / сумма перевода"), "n": 7, "w": 1.2}],
            {"k": "area", "l": T("Contents and packing (describe the wrapping, the inscriptions on it, and every article inside with its value)", "Ichindegisi jana orolushu (orogon nersesin, andagı jazuularrdı jana ichindegi ar bir buyumdu narkı menen süröttöñüz)", "Вложение и упаковка (опишите упаковку, надписи на ней и каждый предмет вложения с его стоимостью)"), "lines": 3},
        ]},
        {"t": T("Grounds for the enquiry", "Suroonun negizi", "Основание розыска"), "rows": [
            {"k": "check", "l": T("What happened", "Emne boldu", "Что произошло"), "opts": [
                T("not received at all", "takır kelgen jok", "не получено совсем"), T("received damaged", "buzulup keldi", "получено повреждённым"), T("contents missing in part", "ichindegisinin bir bölügü jok", "недостача вложения"),
                T("delayed beyond the standard time", "möönötünön kechigip jatat", "задержано сверх срока"), T("handed to a wrong person", "bashka adamga berildi", "вручено другому лицу"), T("COD amount not received", "tapshıruudagı tölöm kelgen jok", "наложенный платёж не получен"),
            ], "cols": 3},
            {"k": "area", "l": T("Circumstances (dates, what the addressee was told, notices received)", "Jagday (kündör, aluuchuga emne aytılgan, alıngan bildirmeler)", "Обстоятельства (даты, что сообщили получателю, полученные извещения)"), "lines": 3},
            [{"k": "check", "l": T("Attached", "Tirkelgen", "Прилагается"), "opts": [T("original receipt or coupon", "tilkat je talon", "квитанция или талон"), T("copy of customs declaration P-2", "P-2 köchürmösü", "копия декларации P-2"), T("damage report of the office", "bölümdün buzuluu aktısı", "акт о повреждении")], "cols": 3, "w": 3},
             {"k": "check", "l": T("Reply", "Joop", "Ответ"), "opts": [T("by post", "pochta menen", "почтой"), T("at the office", "bölümdö", "в отделении")], "cols": 2, "w": 1.2}],
        ]},
    ],
    "declaration": T("I confirm that the information given is true. I understand that compensation is paid only to the sender, or to the addressee if the sender has assigned the right in writing, and that an enquiry about the same item may not be lodged twice.",
                     "Berilgen maalımattın tuura ekenin tastıktaym. Tölöm jönötüüchügö gana, je jönötüüchü ukugun jazuu jüzündö bergen bolso aluuchuga tölönörün jana bir jönötmö boyuncha suroo eki jolu berilbestigin tüshünöm.",
                     "Подтверждаю достоверность сведений. Мне известно, что возмещение выплачивается только отправителю или получателю, если отправитель письменно уступил ему право, и что повторное заявление о розыске того же отправления не принимается."),
    "official": [
        [{"k": "boxes", "l": T("Enquiry No.", "Suroo No.", "№ розыска"), "n": 8, "w": 1.1}, {"k": "date", "l": T("Date received", "Kabıl alıngan kün", "Дата приёма"), "w": 1}, {"k": "date", "l": T("Reply due by", "Joop möönötü", "Срок ответа"), "w": 1}],
        [{"k": "check", "l": T("Result", "Natıyjesi", "Результат"), "opts": [T("found and delivered", "tabılıp tapshırıldı", "найдено и вручено"), T("compensation paid", "tölöm tölöndü", "возмещение выплачено"), T("not found / no liability", "tabılgan jok", "не найдено")], "cols": 3, "w": 2.8}, {"k": "money", "l": T("Compensation", "Tölöm", "Возмещение"), "n": 7, "w": 1.2}],
        {"k": "sign", "l": [T("Head of the post office", "Pochta bölümünün bashchısı", "Начальник отделения"), SIGN_OFF], },
    ],
    "counterfoil": {"t": T("Receipt for an enquiry about a missing item", "Jogolgon jönötmö boyuncha suroonu kabıl alganı tuuraluu tilkat", "Квитанция в приёме заявления о розыске"), "rows": [
        [{"k": "boxes", "l": T("Enquiry No.", "Suroo No.", "№ розыска"), "n": 8, "w": 1.1}, {"k": "boxes", "l": ITEM_NO, "n": 13, "w": 1.7}, {"k": "date", "l": T("Date received", "Kabıl alıngan kün", "Дата приёма"), "w": 1}, {"k": "line", "l": COUNTER, "w": 1.1}],
    ]},
    "notes": [
        T("Compensation under the Postal Services Rules: for a lost registered item without declared value, twice the postage paid; for a lost item with declared value, the declared value and the postage; for partial loss or damage, the part of the declared value corresponding to the loss. Money orders not paid are refunded in full with the fee.",
          "Pochta kızmattarının erejeleri boyuncha tölöm: jarıyalangan baasız jogolgon buyurtma jönötmö üchün — tölöngön akının eki eselengen summası; jarıyalangan baası bar jogolgon jönötmö üchün — jarıyalangan baa jana akı; bölükchö jogoluu je buzuluu üchün — jogotuuga tuura kelgen jarıyalangan baanın bölügü. Tölönbögön akcha kotoruular akısı menen kosho toluk kaytarılat.",
          "Возмещение по Правилам оказания почтовых услуг: за утрату заказного отправления без объявленной ценности — двукратная плата за пересылку; за утрату отправления с объявленной ценностью — объявленная ценность и плата за пересылку; за частичную утрату или повреждение — часть объявленной ценности, соответствующая ущербу. Невыплаченные переводы возвращаются полностью вместе с платой."),
        T("Irad Pochtasy is not liable for ordinary (unregistered) letters and postcards, for items confiscated under the law, or for items sent abroad after they have been handed to the Kazakh postal service, beyond the compensation that service pays.",
          "Irad Pochtası jönököy (buyurtma emes) kattar jana otkrıtkalar, mıyzam boyuncha kamakka alıngan jönötmölör, oshondoy ele chet elge jönötülgön jönötmölör Kazakstan pochta kızmatına berilgenden kiyin, al kızmat tölögön tölömdön tıshkarı joop berbeyt.",
          "«Ирадпочта» не отвечает за простые (незаказные) письма и открытки, за отправления, конфискованные по закону, и за международные отправления после их передачи казахстанской почтовой службе сверх возмещения, выплачиваемого этой службой."),
    ],
}

# ---------------------------------------------------------------- P-21
MONTHS = [("Jan", "Yan", "янв"), ("Feb", "Fev", "фев"), ("Mar", "Mar", "мар"), ("Apr", "Apr", "апр"), ("May", "May", "май"), ("Jun", "Iyun", "июн"),
          ("Jul", "Iyul", "июл"), ("Aug", "Avg", "авг"), ("Sep", "Sen", "сен"), ("Oct", "Okt", "окт"), ("Nov", "Noy", "ноя"), ("Dec", "Dek", "дек")]

FORMS["P-21"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 10/2026", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 112 of 6 October 2026 (subscription campaign 2027)",
    "instructions": [STD_INS[0], NONE_INS,
        T("The 2027 subscription campaign opens on 1 November. Subscribe at any post office by 15 December for delivery from January; during the year, by the 20th of a month for delivery from the following month. Mark with a cross every month for which the title is ordered.",
          "2027-jılkı jazıluu kampaniyası 1-noyabrda achılat. Yanvardan tartıp jetkirüü üchün kaalagan pochta bölümündö 15-dekabrga cheyin jazılıñız; jıl ichinde — kiyinki aydan tartıp jetkirüü üchün aydın 20-kününö cheyin. Basılma buyurtma kılıngan ar bir aydı kayçılash menen belgileñiz.",
          "Подписная кампания на 2027 год открывается 1 ноября. Подпишитесь в любом отделении до 15 декабря для доставки с января; в течение года — до 20-го числа для доставки со следующего месяца. Отметьте крестом каждый месяц подписки."),
        T("Prices for 2027 (delivery to the home or a post-office box included): Talas Herald, index 70011, 45 som a month; Jarchy, index 70014, 12 som a month; Vecherniy Nurzhan, index 70017, 14 som a month; TSU Bulletin, index 70021, 60 som a year; Tartip, index 70025, 25 som a year. The TSU Bulletin and Tartip are subscribed for the whole year only.",
          "2027-jılga bahalar (üygö je pochta yashıgına jetkirüü bahaga kirgen): Talas Jarchısı, indeksi 70011, ayına 45 som; Jarchı, indeksi 70014, ayına 12 som; Vecherniy Nurzhan, indeksi 70017, ayına 14 som; TMU Kabarları, indeksi 70021, jılına 60 som; Tartip, indeksi 70025, jılına 25 som. TMU Kabarlarına jana Tartipke bir jılga gana jazılat.",
          "Цены на 2027 год (доставка на дом или в абонентский ящик включена): Talas Herald, индекс 70011, 45 сомов в месяц; «Джарчы», индекс 70014, 12 сомов в месяц; «Вечерний Нуржан», индекс 70017, 14 сомов в месяц; «Вестник ТГУ», индекс 70021, 60 сомов в год; «Тартип», индекс 70025, 25 сомов в год. На «Вестник ТГУ» и «Тартип» подписка только на весь год."),
    ],
    "sections": [
        {"t": T("Subscriber and delivery address", "Jazıluuchu jana jetkirüü dareki", "Подписчик и адрес доставки"), "rows": [
            {"k": "boxes", "l": "surname"},
            [{"k": "boxes", "l": "first", "w": 2.2}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
            {"k": "check", "l": T("Delivery", "Jetkirüü", "Доставка"), "opts": [T("to the home address", "üy darekine", "на домашний адрес"), T("to a post-office box", "pochta yashıgına", "в абонентский ящик"), T("to an organisation (office address)", "uyumga (keñse dareki)", "в организацию (адрес офиса)")], "cols": 3},
            [{"k": "boxes", "l": "city", "w": 1.4}, {"k": "boxes", "l": T("PO box No.", "Pochta yashıgı No.", "№ а/я"), "n": 5, "w": .6}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .5}],
            [{"k": "boxes", "l": "street", "w": 2.6}, {"k": "boxes", "l": "house", "n": 4, "w": .5}, {"k": "boxes", "l": "flat", "n": 4, "w": .5}],
        ]},
        {"t": T("Titles and months", "Basılmalar jana aylar", "Издания и месяцы"), "rows": [
            {"k": "table", "l": T("Mark each month ordered with X. One line per title.", "Buyurtma kılıngan ar bir aydı X menen belgileñiz. Ar bir basılmaga bir sap.", "Отметьте каждый месяц знаком X. Одна строка на издание."), "numbered": False,
             "cols": [(T("Index", "Indeksi", "Индекс"), 1.3), (T("Title", "Ataluusu", "Издание"), 3.2)] + [(T(m[0], m[1], m[2]), .56) for m in MONTHS] + [(T("Copies", "Nuska", "Экз."), .8), (T("Cost, som", "Baası, som", "Сумма, сом"), 1.2)], "rows": 5},
            [{"k": "money", "l": T("Total to pay", "Bardıgı tölönö turgan", "Всего к оплате"), "n": 7, "w": 1.3}, {"k": "line", "l": T("Total in words", "Bardıgı jazuu menen", "Всего прописью"), "w": 2.2}],
        ]},
    ],
    "declaration": T("I order the titles above for the months marked and pay the whole amount in advance. I understand that a subscription is not cancelled and the amount is not refunded, except on the death of the subscriber or when the publisher stops publication, and that issues not delivered through the fault of the post are delivered later or refunded.",
                     "Jogorudagı basılmalardı belgilengen aylarga buyurtma kılam jana bardık summanı aldın ala tölöym. Jazıluu jokko chıgarılbastıgın jana summa kaytarılbastıgın, jazıluuchu kaytıs bolgondo je basmakana chıgaruunu toktotkondo gana kaytarıların, pochtanın kesirinen jetkirilbegen sandar kiyinchireek jetkirilerin je akısı kaytarıların tüshünöm.",
                     "Заказываю указанные издания на отмеченные месяцы и оплачиваю всю сумму вперёд. Мне известно, что подписка не аннулируется и деньги не возвращаются, кроме случаев смерти подписчика или прекращения выпуска издателем, и что номера, не доставленные по вине почты, доставляются позднее или их стоимость возвращается."),
    "signs": [T("Signature of the subscriber", "Jazıluuchunun kolu", "Подпись подписчика"), "date"],
    "official": [
        [{"k": "boxes", "l": T("Receipt No.", "Tilkat No.", "№ квитанции"), "n": 8, "w": 1.1}, {"k": "boxes", "l": T("Delivery round No.", "Jetkirüü uchastogu No.", "№ доставочного участка"), "n": 3, "w": .9}, {"k": "money", "l": T("Amount received", "Kabıl alıngan summa", "Принято"), "n": 7, "w": 1.25}, {"k": "line", "l": COUNTER, "w": 1}],
    ],
    "counterfoil": {"t": T("Subscription receipt (kept by the subscriber)", "Jazıluu tilkatı (jazıluuchuda kalat)", "Абонемент (остаётся у подписчика)"), "rows": [
        [{"k": "line", "l": T("Subscriber", "Jazıluuchu", "Подписчик"), "w": 1.4}, {"k": "line", "l": T("Indices and months", "Indeksteri jana aylar", "Индексы и месяцы"), "w": 1.6}, {"k": "money", "l": T("Amount paid", "Tölöngön summa", "Оплачено"), "n": 6, "w": 1.25}, {"k": "date", "l": "date", "w": 1}],
    ]},
    "notes": [
        T("Complaints about non-delivery are made at the post office of delivery within 10 days of the date of the missing issue. Other publications registered with the Department of Public Information may be added to the catalogue at the publisher's request; the Irad Pochtasy catalogue lists only titles accepted for 2027.",
          "Jetkirilbegendik tuuraluu dattanuular jetpey kalgan sandın kününön tartıp 10 kündün ichinde jetkirüüchü pochta bölümünö berilet. Kogomduk maalımat departamentinde kattalgan bashka basılmalar basmakananın suranıchı boyuncha kataloggo koshuluşu mümkün; Irad Pochtasının katalogunda 2027-jılga kabıl alıngan basılmalar gana bar.",
          "Жалобы на недоставку подаются в отделение доставки в течение 10 дней с даты недоставленного номера. Другие издания, зарегистрированные в Департаменте общественной информации, могут быть включены в каталог по заявке издателя; в каталоге «Ирадпочты» только издания, принятые на 2027 год."),
    ],
}

# ---------------------------------------------------------------- P-27
FORMS["P-27"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 03/2024", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024, agreed with the Social Fund of the ISEZ",
    "instructions": [STD_INS[0], STD_INS[1], NONE_INS,
        T("The power of attorney is completed in one copy and kept by the post office that serves the principal's address; the attorney shows it with his or her own identity card at each collection. It is not valid without certification in Section E.",
          "Ishenim kat bir nuskada tolturulup, ışenim beruuchunun darekin teyleegen pochta bölümündö saktalat; ışenimdüü adam ar bir aluuda anı öz jeke kuböölügü menen körsötöt. Al E bölümündö tastıktalbasa jaraksız.",
          "Доверенность заполняется в одном экземпляре и хранится в отделении, обслуживающем адрес доверителя; доверенное лицо предъявляет её с собственным удостоверением при каждом получении. Без удостоверения в разделе E доверенность недействительна."),
    ],
    "sections": [
        dict(short_person(T("Principal (the person giving the power)", "Ishenim beruuchu", "Доверитель")), rows=short_person(None)["rows"] + [
            [{"k": "line", "l": ADDR_LINE, "w": 2.6}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .8}]]),
        dict(short_person(T("Attorney (the person authorised to collect)", "Ishenimdüü adam (aluuga ıygarım berilgen)", "Доверенное лицо (уполномоченный на получение)")), rows=short_person(None)["rows"] + [
            [{"k": "line", "l": ADDR_LINE, "w": 2.4}, {"k": "line", "l": T("Specimen signature of the attorney", "Ishenimdüü adamdın kolunun ülgüsü", "Образец подписи доверенного лица"), "w": 1}]]),
        {"t": T("Scope and validity", "Ichimdik jana möönötü", "Объём полномочий и срок"), "rows": [
            {"k": "check", "l": T("I authorise the attorney to receive for me, to sign for and to give receipts for", "Ishenimdüü adamga menin atımdan aluuga jana kol koyuuga ıygarım berem", "Уполномочиваю получать за меня и расписываться за"), "opts": [
                T("registered letters and small packets", "buyurtma kattar jana banderoldor", "заказные письма и бандероли"), T("parcels", "posılkalar", "посылки"),
                T("items with declared value and COD items", "baası jarıyalangan jönötmölör", "с объявл. ценностью и налож. платежом"), T("money orders", "akcha kotoruular", "почтовые переводы"),
                T("pensions and allowances paid by the Social Fund", "Sotsialdık fond tölögön pensiyalar jana jöölökpuldar", "пенсии и пособия Социального фонда"), T("mail held for collection and from a post-office box", "saktalgan pochta jana pochta yashıgınan", "почту до востребования и из а/я"),
            ], "cols": 2},
            [{"k": "boxes", "l": T("Pension book or allowance certificate No.", "Pensiya kitepchesinin je jöölökpul kuböölügünün No.", "№ пенсионной книжки или удостоверения на пособие"), "n": 10, "w": 1.5}, {"k": "line", "l": T("Paying office of the Social Fund (district)", "Sotsialdık fonddun tölööchü bölümü (aymak)", "Выплачивающий отдел Социального фонда (район)"), "w": 1.6}],
            [{"k": "date", "l": T("Valid from", "Küchünö kirgen kün", "Действует с"), "w": 1}, {"k": "date", "l": T("Valid until (not more than 1 year)", "Möönötü (1 jıldan ashpayt)", "Действует по (не более 1 года)"), "w": 1.1}, {"k": "check", "l": T("Substitution", "Bashkaga berüü", "Передоверие"), "opts": [T("not permitted", "uruksat jok", "не допускается")], "cols": 1, "w": .9}],
            [{"k": "line", "l": T("Signature of the principal", "Ishenim beruuchunun kolu", "Подпись доверителя"), "w": 1.6}, {"k": "date", "l": "date", "w": 1}],
        ]},
        {"t": T("Certification of the principal's signature", "Ishenim beruuchunun kolun tastıktoo", "Удостоверение подписи доверителя"), "rows": [
            {"k": "check", "l": T("The signature is certified by", "Koldu tastıktagan", "Подпись удостоверена"), "opts": [
                T("a notary", "notarius", "нотариусом"), T("the head of the post office (principal present, ID shown)", "pochta bölümünün bashchısı (ışenim beruuchu katıshıp, kuböölük körsötüldü)", "начальником отделения (доверитель присутствовал)"),
                T("the director of a hospital or care home (for pensioners staying there)", "oorukananın je karıyalar üyünün direktoru (anda jatkan pensionerler üchün)", "директором больницы или дома престарелых (для пенсионеров)"),
            ], "cols": 1},
            [{"k": "line", "l": T("Notary office or institution, address", "Notariallık keñse je mekeme, dareki", "Нотариальная контора или учреждение, адрес"), "w": 2.2}, {"k": "boxes", "l": T("Register entry No.", "Reestrdegi jazuu No.", "№ по реестру"), "n": 8, "w": 1.2}],
            {"k": "text", "t": T("I certify that the power of attorney was signed in my presence by the principal named in Section A, whose identity has been established from the identity card.",
                                 "Ishenim kattın A bölümündö atalgan, inyıktıgı jeke kuböölük boyuncha anıktalgan ışenim beruuchu tarabınan menin közümchö kol koyulganın tastıktaym.",
                                 "Удостоверяю, что доверенность подписана в моём присутствии доверителем, указанным в разделе A, личность которого установлена по удостоверению личности.")},
            {"k": "sign", "l": [T("Certifying person (name, position)", "Tastıktoochu (atı, kızmatı)", "Удостоверивший (Ф.И.О., должность)"), "date"], "seal": "Seal / Möör / М.П."},
        ]},
    ],
    "official": [
        [{"k": "boxes", "l": T("Registered at the office under No.", "Bölümdö kattalgan No.", "Зарегистрирована в отделении под №"), "n": 8, "w": 1.4}, {"k": "date", "l": T("Date registered", "Kattalgan kün", "Дата регистрации"), "w": 1}, {"k": "line", "l": T("Postmaster (name, signature)", "Bölüm bashchısı (atı, kolu)", "Начальник отделения (Ф.И.О., подпись)"), "w": 1.4}],
    ],
    "notes": [
        T("A power of attorney ends on the date stated in it, or one year after certification if no date is stated; on its revocation by the principal in writing at the post office; and on the death of the principal or the attorney. Pensions are not paid under a power of attorney for months after the month of the principal's death; amounts so received are recovered.",
          "Ishenim kat anda körsötülgön kündö, kün körsötülbösö tastıktalgandan bir jıldan kiyin; ışenim beruuchu anı pochta bölümündö jazuu jüzündö jokko chıgarganda; ışenim beruuchu je ışenimdüü adam kaytıs bolgondo ayaktalat. Ishenim beruuchu kaytıs bolgon aydan kiyinki aylar üchün pensiya ışenim kat boyuncha tölönböyt; ushunday alıngan summalar kaytarılıp alınat.",
          "Доверенность прекращается в указанный в ней день, а если срок не указан — через год после удостоверения; при её письменной отмене доверителем в отделении; со смертью доверителя или доверенного лица. Пенсия по доверенности за месяцы после месяца смерти доверителя не выплачивается; полученные так суммы взыскиваются."),
        T("Certification by the head of the post office and by the director of a hospital or care home is free of charge. Pensioners over 80 and people with a disability of group I may instead have their pension brought home by the postman.",
          "Pochta bölümünün bashchısı jana oorukananın je karıyalar üyünün direktoru tastıktashı akısız. 80 jashtan ashkan pensionerler jana I toptogu mümkünchülügü chektelgen adamdar anın orduna pensiyasın pochtalyon arkıluu üygö ala alat.",
          "Удостоверение начальником отделения и директором больницы или дома престарелых бесплатно. Пенсионеры старше 80 лет и инвалиды I группы могут вместо этого получать пенсию на дому через почтальона."),
    ],
}

# ---------------------------------------------------------------- P-30
FORMS["P-30"] = {
    "ink": INK, "mark": MARK, "rev": "rev. 03/2024", "printnote": PRINT,
    "approved": "Approved by Order of the Director General of Irad Pochtasy No. 31 of 14 February 2024 under the " + RULES,
    "to": T("Head of the post office", "Pochta bölümünün bashchısına", "Начальнику отделения связи"),
    "instructions": [STD_INS[0], NONE_INS,
        T("Boxes are let for 3, 6 or 12 months at the rates in the price list displayed at the counter. The rent for the whole term and a refundable deposit for each key are paid in advance when the box is assigned. Organisations attach an extract from the Register of Firms and a letter naming the persons authorised.",
          "Yashıktar 3, 6 je 12 ayga kassada ilingen baa tizmesindegi baa menen ijaraga berilet. Bardık möönöttün ijara akısı jana ar bir achkıch üchün kaytarıluuchu garantiya tölömü yashık berilgende aldın ala tölönöt. Uyumdar Firmalar reestrinen köchürmö jana ıygarım berilgen adamdardın attarı jazılgan kat tirkeyt.",
          "Ящики сдаются на 3, 6 или 12 месяцев по тарифам прейскуранта, вывешенного в отделении. Арендная плата за весь срок и возвращаемый залог за каждый ключ вносятся вперёд при предоставлении ящика. Организации прилагают выписку из Реестра фирм и письмо с перечнем уполномоченных лиц."),
        T("Keys are issued to the renter against signature in the key register of the office. The office keeps a master key and may open the box only in the presence of two employees, to remove items placed in it in error.",
          "Achkıchtar ijarachıga bölümdün achkıch kitebine kol koyduruu menen berilet. Bölüm bash achkıchtı saktayt jana yashıktı eki kızmatkerdin katıshuusunda gana, aga jañılısh salıngan jönötmölördü aluu üchün acha alat.",
          "Ключи выдаются арендатору под подпись в книге учёта ключей отделения. Отделение хранит контрольный ключ и может вскрыть ящик только в присутствии двух работников, чтобы изъять ошибочно вложенные отправления."),
    ],
    "sections": [
        {"t": T("Renter", "Ijarachı", "Арендатор"), "rows": [
            {"k": "boxes", "l": "surname"},
            [{"k": "boxes", "l": "first", "w": 2.2}, {"k": "boxes", "l": "idno", "n": 9, "w": 1.2}],
            [{"k": "check", "l": T("Renter", "Ijarachı", "Арендатор"), "opts": [T("individual", "jeke adam", "физ. лицо"), T("organisation", "uyum", "организация")], "cols": 2, "w": 1.1}, {"k": "line", "l": "orgname", "w": 1.4}, {"k": "boxes", "l": "regnum", "n": 10, "w": 1.25}],
            [{"k": "line", "l": ADDR_LINE, "w": 2.2}, {"k": "boxes", "l": "phone", "n": 13, "w": 1.3}],
        ]},
        {"t": T("Box and term", "Yashık jana möönöt", "Ящик и срок"), "rows": [
            [{"k": "line", "l": T("Post office (name and address)", "Pochta bölümü (atı jana dareki)", "Отделение связи (название и адрес)"), "w": 2.6}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .8}],
            [{"k": "check", "l": T("Size of box", "Yashıktın ölchömü", "Размер ящика"), "opts": [T("small (letters)", "kichine (kattar)", "малый (письма)"), T("medium (letters, small packets)", "orto (banderoldor)", "средний (бандероли)"), T("large (with packet shelf)", "choñ (tekchesi menen)", "большой (с полкой)")], "cols": 3, "w": 2.6},
             {"k": "check", "l": T("Term", "Möönötü", "Срок"), "opts": [T("3 months", "3 ay", "3 мес."), T("6 months", "6 ay", "6 мес."), T("12 months", "12 ay", "12 мес.")], "cols": 3, "w": 1.2}],
            [{"k": "date", "l": T("Rent from", "Ijaranın bashtalışı", "Аренда с"), "w": 1}, {"k": "date", "l": T("Rent until", "Ijaranın möönötü", "Аренда по"), "w": 1}, {"k": "check", "l": T("Application", "Arız", "Заявление"), "opts": [T("new", "jañı", "новый"), T("renewal", "uzartuu", "продление")], "cols": 2, "w": 1}, {"k": "boxes", "l": T("Box No. (renewal)", "Yashık No. (uzartuu)", "№ ящика (продление)"), "n": 5, "w": .8}],
            [{"k": "check", "l": T("Redirect mail addressed to my home address to this box", "Üy darekime kelgen pochtanı bul yashıkka buruu", "Переадресовать почту с домашнего адреса в ящик"), "opts": [YES, NO], "cols": 4, "w": 2.4}, {"k": "date", "l": T("Redirect from", "Buruu bashtalgan kün", "Переадресация с"), "w": 1}],
        ]},
        {"t": T("Persons authorised to collect from the box", "Yashıktan aluuga ıygarım berilgen adamdar", "Лица, уполномоченные получать почту из ящика"), "rows": [
            {"k": "table", "l": T("Not more than three persons; each shows the identity card on collecting registered items", "Üch adamdan ashpayt; ar biri buyurtma jönötmölördü alganda jeke kuböölügün körsötöt", "Не более трёх лиц; каждый предъявляет удостоверение при получении регистрируемых отправлений"),
             "cols": [("fullname", 4), ("idno", 1.8), (T("Position (organisations)", "Kızmatı (uyumdar)", "Должность (организации)"), 2), (T("Specimen signature", "Kolunun ülgüsü", "Образец подписи"), 1.8)], "rows": 3},
            [{"k": "boxes", "l": T("Number of keys (max. 3)", "Achkıchtardın sanı (3kö cheyin)", "Кол-во ключей (до 3)"), "n": 1, "w": .9}, {"k": "check", "l": T("Notices of registered items and parcels placed in the box", "Buyurtma jönötmölör jana posılkalar tuuraluu bildirmeler yashıkka salınsın", "Извещения о регистрируемых отправлениях и посылках опускать в ящик"), "opts": [YES, NO], "cols": 4, "w": 2.5}],
        ]},
    ],
    "declaration": T("I undertake to observe the rules for the use of post-office boxes: to collect mail regularly; to renew the rent before the last day of the term; not to copy the keys or change the lock; and to return all keys at the end of the rent. I understand that registered items, parcels and money orders are handed over only at the counter on presentation of the notice.",
                     "Pochta yashıktarın paydalanuu erejelerin saktoogo: pochtanı üzgültüksüz aluuga; ijaranı möönötü bütköngö cheyin uzartuuga; achkıchtardın köchürmösün jasatpoogo jana kulpunu almashtırboogo; ijara bütköndö bardık achkıchtardı kaytaruuga mildettenem. Buyurtma jönötmölör, posılkalar jana akcha kotoruular bildirme körsötülgöndö kassada gana berilerin tüshünöm.",
                     "Обязуюсь соблюдать правила пользования абонентскими ящиками: регулярно забирать почту; продлевать аренду до последнего дня срока; не изготавливать дубликаты ключей и не менять замок; сдать все ключи по окончании аренды. Мне известно, что регистрируемые отправления, посылки и переводы выдаются только в окне по извещению."),
    "signs": [T("Signature of the renter", "Ijarachının kolu", "Подпись арендатора"), "date"],
    "official": [
        [{"k": "boxes", "l": T("Box No. assigned", "Berilgen yashık No.", "№ предоставленного ящика"), "n": 5, "w": 1}, {"k": "line", "l": T("Key Nos. issued", "Berilgen achkıchtardın No.", "№ выданных ключей"), "w": 1.2}, {"k": "money", "l": T("Rent paid in advance", "Aldın ala tölöngön ijara", "Аренда внесена вперёд"), "n": 6, "w": 1.2}, {"k": "money", "l": T("Key deposit", "Achkıch garantiyası", "Залог за ключи"), "n": 5, "w": 1.1}],
        {"k": "sign", "l": [T("Head of the post office", "Pochta bölümünün bashchısı", "Начальник отделения"), SIGN_OFF], },
    ],
    "counterfoil": {"t": T("Post-office box rental certificate", "Pochta yashıgın ijaraga aluu kuböölügü", "Свидетельство об аренде абонентского ящика"), "rows": [
        [{"k": "boxes", "l": T("Box No.", "Yashık No.", "№ ящика"), "n": 5, "w": .9}, {"k": "boxes", "l": OFFICE_NO, "n": 3, "w": .7}, {"k": "line", "l": T("Renter", "Ijarachı", "Арендатор"), "w": 1.5}, {"k": "date", "l": T("Rent paid until", "Ijara tölöngön möönöt", "Аренда оплачена по"), "w": 1}, {"k": "boxes", "l": T("Keys", "Achkıchtar", "Ключей"), "n": 1, "w": .5}],
    ]},
    "notes": [
        T("Mail is addressed: name of the renter, P.O. Box No., Post Office No., city. If the rent is not renewed, mail is held for 30 days after the end of the term and then returned to the senders, and the box may be let to another renter. The rent is not refunded on early termination; the key deposit is refunded when all keys are returned. A lost key is replaced, and the lock changed, at the renter's cost.",
          "Pochtaga darek mınday jazılat: ijarachının atı, pochta yashıgı No., pochta bölümü No., shaar. Ijara uzartılbasa, pochta möönöt bütköndön kiyin 30 kün saktalıp, andan kiyin jönötüüchülörgö kaytarılat jana yashık bashka ijarachıga berilishi mümkün. Möönötünön murun toktotkondo ijara akısı kaytarılbayt; achkıch garantiyası bardık achkıchtar kaytarılganda kaytarılat. Jogolgon achkıch jana kulpu ijarachının esebinen almashtırılat.",
          "Почта адресуется: имя арендатора, а/я №, отделение №, город. Если аренда не продлена, почта хранится 30 дней после окончания срока, затем возвращается отправителям, а ящик может быть сдан другому арендатору. При досрочном прекращении аренда не возвращается; залог возвращается после сдачи всех ключей. Утерянный ключ заменяется, а замок меняется за счёт арендатора."),
    ],
}

split_tables(FORMS)
