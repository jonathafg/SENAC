class Aluno:
    def __init__(self, codigo = None, nome = None, matricula = None):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matricula: ", self.matricula)