class Pessoa1:
    def __init__(self, nome, idade,):
        self.nome = nome
        self.idade = idade


    def __str__(self):
        return str(self.__dict__)


p1 = Pessoa1('joão', 15)

print(p1.__str__())
