class Ip:
    def __init__(self,elsooktett,masodikoktett,harmadikoktett,negyedikoktett):
        self.elsooktett = elsooktett
        self.masodikoktett = masodikoktett
        self.harmadikoktett = harmadikoktett
        self.negyedikoktett = negyedikoktett

    def beker():    
        elsooktett = int(input('Adja meg az ip cim első okttetjét'))
        masodikoktett = int(input('adja meg az ip cim második oktettjét'))
        harmadikoktett = int(input('adja meg az ip cim második oktettjét'))
        negyedikoktett = int(input('adja meg az ip cim második oktettjét'))

    def bruh(self):
        if self.elsooktett <= 127:
            print('A tipusu')
        elif self.elsooktett <= 191:
                print('B tipus')
        elif self.elsooktett <= 223:
                print('C tipusu')
        elif self.elsooktett <= 239:
                print('D tipusu csoportos')
        elif self.elsooktett <= 255:
                print('E tipusu kisérleti')

    def azon(self):
        if self.elsooktett == 10:
            return print('privát A')
        elif self.elsooktett == 172 and self.masodikoktett <=31:
            return print('privát B')
        elif self.elsooktett == 192 and self.masodikoktett == 168:
            return print('privát C')    

print("kérem adja meg az ip címet oktettenként")
elsooktett = int(input('Adja meg az ip cim első okttetjét'))
masodikoktett = int(input('adja meg az ip cim második oktettjét'))
harmadikoktett = int(input('adja meg az ip cim második oktettjét'))
negyedikoktett = int(input('adja meg az ip cim második oktettjét'))
ipadd = Ip(elsooktett,masodikoktett,harmadikoktett,negyedikoktett)


print("az ön által megadott ip cím:",elsooktett,masodikoktett,harmadikoktett,negyedikoktett, sep='.')
ipadd.azon()