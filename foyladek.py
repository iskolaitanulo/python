össz = 0

while össz <= 35 and (ivás:=int(input('Hány decit itá'))):
    print(f'Már{(össz:=össz+ivás)/10:3.1f} litert itál')
    if össz >= 25:
        print('Már sikerült elérned a 2.5 litert')
print('béka nö a hasadba')