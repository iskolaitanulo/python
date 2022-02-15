szo1 = input('adjon meg egy szot')
szo2 = input('adjon meg egy szot')
x1 = len(szo1)
x2 = len(szo2)
if x1 > x2:
    print('elso szo nagyobb')
elif x1 == x2:
    print('egyenloek')
else:
    print('masodik szo nagyobb')