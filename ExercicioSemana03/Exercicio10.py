
import Ercecicio9

lista10 = Ercecicio9.listaAlterada
print('começando Exercicio 10')
'''for elemento in lista10:
    if type(elemento) == list:
        for subElemento in elemento:
            if type(subElemento) == str:
                print(len(lista10))
    else:
        print(str(elemento))'''



def remove_strings(lista):
    nova_lista = []
    for item in lista:
        if isinstance(item, list):
            nova_lista.append(remove_strings(item))
        elif not isinstance(item, str):
            nova_lista.append(item)
    return nova_lista

nova_lista10 = remove_strings(lista10)

print(nova_lista10)








