#Metodo que não recebe parâmetro
#e nao tem retorno
def imprimirPi():
    print(3.14)

#executando o método
imprimirPi()


#Metodo que recebe parametros
#e nao retorna um valor
def calcular_imprimir_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    print(area)

#executando o Metodo
calcular_imprimir_area(2,3)


#metodo que recebe parametro
#e retorna um valor
def calcular_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    return area

#executando o metodo
print(calcular_area(2,3))
.