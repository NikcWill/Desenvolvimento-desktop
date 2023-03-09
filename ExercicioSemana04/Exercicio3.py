class Retangulo:
    def __init__(self, base, altura):
        self.base = Retangulo.validador(base)
        self.altura = Retangulo.validador(altura)

    def calculador(self):
        i = self.base * self.altura
        return i

    @staticmethod
    def validador(numero):
        while True:
           if type(numero) == int or type(numero) == float:
                return numero
            else:
                print('Numero preenchido incorreto')





