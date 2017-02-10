import collections
import heapq

class Nodo:


class Cola:
    def __init__(self):
        self.elementos = collections.deque()
    def esVacia(self):
        return len(self.elementos) == 0

    def put(self, d):
        self.elementos.append(d)

    def get(self):
        return self.elementos.popleft()

class ColaPriorizada:
    def __init__(self):
        self.elementos = []
    def esVacia(self):
        return len(self.elementos) == 0

    def put(self, prioridad, d):
        heapq.heappush(self.elementos, (prioridad, d))

    def get(self):
        return heapq.heappop(self.elementos)[1]


class Grafo:
    def __init__(self):
        self.aristas = {}
        
    def vecinos(self, id):
        return self.aristas[id]

    def costo(nodo1, nodo2):
        return self.costos[]
