import heapq

def shortestPath(edges, n, src):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
        
    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append([d, w])

    shortest = {}
    minHeap = [[0, src]]

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, [w1 + w2, n2])

    return shortest

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
