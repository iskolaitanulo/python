t = [ 3, 8, 2, 4, 5, 1, 6 ]

n = len(t)
ker = 3

i = 0
while t[i] != ker:
    i = i+1

print("hanyadik helyen van:", i+1)

t = [ 3, 8, 2, 4, 5, 1, 6 ]

n = len(t)
ker = 5

i = 0
while i < n and t[i] != ker:
    i = i +1

if(i < n):
    print('Van' + str(ker) + 'elem')
    print("Helye", i+1)
else:
    print('nincs' + str(ker) + 'elem!')

a = [ 3, 8, 2, 4, 5, 1, 6 ]
b = []

def dupla(num):
    return num *2

for elem in a:
    b.append(dupla(elem))

print(b)


a = [ 3, 8, 2, 4, 5, 1, 6 ]x 
b = []

for elem in a:
    if elem < 5:
        b.append(elem)

print(b)