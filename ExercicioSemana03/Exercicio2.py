import re

frase = 'Paulo é d4veloper e um b0m musico'
lista = frase.split()

for i in lista:
    for c in i:
        if re.match(r'^[0-9]$', c):
            print(i)
