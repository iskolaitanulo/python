bevetelek  = [3,8,10,19.35,-6,5.1,9,20]

vendegek = 0

for bevetel in bevetelek:
    if bevetel in bevetelek:    
        vendegek += 1

print('A pincér',round(vendegek/2,2),'font fizut kap ')

#mondat

mondat = ['Én','elmentem','a','vasarba','fél','semmivel']

print('A mondat',len(mondat),'szóbol áll')

legröviddebszo = 1000

for szo in mondat:
    if len(szo) < legröviddebszo:
        legröviddebszo = len(szo)
print('a legrovid', legröviddebszo)

irasjelek = '.?!'

for szo in mondat:
    if szo[-1] in irasjelek:
        print('van')
nevelok = ('a','az','egy')

for szo in mondat:
    if szo in nevelok:
        print('van')
print('a modatatbab a fel szocsdaaszó a ',mondat.index('fél')+1,'heylendas klkpksdflfdk ',sep='')

vannagykbetu = False
holvan = None
for index in range(len(mondat)):
    if mondat[index] [0].isupper():
        vannagykbetu = True
        holvan = index

if vannagykbetu:
    print('a',holvan+1)