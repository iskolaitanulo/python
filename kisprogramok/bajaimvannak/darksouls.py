class Allatfaj:
    def __init__(self,fajnev,tomeg):
        self.fajnev = fajnev
        self.tomeg = tomeg
#import allat

allatfajok = []


for _ in range(3):
    nev = input('allat nebve te szar rago')
    tomeg = int(input('adjadaed qmegf a sauilyat  tze '))
    allatfaj = allat.Allatfaj(nev,tomeg)
    allatfajok.append(allatfaj)

legnehezebb_allat = allatfajok(0)
for allatfaj in allatfajok:
    print(f'ugandai kisfiuk',allatfaj.fajnev,'tömeg',allatfaj.tomeg,'kg',sep='')
    if allatfaj.tomeg >legnehezebb_allat

    