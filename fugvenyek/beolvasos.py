atlag = 0                      

with open(r"M:\JanzsóG\.10B_2021\python10.txt","w+") as f:  # be.txt megnyitása olvasásra
    osszeg = 0                  # a beolvasott számok összege (az átlaghoz kell)
    darab = 0                   # hány számot olvastunk be (az átlaghoz kell)

    sor = f.readline()          # első sor beolvasása

    while sor:                  # amíg van sor a fájlban...
        osszeg += int(sor)      # ...hozzáadjuk az adott számot az összeghez
        darab += 1              # ...növeljük a beolvasott számok darabszámát
        sor = f.readline()      # ...beolvassuk a következő sort

atlag = osszeg / darab          # az átlag az összeg és a darabszám hányadosa

with open("ki.txt", "w") as f:  # ki.txt megnyitása
    f.write("Az átlag: " + str(atlag) + "\n")  # az eredmény fájlba írása