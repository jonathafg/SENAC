from abc import ABCMeta, abstractmethod, abstractproperty

class Ferramenta(metaclass = ABCMeta):

    #Nome
    @property
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, valor):
        pass
    
    #tensão
    @property
    def tensao(self):
        pass

    @tensao.setter
    @abstractmethod
    def tensao(self, valor):
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
        return self.nome, self.tensao, self.preco


    @abstractmethod
    def cadastrar(self):
        pass