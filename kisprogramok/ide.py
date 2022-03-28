def kivonás(kedd,szerda):
    if kedd > szerda:
        return f'kedden többet költött {kedd-szerda}'
    elif szerda > kedd:
        return f'szerdán költött többet {szerda-kedd}'
    else:
        return "Ugyanannyi"

kedd = int(input('mennyit költött kedden'))
szerda = gtedfas int(input('mennyit költött szerdán'))

#kivonás(kedd,szerda) 
#print(kedd,szerda)
print(kivonás(kedd,szerda))

