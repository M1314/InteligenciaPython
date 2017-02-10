from estructuras import *

def heurisitica(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1-x2) + abs(y1-y2)

def astar(g, s, m):
    frontera = ColaPriorizada()
    frontera.put(0,s)
    anteriores = {s: None}
    costoAcumulado = {s: 0}

    while not frontera.esVacia():
        actual = frontera.get()

        if actual == m:
            break

        for next in g.vecinos(actual):
            costoN = costoAcumulado[actual] + g.costo(actual, next)
            if costoN not in costoAcumulado or costoN < costoAcumulado[next]:
                costoAcumulado[next] = costN
                p = costoN + heurisitica(m, next)
                frontera.put(next)
                anteriores[next] = actual

    return anteriores, costoAcumulado

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

if __name__ == '__main__':
    main()
