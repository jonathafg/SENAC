
#SET, seta uma variavel, altera uma variavel
#GET, mostra, imprime uma variavel

class Porta:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def setAltura(self,novaAltura):
        self.altura = novaAltura

    def getAltura(self):
        return self.altura


p2 = Porta()
print(p2.altura, '===', p2.largura)

p2.setAltura(200)
print(p2.getAltura(), '===', p2.largura)


p = Porta(210,80)

print(p.altura)


