#kissebb.py
wr = open('kissebb.txt','w')
szam1 = int(input('adjon meg egy szamot'))
szam2 = int(input('adjon meg mégegy számot'))
if szam1 > szam2:
    print('Az első szám a nagyobb')
    wr.write('Az első szám nagyobb')
else:
    print('második szám a nagyobb')
    wr.write('második szám a nagyobb')
wr.close()