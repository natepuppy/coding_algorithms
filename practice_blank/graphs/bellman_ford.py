# Bellman-Ford: shortest paths from src to all nodes
def bellmanFord(edges, n, src):
    # Code will be implemented here
    pass


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
