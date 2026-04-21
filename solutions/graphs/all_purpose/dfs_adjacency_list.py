# Write a function that finds every unique path from node A to node D.

from collections import defaultdict

class Solution:
    def find_paths(self, edges, source, dest):
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)

        result = []
        visited = set() # Handle cycles

        def dfs(node, path):
            if node == dest:
                result.append(path.copy())
                return

            visited.add(node)
        
             # Can't return here b/c 
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()
            
            visited.remove(node)
            
        dfs(source, [source])

        return result

edges = [
    ["A", "B"], ["A", "C"], 
    ["B", "C"], ["B", "D"], 
    ["C", "D"]
]

# Expected Output: [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
print(Solution().find_paths(edges, "A", "D"))


