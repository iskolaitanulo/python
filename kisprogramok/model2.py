wr = open('model.txt','w')
def hanyeves(kor):
    if kor < 20:
        return('csitri')
        
    elif kor == 20:
        return('alkalmazhato')
    else:
        return('vén')
def mennyimagas(magassag):
    if magassag >= 170 and magassag <= 175:
        return('nagyon jo')
    else:
        return('nem naon jo')

kor = int(input('Hany eves'))
model = input('model neve?')
magassag = int(input('Mennyi magasaga'))
print(hanyeves(kor))
print(mennyimagas(magassag))
print(model)
wr.write(hanyeves(kor))
wr.write(mennyimagas(magassag))
wr.write(model ) 
wr.close()
#Józsi copyright