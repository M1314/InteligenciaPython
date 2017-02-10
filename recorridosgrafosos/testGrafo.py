from estructuras import *


def bsV02(g, s):
    frontera = Cola()
    frontera.put(s)
    anteriores = {}
    anteriores[s] = None

    while not frontera.esVacia():
        actual = frontera.get()
        for next in g.vecinos(actual):
            if next not in anteriores:
                frontera.put(next)
                anteriores[next] = actual
    return anteriores

# s es start y m es la meta, g es el grafo
def bsV03(g, s, m):
    frontera = Cola()
    frontera.put(s)
    anteriores = {}
    anteriores[s] = None

    while not frontera.esVacia():
        actual = frontera.get()

        if actual == m:
            break

        for next in g.vecinos(actual):
            if next not in anteriores:
                frontera.put(next)
                anteriores[next] = actual

    return anteriores

def main():
    g = Grafo()
    g.aristas ={
    'A': ['B'],
    'B': ['A','C','D'],
    'C': ['A'],
    'D': ['E','A'],
    'E': ['B'],
    }
    #bsV01(g, 'D')
    print(bsV02(g,'D'))
    print(bsV03(g,'D','B'))

if __name__ == '__main__':
    main()
