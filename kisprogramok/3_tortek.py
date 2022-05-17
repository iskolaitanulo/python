class Tortek:
    def kiir(self):
        print(self.szamlalo/self.nevezo)
    def beker(self):
        self.szamlalo = int(input('Kérem a számlálót'))
        self.nevezo = int(input("Kérem a nevezőt"))
    def szamlalotad(self):
        return self.szamlalo
tort = Tortek()
tort.nevezo = 6
tort.szamlalo = 12
tort.kiir()