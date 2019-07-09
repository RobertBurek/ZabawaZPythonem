# obecnyDzien = 'Wtorek'
# swietoPanstwowe = False

# if obecnyDzien == 'Niedziela':
#     print('Jest niedziela, mamy wolne')
# elif swietoPanstwowe == True:
#     print('Nie ma niedzieli, ale jest święto, mamy wolne')
# else:
#     print('Dzień pracujący')

# luty = [['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
#          'Piątek', 'Sobota', 'Niedziela'],
#         ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
#          'Piątek', 'Sobota', 'Niedziela'],
#         ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
#          'Piątek', 'Sobota', 'Niedziela'],
#         ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
#          'Piątek', 'Sobota', 'Niedziela']]
# for tydzien in luty:
#     print(tydzien)
#     for dzien in tydzien:
#         print(dzien)

# for x in range(5):
#     print(x)


# liczbyPierwsze = [2, 3, 5, 7, 13]
# pustaLista = []

# print(dzienTygodnia[9])

# lista = [1,2,3,5,4,5]
# lista.remove(5)
# print(lista)

# lista = []
# lista.append('Poniedziałek')
# lista.append('Wtorek')
# lista.append('Środa')
# lista.append('Czwartek')
# lista.append('Piątek')
# lista.append('Sobota')
# lista.append('Niedziela')
# print(lista)

# lista = ['Poniedziałek', 'Wtorek', 'Środa',
#          'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# lista.remove('Poniedziałek')
# lista.remove('Wtorek')
# lista.remove('Środa')
# lista.remove('Czwartek')
# print(lista)

# x = 1
# while(x < 100):
#     if x % 3 == 0:
#         print(x)
#     x = x + 1

# kolkoKrzyzyk = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]

# lewyGornyRog = kolkoKrzyzyk[0][0]
# lewyGornyRog = kolkoKrzyzyk[2][0]

# dzien = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
#          'Piątek', 'Sobota', 'Niedziela']
# for i in range(4, len(dzien)):
#     print('Dzień ' + str(i+1) + ': ' + dzien[i] + ' - weekend')

# x = 'Robert'
# y = 'Burek'
# print('Witam, nazywam się ' + x + ' ' + y)

# dd = 20
# mm = '06'
# rrrr = 2019
# print('Dzisiaj jest ' + str(dd) + '.' + mm + '.' + str(rrrr))

# tab = [99, 333, 555, 111, 666, 258, 3249, 25847, 2356895, 5847552]
# print(tab)
# podzialne = []
# for i in range(len(tab)):
#     if tab[i] % 9 == 0:
#         podzialne.append(tab[i])
# print(podzialne)

# tab = ['duży', 'człowiek', 'jest', 'fajnie', 'ubrany',
#        'dzisiaj', 'mafajnie', 'spodnie', 'bluzeczkę']
# print(tab)
# szukane = 'fajnie'
# for i in range(len(tab)):
#     if tab[i] == szukane:
#         print('znalazłem słowo: ' + tab[i])

# tab = [99, 333, 555, 111, 666, 25847, 2356895, 5847552]
# print(tab)
# suma = 0
# for i in range(len(tab)):
#     suma = suma + tab[i]
# print('suma: ' + str(suma))
# print('średnia: ' + str(suma/len(tab)))

# rok = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
#        'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
# print(rok)
# for i in range(len(rok)):
#     print('miesiąc ' + rok[i] + ' ma znaków: ' + str(len(rok[i])))

# silnia = 1
# for i in range(1, 10):
#     silnia = silnia * i
# print('silnia z 10 wynosi: ' + str(silnia))


# for i in range(1,101):
#     wynik=''
#     if (i)%3==0:
#         wynik='Fizz'
#     if (i)%5==0:
#         wynik='Buzz'
#     if (i)%3==0 and i%5==0:
#         wynik="Fizz Buzz"
#     if len(wynik)==0:
#         print((i))
#     else:
#         print(wynik)


# def kwadrat(a):
#     wynik = a * a
#     return wynik

# print(kwadrat(3))

# def poleProstokata(a, b):
#     if a > 0 and b > 0:
#         return a * b

# pole=poleProstokata(-1,-2)
# print(pole)
# pole+=3
# print(pole)

# def funkcjaNaPozniej():
#     pass

# x = 'To jest zmienna zewnętrzna'
# def printNowy(a):
#     # global x
#     # x=x+' takatam'
#     print(x)
#     print(a)

# printNowy('test funkcji')

# x = 10

# def zmienX():
#     x = 20
#     print("x wewnątrz funkcji = " + str(x))

# zmienX()
# print("x poza funkcją = " + str(x))


# x = 10

# def zmienX(z):
#     global x
#     print("x przed zmianą = " + str(x))
#     x = x + 20
#     print("x wewnątrz funkcji = " + str(x))
#     global y
#     y=z+30

# zmienX(50)
# print("x poza funkcją = " + str(x))
# print("x poza funkcją = " + str(y))


# def czyJestUlamkiem(a):
#     if a%1==0:
#         print('Liczba ' + str(a) + ' nie jest ułamkiem')
#     else:
#          print('Liczba ' + str(a) + ' jest ułamkiem')

# czyJestUlamkiem(2/3)


# def potegowanie(a,r):
#     potega = 1
#     if r < 0:
#         print('Ujemny wykładnik potęgi.')
#     else:
#         if r > 0:
#             for i in range(r):
#                 potega = potega * a
#         print('Wynik potęgowania: ' + str(potega))

# potegowanie(2,0)

# def silnia(a):
#     silnia = 1
#     if a <= 0:
#         print('Brak wyniku.')
#     else:
#         for i in range(1,a+1):
#             silnia=silnia*i
#         print('Silnia wynosi: '+str(silnia))

# silnia(20)

osoba = {
    'imie': 'Robert',
    'nazwisko': 'Burek',
    'rokUrodzenia': 1977
}

print(osoba['imie'])
print(osoba['nazwisko'])
print(osoba['rokUrodzenia'])

osoba['rokUrodzenia'] = 1970
print(osoba)
