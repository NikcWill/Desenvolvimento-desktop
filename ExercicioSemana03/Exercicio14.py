from Exercicio11 import validador

listaNomes = ["Ana", "João", "Maria", "Pedro", "Sofia"]
lista = validador()


arr = [1, 2, 3, 4 ['ana', 'joao', 'pedro', 'maria']]


def montadorLista (lista1, lista2):
    novaLista = []
    for i in lista1:
        if type(i) == list:
            novaLista.append(montadorLista(i))
        elif type(i) != str:
            novaLista.append(str(i))
        else:
            novaLista.append(i)
    for i in lista2:
        if type(i) == list:
            novaLista.append(montadorLista(i))
        elif type(i) != str:
            novaLista.append(str(i))
        else:
            novaLista.append(i)
    return novaLista


resultado = montadorLista(lista, listaNomes)

strmontada = ' '.join(str(x) for x in resultado)
print(strmontada)
print(type(strmontada))