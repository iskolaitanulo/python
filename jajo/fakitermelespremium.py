import random

wr = open("fa.txt","w")
fa = []
szam = 0
while szam != 31:
    kitermeles = random.randit(50,100)
    fa.append(kitermeles)
    szam += 1

össz = 0
for megtermelt in fa:
    össz += megtermelt
print(f"A márciusi összes fatermeles {össz}")
wr.write(f"A márciusi összes fatermeles {össz}")

átlag = össz/len(fa)
print(f"AS márciusi kitermeles fa átlaga: {átlag}")
wr.write(f"/nA marciusi kitermelt fa átlaga:{átlag}")
legkisebb = min(fa)
legnagyobb = max(fa)
"""
for i in fa
    if i < legkisebb
        legkisebb = i
    elif i > legnagyobb
        legnagyobb = i 
"""
print(f"a legkisebb{legkisebb} és legnagyobb {legnagyobb}")
wr.write(f"a legkisebb{legkisebb} és legnagyobb {legnagyobb}")

if 40 in fa:
    print("Volt olyan nap,amikor 40 volt a kitermelt fa")
    wr.write("Volt olyan nap,amikor 40 volt a kitermelt fa")
else:
    print("nem vót")
    wr.write("nem vót")

van40 = False
for x in fa:
    if x ==40:
        print("Vanilyen")
        van40 = True
        break
    else:
        print("nnininincs")

nagytermelesszam = 0
nagytermelesossz = 0
for x in fa:
    if x > 70:
        nagytermelesszam += 1
        nagytermelesossz += x
össztermelesszaza = nagytermelesossz/össz*100