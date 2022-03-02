class Tortek:
    def __init__(self):
        self.szamlalo = 0
        self.neveto = 1
    
    def kiir(self):
        print("%d/%d" % (self.szamlalo,self.nevezo), end = " ")
    #pass
    
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót:"))
        self.nevezo = int(input("kérem a nevezot:"))
    def szamlalotad(self):
        return self.szamlalo
    def nevezotad(self):
        return self.nevezo
   
#tort.szamlalo = 12
tort = Tortek()
tort.beker()
tort.kiir()
print(tort.szamlalotad())
print(tort.nevezotad())