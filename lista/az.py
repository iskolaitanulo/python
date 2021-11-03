forrasfajl = open('raspberries.txt','w',encoding='utf8')
rpik = []
for sor in forrasfajl:
    rpik.append(sor.strip().split(';'))
forrasfajl.close()