def Dijkstra(graph, start, end):
    pi = {node: None for node in graph}
    d = {node: float('inf') for node in graph}
    d[start] = 0
    visited = set()

    current_node = start
    while current_node != end:
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = d[current_node] + weight
            if distance < d[neighbor]:
                d[neighbor] = distance
                pi[neighbor] = current_node
        # Choix du prochain nœud non visité avec la distance minimale
        min_distance = float('inf')
        next_node = None
        for node in graph:
            if node not in visited and d[node] < min_distance:
                min_distance = d[node]
                next_node = node
        if next_node is None:
            break
        current_node = next_node

    # Construction du chemin à partir de la destination vers le départ
    path = []
    while current_node is not None:
        path.insert(0, current_node)
        current_node = pi[current_node]

    return path, d[end]

# Votre graphe G
G = {
    'A': {'B': 8, 'C': 6, 'H': 15, 'D': 5, 'G': 6},
    'B': {'A': 8, 'D': 10, 'E': 14, 'F': 8, 'G': 10},
    'C': {'D': 5, 'A': 6, 'H': 8},
    'D': {'A': 5, 'B': 10, 'C': 5, 'E': 6},
    'E': {'B': 14, 'D': 6, 'F': 10},
    'F': {'B': 8, 'E': 10, 'G': 12},
    'G': {'A': 6, 'B': 10, 'H': 12, 'F': 12},
    'H': {'A': 15, 'C': 8, 'G': 12}
}

start_vertex = 'A'
end_vertex = 'H'
shortest_path, shortest_distance = Dijkstra(G, start_vertex, end_vertex)

print("Le chemin le plus court de", start_vertex, "à", end_vertex, "est :", shortest_path)
print("La distance totale est :", shortest_distance)
