import subprocess

uczeniowie = ['Robert Mak', 'Ryszard Nowak', 'Anna Mak', 'Monika Zdun']
nauczyciele = ['Maria Konopka', 'Janusz Miłosz', 'Anna Mak', 'Ryszard Nowak',
               'Anna Nosowska', 'Henryk Kozłowski', 'Monika Zatorska']
przedmioty = ['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']
oceny = []

ocena1 = {'uczen': uczeniowie[1], 'przedmiot': przedmioty[3], 'ocena': 5,
          'dataWystawienia': '12.07.2019', 'nauczyciel': nauczyciele[0]}
ocena2 = {'uczen': uczeniowie[0], 'przedmiot': przedmioty[0], 'ocena': 4,
          'dataWystawienia': '11.07.2019', 'nauczyciel': nauczyciele[1]}
ocena3 = {'uczen': uczeniowie[2], 'przedmiot': przedmioty[1], 'ocena': 3,
          'dataWystawienia': '12.06.2019', 'nauczyciel': nauczyciele[2]}

oceny.append(ocena1)
oceny.append(ocena2)
oceny.append(ocena3)


def dodajOcene():
    uczen = 0
    while uczen <= 0 or uczen > len(uczeniowie):
        subprocess.call("cls", shell=True)
        wypiszBaze(uczeniowie)
        uczen = int(input('Wybierz ucznia (1..' + str(len(uczeniowie)) + '): '))
    przedmiot = 0
    while przedmiot <= 0 or przedmiot > len(przedmioty):
        subprocess.call("cls", shell=True)
        wypiszBaze(przedmioty)
        przedmiot = int(
            input('Wybierz przedmiot (1..' + str(len(uczeniowie)) + '): '))
    ocena = 0
    while ocena < 1 or ocena > 6:
        subprocess.call("cls", shell=True)
        ocena = int(input('Podaj ocenę (1..6): '))
    subprocess.call("cls", shell=True)
    dataWystawienia = str(input('Podaj datę wystawienia (dd.mm.rrrr): '))
    nauczyciel = 0
    while nauczyciel <= 0 or nauczyciel > len(nauczyciele):
        subprocess.call("cls", shell=True)
        wypiszBaze(nauczyciele)
        nauczyciel = int(
            input('Wybierz nauczyciela(1..' + str(len(nauczyciele)) + '): '))
    nowaOcena = {'uczen': uczeniowie[uczen-1], 'przedmiot': przedmioty[przedmiot-1],
                 'ocena': ocena, 'dataWystawienia': dataWystawienia, 'nauczyciel': nauczyciele[nauczyciel-1]}
    oceny.append(nowaOcena)
    wypiszBaze(oceny)


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1)+') '+str(baza[i]))
    else:
        print('Brak danych!!!')


dodajOcene()
