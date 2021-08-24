from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica
from Aluno import Aluno

print("---- PESSOA ----")
p1 = Pessoa("Jonatha", "(51) 9 9532-5882")
p1.imprimir()

print("---- FISICA ----")
f1 = Fisica("João", "(51) 9 123456", "000.000.000-00")
f1.imprimir()

print("---- JURIDICA ----")
j1 = Juridica("SENAC", "(51) 9 123456", "XX. XXX. XXX/0001-XX")
j1.imprimir()

print("---- ALUNO ----")
a1 = Aluno("Joaozinho", "5111111", "000.000.000-54", "ABC35")
a1.imprimir()