from Fisica import Fisica

class Aluno(Fisica):
    def __init__(self, nomeA = "Joaozinho", foneA = None, cpfA = None, matriculaA = "12345678910"):
        super().__init__()
        self.matricula = matriculaA

    def imprimir(self):
        super().imprimir()
        print("Matricula: ", self.matricula)
