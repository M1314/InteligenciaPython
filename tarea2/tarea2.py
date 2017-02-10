import random
import datetime

saludos = ("hola", "quibo", "que onda", "que tal", "buenos dias")
respuestas = ("k pex", "que pachuca", "hey", "tschus")
despedidas = ("adios", "nos vemos", "luego", "bye")
nombres = ("llamas", "nombre")
hora = ("hora", "tiempo", "reloj")
dianoche = ("dia", "noche")
pelicula = ("pelicula", "aburrido", "cine", "peliculas")
peliculas = ("hunt for the wilderpeople", "sing street", "avengers")
def saluda(enunciado):
	indice = random.randint(0, len(respuestas) - 1)
	for palabra in enunciado.split():
		if palabra.lower() in saludos:
			return respuestas[indice]
		elif palabra.lower() in despedidas:
			return despedidas[indice]
		elif palabra.lower() in nombres:
			return "Tlaloc"
		elif palabra.lower() in hora:
			return datetime.datetime.now()
		elif palabra.lower() in dianoche:
			fecha = datetime.datetime.now().strftime("%c")
			hr = fecha.split()[3]
			hr = hr.split(":")[0]
		
			if int(hr) < 6 or int(hr) > 18:
				return "noche"
			else:
				return "dia"
		elif palabra.lower() in pelicula:
			indice = random.randint(0, len(peliculas) - 1)
			return peliculas[indice]

	return "no entiendo"
def main():
	enunciado = input("escribe tu enunciado: ")
	print(saluda(enunciado))

if __name__ == '__main__':
	main()
