szam = int(input('irjon be egy jegyet'))
while szam <=49:
    if szam <= 50:
    print('ötös')     
elif szam <= 29 :
    print('elégtelen')
elif szam <= 37 :
    print('elégséges')
elif szam <= 38 :
    print('közepes')
elif szam <= 49 :
    print('jó')
elif szam <= 55 :
    print('kitünő')
    print('nem ötös')
    szam = int(input('irjon be egy jegyet'))

    
