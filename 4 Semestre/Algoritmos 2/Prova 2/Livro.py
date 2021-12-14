from Autor import Autor
class Livro(Autor):

    def __init__(self, id, titulo, autor: Autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def cadastrar(self):
        Livro.id = input("Digite o id do seu Livro: ")
        Livro.titulo = input("Digite o titulo do seu Livro: ")
        Livro.autor = input("Digite o autor do seu Livro: ")
