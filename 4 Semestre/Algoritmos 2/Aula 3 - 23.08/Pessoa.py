class Pessoa:
    def __init__(self, nomeP = None, foneP = None):
        self.nome = nomeP
        self.fone = foneP

    
    def imprimir(self):
        print("Nome: ", self.nome)
        print("Telefone: ", self.fone)
        