import subprocess
import datetime
import time

uczeniowie = [{'imieNazwisko': 'Robert Mak', 'klasa': '1B'}, {'imieNazwisko': 'Ryszard Nowak', 'klasa': '2C'},
              {'imieNazwisko': 'Anna Mak', 'klasa': '3A'}, {'imieNazwisko': 'Monika Zdun', 'klasa': '1B'}]
oceny = [{'uczen': 'Robert Mak', 'klasa': '1B', 'przedmiot': 'matematyka',
          'ocena': 5, 'nauczyciel': 'Anna Nosowska'},
         {'uczen': 'Robert Mak', 'klasa': '1B', 'przedmiot': 'matematyka',
             'ocena': 3, 'nauczyciel': 'Anna Nosowska'},
         {'uczen': 'Anna Mak', 'klasa': '3A', 'przedmiot': 'geografia',
             'ocena': 6, 'nauczyciel': 'Monika Zatorska'},
         {'uczen': 'Robert Mak', 'klasa': '1B', 'przedmiot': 'matematyka',
             'ocena': 4, 'nauczyciel': 'Anna Nosowska'},
         {'uczen': 'Robert Mak', 'klasa': '1B', 'przedmiot': 'geografia',
             'ocena': 1, 'nauczyciel': 'Anna Nosowska'},
         {'uczen': 'Robert Mak', 'klasa': '1B', 'przedmiot': 'matematyka', 'ocena': 2, 'nauczyciel': 'Anna Nosowska'}]
nauczyciele = ['Maria Konopka', 'Janusz Miłosz', 'Zuzanna Nowak',
               'Anna Nosowska', 'Henryk Kozłowski', 'Monika Zatorska']
przedmioty = ['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']

def wypiszListe(lista):
    print('-----------------------------------------------')
    for i in range(len(lista)):
        print(str(i+1)+' - '+str(lista[i]))
    if len(lista) == 0:
        print('                 Brak danych')
    print('-----------------------------------------------')

def wypiszListy():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    print('-----------------------------------------------')
    print('                    OCENY')
    wypiszListe(oceny)
    print('-----------------------------------------------')
    print('                 NAUCZYCIELE')
    wypiszListe(nauczyciele)
    print('-----------------------------------------------')
    print('                 PRZEDMIOTY')
    wypiszListe(przedmioty)

