wr = open('vizsgazok.txt','w')
nev = None
def sikeres(pontszam):
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
        if sikeres(pontszam):
            print("vizsgaja sikeres")
            wr.write('vizsgaja sikeres')
        else:
            print('nem ment át a vizsgan')
            wr.write('nem ment át a vizsgan')
wr.close()

