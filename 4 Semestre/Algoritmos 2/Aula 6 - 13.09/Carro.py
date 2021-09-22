from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    @property
    def ano(self):
        return self.ano

    @ano.setter
    def ano(self, valor):
        self.ano = valor