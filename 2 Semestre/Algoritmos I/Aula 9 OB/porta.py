class Porta:
    def __init__(self):
        self.altura = 210
        self.largura = 80
        self.cor = None
        self.status = False
    
    def pintar_porta(self, cor):
        self.cor = cor

    def abrir_porta(Self):
        self.status = True

    def fechar_porta(self):
        self.status = False

    def mostrar_status_porta(self):
        print("Status:",self.status)
        print(" Alt.",self.altura, "Larg.",self.largura, " Cor:",self.cor)


print("=============")
porta2 = Porta()
porta2.pintar_porta("Vermelho")
porta2.fechar_porta()
porta2.abrir_porta()

