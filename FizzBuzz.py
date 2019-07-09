wynik=''
for i in range(1,101):
    if (i)%3==0:
        wynik='Fizz'
    if (i)%5==0:
        wynik='Buzz'
    if (i)%3==0 and i%5==0:
        wynik="Fizz Buzz" 
    if len(wynik)==0:
        print((i))
    else:
        print(wynik)
    wynik=''

print('')
print('W drugą strone:')
print('') 

wynik=''
for i in range(0,100):
    if (100-i)%3==0:
        wynik='Fizz'
    if (100-i)%5==0:
        wynik='Buzz'
    if (100-i)%3==0 and (100-i)%5==0:
        wynik="Fizz Buzz" 
    if len(wynik)==0:
        print((100-i))
    else:
        print(wynik)
    wynik=''
