from No import No
from Livro import Livro

class Fila(Livro):

	def __init__(self):
	    self.inicio = None
	    self.fim = None
	    self.tamanho = 0

	def adicionar(self, valor):
		no = No( valor )
		if self.tamanho == 0:
			self.inicio = no
			self.fim = no
		else:
			self.fim.proximo = no
			self.fim = no
		self.tamanho += 1
		self.imprimir()


	def imprimir(self):
		texto = ""
		if self.inicio == None :
			texto = "Fila Vazia!"
		else:
			aux = self.inicio
			while ( aux ) :
				texto = texto + str( aux.dado ) + "  -  "
				aux = aux.proximo
		print( texto )
		print(" ---------------------------------------------------")


	def remover(self):
		if self.tamanho == 0:
			print( "Fila Vazia!")
		elif self.tamanho == 1:
			self.inicio = None
			self.fim = None
			self.tamanho = 0
		else:
			self.inicio = self.inicio.proximo
			self.tamanho -= 1
		self.imprimir()