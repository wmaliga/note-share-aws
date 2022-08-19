import database

testNote1 = {
    'id': '4c79575f-4a6a-4901-8d42-7650edb72c10',
    'type': 'PUBLIC',
    'title': 'Szybkie pate Jamiego',
    'expirationDate': '2031-06-08',
    'data': """Składniki:
- wątróbki drobiowe
- boczek
- masło
- szalotka
- calvados/whisky
- pikle i pietruszka
- oliwa
- bagietka do podania

Na patelni topimy masło i wrzucamy posiekany boczek, całe wątróbki i posiekaną szalotkę. Po usmażeniu dolewamy alkoholu i podpalamy. Lekko studzimy i drobno siekamy.

Podajemy na bagietce, przyozdabiamy drobno pokrojonymi piklami i pietruszką."""
}

testNote2 = {
    'id': 'f9c261d6-66a6-4f60-bb61-62ca908960f4',
    'type': 'PUBLIC',
    'title': 'Spring rolls',
    'expirationDate': '2032-06-08',
    'data': """Składniki:
papier ryżowy
warzywka: marchew / seler naciowy / kalarepka
wypełniacz: kapusta czerwona / mix sałat
mięsko: łosoś pieczony / krewetki

Sos (2 osoby):
łyżka tartego imbiru
ząbek tartego czosnku
łyżka sosu ostrygowego
łyżka sosu sojowego
łyżka sosu słodkie chilli
łyżeczka oleju sezamowego (opcjonalnie)

Majonez wasabi:
majonez
wasabi

Przygotowanie:
1. Jeżeli używamy surowego łososia należy go upiec z sosem sojowym.
2. Surowe krewetki usmażyć.
3. Warzywka kroimy w cienkie słupki.
4. Kapustę / sałatę rozdrabniany.
5. Łososia kroimy w słupki.
6. Papier ryżowy moczymy krótko z dwóch stron i kładziemy na desce.
7. Składniki układamy od najładniejszych do mniej reprezentacyjnych i zawijamy."""
}

testNote3 = {
    'id': 'e9d89f8b-52b3-49c4-b059-6daee4713148',
    'type': 'PUBLIC',
    'title': 'Enchiladas',
    'expirationDate': '2033-06-08',
    'data': """Składniki:
1 duża pierś z kurczaka
1 cebula czerwona
1 ząbek czosnku
1 puszka pomidorów
1/2 czerwonej papryki
4 tortille kukurydziane
oliwa z oliwek
100 g sera Cheddar
sól
pieprz
kmin rzymski
kolendra

Sposób przygotowania:

1. Kurczaka należy pokroić na małe kawałki i usmażyć na oliwie, doprawiając kolendrą, kuminem, pieprzem i solą. W międzyczasie można zetrzeć ser, jeśli kupiliśmy cały kawałek.

2. Na osobnej patelni smażymy posiekaną w piórka cebulę, z wyciśniętym czosnkiem i pokrojoną w kostkę papryką czerwoną. Smażymy, aż papryka będzie miękka. Do warzyw dodajemy pomidory z puszki i gotujemy około 8 minut. Na koniec dodajemy kumin i kolendrę

3. Połowę sosu pomidorowego wlewamy do usmażonego kurczaka i mieszamy. Podsmażamy chwilę i dodajemy ser. Podsmażamy do momentu, aż ser się roztopi

4. Na tortille wykładamy nadzienie z kurczaka i sosu i ciasno zwijamy. Wkładamy je do naczynia żaroodpornego i polewamy pozostałym sosem oraz posypujemy resztą sera. Pieczmy w 180 stopniach Celsjusza przez 10 minut, aż ser się roztopi i lekko przypiecze."""
}

