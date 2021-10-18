from Furadeira import Furadeira
from Lixadeira import Lixadeira

print("--------------------------------------------------------------------------------")
print("Escolha entre as opções abaixo qual ferramenta você deseja cadastrar: ")
print("1 - Lixadeira: ")
print("2 - Furadeira: ")
print("--------------------------------------------------------------------------------")
opcao = int(input(""))
if opcao == 1:
    d1 = Lixadeira
    d1.cadastrar(Lixadeira)
    
elif opcao == 2:
    d1 = Furadeira
    d1.cadastrar(Furadeira)
else:
    print("Você informou um valor invalido")

