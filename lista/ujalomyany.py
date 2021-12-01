"""
def aluhuzas():
    for _ in range(10):
        print('-',end='')
    print('')

print('Ez egyfontos figyelmeztetés!')
aluhuzas('')
print('Minden sora nagyon fontos!')
aluhuzas('')
print('')
aluhuzas('')



def aluhuzas(jel):
    for _ in range(10):
        print(jel,end='')
    print('')

print('Ez egyfontos figyelmeztetés!')
aluhuzas('-')
print('Minden sora nagyon fontos!')
aluhuzas('*')
print('k')
aluhuzas('~')
"""
def pluszketto(szam):
    print(szam+2)

print('5+2=', end='')
pluszketto(5)
print('4+2=', end='')
pluszketto(4)

def pluszketto(szam):
    return szam+2

print('5+2=',pluszketto(5))
print('4+2=',pluszketto(4))

def megitel(mondat):
    if len(mondat) > 0:
        if mondat[-1] != '!' and mondat[-1] != '?' and mondat[-1] != '.':
            print('SZABI BUZHETERO')
        else:
            print('igazan szép') 

mondat = None
while mondat != '':
    mondat = input('Irj de ami nem de nem vagy akkor mikro egy mondatot')
    megitel(mondat)
    
def pozneg(szam):
    if szam > 0: 
        print(szam,'pozitiv.')
    elif szam < 0:
        print(szam,'negativ')
    else:
        print('A szam nulla')

szam = None
while szam != '':
    szam = input('irj ide egyet')
    if szam != '':
        szam = float(szam)
        pozneg(szam)
        