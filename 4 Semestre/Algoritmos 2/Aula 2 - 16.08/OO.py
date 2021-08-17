#Criando Classe
class MinhaClasse:
    x = 5

print(MinhaClasse)

#Criando um Objeto
p1 = MinhaClasse()
print(p1.x)

#Metodo construtor da classe
class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = input("Digite o nome: ")

p1 = Pessoa(25)
p1.nome = input("Digite seu nome: ")

print('Nome: ', p1.nome)
print('Idade: ', p1.idade)

#Metodos de uma classe
class Pessoa:
    def __init__ (self,nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Idade:", self.idade)

    p1 = Pessoa("Maria", 25)
    p1.imprimir()