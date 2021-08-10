menu = '''
0- Finaliza
1- adicionar a lista
2- retirar da lista
3- alterar o numero da sala na lista
4- lista
escolha:
'''
sala = []

def mostra (e):
    if e == '1':
        inserieLista()
    if e == '2':
        retiraLista()
    if e == '3':
        retorno('opção 3')
    if e == '4':
        retorno('opção 4')
        

def inserieLista ():
    numero= input("Informe o numero da sala que deseja inserir na lista: ")
    sala.append(numero)

def retiraLista ():
    print("Sua lista atual, contem os seguintes dados: ")
    for x in sala:
        print(x)
    print("Qual valor você deseja retirar ? ")
    numero = input ("Insira o número da sala que será retirado")
    for x in sala:
        if x == numero:
            sala.remove(x)

def alteraLista ():
    print("Sua lista atual, contem os seguintes dados: ")
    for x in sala:
        print(x)
    numero2 = input("Qual valor você deseja alterar ? ")
    numero = input ("Qual sera o novo valor ?")
    for x in sala:
        if x == numero2:
            sala.index(numero2)
            sala.remove(x)
    


while True:
    escolha = input (menu)
    if escolha == '0':
        break

    mostra(escolha)
