class Libro:
	def __init__(self):
		self.p = list()
	def carga(self, archivo):
		self.p = list(open(archivo).read().split())
		return True
	def size(self):
		return len(self.p)
	def contiene(self, palabra):
		return palabra.lower() in self.p
	def lista(self):
		return self.p
