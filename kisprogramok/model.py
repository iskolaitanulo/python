model = input('model neve?')
kor = int(input('Hany eves'))
magassag = int(input('Mennyi magasaga'))
if kor < 20:
    print('csitri')
elif kor == 20:
    print('alkalmazhato')
else:
    print('vén')
if magassag >= 170 and magassag <= 175:
    print('naon jo')
else:
    print('naon nem jo')