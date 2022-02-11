wr = open('hom.txt','w')
hom= [9,-16,-19,-8,-2,14,15,16,-8,8,-3,-9,-4,-3,18,-17,-7,-1,7,10,-12,14,7,6,-6,-20,10,3]
februar = False

if len(hom) == 20:
    februar = True
    print('igen')
    wr.write('\nigen')
else:
    print('nem')
    wr.write('\nnem')


nap = 0
if -2 in hom:
    nap = hom.index(-2)+1
    print(f'igen ezen a napon{nap}')
    wr.write(f'\nnapocska {nap}')
else:
    ('nem')



hanyszr = 0
for x in hom:
    if x <= -2:
        hanyszr += 1
print(hanyszr)
wr.write(f'\nennyiszer {hanyszr}')

legkevesebb = min(hom)
legtöbb = max(hom)
print(f'legkevesebb {legkevesebb}')
wr.write(f'ennyi {legkevesebb}')
print(f'ennyi a legtöbb{legtöbb}')
wr.write(f'ennyi a legtöbb{legtöbb}')

print(sum(hom)/len(hom))
atlag = (sum(hom)/len(hom))
print(f'atlag {atlag}')
wr.write(f'csori {atlag}')
hoing = (legtöbb-legkevesebb)
print(f'hoinggaaas {hoing}')
wr.write(f'hoingas {hoing}')
wr.close()
#Sólya József copyright  