from abc import ABCMeta, abstractmethod, abstractproperty

class Computador(metaclass = ABCMeta):

    #Modelo
    @property
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass
    
    #Cor
    @property
    def cor(self):
        pass

    @cor.setter
    @abstractmethod
    def cor(self, valor):
        pass
    
    #Preco
    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass


    def getInformacoes(self):
        return self.modelo, self.cor, self.modelo


    @abstractmethod
    def cadastrar(self):
        pass



