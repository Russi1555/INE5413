
#TODAS AS BUSCAS E CHECAGENS SÃO FEITAS COM O INDICE NÃO O ROTULO

import math
from collections import deque

class Grafo:
    def __init__(self, arquivo):
        self.V = {} #{ "a": {"rotulo": 'zap', "indice":2}, "b": {"rotulo": "whats", "indice": 5}, "c": {"rotulo": "azul", "indice": 7}} #deletar essa inicialização. puramente pra teste
        self.A = [] # [ [V1,V2,PESO1], ..., [Vx,Vy,PESOn] ]
        self.ler(arquivo)

    def ler(self,arquivo):
        leitura = open(arquivo, "r")

        for linhas in leitura:

            if "*vertices" in linhas:
                n_vertices = int(linhas.strip().split(" ")[1])
                count = 0

            else:

                if count < n_vertices:
                    indice, rotulo = linhas.strip().split(" ")
                    self.V[indice] = {"rotulo": rotulo, "indice": indice}
                    count += 1

                elif "*edges" not in linhas:
                    a,b,peso = linhas.strip().split(" ")
                    self.A.append([a,b,peso])

    def qtdVertices(self): #Funciona
        return len(self.V.keys())

    def qtdArestas(self): #Funciona
        return len(self.A)

    def grau(self, v): #funciona
        count = 0
        for aresta in self.A:
            if v in aresta:
                count += 1
        return count

    def rotulo(self, v): #funciona
        return self.V.get(v).get("rotulo")

    def haAresta(self, u, v): #Funciona
        for aresta in self.A:
            if self.V.get(u).get("indice") in aresta and self.V.get(v).get("indice") in aresta:
                return True
        return False

    def peso(self, u, v): #Funciona
        for aresta in self.A:
            if u in aresta and v in aresta:
                return aresta[2]
        return False

    def vizinhos(self,v): #funciona
        vizinhos = []
        for aresta in self.A:
            if v in aresta:
                if v != aresta[1]:
                    vizinhos.append(self.V.get(aresta[1]))
                if v != aresta[0]:
                    vizinhos.append(self.V.get(aresta[0]))
        return vizinhos

    def busca_em_largura(self, s):
        visitados = [False] * (self.qtdVertices()+1)
        distancia = [math.inf] * (self.qtdVertices()+1)
        antecessor = [None] * (self.qtdVertices()+1)
        fila = []
        niveis = {0: [s]}


        visitados[s] = True
        distancia[s] = 0
        fila.append(self.V.get(str(s)))


        while len(fila) > 0:
            u = fila.pop(0)
            for vertice in self.vizinhos(u.get("indice")):
                j = int(vertice.get("indice"))
                if not visitados[j]:
                    visitados[j] = True
                    distancia[j] = distancia[int(u.get("indice"))] + 1
                    antecessor[j] = u
                    fila.append(vertice)

                    encontrados_no_nivel = niveis.get(distancia[j], [])
                    encontrados_no_nivel.append(j)
                    niveis.update({distancia[int(vertice.get("indice"))] : encontrados_no_nivel})

        for key, value in niveis.items():
            print(str(key) + ":", str(value)[1:-1])







    def floyd_warshall(self):
        n_vertices = self.qtdVertices()
        distancias = []
        for i in range(n_vertices):
            distancia_u_v = []
            for j in range(n_vertices):
                if i == j :
                    distancia_u_v.append(0)
                else:
                    distancia_u_v.append(math.inf)
            distancias.append(distancia_u_v)
        
        for aresta in self.A:
            distancias[aresta[0]-1][aresta[1]-1] = aresta[2]
            distancias[aresta[1]-1][aresta[0]-1] = aresta[2]

        for i in range(len(distancias)):
            for linha in range(len(distancias)):
                for coluna in range(len(distancias[linha])):
                    distancias[linha][coluna] = min(distancias[linha][coluna], distancias[linha][i] + distancias[i][coluna])

        c_linha = 1
        for linha in distancias:
            print(str(c_linha) + ":",  str(linha)[1:-1])
            c_linha += 1






G = Grafo("email.net")
G.floyd_warshall




