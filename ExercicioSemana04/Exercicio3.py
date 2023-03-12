import re

inteiros = re.compile(r'^[1-9]\d*$')
quebrados = re.compile(r'^\b\d+\.\d+\b$')


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calculador(self):
        i = self.base * self.altura
        print('A area do retangulo é: ')
        return float(i)


    @staticmethod
    def validador():
        while True:
            n = input(' Escreva o numero: ')
            if inteiros.findall(n):
                return int(n)
            elif quebrados.findall(n):
                return float(n)
            else:
                print('Numero preenchido incorreto')


r = Retangulo(Retangulo.validador(), Retangulo.validador())
print(r.calculador())
