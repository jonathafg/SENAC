from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self.__tempoDeBateria = tempoDeBateria

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

    #tempoDeBateria
    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__tempoDeBateria = valor

    def cadastrar(self):
        Notebook.modelo = input("Digite o modelo do seu Notebook: ")
        Notebook.cor = input("Digite a cor do seu Notebook: ")
        Notebook.preco = input("Digite o preco do seu Notebook: ")
        Notebook.tempoDeBateria = input("Digite a duração da bateria do seu Notebook: ")

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self.tempoDeBateria

    #metodo imprimir somente para teste de coleta de dados
    def imprimir(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preco: ", self.preco)
        print("Tempo da Bateria: ", self.tempoDeBateria)