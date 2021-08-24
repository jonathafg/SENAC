from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nomeF = None, foneF = None, cpfF = None):
        #Pessoa.__init__(nomeF, foneF)
        super().__init__(nomeF, foneF)
        self.cpf = cpfF

    def imprimir(self):
        super().imprimir()
        print("CPF: ", self.cpf)