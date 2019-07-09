# BLOK DEKLARACJI PROGRAMU
# ------------------------

bazaKsiazek = []
ileKsiazek = 0

ksiazka1 = {'tytul': 'Jaś Fasola', 'autor': 'Mick Nilson',
            'rokWydania': 1958, 'iloscStron': 45, 'twardaOprawa': True}
ksiazka2 = {'tytul': 'Jaś i Małgosia', 'autor': 'Bracia Grimm',
            'rokWydania': 1932, 'iloscStron': 20, 'twardaOprawa': True}


def dodajKsiazke(tytul, autor, rokWydania, iloscStron, twardaOprawa):
    nowaKsiazka = {'tytul': tytul, 'autor': autor,
                   'rokWydania': rokWydania, 'iloscStron': iloscStron, 'twardaOprawa': twardaOprawa}
    juzJest = False
    for i in range(len(bazaKsiazek)):
        if bazaKsiazek[i]['tytul'] == tytul:
            juzJest = True
    if juzJest == False:
        bazaKsiazek.append(nowaKsiazka)
    else:
        print('Książka o takim tytule jest już w bazie!')


def wypiszKsiazkiPoRokuWydania(rokWydania):
    nowaBazaKsiazek = []
    for i in range(len(bazaKsiazek)):
        if bazaKsiazek[i]['rokWydania'] >= rokWydania:
            nowaBazaKsiazek.append(bazaKsiazek[i])
    global ileKsiazek
    ileKsiazek = len(nowaBazaKsiazek)
    print('---------------------------------------------------------------------')
    print('              KSIĄŻKI wydane po ' + str(rokWydania) + ' roku')
    print('---------------------------------------------------------------------')
    wypiszBaze(nowaBazaKsiazek)


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1)+') '+str(baza[i]))
    else:
        print('Brak książek w bazie!!!')


def testFunkcji():
    print('')
    print('---------------------------------------------------------------------')
    print('-------------------------POCZĄTEK TESTÓW-----------------------------')
    print('---------------------------------------------------------------------')
    global ileKsiazek
    ileKsiazek = len(bazaKsiazek)
    # Spróbujemy dodać książkę do bazy o tym samym tytule (tytuł pierwszej książki w bazie) poprzez funkcję,
    # jeżeli długość listy NIEwzrośnie funkcja działa poprawnie
    if ileKsiazek > 0:
        dodajKsiazke(bazaKsiazek[0]['tytul'], ' ', 2001, 148, True)
        if len(bazaKsiazek) == ileKsiazek:
            print('Funkcja dodajKsiazke() - ten sam tytuł - działa poprawnie.')
        else:
            print('Funkcja dodajKsiazke() - ten sam tytuł - NIE DZIAŁA poprawnie.')
    else:
        print(
            'Brak książek w bazie. Funkcja dodajKsiazke() - ten sam tytuł - NIESPRAWDZONA')
    # Sprawdzimy ileKsiazek jest wydanych po 1950, następnie dodamy ręcznie do bazy książkę wydaną po 1950 roku, 
    # jeżeli ileKsiazek zwiększy się o jeden, wtedy funkcja działa poprawnie
    wypiszKsiazkiPoRokuWydania(1950)
    ileTeraz = ileKsiazek
    bazaKsiazek.append({'tytul': '', 'autor': '',
                        'rokWydania': 1951, 'iloscStron': 0, 'twardaOprawa': True})
    wypiszKsiazkiPoRokuWydania(1950)
    if ileKsiazek == ileTeraz+1:
        print('Funkcja wypiszKsiazkiPoRokuWydania() działa poprawnie.')
    else:
        print('Funkcja wypiszKsiazkiPoRokuWydania() NIE DZIAŁA poprawnie.')
    print('---------------------------------------------------------------------')
    # Spróbujemy dodać książkę do bazy poprzez funkcję, jeżeli długość listy wzrośnie o jeden
    # funkcja działa poprawnie
    ileKsiazek = len(bazaKsiazek)
    dodajKsiazke('Janosik', 'Ktoś Inny', 1986, 56, False)
    if len(bazaKsiazek) == ileKsiazek+1:
        print('Funkcja dodajKsiazke() działa poprawnie.')
    else:
        print('Funkcja dodajKsiazke() NIE DZIAŁA poprawnie.')
    print('---------------------------------------------------------------------')
    print('---------------------------KONIEC TESTÓW-----------------------------')
    print('---------------------------------------------------------------------')


# BLOK DZIAŁANIA PROGRAMU
# -----------------------

bazaKsiazek.append(ksiazka1)
bazaKsiazek.append(ksiazka2)

dodajKsiazke('Jakaś historia', 'Inny Autor', 2001, 148, True)
dodajKsiazke('Fasolka', 'Ktoś Tam', 1972, 125, False)

print('---------------------------------------------------------------------')
print('                        KSIĄŻKI w bazie')
print('---------------------------------------------------------------------')
wypiszBaze(bazaKsiazek)

wypiszKsiazkiPoRokuWydania(1960)

testFunkcji()