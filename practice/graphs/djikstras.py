import heapq

def shortestPath(edges, n, src):
    # Code will be implemented here
    return {}

# -------------------------
# ACTUAL USAGE
# -------------------------

edges = [
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 5),
    (2, 4, 10),
    (3, 4, 3)
]

n = 4        # number of nodes
src = 1      # starting node

result = shortestPath(edges, n, src)

print("Shortest distances from node", src)
for node in range(1, n + 1):
    print(f"Node {node}: {result.get(node, 'unreachable')}")
