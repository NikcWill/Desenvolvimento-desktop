
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

print(f'As consoantes são: {consoantes} e num total de {cont}')'''






