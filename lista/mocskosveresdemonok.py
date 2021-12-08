import random , codecs

szam1 = random.randrange(10,50)
szam2 = int(input("szam"))
SZAM3 = 420
print(szam1,szam2,SZAM3)
if SZAM3%2 == 0:
    print("paros") 
else:
    print("paratlan")

wr = open('fajazelet.txt','w')
wr.write('adssdasdsdassddasd')
wr.close

wr = codecs.open('bajok.txt','a', encoding='utf8')
wr.write = ('szeretem a pitont (ironia)')
print(wr)
wr.close

f = open("fajazelet.txt")
tartalom = f.read()
print(tartalom)
f.close

lista2=["bruh"]

with open("jozse.txt",'w') as file:
    for item in lista2:
        file.write("%s\n" % item)


f = open('csimgi','r')
tartalom = f.read()




y = open('elérésihely','r')
tartalom = y.read()
print(tartalom)
y.close