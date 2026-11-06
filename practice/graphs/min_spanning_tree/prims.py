from collections import defaultdict
import heapq

# Used to find MST on UNDIRECTED, WEIGHTED, and CONNECTED graphs
def minimumSpanningTree(edges, n):
    if len(edges) == 0:
        return [], 0
    
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    
    start_node = edges[0][0]

    heap = []
    for weight, end in graph[start_node]:
        heapq.heappush(heap, (weight, start_node, end))

    mst = []
    length = 0
    visited = set()
    visited.add(start_node)

    while heap:
        weight, start, end = heapq.heappop(heap)

        if end in visited:
            continue

        mst.append((start, end))
        length += weight
        visited.add(end)

        if len(visited) == n: # Dont forget this!!!!! - Would work without, but makes it much faster
            break

        for n_weight, neighbor in graph[end]:
            if neighbor not in visited:
                heapq.heappush(heap, (n_weight, end, neighbor))

    return mst, length


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

result = minimumSpanningTree(edges, 4)
print(result[0])
print(result[1])
# Output: 
# [(1, 3), (3, 4), (1, 2)]
# 6
























    #  if not edges:
    #     return []
    
    # graph = defaultdict(list)
    # for u, v, w in edges:
    #     graph[u].append((w, v))
    #     graph[v].append((w, u))
    
    # src = edges[0][0]

    # heap = []
    # mst = []
    # visited = set()
    # visited.add(src)

    # for w, v in graph[src]:
    #     heapq.heappush(heap, (w, src, v))
    
    # while heap:
    #     w, u, v = heapq.heappop(heap)

    #     if v in visited: # Dont forget this!!!!!
    #         continue

    #     mst.append((u, v))

    #     if len(visited) == n: # Dont forget this!!!!!
    #         return mst

    #     for weight, neighbor in graph[v]:
    #         if neighbor not in visited:
    #             heapq.heappush(heap, (weight, v, neighbor))

    #     visited.add(v)

    # return mst