pracownicy = []

pracownik1 = {'imie': 'Robert', 'nazwisko': 'Burek',
              'stanowisko': 'lekarz', 'pensja': 5000}
pracownik2 = {'imie': 'Marian', 'nazwisko': 'Kowalski',
              'stanowisko': 'makler', 'pensja': 12000}
pracownik3 = {'imie': 'Anna', 'nazwisko': 'Makowska',
              'stanowisko': 'programista', 'pensja': 8000}
pracownik4 = {'imie': 'Marian', 'nazwisko': 'Jaki',
              'stanowisko': 'makler', 'pensja': 12000}
pracownik0 = {'imie': 'XXXXXXX', 'nazwisko': 'YYYYYYYYY',
              'stanowisko': 'ZZZZZZZ', 'pensja': 10000}
pracownik5 = {'imie': 'Marianek', 'nazwisko': 'Jaki',
              'stanowisko': 'ślusarz', 'pensja': 1000}
pracownik6 = {'imie': 'Maria', 'nazwisko': 'Jaka',
              'stanowisko': 'dyrektor', 'pensja': 2000}
pracownik7 = {'imie': 'Maria', 'nazwisko': 'TakaO',
              'stanowisko': 'ślusarz', 'pensja': 1000}
pracownik8 = {'imie': 'Zbyszek', 'nazwisko': 'Jaki',
              'stanowisko': 'malarz', 'pensja': 12000}
pracownik9 = {'imie': 'Marianek', 'nazwisko': 'Nowak',
              'stanowisko': 'ślusarz', 'pensja': 1000}

pracownicy.append(pracownik1)
pracownicy.append(pracownik2)
pracownicy.append(pracownik3)
pracownicy.append(pracownik4)
pracownicy.append(pracownik5)
pracownicy.append(pracownik0)
pracownicy.append(pracownik6)
pracownicy.append(pracownik7)
pracownicy.append(pracownik8)
pracownicy.append(pracownik9)


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1) + ') ' + str(baza[i]['imie'])+' ' + str(
                baza[i]['nazwisko'])+' (' + str(baza[i]['stanowisko']) + ' ' + str(baza[i]['pensja']) + ')')
    else:
        print('Brak danych w bazie!!!')


def sprawdzCzyJest(imie, nazwisko, stanowisko, pensja):
    szukanaPracownik = {'imie': imie, 'nazwisko': nazwisko,
                        'stanowisko': stanowisko, 'pensja': pensja}
    if szukanaPracownik in pracownicy:
        return False
    else:
        return True


def dodajPracownika(imie, nazwisko, stanowisko, pensja):
    nowyPracownik = {'imie': imie, 'nazwisko': nazwisko,
                     'stanowisko': stanowisko, 'pensja': pensja}
    if sprawdzCzyJest(imie, nazwisko, stanowisko, pensja):
        pracownicy.append(nowyPracownik)
    else:
        print('Pracownik o takich danych jest już w bazie!')


def listaPracownikowZMaxPencja():
    maxPensja = 0
    listaPracownikowMaxPensja = []
    if len(pracownicy) > 0:
        for i in range(len(pracownicy)):
            if pracownicy[i]['pensja'] >= maxPensja:
                maxPensja = pracownicy[i]['pensja']
        for j in range(len(pracownicy)):
            if pracownicy[j]['pensja'] == maxPensja:
                listaPracownikowMaxPensja.append(pracownicy[j])
    wypiszBaze(listaPracownikowMaxPensja)


def listaPracownikowZMinPencja():
    minPensja = pracownicy[0]['pensja']
    listaPracownikowMinPensja = []
    if len(pracownicy) > 0:
        for i in range(len(pracownicy)):
            if pracownicy[i]['pensja'] <= minPensja:
                minPensja = pracownicy[i]['pensja']
        for i in range(len(pracownicy)):
            if pracownicy[i]['pensja'] == minPensja:
                listaPracownikowMinPensja.append(pracownicy[i])
    wypiszBaze(listaPracownikowMinPensja)


