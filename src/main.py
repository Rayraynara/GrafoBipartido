import os
from graph_generator.gerador_grafo import generate_random_graph, save_graph_to_txt
from grafo_bipartido import eh_bipartido,ler_grafo_arquivo

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
