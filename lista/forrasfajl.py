nev = input("irja be a nevet")
ev = int(input("irja be az évkorát"))
while ev > 18:
    print("evkor tul nagy")
    ev = int(input("irja be az évkorát"))

if ev <= 3:
    print("Totyogóknak a kettes számrendszerről")
elif ev <= 6:
    print("Hackeljük meg az óvodát!")
elif ev <= 14:
    print("Felhőtechnológia a menzán")
elif ev <= 18:
    print("Big data a középiskolában")
az = "{0} éves vagy és neved{1}".format(ev,nev)

print(az)
print(5*5*5*5**5*5*5*5*5*5*5*5*5*5*5*5**5*5*5*5*5*5*5*5*55*5*5*5*5**5*5*5*55**5*5*5*5*5*5*5*5**55*5*5*5*5*5**5*5*5*5*5*5*5*5*5*5*5*5)