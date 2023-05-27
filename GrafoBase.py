"""
Implementación de Grafos a través de diccionarios
author @MaríaJoséVelázquez
"""
from collections import deque

class grafo:
    def __init__(self):
        self.G={}

    def insertaDireccionado(self,v1,v2,w=0):
        if v1 not in self.G:
            self.G[v1]={}#creamos un diccionario para cada nodo, el diccionario contendra los adjacentes
        if v2 not in self.G:
            self.G[v2] = {}
        self.G[v1][v2]=w

    def inserta(self,v1,v2,w=0):
        self.insertaDireccionado(v1,v2,w)
        self.insertaDireccionado(v2, v1, w)

    #Recorrido en profundidad
    def DFS(self):
        visitados = {} #diccionario de nodos visitados
        for i in self.G:
            visitados[i] = False #agregamos todos los nodos al diccionario con valor false
        lista = []#el metodo regresa una lista en el orden en el que se visita los nodos
        for i in visitados:
            if not visitados[i]:#si visitados i es falso
                self.__DFS(i, visitados, lista)
        return lista

    def __DFS(self, actual, visitados, lista):
        if visitados[actual]: #es verdadero, termina
            return
        visitados[actual] = True #se marca como visitado
        lista += [actual]#se agrega a la lista
        for vi in self.G[actual]:#para todo adjacente
            self.__DFS(vi, visitados, lista)

   #Recorrido en profundidad
    def BFS(self):
        cola=deque()#creamos una cola fifo
        lista=[]#gusrdamos como vamos visitando
        visitados={}
        for nodo in self.G:
            visitados[nodo]=False
        for n in visitados:
            if visitados[n]==False:#si no lo hemos visitado agregamos a la cola
                cola.append(n)
                self.__BFS(lista,visitados,cola)
        return lista #regrfesamos la lista con el orden en el que se exploro

    def __BFS(self,lista,visitados,cola):
        while cola:#mientras la cola no este vacia
            actual=cola.pop()#sacamos de la cola
            visitados[actual]=True#marcamos como visitado
            lista += [actual]#agregamos a la lista
            for adj in self.G[actual]:#para todo adjacente
                if adj not in visitados:#si no esta visitado
                    cola.append(adj)#se agrega a la cola





"""
Pruebas
"""
g=grafo()
g.inserta('a','b')
g.inserta('a','e')
g.inserta('a','s')
g.inserta('s','b')
g.inserta('s','c')
g.inserta('s','d')
g.inserta('c','d')
g.inserta('d','e')

print(g.G)
print(g.DFS())
print(g.BFS())

