class Vizsgazo():
    def __init__(self): #Konstruktor
        self.nev = input("Adja meg a nevet")
        self.pont = int(input('Adja meg pontszam'))
    def sikeres(self):
        if self.pont >= 48:
            return True
        else:
            return False

diak = Vizsgazo()#Példány
print(diak.sikeres()) 