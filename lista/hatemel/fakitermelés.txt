import random
wr = open("fa.txt","w")
fa = []
for x in range(32):
    x = random.randrange(50,100)
    wr.write(str(x))
    print(x)
fa.append(x)
wr.write(f' ennyi egy napi{x}')
print(f'ennyi egy havi{x}')
napok = (len(fa))
print(f'{napok}')
wr.write({napok})
összes = (sum(fa))
wr.write({összes})
print({összes})
átlag = (sum(fa)/len(fa))
wr.write({átlag})
print(sum(fa)/len(fa))


legkevesebb = min(fa)
legtöbb = max(fa)
legkisebb_szama = fa.index(legkevesebb)
legnagyobb_szama= fa.index(legtöbb)
print(f"A legkevesebb termelés  {legkevesebb} volt, a {legkisebb_szama}. napon.")
napok = fa.index(legtöbb)
print(f"A legnagyobb termelés {legtöbb}ennyi volt és ezen a napon {legnagyobb_szama} ")

