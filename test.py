from diccionario import Diccionario
def main():
	dic = Diccionario()
	dic.carga("words.txt")
	print(dic.size())
	if dic.contiene("Also") == True:
		print("YEEEESS")

if __name__ == '__main__':
	main()
