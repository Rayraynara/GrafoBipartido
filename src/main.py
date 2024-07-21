import os
from graph_generator.gerador_grafo import generate_random_graph, save_graph_to_txt
from grafo_bipartido import Grafo, eh_bipartido

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

def main():
    nodes = int(input("Digite o número de nós: "))
    edges = generate_random_graph(nodes)
    save_graph_to_txt(nodes, edges)
    print(f"Grafo gerado com {len(edges)} arestas e salvo em graph.txt")

    nome_arquivo = "data/graph.txt"
    grafo = ler_grafo_arquivo(nome_arquivo)

    bipartido, particao1, particao2 = eh_bipartido(grafo)

    if bipartido:
        print("O grafo é bipartido.")
        print("Partição 1:", particao1)
        print("Partição 2:", particao2)
    else:
        print("O grafo não é bipartido.")

if __name__ == "__main__":
    main()
