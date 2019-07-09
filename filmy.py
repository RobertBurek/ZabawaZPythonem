import subprocess

filmy = []
obsada = []

aktorzy = ["Bruce Willis", 'Olivia Culpo', 'Frank Grillo',
           'Betty Buckley', 'Helen Mirren', 'Anthony Hopkins']
obsada1 = ["Bruce Willis", 'Olivia Culpo']
obsada2 = [aktorzy[0], aktorzy[2], aktorzy[3]]
obsada3 = [aktorzy[0], aktorzy[4], aktorzy[5]]

film1 = {'tytul': 'Odwet', 'rokProdukcji': 2018,
         'rezyser': 'Brian A. Miller', 'obsada': obsada1}
film2 = {'tytul': 'Split', 'rokProdukcji': 2016,
         'rezyser': 'M. Night Shyamalan', 'obsada': obsada2}
film3 = {'tytul': 'Red 2', 'rokProdukcji': 2013,
         'rezyser': 'Dean Parisot', 'obsada': obsada3}

filmy.append(film1)
filmy.append(film2)
filmy.append(film3)


def dodajFilm(tytul, rezyser, rokProdukcji):
    obsada = wybierzObsade()
    filmy.append({'tytul': tytul, 'rokProdukcji': rokProdukcji,
                  'rezyser': rezyser, 'obsada': obsada})


def wybierzObsade():
    aktor = 1
    while aktor != 0:
        if len(aktorzy) > 0:
            subprocess.call("cls", shell=True)
            print('0) Koniec wybierania')
            for i in range(len(aktorzy)):
                print(str(i+1) + ') ' + aktorzy[i])
            print('Wybrani:' + str(obsada))
        aktor = int(
            input('Wybierz aktora do obsady (0..' + str(len(aktorzy)) + '): '))
        if aktor > 0 and aktor <= len(aktorzy):
            obsada.append(aktorzy[aktor-1])
    return obsada


def wypiszBaze(baza):
    if len(baza) > 0:
        for i in range(len(baza)):
            print(str(i+1) + ') "' + str(baza[i]['tytul'])+'" - reżyseria: ' + str(
                baza[i]['rezyser'])+' (' + str(baza[i]['rokProdukcji'])+'), obsada:' + str(filmy[i]['obsada']))
    else:
        print('Brak danych w bazie!!!')


def wypiszFilmyPoRokuProdukcji(rokProdukcji):
    nowaBazaFilmow = []
    for i in range(len(filmy)):
        if filmy[i]['rokProdukcji'] >= rokProdukcji:
            nowaBazaFilmow.append(filmy[i])
    # global ileFilmow
    # ileFilmow = len(nowaBazaFilmow)
    print('--------------------------------------------------------------------------')
    print('                     FILMY wyprodukowane po ' + str(rokProdukcji) + ' roku')
    print('--------------------------------------------------------------------------')
    wypiszBaze(nowaBazaFilmow)


dodajFilm("Odwet 2", 'Brian A. Miller', 2019)
print('-------------------------------FILMY W BAZIE------------------------------')
wypiszBaze(filmy)
wypiszFilmyPoRokuProdukcji(2017)
