from abc import ABCMeta, abstractmethod, abstractproperty

class Veiculo(metaclass=ABCMeta):
    @property
    @abstractproperty
    def ano(self):
        pass

    @ano.setter
    @abstractmethod
    def ano(self, valor):
        pass

