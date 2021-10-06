szam = int(input('irjon be egy szamot'))
if szam<=13:
    print('Gyermek') 
elif szam<=17:
    print('Fiatalkoru')
elif szam<=23:
    print('Ifju')
elif szam<=59:
    print('Felnőtt')
elif szam>=60:
    print('idos')