import networkx as nx
import matplotlib.pyplot as plt
from random import randint, choice

graph = nx.Graph()


def random_edges(graph, nodes):
    graph.add_nodes_from(range(0, nodes))
    for i in graph.nodes():
        for j in graph.nodes():
            if i < j:
                random_value = randint(0, 2)
                if random_value == 1:
                    graph.add_edge(i, j, weight=randint(1, 5))


random_edges(graph, 8)


def dijkstra(graph, start, end):

    visited = set()
    unvisited = set(graph.nodes)
    distances = {start: 0}
    shortest_paths = {start: [start]}

    for node in unvisited:
        if node != start:
            distances[node] = float("inf")

    current_node = start

    while len(unvisited) > 0:
        if current_node == end:
            break

        if min([distances[node] for node in unvisited]) == float("inf"):
            print('Sciezka nie istnieje')
            break
        connections = graph[current_node]

        for node in connections:
            if distances[current_node] + graph[current_node][node]["weight"] < distances[node]:
                distances[node] = distances[current_node] + graph[current_node][node]["weight"]
                shortest_paths[node] = shortest_paths[current_node] + [node]
        # mark current_node as visited
        visited.add(current_node)
        unvisited.remove(current_node)
        # choose node with the minimum distance
        current_node = sorted([(node, distances[node]) for node in unvisited], key=lambda x: x[1])[0][0]

    print(f"Sciezka: {shortest_paths[end]}, Koszt przebycia: {distances[end]}")
    weights = []
    for i in range(0, len(shortest_paths[end]) - 1):
        weights.append(graph[shortest_paths[end][i]][shortest_paths[end][i + 1]]["weight"])
    print(f"Wagi: {weights} ")


start = choice(list(graph.nodes))
end = choice(list(graph.nodes))
while end == start:
    end = choice(list(graph.nodes))
dijkstra(graph, start, end)

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()
