a= "Helló, Világ!"
tt = a.upper()
print(tt)

a = "Hello, World!"
print(a.lower())

#A replace()módszer egy karakterláncot egy másik karakterlánccal helyettesít:
a = "Hello, World!"
print(a.replace("H", "J"))

txt = "I like bananas"
x = txt.replace("bananas", "apples")

#A strip()módszer eltávolítja a szóközöket az elejéről vagy a végéről:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#A split()metódus részláncokra osztja a karakterláncot, ha megtalálja az elválasztó példányait:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Konkatenáció
a = "Hello"
b = "World"
c = a + b
print(c)

#Ha szóközt szeretne hozzáadni közéjük, adjon hozzá egy " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

gyumolcs = "banán"
m = gyumolcs[1]
print(m)

m = gyumolcs[0]
print(m)

lista = list(enumerate(gyumolcs))
print(lista)
primek=[2,3,5,7,11,13,17,19,23,29,31]
p4 =primek[4]
print(p4)

gyumolcs ="banán"
hossz = len(gyumolcs)
print(hossz)

sz = len(gyumolcs)
utolso = gyumolcs[sz-1]
print(utolso)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i+=1

for c in gyumolcs:
    print(c)

elotag="Törp"
utotagok_listaja = ["erős","költő","morgó","öltő","papa","picur","szakál"]
for utotag in utotagok_listaja:
    print(elotag + utotag)

s ="A Karib-tenger kalózai"
print(s[0:1]) 
print(s[2:14])
print(s[15:22])

gyumolcs="banán"
gy = gyumolcs[:3]
print(gy)
gy = gyumolcs[3:]
print(gy)
gy = gyumolcs[3:999]
print(gy)

txt = "Hello,welcome to my world."
x = txt.find("welcome")
y = txt.find("w")
print(x)

nev = "jozsi"
kor=69
s2= "A nevem {1}, és {0} éves vagyok.".format(kor,nev)
print(s2)


