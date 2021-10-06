import cmath , math 
a =input('Irja be azelsőegyütthatót')
a =float(a)
while a==0:
    print('ez a nem jó')
   a =input('Irja be azelsőegyütthatót')
   a =float(a)
b = input('Irja be a másodikegyütthato')
b =float(b)
c = input('Irja be a konstanst')
c =float(c)
d = b*b-4*a*c˘
print('diszkirminánsértéke')
if d>=0
    print('ez a szám valós')
    x1=(-b-cmath.sqrt((d))/2*a
    x2=(-b+cmath.sqrt((d))/2*a
    print('egyik megoldás' , x1)
    print('egyik megoldás' , x2)
    
else:
    print('ez a szám nem valós')
    x1=(-b-cmath.sqrt((d))/2*a
    x2=(-b+cmath.sqrt((d))/2*a
    print('egyik megoldás' , x1)
    print('egyik megoldás' , x2)