# Write a function that finds every unique path from node A to node D.

from collections import defaultdict
class Solution:
    def find_paths(self, edges, source, dest):
        if not edges or source is None or dest is None: # use "is not None" in case of a 0
            return []

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        result = []
        visiting = set()

        def dfs(node, path):
            if node == dest:
                result.append(path.copy())
                return
            
            visiting.add(node)

            for neighbor in graph[node]:
                if neighbor not in visiting:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()

            # You mark a node as visited to avoid cycles within the current path,
            # but you must remove it after backtracking so it can be used in other independent paths.
            visiting.remove(node)

        dfs(source, [source]) # What do I do if source == dest???

        return result
        

        



edges = [
    ["A", "B"], ["A", "C"], 
    ["B", "C"], ["B", "D"], 
    ["C", "D"]
]

# Expected Output: [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
print(Solution().find_paths(edges, "A", "D"))





















        # graph = defaultdict(list)
        # for start, end in edges:
        #     graph[start].append(end)

        # result = []
        # visited = set() # Handle cycles

        # def dfs(node, path):
        #     if node == dest:
        #         result.append(path.copy())
        #         return

        #     visited.add(node)
        
        #      # Can't return here b/c 
        #     for neighbor in graph[node]:
        #         if neighbor not in visited:
        #             path.append(neighbor)
        #             dfs(neighbor, path)
        #             path.pop()
            
        #     visited.remove(node)
            
        # dfs(source, [source])

        # return result