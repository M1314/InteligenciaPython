import random
import datetime

def habla(archivo):
	palabras = open(archivo).read().split('\n')
	result = ""
	for i in range(1, 10):
		id1 = random.randint(0, 100)
		id2 = random.randint(100, 15000)
		id3 = random.randint(15000, 38989)

		result = result + palabras[id1].split()[1] +" "+ palabras[id2].split()[1] +" "+ palabras[id3].split()[1]+" "
	print(result)

def main():
	habla("freq.txt")

if __name__ == '__main__':
	main()
