import random

def generate_random_graph(nodes, edge_probability=0.5):
    edges = []
    for u in range(nodes):
        for v in range(u + 1, nodes):
            if random.random() < edge_probability:
                weight = random.randint(1, 10)
                edges.append((u, v, weight))
    return edges

def save_graph_to_txt(edges, filename="data/graph.txt"):
    with open(filename, "w") as f:
        for u, v, weight in edges:
            f.write(f"{u} {v} {weight}\n")

def main():
    nodes = int(input("Digite o número de nós: "))
    edges = generate_random_graph(nodes)
    save_graph_to_txt(edges)
    print(f"Grafo gerado com {len(edges)} arestas e salvo em graph.txt")
