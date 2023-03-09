class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.parado = True

    def __str__(self):
        return str(self.__dict__)

    def caminhar(self):
        if self.parado:
            self.parado = False
            return 'andando'
        else:
            return 'Continua andando'

    def parando(self):
        if not self.parado:
            self.parado = True
            return 'parado'
        else:
            return 'Continua parado maluco'


p1 = Pessoa('Nicolas', 12)



print(p1.caminhar(), p1.caminhar())


print(p1.parando(), p1.caminhar(), p1.parando())


