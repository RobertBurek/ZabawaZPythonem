
uczeniowie=[{'imieNazwisko':'Robert Mak', 'klasa':'1B'}, {'imieNazwisko':'Ryszard Nowak', 'klasa':'2C'}, {'imieNazwisko':'Anna Mak', 'klasa':'3A'}, {'imieNazwisko':'Monika Zdun','klasa': '1B'}]
nauczyciele=['Maria Konopka', 'Janusz Miłosz', 'Anna Nosowska', 'Henryk Kozłowski', 'Monika Zatorska']
przedmioty=['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']

def czyJestTakiUczen(imieNazwisko, klasa):
    szukanyUczen = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
    if szukanyUczen in uczeniowie:
        return False
    else:
        return True


def dodajUcznia(imieNazwisko, klasa):
    nowyUczen = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
    if czyJestTakiUczen(imieNazwisko, klasa):
        uczeniowie.append(nowyUczen)
    else:
        print('W bazie jest już uczeń o takich danych')


def dodajUczniaKlawiatura():
    koniec=False
    while koniec==False:
        imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
        klasa = str(input('Klasa ucznia (1B,2A...3C): '))
        dodajUcznia(imieNazwisko, klasa)
        takNie=str(input('Chcesz dodać kolejnego ucznia? Y/N: '))
        if takNie=='Y' or takNie=='y':
            koniec=False
        else:
            koniec=True
    wypiszBaze(uczeniowie)


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1)+') '+str(baza[i]))
    else:
        print('Brak danych!!!')



dodajUcznia('Roman Konieczny', '1B')
dodajUczniaKlawiatura()


