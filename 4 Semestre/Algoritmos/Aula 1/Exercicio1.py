NomeProdutos = ["Refrigerante", "Cafe", "Batata", "Feijao"]
PrecoProdutos = ["5.50", "3.25", "1.35", "2.00"]
QtdaProdutos = ["5", "15", "8", "22"]

def imprimir_Produto(posicao):
    posicao = int(posicao)
    print(NomeProdutos[posicao], PrecoProdutos[posicao], QtdaProdutos[posicao])
    
def apagar_Produto(posicao):
    posicao = int(posicao)
    NomeProdutos.pop(posicao)
    PrecoProdutos.pop(posicao)
    QtdaProdutos.pop(posicao)
    print(NomeProdutos, PrecoProdutos, QtdaProdutos)


posicao = int(input ("Informe a posição do produto que deseja imprimir e excluir (de 0 a 3): "))

imprimir_Produto(posicao)
apagar_Produto(posicao)
.