def zmienDanePracownika(pracownik, noweImie, noweNazwisko, noweStanowisko, nowePensja):
    if not pracownik in pracownicy:
        print('Nie ma takiej osoby')
    else:
        index = pracownicy.index(pracownik)
        pracownicy[index]['imie'] = noweImie
        pracownicy[index]['nazwisko'] = noweNazwisko
        pracownicy[index]['stanowisko'] = noweStanowisko
        pracownicy[index]['pensja'] = nowePensja


def usunPracownika(pracownik):
    if pracownik in pracownicy:
        pracownicy.remove(pracownik)
    else:
        print('Nie ma takiej osoby')


def dodawaniePracownikaKlawiatura():
    koniec = False
    while koniec == False:
        imie = str(input('Podaj imie: '))
        nazwisko = str(input('Podaj nazwisko: '))
        stanowisko = str(input('Podaj stanowisko: '))
        pensja = int(input('Podaj stanowisko: '))
        dodajPracownika(imie, nazwisko, stanowisko, pensja)
        takNie = str(input('Chcesz dodać kolejnego pracownika? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            koniec = False
        else:
            koniec = True
    print('---------------------------------------------------------------------')
    print('                            Pracownicy w bazie')
    print('---------------------------------------------------------------------')
    wypiszBaze(pracownicy)


# Wypisanie wzystkich pracowników
print('---------------------------------------------------------------------')
print('                           Obecnie w bazie')
print('---------------------------------------------------------------------')
wypiszBaze(pracownicy)

# Próba dodania pracownika o tych samych danych
print('---------------------------------------------------------------------')
print('         Próba dodania pracownika o tych samych danych')
print('---------------------------------------------------------------------')
print('Pracownik:  Robert Burek (lekarz 5000)')
dodajPracownika('Robert', 'Burek', 'lekarz', 5000)

# Zmiana danych pracownika
print('---------------------------------------------------------------------')
print('                     Zmiana danych pracownika')
print('---------------------------------------------------------------------')
print('Pracownik:  Robert Burek (lekarz 5000)')
print('Nowe dane:  Marian Burek-Kowalski (malarz 3500)')
zmienDanePracownika(pracownik1, 'Marian', 'Burek-Kowalski', 'malarz', 3500)

# Dodanie nowego pracownika
print('---------------------------------------------------------------------')
print('                       Dodanie nowego pracownika')
print('---------------------------------------------------------------------')
print('Anna Nowakowska (stomatolog 8400)')
dodajPracownika('Anna', 'Nowakowska', 'stomatolog', 8400)


# Wypisanie wzystkich pracowników
print('---------------------------------------------------------------------')
print('                            Pracownicy w bazie')
print('---------------------------------------------------------------------')
wypiszBaze(pracownicy)

# Usuwam pracownika
print('---------------------------------------------------------------------')
print('                            Usuwam pracownika')
print('---------------------------------------------------------------------')
print('XXXXXXX YYYYYYYYY (ZZZZZZZ 10000)')
usunPracownika(pracownik0)

# Wypisanie wzystkich pracowników
print('---------------------------------------------------------------------')
print('                         Pracownicy w bazie')
print('---------------------------------------------------------------------')
wypiszBaze(pracownicy)

# Max pensje ma pracownik
print('---------------------------------------------------------------------')
print('                       Max pensje ma pracownik')
print('---------------------------------------------------------------------')
listaPracownikowZMaxPencja()

# Min pensje ma pracownik
print('---------------------------------------------------------------------')
print('                     Min pensje ma pracownik')
print('---------------------------------------------------------------------')
listaPracownikowZMinPencja()

# Dodanie pracownika z klawiatury
print('---------------------------------------------------------------------')
print('                     Dodanie pracownika z klawiatury')
print('---------------------------------------------------------------------')
dodawaniePracownikaKlawiatura()
