class Restaurante:

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.aberto = False

    def descreva_restaurante(self):
        print(f'O {self.nome} é um restaurante de tipo {self.tipo_cozinha}')

    def abrir_restaurante (self):
        if self.aberto == False:
            print(f'O restaurante {self.nome} abriu agora')
            self.aberto = True
        else:
            print('O restaurante já está aberto')


    def fechar_restaurante (self):
        if self.aberto == True:
            print(f'O restaurante {self.nome} fechou agora')
            self.aberto = False
        else:
            print('O restaurante já está fechado')

r1 = Restaurante('mane da ilha', 'churracaria')

r1.descreva_restaurante()

r1.abrir_restaurante()
r1.abrir_restaurante()
r1.fechar_restaurante()
r1.fechar_restaurante()
