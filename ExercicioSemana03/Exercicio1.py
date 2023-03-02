
lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']
print(lista_nomes)
for i in lista_nomes:
    if (i is None) or (i == ''):
        lista_nomes.remove(i)

lista_nomes = [nomes.strip() for nomes in lista_nomes]
print(lista_nomes)


