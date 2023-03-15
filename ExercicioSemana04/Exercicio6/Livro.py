class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    def imprimir (self):
        print(f'O Titulo do livro é: {self.titulo} \n'
              f'O Autor do livro é: {self.autor} \n'
              f'O Ano do livro é: {self.ano} \n')


