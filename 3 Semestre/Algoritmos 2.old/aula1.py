def imprimirPi():
    print("Valor do Pi:")
    print(3.14)

#imprimirPi()

def getSalario():
    return 1045.0

#print( getSalario() )

def calcular_imprimir_area (largura, comprimento):
    area = float(largura) * float(comprimento)
    print(area)

calcular_imprimir_area(2,3)

def calcula_area (largura, comprimento):
    area = float(largura) * float(comprimento)
    return area

altura = 5
volume = altura * calcula_area(4,6)
print(volume)