from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nomeJ = None, foneJ = None, cnpjJ = None):
        #Pessoa.__init__(nomeF, foneF)
        super().__init__(nomeJ, foneJ)
        self.cnpj = cnpjJ

    def imprimir(self):
        print("Razão Social: ", self.nome)
        print("Telefone: ", self.fone)
        print("CNPJ: ", self.cnpj)

