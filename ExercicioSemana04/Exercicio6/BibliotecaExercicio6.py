
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar (self, livro):
        self.livros.append(livro)

    def remover (self, livro):
        self.livros.remove(livro)

    def mostrar_detalhes_livros(self):
        for i in self.livros:
            print(
                f'O Titulo do livro é: {i.titulo} \n'
                f'O Autor do livro é: {i.autor} \n'
                f'O Ano do livro é: {i.ano} \n')


