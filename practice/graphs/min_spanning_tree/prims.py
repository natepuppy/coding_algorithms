from collections import defaultdict
import heapq

# Used to find MST on UNDIRECTED, WEIGHTED, and CONNECTED graphs
def minimumSpanningTree(edges, n):
    if n <= 1:
        return [0, []]
    if not edges:
        return None
    
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    start_node = edges[0][0]
    mst = []
    heap = []
    total_weight = 0
    
    visited = set() # You need a visited set
    visited.add(start_node)

    for weight, node in graph[start_node]:
        heapq.heappush(heap, (weight, start_node, node))
    
    while heap:
        weight, src, dest = heapq.heappop(heap)

        if dest in visited: # Two visited checks
            continue

        # Do these first!!!!!
        mst.append((src, dest, weight))
        visited.add(dest)
        total_weight += weight

        if len(visited) == n: # Dont forget this!!!!!
            return [total_weight, mst]

        for w, neighbor in graph[dest]:
            if neighbor not in visited: # Two visited checks
                heapq.heappush(heap, (w, dest, neighbor))
    
    return [0, []] # if the graph wasn't connected



        






    

    







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