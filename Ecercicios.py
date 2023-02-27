
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
    print('os textos são diferentes!')'''