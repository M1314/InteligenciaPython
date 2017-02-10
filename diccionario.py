class Diccionario:
	def __init__(self):
		self.palabras = set()
	
	def carga(self, archivo):
		self.palabras = set(open(archivo).read().split())
		return True
	
	def size(self):
		return len(self.palabras)

	def contiene(self, palabra):
		return palabra.lower() in self.palabras

