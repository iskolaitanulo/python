import math
import random
import math
"""
bejutott = False
 
while not bejutott:
    felhasznalonev = input("Kérem a nevét a kollegának maga ön!!!44!!")
    jelszo =  input('kérem adja meg a kártyaszámát nevét mindent')
if felhasznalonev == "teknos99" and jelszo == "almafa12":
    print("Belépés engedélyezve")
    bejutott = True
else:
    print('Belépés nem  cs brom ')
"""
def nevelo():
    magganggahazogannak = 'aáeéiíoöőuú'
    for _ in range(3):
        szo = input('adjon meg fonevet')
        if szo[0].lower() in magganggahazogannak:
            print(f'magánhangzoval kezdodik az {szo.upper()}')
            pass
        else:
            print(f'szo massalhangzoval kezdodik a {szo.upper()} ')
        
def jelzo():
    return random.choice(['piros', 'nagy', 'konnyed'])

nevelo()

# henger 
class Henger:
    def __init__(self,sugar,kozzeppont = (0,0) , magassag = 10):
        self.kozzeppont = kozzeppont
        self.sugar = sugar
        self.magassag = magassag
    def terulet (self) : 
        return self.sugar*pow(math.pi,2) 
    def felszin 
        pass

