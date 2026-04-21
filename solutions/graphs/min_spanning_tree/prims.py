from collections import defaultdict
import heapq

# Used to find MST on UNDIRECTED, WEIGHTED, and CONNECTED graphs
def minimumSpanningTree(edges, n):
    if not edges:
        return 0
    
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    # Heap Format: (weight, target_node)
    heap = [(0, edges[0][0])]
    visited = set()
    total_cost = 0
    
    while heap and len(visited) < n:
        weight, u = heapq.heappop(heap)
        
        if u in visited:
            continue
        
        visited.add(u)
        total_cost += weight
        
        for next_weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (next_weight, v))

    if len(visited) == n:
        return total_cost
    else:
        return -1

# -------- RUN IT --------

# Given the following graph, determine the minimum required 
# cost to connect all points in the graph. Return the cost 
# and the minimum spanning tree

# Are the edges directed or undirected?? In this case undirected.
edges = [
    (1, 2, 3),
    (1, 3, 1),
    (2, 3, 7),
    (2, 4, 5),
    (3, 4, 2)
]

print(minimumSpanningTree(edges, 4))
# Output: [(1, 3), (3, 4), (1, 2)]
