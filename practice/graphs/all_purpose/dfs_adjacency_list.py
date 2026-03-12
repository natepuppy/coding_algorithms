from collections import defaultdict

# Write a function that finds every unique path from node A to node D.
def solution(edges, start_node, end_node):
    adj_list = defaultdict(lambda: [])
    for start, end in edges:
        adj_list[start].append(end)
    
    result = []

    # Do I need memoization? - No because I need to keep track of EVERY path, not just the count of paths

    visited = set() # Handle cycles

    def dfs(node, path):
        if node == end_node:
            result.append(path.copy())
            return
        
        visited.add(node)
        
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        
        visited.remove(node)
    
    dfs(start_node, [start_node])

    return result

edges = [
    ["A", "B"], ["A", "C"], 
    ["B", "C"], ["B", "D"], 
    ["C", "D"]
]

# Expected Output: [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
print(solution(edges, "A", "D"))


