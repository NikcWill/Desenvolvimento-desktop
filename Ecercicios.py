
'''#Exercício 01

nome = input('Escreva seu nome: ').upper()[::-1]

print(nome)

#Exercício 02

str1 = input('Escreva um texto:')
str2 = input('Escreva outro texto: ')

print(f'O primeiro texto é {str1} e tem {len(str1)} letras')
print(f'O primeiro texto é {str2} e tem {len(str2)} letras')

if(len(str1) == len(str2) and (str1 == str2)):
    print('OS textos são iguais')
elif(len(str1) == len(str2)):
    print('Os textos tem o mesmo tamanho, porem são diferentes')
else:
    print('os textos são diferentes!')


#Exercicio03

vogais = ['a','e','i','o','u']
consoantes = []
cont = 0

texto = input("informe um texto: ")

for letra in texto:
    if (letra in vogais):
        consoantes.append(letra)
        cont = cont + 1

print(f'As consoantes são: {consoantes} e num total de {cont}')

#Ercecicio 04

tam = float(input('insira o tamanho do arquivo em MB: '))
vel = float(input('insira a velocidade da sua internet em Mbps: '))

tempo = float((tam/vel)*8)/60

print(f'O tempo estimado em minutos é de {tempo:.2f}')'''

#Exercicio 5


turmas = int(input('Insira o numer de turmas: '))
alunos = int(input('Insira quantidade de alunos'))



