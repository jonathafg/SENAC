from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, rotacoes):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._rotacoes = rotacoes

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

    #rotacões
    @property
    def rotacoes(self):
        return self._rotacoes

    @rotacoes.setter
    def rotacoes(self, valor):
        self._rotacoes = valor


    def getInformacoes(self):
        return self.nome, self.tensao, self.preco, self.rotacoes

    def cadastrar(self):
        Lixadeira.nome = input("Digite o nome da sua Lixadeira: ")
        Lixadeira.tensao = input("Digite a tensao da sua Lixadeira: ")
        Lixadeira.preco = input("Digite o preco da sua Lixadeira: ")
        Lixadeira.rotacoes = input("Digite a qtd de rotacões da sua Lixadeira: ")

