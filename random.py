import random

egyik = random.randint(1,10)
másik = random.randint(1,10)
összeg =egyik+másik
print(összeg)
if összeg%2==0:
    print('páros')
else:
    print('páratlan')

