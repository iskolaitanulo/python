import random
szam1 = float(input("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
szam2 = random.randrange(10 , 50)
SZAM3 = 5
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
if szam1 % 2 == 0:
    print("elkap az agybaj")
else:
    print("nem kap el az agybaj")
print(szam1, szam2)
