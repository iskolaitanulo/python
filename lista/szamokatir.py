szam = None
def pozneg(szam):
    if szam > 0:
        print(szam,'pozitiv')
    elif szam < 0:
        print(szam,'negativ')
    else:
        print('A szám nulla mint az iqm')

while szam != " ":
    szam = input("pakolja ki")
    if szam != " ":
        szam = float(szam)
    pozneg(szam)

wr = open("SJ.txt","w")
wr.write(szam)
wr.close()



