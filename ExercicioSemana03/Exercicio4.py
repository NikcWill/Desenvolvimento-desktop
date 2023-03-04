import random

i = 0
list = []
separador = ","

while True:
    n = random.randint(20, 1580)
    if i >= 10:
        break
    list.append(n)
    i += 1

resultado = separador.join(str(item) for item in list)
print(resultado)