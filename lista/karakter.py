szoveg = 'szoveg'
lista =['l','i','s','t','a']

print(szoveg)
print(lista)

print("".join(lista))

print(szoveg[0],szoveg[-1])
print(lista[0],lista[-1]) 

for karakter in szoveg:
    # print(len(szoveg))
    print(karakter,' ', end = '')
    # ha minden ármányság igaz
print('')

for elem in lista:
    print(elem,' ', end = '')

mondat = None
while mondat != '':
    mondat = input('Kérek egy mondatot')
if len(mondat) >0:
     if mondat[-1] != '.' and mondat[-1] != '!' and mondat[-1] != '?':
        print('kys')
else:
        print('gg')