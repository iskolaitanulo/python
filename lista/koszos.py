import random
def nem():
    vizsgalt = nev
    if vizsgalt in lista:
        print("benne van")
    else:
        print('Nincs benne')



nev = input('kérem adja meg a nevét')
print(nev)

jatek = ["dobokocka","pontaz","köcsög"]
ajandek = random.choice(jatek)
print(f' {nev} a kovetkezot kapta {ajandek}')


lista = ['sandi','Anfi','az','bruh']
nem()