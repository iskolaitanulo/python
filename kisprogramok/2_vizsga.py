nev = None
def siker(pontszam):
    if pontszam>=48:
        return  True
        
    else:
        return False
        
vizsgazoneve = input('mi a neve')
pontszam = int(input('pontszama'))
while vizsgazoneve != "":
    vizsgazoneve = input('mi a neve')
    if vizsgazoneve:
        pontszam = int(input('pontszama'))
        if siker(pontszam):
            print("vizsgaja sikeres")
            break
        else:
            print('nemlol')
    