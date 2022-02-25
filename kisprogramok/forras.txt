visszaszamla = int(input('adja meg pozitiv szam'))
ora = visszaszamla
while visszaszamla != 0:  
    print(visszaszamla)
    asd = input('felfuggeszted?')
    if asd == 'igen':
        ora += 1
        print('felfuggesztve')
    else:
        print('nem')
        visszaszamla -= 1

if visszaszamla == 0:
    print('kiloves')

print('ennyi ora telt el',ora)
#jozsi copyright all rights reserved