testNote4 = {
    'id': '65eb0240-3eaa-47bb-87cb-68b1f5dfb8cb',
    'type': 'PUBLIC',
    'title': 'Risotto grzybowe',
    'expirationDate': '2034-06-08',
    'data': """Składniki (porcja dla 4 osób):
suszone borowiki – 15 g
brązowe pieczarki – 400 g
cebula dymka – 1 pęczek
szalotka – 2 szt.
parmezan – 50 g
ryż do risotta – 250 g (120 g dla dwóch osób)
masło – 3 łyżki
białe wino wytrawne – 100 ml
bulion warzywny – 1 l
sól
pieprz

KROK 1: NAMACZAMY SUSZONE BOROWIKI
Suszone borowiki zalewamy 150 ml wrzącej wody i pozostawiamy na 10 minut. Grzyby osączamy na gęstym sitku. Zostawiamy wodę z moczenia grzybów. Borowiki opłukujemy, osuszamy i drobno kroimy. Pieczarki oczyszczamy i kroimy w plasterki. Dymki oczyszczamy i kroimy w krążki. Parmezan ścieramy drobno na tarce.

KROK 2: GOTUJEMY RISOTTO
Szalotki obieramy i kroimy drobno. Smażymy z ryżem na 1 łyżce gorącego masła przez 2 minuty. Zalewamy winem i czekamy, aż odparuje. Dolewamy wody z moczenia grzybów, a następnie stopniowo dodajemy bulion i gotujemy na wolnym ogniu przez 20-25 minut, mieszając od czasu do czasu, aż ryż będzie kremowy. Na drugiej patelni podsmażamy dymkę, pieczarki i borowiki na 1 łyżce gorącego masła przez 8-10 minut. Doprawiamy solą i pieprzem. Pozostałe masło i parmezan dodajemy do risotta i mieszamy, doprawiamy do smaku i pozostawiamy na krótko pod przykryciem. Podajemy z grzybami.

https://kuchnialidla.pl/risotto-grzybowe"""
}

testNote5 = {
    'id': 'f14cb915-e9e0-4864-b1e5-ea69da76df23',
    'type': 'PUBLIC',
    'title': 'Sos koperkowy',
    'expirationDate': '2035-06-08',
    'data': """Składniki na 4 porcje:
- 1 i 1/2 szklanki bulionu, rosołu
- ok. 1/4 łyżeczki kurkumy
- 1 pełna łyżka mąki
- 1/3 szklanki śmietanki kremówki 30%
- po ok. 1/4 łyżeczki białego i czarnego pieprzu oraz granulowanego czosnku
- 1 łyżka masła
- 1 pęczek koperku
- 1 łyżeczka soku z cytryny

Przygotowanie:
Bulion zagotować z kurkumą. W miseczce dokładnie rozprowadzić mąkę w śmietance, następnie wlewać ją do bulionu ciągle mieszając, zagotować na małym ogniu.
W międzyczasie doprawić solą, białym i czarnym pieprzem oraz czosnkiem w proszku. Gotować przez ok. 1 minutę co chwilę mieszając.
Dodać masło, sok z cytryny i posiekany koperek, podgrzewać jeszcze przez chwilę ciągle mieszając. Odstawić z ognia (można przygotować wcześniej)."""
}

testNote6 = {
    'id': '8b4fe685-aebf-49e1-aada-46c3ae6ce62c',
    'type': 'PUBLIC',
    'title': 'Szparagi z sosem serowym',
    'expirationDate': '2036-06-08',
    'data': """Składniki:
Pęczek szparagów
Szynka serano
Ser Lazur
Śmietana 18%
Masło
Sól

Szparagi gotujemy 10 minut w wodzie z łyżką masła i łyżeczką soli. Ser drobno kroimy i rozpuszczamy w śmietanie na małym ogniu. Podajemy z szynką parmeńską."""
}

testNote7 = {
    'id': '9a395a40-8110-4242-9904-d6c2fea41ff9',
    'type': 'PUBLIC',
    'title': 'Guacamole',
    'expirationDate': '2037-06-08',
    'data': """Składniki:
1 duże awokado (miękkie)
świeżo wyciśnięty sok z połowy limonki (ew. cytryny)
pół małej czerwonej cebuli
trochę szczypiorku
1 pomidor
garść świeżej poszatkowanej kolendry
pół łyżeczki roztartego lub zmielonego kuminu (kminu rzymskiego)
szczypta soli i pieprzu do smaku
sól

Przygotowanie:
Przekroić awokado i wybrać miąższ łyżką, wymieszać z sokiem z limonki.
Pomidora bez pestek i bez skórki pokroić bardzo drobno i dodać do miski.
Cebulę i szczypiorek pokroić bardzo drobno i dodać razem z drobno pokrojoną kolendrą.
Posolić i popieprzyć do smaku."""
}

testNote8 = {
    'id': '3430a389-569d-403a-8cfb-e96caf42125d',
    'type': 'PRIVATE',
    'password': 'pass',
    'title': 'Ciasto do pierogów',
    'expirationDate': '2038-06-08',
    'data': """Składniki:
600 g mąki
1 jako
3 łyżki oleju
200 ml ciepłej wody
Szczypta soli"""
}


def test_data(event, context):
    load(testNote1)
    load(testNote2)
    load(testNote3)
    load(testNote4)
    load(testNote5)
    load(testNote6)
    load(testNote7)
    load(testNote8)

    return {
        "statusCode": 200
    }


def load(note):
    print(f"Loading note: {note['title']} [{note['id']}]")
    database.save_note(note)
