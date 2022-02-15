nev = None
def siker(pontszam):
    if pontszam>=48:
        return  True
        print('sikeres')
    else:
        return False
        print('buko')
vizsgazoneve = input('mi a neve')
pontszam = int(input('pontszama'))
while vizsgazoneve != "":
    vizsgazoneve = input('mi a neve')
    if vizsgazoneve:
        pontszam = int(input('pontszama'))
        if siker(pontszam):
            print("vizsgaja sikeres")
        else:
            print('nemlol')
    