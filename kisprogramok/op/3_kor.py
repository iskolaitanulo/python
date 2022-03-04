#OTTVAN BAZDMEGH
import math
import random
class Kor:
    def __init__ (self, zsugar,kozeppont = (0,0)):
        self.kozeppont = kozeppont
        self.zsugar = zsugar

    def terulet(self):
        return self.zsugar*math.pow(math.pi,2) 
    def kerulet(self):
        return self.zsugar*2*math.pi 
    def info(self):
        print(f'A(z) ennyi vót {self.zsugar} egység sugaru,{self.kozeppont} középpontzu kro rtetere {self.terulet():.2f} egyseg kerulete {self.kerulet():.2f}')
#peldanyositas   
kor_01 = Kor(5,(2,6))
kor_01.info()
#medodus
print(kor_01.terulet()) 
#tesztelés
print(type(kor_01))
print(isinstance(kor_01,Kor))

korok = []

for _ in range(5):
    kor = Kor(random.randrange(0,10))
    korok.append(kor)

for kor in korok:
    kor.info()

print('Jenő bite a senpaiom uwu')
print("Lépésharcsa")