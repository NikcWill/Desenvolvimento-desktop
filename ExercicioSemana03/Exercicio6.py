listacomp = []
print("Os numeros sorteados são: ")

import ExercicioSemana03.Exercicio4

print('Estes numeros são de indice impares !')

for i in ExercicioSemana03.Exercicio4.list:
    listacomp.append(i)

for j in range(len(listacomp)):
    if j % 2 != 0:
        print(listacomp[j])
