wr=open('monog.txt','w')

def monogram(nev):
    szokosz = nev.index(' ')
    return nev[0] + '. ' + nev[szokosz+1] +'.'
nev = input('irjabe')
print(nev,'monogramja:',monogram(nev))

def kisnagy(nev):
    return "nagy " + nev.upper() + "kisbetus " + nev.lower()
print(kisnagy(nev))
wr.write(f'{kisnagy(nev)}')


