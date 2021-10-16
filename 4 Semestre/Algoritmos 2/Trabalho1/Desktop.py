from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self._potenciaDaFonte = potenciaDaFonte

    #modelo
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    #Cor
    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    #Preco
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    #potenciaDaFonte
    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        self._potenciaDaFonte = valor

    def cadastrar(self):
        Desktop.modelo = input("Digite o modelo do seu Desktop: ")
        Desktop.cor = input("Digite a cor do seu Desktop: ")
        Desktop.preco = input("Digite o preco do seu Desktop: ")
        Desktop.potenciaDaFonte = input("Digite a potencia da fonte do seu Desktop: ")

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self.potenciaDaFonte

    #metodo imprimir somente para teste de coleta de dados
    def imprimir(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preco: ", self.preco)
        print("Potencia da Fonte: ", self.potenciaDaFonte)

