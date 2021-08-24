class Pessoa:
    def __init__ (self, codigo, nome, end, fone):
        self.codigo = codigo
        self.nome = nome
        self.endereco = end
        self.fone = fone


    def imprimir(self):
        print("Nome: ", self.nome)
        print("Endereco: ", self.end)

    
class Fisica(Pessoa):
    def __init__(self, codigo, nome, end, fone, cpf):
        Pessoa.__init__(self, codigo, nome, end, fone)
        self.cpf = cpf




