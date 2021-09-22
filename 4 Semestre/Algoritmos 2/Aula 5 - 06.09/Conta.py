class Conta:

    def __ini__(self):
        self.__saldo = 0.0

    def __descontarTarifa(self):
        self.__saldo -= 1.99

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__descontarTarifa()
            print("Valor depositado")
        else:
            print("Valor não permitido")

    def sacar(self, valor):
        if valor > 0:
            self.__saldo -= valor
            self.__descontarTarifa()
            print("Saque depositado")
        else:
            print("Valor não permitido")

    def getSaldo(self):
        return self.__saldo