from collections import deque

class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self.num_arestas = 0

    def adicionar_aresta(self, u, v):
        if u not in self.adjacencia:
            self.adjacencia[u] = []
        if v not in self.adjacencia[u]:
            self.adjacencia[u].append(v)
            self.num_arestas += 1
        if v not in self.adjacencia:
            self.adjacencia[v] = []
        if u not in self.adjacencia[v]:
            self.adjacencia[v].append(u)

    def obter_adjacencia(self):
        return self.adjacencia

    def obter_num_arestas(self):
        return self.num_arestas

def ler_grafo_arquivo(nome_arquivo):
    grafo = Grafo()
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        V = int(linhas[0].strip())
        for i in range(1, len(linhas)):
            linha = list(map(int, linhas[i].strip().split()))
            if len(linha) > 1:
                u = linha[0]
                vizinhos = linha[1:]
                for v in vizinhos:
                    grafo.adicionar_aresta(u, v)
    print(f"Adjacência do grafo: {grafo.obter_adjacencia()}")                
    return grafo

def eh_bipartido(grafo):
    adjacencia = grafo.obter_adjacencia()
    cor = {}
    particao1 = []
    particao2 = []

    for vertice in adjacencia.keys():
        if vertice not in cor:
            cor[vertice] = 0
            fila = deque([vertice])

            while fila:
                atual = fila.popleft()
                for vizinho in adjacencia[atual]:
                    if vizinho not in cor:
                        cor[vizinho] = 1 - cor[atual]
                        fila.append(vizinho)
                    elif cor[vizinho] == cor[atual]:
                        return False, None, None

    for vertice, c in cor.items():
        if c == 0:
            particao1.append(vertice)
        else:
            particao2.append(vertice)

    return True, particao1, particao2
