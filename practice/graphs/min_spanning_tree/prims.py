import heapq
from collections import defaultdict

# Use for Dense Graphs
# Use these when you want to connect all nodes together with the absolute minimum total edge weight
def minimumSpanningTree(edges, n):
    if len(edges) == 0:
        return [], 0

    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((weight, end))
        graph[end].append((weight, start))

    visited = set()
    mst = []
    total_weight = 0

    # weight, start, end
    start = edges[0][0]
    queue = [(0, None, start)]

    while queue and len(visited) < n: # Do both conditions here
        weight, parent, child = heapq.heappop(queue) # treat is like a parent-child relationship

        # CRITICAL: Similar to Djikstra's, we need to do this because 
        # a single node could be added to the heap multiple times. So 
        # if we already found an optimal solution, we don't want to 
        # revisit this node, that is why we have to check if it is in 
        # visited twice.
        if child in visited:
            continue

        visited.add(child)

        if parent is not None:
            mst.append((parent, child))
            total_weight += weight

        for new_weight, new_child in graph[child]:
            if new_child not in visited:
                heapq.heappush(queue, (new_weight, child, new_child))

    return mst, total_weight

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
