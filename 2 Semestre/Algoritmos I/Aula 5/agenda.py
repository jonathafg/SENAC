agenda = {'joao': '111', 'ana': '222', 'claudio': '333', 'pedro': '444'}

'''
inserir dados no dicionario
'''

#for x in range(4):
#    nome = input("Nome:")
#    telefone = input("Telefone: ")
#    agenda[nome] = telefone

'''
Alterar dados do dicionario
'''
#print('Agenda completa (dicionario) \n' ,agenda)
#nome = input("Nome para Localizar na agenda: ")
#novoTelefone = input("Digite o novo número de telefone: ")
#agenda[nome] = novoTelefone

'''
Deletar dados do dicionario
'''
#nome = input("Nome para Excluir da lista: ")
#del (agenda[nome])

print(agenda)

print("Agenda Completa (Dicionario) \n", agenda)
for chave in agenda.items():
    print(chave)



