from collections import defaultdict
import heapq


# Use when finding the shortest path from one starting node to 
# all other nodes in a graph with non-negative edge weights.
def shortestPath(edges, n, src):
    graph = defaultdict(list)
    for start, end, distance in edges:
        graph[start].append((distance, end))
    
    queue = [(0, src)]

    # distances = defaultdict(lambda: float("inf"))
    distances = {i: float("inf") for i in range(1, n + 1)}
    distances[src] = 0 # Update src distance to start

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_dist:
            continue # Don't go through neighbors if we have seen a better version of this already.
        
        for neighbor_dist, neighbor_node in graph[curr_node]:
            new_total_dist = neighbor_dist + curr_dist

            if new_total_dist < distances[neighbor_node]:
                distances[neighbor_node] = new_total_dist # update the distance here
                heapq.heappush(queue, (new_total_dist, neighbor_node))
    
    return distances

# From node 1, find the shortest path to every other node
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





















































# adj_list = defaultdict(lambda: [])
#     for start, end, distance in edges:
#         adj_list[start].append((distance, end))

#     distances = defaultdict(lambda: float("inf"))
#     queue = []
#     distances[src] = 0

#     queue = [(0, src)]

#     while queue: 
#         current_distance, node = heapq.heappop(queue)
        
#         # Stale Entry Guard: If we already found a shorter way, ignore this pop
#         if current_distance > distances[node]:
#             continue
        
#         for weight, neighbor in adj_list[node]:
#             new_dist = weight + current_distance

#             # Early Relaxation
#             if new_dist < distances[neighbor]:
#                 distances[neighbor] = new_dist # must do this here
#                 heapq.heappush(queue, (new_dist, neighbor))

#     return distances