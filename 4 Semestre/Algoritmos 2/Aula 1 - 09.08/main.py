#Sem Parametros e sem retorno
def imprimirOla():
    print("Olá Pessoal")
    print("Bem-vindos ao novo semestre")


#Com parâmetros e com retorno
def getCalculaSalario(horas, valorHora):
    salario = horas * valorHora
    return salario


#Com parâmetros e sem retorno
def imprimirSalario(horas, valorHora):
    salario = horas * valorHora
    print("Salário: ", salario)

#Com parâmetros e sem retorno
def imprimirSalario2(horas, valorHora):
    salario = getCalculaSalario (horas, valorHora)
    print("Salario: ", salario)
    .


#Sem parâmetros e com retorno
def getValorPI():
    return 3.14


areaCirculo = getValorPI() * (2* 2) 
print("Área do circulo com raio 2: ", areaCirculo)

imprimirSalario2(100, 20)

carros = ["Uno", "Doblo", "Toro"]
print(carros)

print(carros[1])

posicao = int(input ("Informe a posição do veiculo (de 0 a 2): "))

print("Carro Selecionado: ", carros[posicao])

