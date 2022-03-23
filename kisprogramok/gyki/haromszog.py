import math
a = int(input("első oldal"))
b = int(input("masodik oldal"))
c = int(input("harmadik oldal"))
s = (a+b+c)/2
elsoszog = math.sqrt(s*(s-a)+(s-b) + (s-c))

a1 = int(input("első oldal"))
b1 = int(input("masodik oldal"))
c1 = int(input("harmadik oldal"))
s1 = (a1+b1+c1)/2
mashszog = math.sqrt(s1*(s1-a1)+(s1-b1) + (s1-c1))

if elsoszog < mashszog:
    print("elso hszög nagyobb")
elif elsoszog < mashszog:
    print("az eéső hszög nagyobb")
else:
    print('ketto egyenlo')