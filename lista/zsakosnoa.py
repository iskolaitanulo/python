import random

zsákok =[5,6,3,7,88,7.11] 
nap = "kicsi"
hetnapja = None
for index in range(len(zsákok)):
    if zsákok[index] == nap:
        melyiknap = index
        hetnapja = True
        break
if hetnapja:
    print(f's legkisebb zsakot a het kovi napjan emelgette {melyiknap + 1}')
#copyright 2022 József Sólya production
for zsák2 in range(7):
    zsák2.append(random.randit(5,50))
print(zsák2)
