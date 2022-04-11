import math 
import random

a = random.randint(2,10)
b = random.randint(2,10)
c = random.randint(2,10)
"""
a = int(input('a oldal '))
b = int(input('b oldal '))
c = int(input('c oldal '))
"""

k = a+b+c
print(a,b,c)

print (f'a háromszög kerülete {a+b+c}')
print('Héron képlet')
s = k/2
ter = s*(math.sqrt(s-a)*(s-b)*(s-c))
print (f'a háromszög területe {ter}')