#zsák
wr = open('zsák.txt','w')
zs = [2,9,19,20,5,7,11]
total = sum(zs)
darab = len(zs)
atlag = total/darab
print(f'Átlag {atlag}')
print(f'a zsák össztömege {total} kg')
wr.write(f'Átlag {atlag}')
db = 0
for i in zs :
    if i>5:
        db+=1 
print(f'A listában 5nél nagyobb szam')    


n = len(zs)
ker = 5
i = 0
while i < n and zs[i] != ker:
    i = i +1

if i<n:
    print("Van ilyen az ötödik helyen:", ker)
else:
    print("nincs ilyen elem", ker)

wr.close()