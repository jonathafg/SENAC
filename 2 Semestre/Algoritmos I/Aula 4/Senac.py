menu = '''
Menu                                        

    0-  Finalizar                           
    1-	Cadastrar sala na lista              
    2-	Listar salas cadastradas             
    3-	Alterar a numeração de alguma sala   
    4-	Excluir uma sala da lista            
    5-	Relatório de sala por andar          

Escolha: '''

menu_alteracao = '''

Menu Alteração 

    1-  Sala                        
    2-	Andar                       
    3-	Capacidade da Sala          
    4-	Quantidade de Computadores  
  
    Escolha: '''

ListaDeSalas            = []
ListaDeAndar            = []
ListaDeCapacidadeAlunos = []
ListaDeQtdComputadores  = []

def CadastraSala ():
    while True:
        sala = input("Informe o número da sala que deseja Cadastrar: ")
        if sala in ListaDeSalas:
            input("Sala já Cadastrada, insira uma nova sala! ")
        else:
            return sala

def CadastraAndar ():
    andar = input("Informe o andar da sala que deseja Cadastrar: ")

    return andar

def CadastraCapacidade ():
    qtd_maxima = 40
    qtd_minima = 0

    while True:
        try:
            qtd_sala = int(input("informe a quantidade de lugares na sala de Aula: "))
            if qtd_sala >= qtd_minima and qtd_sala <= qtd_maxima:
                return qtd_sala
            input("A Capacidade da sala de Aula deve ser entre 0 e 40! ")
        except:
            input("A capacidade precisa ser informada atráves de númerais! " )

def CadastraQtdComputadores ():
    qtd_minima = 0

    while True:
        try:
            qtd_computadores = int(input("Informe a quantidade de computadores da Sala de Aula: "))
            if qtd_computadores >= qtd_minima:
                return qtd_computadores
            input("A Capacidade da sala de aula deve ser maior ou igual a 0! ")
        except:
            input("A Capacidade precisa ser informada através de númerais! ")

def CadastraDadosSala ():

    ListaDeSalas.append(CadastraSala())
    ListaDeAndar.append(CadastraAndar())
    ListaDeCapacidadeAlunos.append(CadastraCapacidade())
    ListaDeQtdComputadores.append(CadastraQtdComputadores())

''' 
CONVERSAR COM O TIO IVO DEPOIS, POIS NÃO ENTENDI ESTA PARTE E COPIEI DO CÓDIGO DELE
'''

def relatorio_salas():   

    print("    sala - andar - capacidade pessoas - qtde computadores")
    print("    _____________________________________________________")
    for ind,sala in enumerate(ListaDeSalas):
        print("    {0}{1}{2}{3}"
               .format(
                    str(sala).ljust(7), 
                    str(ListaDeAndar[ind]).ljust(8),
                    str(ListaDeCapacidadeAlunos[ind]).center(21),
                    str(ListaDeQtdComputadores[ind]).center(18)
                    )
            )
    input(' [Enter] Continua...')




def Escolhe_sala ():
    relatorio_salas ()

    sala = input("Informe a sala que deseja alterar: ")
    if sala in ListaDeSalas:
        return ListaDeSalas.index(sala)
    input("Esta sala não esta cadastrada! ")
    return Escolhe_sala()



def altera_conforme(ind,opcao):
    if opcao == '1':
        ListaDeSalas[ind]
    elif opcao == '2':
        ListaDeAndar[ind]
    elif opcao == '3':
        ListaDeCapacidadeAlunos[ind]
    else:
        ListaDeQtdComputadores[ind]



def escolhe_que_alterar():
    escolha = input(menu_alteracao)
    if escolha in ('1','2','3','4'):
        return escolha
    input('...Opção não existe no menu. [Enter]')
    return escolhe_que_alterar()


'''
ATÉ AQUI NÃO CONSEGUI FAZER
'''


def alterar_dados_sala():

    altera_conforme(Escolhe_sala(), escolhe_que_alterar())


def Exclui_Sala ():
    relatorio_salas ()

    DigitaSala = input("insira a sala que deseja excluir: ")
    if DigitaSala in ListaDeSalas:
        ind = ListaDeSalas.index(DigitaSala)
        ListaDeSalas.remove(DigitaSala)
        ListaDeAndar.pop (ind)
        ListaDeCapacidadeAlunos.pop (ind)
        ListaDeQtdComputadores.pop (ind)

        input("Sala Removida com Sucesso! ")
    else:
        input("A sala digitada não esta cadastrada no sistema! ")


def imprime_so_andares(lista_andares_cadastrados):
    print('Andares Cadastrados')
    print('-------------------')
    lista_andares_cadastrados.sort()
    for andar in lista_andares_cadastrados:
        print(' '*5,andar)



def andares_cadastrados(): 
    lista_andares_cadastrados = [] # cria lista somente com os andares cadastrados, sem repetição
    def identifica_os_andares():
        for andar in ListaDeAndar:
            if andar not in lista_andares_cadastrados:
                lista_andares_cadastrados.append(andar)

    identifica_os_andares()
    imprime_so_andares(lista_andares_cadastrados)

def escolha_andar():
    andares_cadastrados()
    return input('Escolha o andar: ')

def salas_do_andar(andar):
    print(' '*8,'Salas do',andar,':')
    print(' '*8,'------------')
    for ind,sala in enumerate(ListaDeSalas):
        if ListaDeAndar[ind] == andar:
            print(' '*8,sala)


def relatorio_por_andar():
    salas_do_andar(escolha_andar())
    input('')



escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        CadastraDadosSala()
    elif escolha == '2':
        relatorio_salas()
    elif escolha == '3':
        alterar_dados_sala()
    elif escolha == '4':
        Exclui_Sala()
    elif escolha == '5':
        relatorio_por_andar()
    else:
        input("\n\n Opção Invalida! ")
