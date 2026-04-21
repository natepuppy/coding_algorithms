from collections import defaultdict
import heapq

# Used when finding the shortest path from one starting node to 
# all other nodes in a graph with non-negative edge weights.
def shortestPath(edges, n, src):
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((weight, end))
    
    distances = [float("inf")] * n
    distances[src] = 0
    heap = [(0, src)]

    while heap:
        weight, node = heapq.heappop(heap)

        if weight > distances[node]:
            continue # Just continue here!!!!!
        
        for w, neighbor in graph[node]:
            new_weight = w + weight

            if new_weight < distances[neighbor]: # Check distances before pushing onto the queue
                heapq.heappush(heap, (new_weight, neighbor))
                distances[neighbor] = new_weight # Update distances here!!!!
    
    return distances
        

            








# Important Note: I need both if statements because there might have been 
# something in the queue, and while it was in the queue we found a shorter path

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
















    # graph = defaultdict(list)
    # for start, end, distance in edges:
    #     graph[start].append((distance, end))

    # # distances = defaultdict(lambda: float("inf"))
    # distances = {}
    # for i in range(1, n + 1):
    #     distances[i] = float("inf")

    # distances[src] = 0 # Update src distance to start

    # queue = [(0, src)]

    # while queue:
    #     curr_dist, curr_node = heapq.heappop(queue)

    #     if distances[curr_node] < curr_dist:
    #         continue # Don't go through neighbors if we have seen a better version of this already.
        
    #     for neighbor_dist, neighbor_node in graph[curr_node]:
    #         new_total_dist = neighbor_dist + curr_dist

    #         if new_total_dist < distances[neighbor_node]:
    #             distances[neighbor_node] = new_total_dist # update the distance here
    #             heapq.heappush(queue, (new_total_dist, neighbor_node))
    
    # return distances