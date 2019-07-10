import subprocess

transakcje = []
listaZakupow=[]

towary = ["mleko", 'chleb', 'masło', 'ziemniaki', 'marchew','cebula']
ceny = [3.1, 2.55, 5.21, 3.30, 4.20, 3.99]
klienci = ["Bruce Willis", 'Roman Nowak', 'Anna Kowalska']

transakcja1 = {
    'klient': klienci[0],
    'dataZakupu': '21-05-2019',
    'listaTowarow': [towary[0], towary[3], towary[5]],
    'wartosc': ceny[0] + ceny[3] + ceny[5],
}
transakcja2 = {
    'klient': klienci[2],
    'dataZakupu': '12-06-2019',
    'listaTowarow': [towary[1], towary[2],towary[4]],
    'wartosc': ceny[1] + ceny[2] + ceny[4],
}
transakcja3 = {
    'klient': klienci[1],
    'dataZakupu': '05-06-2019',
    'listaTowarow': [towary[0], towary[2], towary[3]],
    'wartosc': ceny[0] + ceny[2] + ceny[3],
}


def listaZakupowKlienta():
    towar = 1
    wartosc = 0
    while towar != 0:
        if len(towary) > 0:
            subprocess.call("cls", shell=True)
            print('0) Koniec zakupów')
            for i in range(len(towary)):
                print(str(i+1) + ') ' + towary[i] + '   cena: '+ str(ceny[i]))
            print('Wybrane: ' + str(listaZakupow))
            print('Koszt: ' + str(wartosc))
        towar = int(input('Wybierz aktora do obsady (0..' + str(len(towary)) + '): '))
        if towar > 0 and towar <= len(towary):
            listaZakupow.append(towary[towar-1])
            wartosc = round(wartosc + ceny [towar-1], 2)
    return [listaZakupow, wartosc]

def nowaTransakcja(klient, dataZakupu):
    listaZakupowiCena=listaZakupowKlienta()
    listaZakupow = listaZakupowiCena[0]
    wartosc = listaZakupowiCena[1]
    nowaTransakcja={'klient': klient, 'dataZakupu': dataZakupu, 'listaTowarow': listaZakupow, 'wartosc': wartosc} 
    transakcje.append(nowaTransakcja)  
    return nowaTransakcja

transakcje = [transakcja1, transakcja2, transakcja3]

def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1) + ') ' + str(baza[i]))
    else:
        print('Brak osób w bazie!!!')

nowaTransakcja(klienci[2], '05-06-2019')
wypiszBaze(transakcje)
