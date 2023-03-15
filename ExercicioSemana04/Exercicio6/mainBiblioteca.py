from ExercicioSemana04.Exercicio6.Livro import Livro
from ExercicioSemana04.Exercicio6.BibliotecaExercicio6 import Biblioteca

minha_bib = Biblioteca()
livro1 = Livro('As Cronicas de narnia', "CS Lewis", 1954)
livro2 = Livro('O imbecil coletivo', 'Olavo de carvalho',2020)
livro3 = Livro('Python para iniciantes', 'Chrystian', 2023)

lista_livros = [livro1,livro2,livro3]

for liv in lista_livros:
    minha_bib.adicionar(liv)

minha_bib.mostrar_detalhes_livros()