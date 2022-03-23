def sikeres():

    if pontszam >= 48:
        return ':)'
    elif pontszam == 48:
        return ':D'
    else:
        return ':('


nev = input('Adja meg a nevet')
pontszam =  int(input('Menyi vot ponstazm??'))
while nev != '':
    nev = input('Adja meg a nevet')
    pontszam =  int(input('Menyi vot ponstazm??'))
    print(sikeres())

"""
nev = None

while nev != '':
    nev = input('mia aneeve')
    if nev:
        pontszam = int(input('Mennyi pontot ért el?'))
        if sikeres(pontszam)
            print(nev,'vizsgaja sikeres')
        else:
            print(nev,'vizsgaja sikeretlen')
"""

"""
if pontszam >= 48:
    print(':)')
elif pontszam == 48:
    print(':D')
else:
    print(':(')
"""