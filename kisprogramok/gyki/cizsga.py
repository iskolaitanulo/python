def sikeres (pontszám):
    if pontszám>=48:
        return True
    else:
        return False
név = None

while név != " ":
    név = input('Add meg a vizsgázo nevét')
    if név:
        pontszám = int(input('Add meg a pontszamot'))
        if sikeres(pontszám):
            print(név, 'vizsgaaja siekresaw' )
        else:
            print(név,'csalodás vagy bróm')
    