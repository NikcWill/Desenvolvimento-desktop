class Carro:
    def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

    def imprimir (self):
        print(f'A marca do carro é: {self.marca} \n'
              f'O modelo do carro é: {self.modelo} \n'
              f'O Ano do carro é: {self.ano} \n')

c1 = Carro('forde', 'ka','ano')

c1.imprimir()