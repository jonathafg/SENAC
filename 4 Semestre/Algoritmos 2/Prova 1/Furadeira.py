from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, potencia):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._potencia = potencia

    #nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    #tensao
    @property
    def tensao(self):
        return self._tensao

    @tensao.setter
    def tensao(self, valor):
        self._tensao = valor

    #Preco
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    #potencia
    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, valor):
        self._potencia = valor


    def getInformacoes(self):
        return self.nome, self.tensao, self.preco, self.potencia
    

    def cadastrar(self):
        Furadeira.nome = input("Digite o nome da sua Furadeira: ")
        Furadeira.tensao = input("Digite a tensao da sua Furadeira: ")
        Furadeira.preco = input("Digite o preco da sua Furadeira: ")
        Furadeira.potencia = input("Digite a potencia da sua Furadeira: ")


