import random

def generate_random_graph(nodes, edge_probability=0.5):
    edges = []
    for u in range(nodes):
        for v in range(u + 1, nodes):
            if random.random() < edge_probability:
                weight = random.randint(1, 10)
                edges.append((u, v, weight))
    return edges

def save_graph_to_txt(total, edges, filename="data/graph.txt"):
    with open(filename, "w") as f:
        f.write(f"{total}\n")
        for u, v, weight in edges:
            f.write(f"{u} {v} {weight}\n")
