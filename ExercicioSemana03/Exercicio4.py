import random

i = 0
list = []


while True:
    n = random.randint(20, 1580)
    if i >= 10:
        break
    list.append(n)
    i += 1

for numero in list:
    print(numero)