def dodajUcznia():
    koniec = False
    while koniec == False:
        imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
        klasa = str(input('Klasa ucznia (1B,2A...3C): '))
        uczen = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
        uczeniowie.append(uczen)
        print('Dodano ucznia ' +
              uczen['imieNazwisko']+' do klasy '+uczen['klasa'])
        takNie = str(input('Chcesz dodać kolejnego ucznia? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            koniec = False
        else:
            koniec = True
    wypiszListe(uczeniowie)

def modyfikujUcznia():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    nr = int(input('Podaj numer ucznia: '))
    if nr > len(uczeniowie) or nr < 1:
        print('Lista obejmuje '+str(len(uczeniowie))+' uczniów.')
        print('Sprubój jeszcze raz.')
    else:
        takNie = str(input('Czy chodzi o ucznia: ' +
                           uczeniowie[nr-1]['imieNazwisko']+' ('+uczeniowie[nr-1]['klasa']+')? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
            klasa = str(input('Klasa ucznia (1B,2A...3C): '))
            uczeniowie[nr-1]['imieNazwisko'] = imieNazwisko
            uczeniowie[nr-1]['klasa'] = klasa
    print('Zmodyfikowano ucznia nr '+str(nr)+') '+imieNazwisko+' ('+klasa+')')

def usunUcznia():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    imieNazwisko = str(input('Podaj imie i nazwisko ucznia do usunięcia: '))
    klasa = str(input('Podaj klasę ucznia (1B,2A...3C): '))
    uczenDoUsuniecia = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
    if uczenDoUsuniecia in uczeniowie:
        takNie = str(input('Czy chcesz usunąć ucznia: ' +
                           imieNazwisko+' ('+klasa+') z listy uczniów? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            uczeniowie.remove(uczenDoUsuniecia)
            print('Usunięto ucznia z listy.')
            print('-----------------------------------------------')
            print('                  UCZNIOWIE')
            wypiszListe(uczeniowie)
    else:
        print('Nie ma takiego ucznia na liście.')

def wypiszOcene(ocenaUcznia):
    print(str(ocenaUcznia['przedmiot'])+'   '+str(ocenaUcznia['ocena']
                                                  )+'  wystawiona przez: '+str(ocenaUcznia['nauczyciel']))

def ocenyUcznia():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    nrU = int(input('Podaj numer ucznia: '))
    if nrU > len(uczeniowie) or nrU < 1:
        print('Lista obejmuje '+str(len(uczeniowie))+' uczniów.')
        print('Sprubój jeszcze raz.')
    else:
        takNie = str(input('Oceny z wybranego przedmiotu? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            print('-----------------------------------------------')
            print('                  PRZEDMIOTY')
            wypiszListe(przedmioty)
            nrP = 0
            while nrP == 0:
                nrP = int(input('Wybierz przedmiot: '))
                if nrP > len(przedmioty) or nrP < 1:
                    nrP = 0
            print('-----------------------------------------------')
            print('    OCENY ucznia ' +
                  uczeniowie[nrU-1]['imieNazwisko']+' ('+uczeniowie[nrU-1]['klasa']+')')
            print('-----------------------------------------------')
            for i in range(len(oceny)):
                if oceny[i]['uczen'] == uczeniowie[nrU-1]['imieNazwisko'] and oceny[i]['klasa'] == uczeniowie[nrU-1]['klasa'] and oceny[i]['przedmiot'] == przedmioty[nrP-1]:
                    wypiszOcene(oceny[i])
            print('-----------------------------------------------')
        else:
            print('-----------------------------------------------')
            print('    OCENY ucznia ' +
                  uczeniowie[nrU-1]['imieNazwisko']+' ('+uczeniowie[nrU-1]['klasa']+')')
            print('-----------------------------------------------')
            for i in range(len(oceny)):
                if oceny[i]['uczen'] == uczeniowie[nrU-1]['imieNazwisko'] and oceny[i]['klasa'] == uczeniowie[nrU-1]['klasa']:
                    wypiszOcene(oceny[i])
            print('-----------------------------------------------')

def ocenyWybranegoUcznia(uczen):
    print('-----------------------------------------------')
    print('    OCENY ucznia '+uczen['imieNazwisko']+' ('+uczen['klasa']+')')
    print('-----------------------------------------------')
    for i in range(len(oceny)):
        if oceny[i]['uczen'] == uczen['imieNazwisko'] and oceny[i]['klasa'] == uczen['klasa']:
            wypiszOcene(oceny[i])
    print('-----------------------------------------------')

def dodajOcene():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    nrU = int(input('Podaj numer ucznia: '))
    if nrU > len(uczeniowie) or nrU < 1:
        print('Lista obejmuje '+str(len(uczeniowie))+' uczniów.')
        print('Sprubój jeszcze raz.')
    else:
        print('-----------------------------------------------')
        print('                  PRZEDMIOTY')
        wypiszListe(przedmioty)
        nrP = 0
        while nrP == 0:
            nrP = int(input('Wybierz przedmiot: '))
            if nrP > len(przedmioty) or nrP < 1:
                nrP = 0
        ocena = 0
        while ocena == 0:
            ocena = int(input('Podaj ocenę (1..6): '))
            if ocena < 1 or ocena > 6:
                ocena = 0
        print('-----------------------------------------------')
        print('                  NAUCZYCIELE')
        wypiszListe(nauczyciele)
        nrN = 0
        while nrN == 0:
            nrN = int(input('Ocenę wystawił: '))
            if nrN > len(nauczyciele) or nrN < 1:
                nrN = 0
        imieNazwisko = uczeniowie[nrU-1]['imieNazwisko']
        klasa = uczeniowie[nrU-1]['klasa']
        wybranyUczen = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
        ocenaNowa = {'uczen': imieNazwisko, 'klasa': klasa,
                     'przedmiot': przedmioty[nrP-1], 'ocena': ocena, 'nauczyciel': nauczyciele[nrN-1]}
        oceny.append(ocenaNowa)
        ocenyWybranegoUcznia(wybranyUczen)

def najlepszyUczen():
    print('-----------------------------------------------')
    print('                  PRZEDMIOTY')
    wypiszListe(przedmioty)
    nrP = 0
    while nrP == 0:
        nrP = int(input('Wybierz przedmiot: '))
        if nrP > len(przedmioty) or nrP < 1:
            nrP = 0
    ocenyPrzedmiot = []
    for i in range(len(oceny)):
        if oceny[i]['przedmiot'] == przedmioty[nrP-1]:
            ocenyPrzedmiot.append(oceny[i])
    sredniaUcznia = []
    for i in range(len(uczeniowie)):
        ileOcen = 0
        sumaOcen = 0
        for j in range(len(ocenyPrzedmiot)):
            if ocenyPrzedmiot[j]['uczen'] == uczeniowie[i]['imieNazwisko'] and ocenyPrzedmiot[j]['klasa'] == uczeniowie[i]['klasa']:
                sumaOcen += ocenyPrzedmiot[j]['ocena']
                ileOcen += 1
        if ileOcen != 0:
            sredniaUcznia.append(
                {'uczen': uczeniowie[i]['imieNazwisko'], 'klasa': uczeniowie[i]['klasa'], 'srednia': sumaOcen/ileOcen})
    maxSrednia = {'uczen': '', 'klasa': '', 'srednia': 0}
    if len(sredniaUcznia) != 0:
        for i in range(len(sredniaUcznia)):
            if sredniaUcznia[i]['srednia'] > maxSrednia['srednia']:
                maxSrednia = sredniaUcznia[i]
        print('Najlepszym uczniem z przedmiotu '+przedmioty[nrP-1])
        print('jest '+maxSrednia['uczen']+' z '+maxSrednia['klasa'] +
              ' ze średnią '+str(maxSrednia['srednia']))
    else:
        print('Nie ma najlepdszego ucznia z tego przedmiotu.')

def najgorszyUczen():
    print('-----------------------------------------------')
    print('                  PRZEDMIOTY')
    wypiszListe(przedmioty)
    nrP = 0
    while nrP == 0:
        nrP = int(input('Wybierz przedmiot: '))
        if nrP > len(przedmioty) or nrP < 1:
            nrP = 0
    ocenyPrzedmiot = []
    for i in range(len(oceny)):
        if oceny[i]['przedmiot'] == przedmioty[nrP-1]:
            ocenyPrzedmiot.append(oceny[i])
    sredniaUcznia = []
    for i in range(len(uczeniowie)):
        ileOcen = 0
        sumaOcen = 0
        for j in range(len(ocenyPrzedmiot)):
            if ocenyPrzedmiot[j]['uczen'] == uczeniowie[i]['imieNazwisko'] and ocenyPrzedmiot[j]['klasa'] == uczeniowie[i]['klasa']:
                sumaOcen += ocenyPrzedmiot[j]['ocena']
                ileOcen += 1
        if ileOcen != 0:
            sredniaUcznia.append(
                {'uczen': uczeniowie[i]['imieNazwisko'], 'klasa': uczeniowie[i]['klasa'], 'srednia': sumaOcen/ileOcen})
    minSrednia = {'uczen': '', 'klasa': '', 'srednia': 7}
    if len(sredniaUcznia) != 0:
        for i in range(len(sredniaUcznia)):
            if sredniaUcznia[i]['srednia'] < minSrednia['srednia']:
                minSrednia = sredniaUcznia[i]
        print('Najsłabszym uczniem z przedmiotu ' + przedmioty[nrP-1])
        print('jest '+minSrednia['uczen']+' z ' + minSrednia['klasa'] +
              ' ze średnią '+str(minSrednia['srednia']))
    else:
        print('Nie ma najsłabszego ucznia z tego przedmiotu.')

def najwyzszaSrednia():
    sredniaUcznia = []
    for i in range(len(uczeniowie)):
        ileOcen = 0
        sumaOcen = 0
        for j in range(len(oceny)):
            if oceny[j]['uczen'] == uczeniowie[i]['imieNazwisko'] and oceny[j]['klasa'] == uczeniowie[i]['klasa']:
                sumaOcen += oceny[j]['ocena']
                ileOcen += 1
        if ileOcen != 0:
            sredniaUcznia.append(
                {'uczen': uczeniowie[i]['imieNazwisko'], 'klasa': uczeniowie[i]['klasa'], 'srednia': sumaOcen/ileOcen})
    print(sredniaUcznia)
    maxSrednia = {'uczen': '', 'klasa': '', 'srednia': 0}
    if len(sredniaUcznia) != 0:
        for i in range(len(sredniaUcznia)):
            if sredniaUcznia[i]['srednia'] > maxSrednia['srednia']:
                maxSrednia = sredniaUcznia[i]
        print('Najlepszym uczniem ze wszystkich uczniów')
        print('jest '+maxSrednia['uczen']+' z '+maxSrednia['klasa'] +
              ' ze średnią '+str(maxSrednia['srednia']))
    else:
        print('Nie ma najlepdszego ucznia.')

tak = True
while tak == True:
    subprocess.call("cls", shell=True)
    print(' MENU: ')
    print('1 - Dodaj ucznia')
    print('2 - Modyfikuj ucznia')
    print('3 - Usun ucznia')
    print('4 - Oceny ucznia')
    print('5 - Dodaj ocenę')
    print('6 - Najlepszy uczeń')
    print('7 - Najgorszy uczeń')
    print('8 - Najwyższa średnia')
    print('9 - Wszystkie listy')
    print('0 - Koniec')
    wybor = int(input('Twój wybór: '))
    if wybor == 1:
        dodajUcznia()
    if wybor == 2:
        modyfikujUcznia()
    if wybor == 3:
        usunUcznia()
    if wybor == 4:
        ocenyUcznia()
    if wybor == 5:
        dodajOcene()
    if wybor == 6:
        najlepszyUczen()
    if wybor == 7:
        najgorszyUczen()
    if wybor == 8:
        najwyzszaSrednia()
    if wybor == 9:
        wypiszListy()
    if wybor == 0:
        tak = False
    pauza = input('')
 #   time.sleep(5)
