def canta(word, n):
	for x in range(n):
		print(x,word)

def main():
	canta("Hello World", 13)
	ascii()
	x = input("Dame una palabra: ")
	y = input("Dame una palabra: ")
	if x == y:
		print("Son iguales")
	else:
		print("No son iguales")

def ascii():
	for x in range(65, 65+26):
		print("{} == {}".format(chr(x),x))
		
	
if __name__ == '__main__':
	main()
