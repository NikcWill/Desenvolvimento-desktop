import re

cont = 1
exp = re.compile(r'^\d+$')

while True:
    n = input('Escreva um número natural que te falo os 10 proximos: ')
    if exp.match(n):
        numValidado = int(n)
        break
    print('O valor não é um número natural válido tente novamente!')

while cont <= 10:
    print(numValidado + cont);
    cont += 1