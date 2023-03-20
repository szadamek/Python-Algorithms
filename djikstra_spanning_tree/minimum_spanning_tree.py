import networkx as nx
import matplotlib.pyplot as plt

nodes_v = 8
graph = nx.Graph()
graph.add_nodes_from(range(1, nodes_v+1))
graph.add_edge(0, 1, weight=4)
graph.add_edge(0, 2, weight=7)
graph.add_edge(1, 2, weight=11)
graph.add_edge(1, 3, weight=9)
graph.add_edge(2, 5, weight=1)
graph.add_edge(1, 5, weight=20)
graph.add_edge(3, 4, weight=2)
graph.add_edge(4, 5, weight=1)
graph.add_edge(3, 6, weight=6)
graph.add_edge(4, 6, weight=10)
graph.add_edge(4, 7, weight=5)
graph.add_edge(5, 7, weight=3)
graph.add_edge(5, 8, weight=15)
graph.add_edge(6, 8, weight=5)
graph.add_edge(7, 8, weight=12)

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()


def prim(graph, nodes):

    graph = nx.to_pandas_adjacency(graph)

    visited = [0 for i in range(nodes)]

    visited[0] = 1
    min_way = 0
    result = []
    print("Krawedzie w drzewie rozpinajacym - algorytm Prime'a:")

    while len(result) < nodes - 1:

        minimum = float('inf')
        a = 0
        b = 0

        for i in range(nodes):
            if visited[i]:
                for j in range(nodes):
                    if (not visited[j]) and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            a = i
                            b = j

        visited[b] = 1
        print(f"wierzcholki:{a}  {b} -  waga: {int(graph[a][b])}")
        min_way += int(graph[a][b])
        result.append([a, b, int(graph[a][b])])

    print("Suma najmniejszego kosztu: ", min_way)
    return result



new_tree = prim(graph, nodes_v)

minSpanTree = nx.Graph()
minSpanTree.add_nodes_from(range(1, len(new_tree)))
for edge in new_tree:
    minSpanTree.add_edge(edge[0], edge[1], weight=edge[2])
pos = nx.spring_layout(minSpanTree)
nx.draw_networkx(minSpanTree, pos)
labels = nx.get_edge_attributes(minSpanTree, 'weight')
nx.draw_networkx_edge_labels(minSpanTree, pos, edge_labels=labels)
plt.show()
