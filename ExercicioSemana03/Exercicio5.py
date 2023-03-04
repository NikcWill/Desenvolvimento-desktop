
import ExercicioSemana03.Exercicio4

controle = 0

for numero2 in ExercicioSemana03.Exercicio4.list:
    if numero2 < 1500 and numero2 % 5 == 0:
        if (95 < numero2 < 150):
            controle = numero2 + 1
            print(f'Esse numero está dentro da lacuna 95 a 150 -- {controle} -- ')

        print(f'{numero2} É divisivel por 5 ')
    elif numero2 > 1500:
       print(f"Acabou numero {numero2} é maior que 1500")
       break







