elsooktett = int(input('Adja meg az ip cim első okttetjét'))
masodikoktett = int(input('adja meg az ip cim második oktettjét'))


def tipus():
    if elsooktett <= 127:
        return('A tipusu')
    elif elsooktett <= 191:
        return('B tipus')
    elif elsooktett <= 223:
        return('C tipusu')
    elif elsooktett <= 239:
        return('D tipusu csoportos')
    elif elsooktett <= 255:
        return('E tipusu kisérleti')
def priv():
    if elsooktett == 10:
        return('privát A')
    elif elsooktett == 172 and masodikoktett <=31:
        return('privát B')
    elif elsooktett == 192 and masodikoktett == 168:
        return('privát C')

print(tipus())
print(priv())




