reggeli = {'vaj','tea','piritos'}
ebed = {}
ebed = set(['halaszlé','kenyer',True])
print(type(ebed))
print(ebed)


reggeli = {'vaj','tea','piritos'}
reggeli.add('víz')
reggeli.remove('tea')
#reggeli.remove('mentális állapot') nhibár ir ki mert nincs ilyena halmazba
reggeli.discard('bármit')


print(reggeli)

print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

gyumikosar = {'eper','alma','szilva','eper'}
fajta = set()
for gyumolcs in gyumikosar:
    fajta.add(gyumolcs)
print(fajta)