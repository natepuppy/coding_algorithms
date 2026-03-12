from collections import defaultdict
from collections import deque

# In a graph with a negative cycle, the concept of a "shortest path" 
# doesn't exist unless you have a constraint of k.

# Use when finding the shortest path from one node to 
# all others when the graph has negative edge weights
def bellman_ford_bfs_version(n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        prices = [float("inf")] * n
        prices[src] = 0

        #       weight, node, level
        queue = deque([(0, src, 0)])

        while queue:
            curr_cost, curr_airport, stops = queue.popleft()

            if stops > k:
                continue

            for neighbor, cost in graph[curr_airport]:
                total_cost = curr_cost + cost
                if total_cost < prices[neighbor]:
                    prices[neighbor] = total_cost
                    queue.append((total_cost, neighbor, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1

def bellman_ford(n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for stop in range(k + 1):
            temp_prices = prices.copy()

            for start, end, price in flights:
                if prices[start] == float("inf"):  # prices, not temp_prices
                    continue
                
                new_total = price + prices[start] # prices, not temp_prices
                if new_total < temp_prices[end]:
                    temp_prices[end] = new_total
            
            prices = temp_prices.copy()
        
        if prices[dst] == float("inf"):
            return -1
        
        return prices[dst]


            




# There are n airports, labeled from 0 to n - 1, which are connected by some flights. 
# You are given an array flights where flights[i] = [from_i, to_i, price_i] represents 
# a one-way flight from airport from_i to airport to_i with cost price_i. You may assume 
# there are no duplicate flights and no flights from an airport to itself.
# Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.

# n = 4
# flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
# src = 0
# dst = 3
# k = 2

# print(f"Cheapest price: {bellman_ford(n, flights, src, dst, k)}")
# # Expected Output: 500

n = 5
flights = [
    [0, 1, 1],
    [1, 2, 1],
    [2, 4, 100],     # cheap chain (3 edges)

    [0, 3, 10],
    [3, 4, 1],     # valid path (2 edges)
]

src = 0
dst = 4
k = 3   # at most 2 stops (3 edges allowed)

print(bellman_ford_bfs_version(n, flights, src, dst, k))
print(bellman_ford(n, flights, src, dst, k))
