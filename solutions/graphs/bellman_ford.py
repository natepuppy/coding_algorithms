# Bellman-Ford: shortest paths from src to all nodes
def bellmanFord(edges, n, src):
    dist = {}
    for i in range(1, n + 1):
        dist[i] = float("inf")
    dist[src] = 0

    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


# -------- RUN IT --------

edges = [
    (1, 2, 4),
    (1, 3, 5),
    (2, 3, -3),
    (3, 4, 4),
    (2, 4, 6)
]

print(bellmanFord(edges, 4, 1))
# Output: {1: 0, 2: 4, 3: 1, 4: 5}

# That’s it — plain Bellman–Ford, shortest paths from node 1,
# including negative edge weights (no negative cycles).
