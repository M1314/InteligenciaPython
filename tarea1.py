from diccionario import Diccionario
from Libro import Libro
def main():
		dic = Diccionario()
		dic.carga("words.txt")
		libro = Libro()
		libro.carga("cano.txt")
		
		cont = 0
		contDef = 0
		contInd = 0
		for word in libro.lista():
			if dic.contiene(word):
				print("La palabra ", word, "si esta", "cont: ", cont)
				cont+=1
	 		else:
				print("La palabra ", word, "no esta")

			if word in ["a", "an"]:
				contInd+=1
			if word in ["The", "the"]:
				contDef+=1


		print("Palabras del libro", libro.size())
		print("Palabras del diccionario", dic.size())
		print("Palabras en el diccionario: ", cont)
		print("Veces de 'the' en el libro", contDef)
		print("Veces de 'a' o 'an' en el libro", contInd)
if __name__ == '__main__':
	main()
