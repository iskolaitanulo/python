import random 


szám1 = float(input('adj meg egy szamot'))
szám2 = random.randrange(10, 50)
SZAM3 = (8)
print(szám1,szám2,SZAM3)

if szám1 % 2==1:
    print("ez a szam páros")
else:
    print("ez szam páratlan")
 
szamok = []
szamok.append(szám1)
szamok.append(szám2)
szamok.append(SZAM3)
print(szamok)
szamok.extend(1,2)
print(szamok)
szamok.remove(1)
print(szamok)
szamok.reverse
print(szamok)
szamok.sort()
print(szamok)
szamok.clear
print(szamok)
halmaz = {}
halmaz.add(szám1)
halmaz.add(szám2)
halmaz.add(SZAM3)
