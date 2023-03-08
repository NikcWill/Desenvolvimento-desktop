import re

exp = re.compile(r'^\d+$')
print('Exercicio 11 começa aqui')


def montadorDeList(qtd: int):
    lista = []
    for item in range(qtd):
        lista.append(int(input('digite um numero a ser acrecentado a lista: ')))
    return lista


def validador():
    while True:
        n = input(' Escreva a quantidade de itens a se gerar: ')
        if exp.match(n):
            return montadorDeList(int(n))
        else:
            print('Numero preenchido incorreto')


if __name__ == '__main__':
    print(validador())
