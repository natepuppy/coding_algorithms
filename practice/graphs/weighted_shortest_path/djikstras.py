from collections import defaultdict
import heapq

# Use Dijkstra’s when you need the shortest path from a 
# single source in a weighted graph with no negative edges.
def shortestPath(edges, n, src):
    if len(edges) == 0:
        return []

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
    
    distances = [float("inf")] * n
    distances[src] = 0 # Dont forget this!!!!!
    heap = [(0, src)]

    while heap:
        weight, node = heapq.heappop(heap)

        if weight > distances[node]: # Two distance checks
            continue

        distances[node] = weight

        for w, neighbor in graph[node]:
            new_weight = w + weight

            if new_weight < distances[neighbor]: # Two distance checks
                heapq.heappush(heap, (new_weight, neighbor))
                distances[neighbor] = new_weight # ONLY update distances here!!!!!
    
    return distances


# From node 1, find the shortest path to every other node
edges = [
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 5),
    (2, 0, 10),
    (3, 0, 3)
]

n = 4        # number of nodes
src = 1      # starting node

result = shortestPath(edges, n, src)

print("Shortest distances from node", src)
for node in range(1, n + 1):
    print(f"Node {node}: {result.get(node, 'unreachable')}")











    if not edges:
        return []

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
    
    distances = [float("inf")] * n
    distances[src] = 0

    heap = []
    heap.append((0, src))

    while heap:
        weight, node = heapq.heappop(heap)

        if weight > distances[node]: # DONT forget this here!
            continue

        for w, neighbor in graph[node]:
            new_weight = weight + w

            if new_weight < distances[neighbor]: # Dont foget this here!!!!!
                heapq.heappush(heap, (new_weight, neighbor))
                distances[neighbor] = new_weight # ONLY update distances here!!!!!

    return distances