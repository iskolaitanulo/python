elsooktett = int(input('Adja meg az ip cim első okttetjét'))
masodikoktett = int(input('adja meg az ip cim második oktettjét'))
if elsooktett <= 127:
    print('A tipusu')
elif elsooktett <= 191:
    print('B tipus')
elif elsooktett <= 223:
    print('C tipusu')
elif elsooktett <= 239:
    print('D tipusu csoportos')
elif elsooktett <= 255:
    print('E tipusu kisérleti')

if elsooktett == 10:
    print('privát A')
elif elsooktett == 172 and masodikoktett <=31:
    print('privát B')
elif elsooktett == 192 and masodikoktett == 168:
    print('privát C')


