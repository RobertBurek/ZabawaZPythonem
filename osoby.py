osoby = []

osoba1 = {'imie': 'Robert', 'nazwisko': 'Burek', 'rokUrodzenia': 1970}
osoba2 = {'imie': 'Marian', 'nazwisko': 'Kowalski', 'rokUrodzenia': 1965}
osoba3 = {'imie': 'Anna', 'nazwisko': 'Makowska', 'rokUrodzenia': 1984}

# osobaAdres1 = {'imie': 'Robert', 'nazwisko': 'Burek', 'rokUrodzenia': 1977, 'adres':{
#         'miasto': 'Warszawa', 'ulica': 'Jakaś', 'nrDomu': 25}}
# osobaAdres2 = {'imie': 'Marek', 'nazwisko': 'Nowak', 'rokUrodzenia': 1987, 'adres':{}}
# osobaAdres3 = {'imie': 'Zygmunt', 'nazwisko': 'Mirowski', 'rokUrodzenia': 1985, 'adres':{}}


osoby.append(osoba1)
osoby.append(osoba2)
osoby.append(osoba3)

# osoby.append(osobaAdres1)
# osoby.append(osobaAdres2)
# osoby.append(osobaAdres3)
# print(osoby)
# osoby=[]


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1) + ') ' + str(baza[i]['imie'])+' ' + str(
                baza[i]['nazwisko'])+' (' + str(baza[i]['rokUrodzenia'])+')')
    else:
        print('Brak osób w bazie!!!')


def sprawdzCzyJest(imie, nazwisko, rokUrodzenia):
    szukanaOsoba = {'imie': imie, 'nazwisko': nazwisko, 'rokUrodzenia': rokUrodzenia}
    if szukanaOsoba in osoby:
        return False
    else:
        return True


def dodajOsobe(imie, nazwisko, rokUrodzenia):
    nowaOsoba = {'imie': imie, 'nazwisko': nazwisko, 'rokUrodzenia': rokUrodzenia}
    if sprawdzCzyJest(imie, nazwisko, rokUrodzenia):
        osoby.append(nowaOsoba)
    else:
        print('Osoba o takich danych jest już w bazie!')


def osobyUrodzonePo(rokUrodzenia):
    nowaBazaOsob = []
    for i in range(len(osoby)):
        if osoby[i]['rokUrodzenia'] >= rokUrodzenia:
            nowaBazaOsob.append(osoby[i])
    global ileOsob
    ileOsob = len(nowaBazaOsob)
    print('---------------------------------------------------------------------')
    print('              Osoby urodzone po ' + str(rokUrodzenia) + ' roku')
    print('---------------------------------------------------------------------')
    wypiszBaze(nowaBazaOsob)


def zmienDaneOsoby(osoba, noweImie, noweNazwisko, nowyRokUrodzenia):
    if not osoba in osoby:
        print('Nie ma takiej osoby')
    else:
        index = osoby.index(osoba)
        osoby[index]['imie'] = noweImie
        osoby[index]['nazwisko'] = noweNazwisko
        osoby[index]['rokUrodzenia'] = nowyRokUrodzenia



def dodawanieOsobyKlawiatura():
    koniec=False
    while koniec==False:
        imie = str(input('Podaj imie: '))
        nazwisko = str(input('Podaj nazwisko: '))
        rokUrodzenia = int(input('Podaj rok urodzenia: '))
        dodajOsobe(imie,nazwisko,rokUrodzenia)
        takNie=str(input('Chcesz dodać kolejnego ucznia? Y/N: '))
        if takNie=='Y' or takNie=='y':
            koniec=False
        else:
            koniec=True
    print('---------------------------------------------------------------------')
    print('                            Osoby w bazie')
    print('---------------------------------------------------------------------')
    wypiszBaze(osoby)


# Próba dodania osoby o tych samych danych
print('---------------------------------------------------------------------')
print('             Próba dodania osoby o tych samych danych')
print('---------------------------------------------------------------------')
print('Osoba:  Robert Burek (1970)')
dodajOsobe('Robert', 'Burek', 1970)
# Zmiana danych osoby
print('---------------------------------------------------------------------')
print('                     Zmiana danychosoby')
print('---------------------------------------------------------------------')
print('Osoba:  Robert Burek (1970)')
print('Nowe:  Marian Burek (1980)')
zmienDaneOsoby(osoba1,"Marian",'Burek',1980)
# Dodanie nowej osoby
print('---------------------------------------------------------------------')
print('                       Dodanie nowej osoby')
print('---------------------------------------------------------------------')
dodajOsobe('Marek', 'Nowak', 1986)
print('Marek Nowak (1986)')
# Wypisanie wzystkich osób
print('---------------------------------------------------------------------')
print('                            Osoby w bazie')
print('---------------------------------------------------------------------')
wypiszBaze(osoby)
# Wyszukanie osób urodzony po 1980
osobyUrodzonePo(1980)
# Dodanie osoby z klawiatury
print('---------------------------------------------------------------------')
print('                     Dodanie osoby z klawiatury')
print('---------------------------------------------------------------------')
dodawanieOsobyKlawiatura()
