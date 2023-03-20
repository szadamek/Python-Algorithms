import networkx as nx
import matplotlib.pyplot as plt
import random


graph = nx.Graph()

def random_Edges(graph, N_nodes):
    graph.add_nodes_from(range(0, N_nodes))
    for i in graph.nodes():
        for j in graph.nodes():
            if i < j:
                value = random.randint(0, 8)
                if value == 8:
                    graph.add_edge(i, j)

random_Edges(graph, 8)


def connected(graph):
    results = []
    visited = set()
    for node in graph:
        if node not in visited:
            connections = bfs(graph, node)
            visited.update(connections)
            results.append(connections)
    return results


def bfs(graph, node):
    """Breath-first search"""
    visited = set()
    nearNodes = {node}
    while nearNodes:
        currentNodes = nearNodes
        nearNodes = set()
        for node in currentNodes:
            if node not in visited:
                visited.add(node)
                nearNodes.update(graph[node])
                print(graph[node])
    return visited


nx.draw_networkx(graph)
print(f"Wierzcholki: {graph.nodes}")
print(f"Krawedzie: {graph.edges}")
print(f"Polaczone wierzcholki: {connected(graph)}")
plt.show()
