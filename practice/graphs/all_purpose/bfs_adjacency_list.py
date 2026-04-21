# Used for shortest path when NOT weighted
from collections import defaultdict
from collections import deque
class Solution:
    def bfs(self, edges, source, dest):
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        queue = deque()
        queue.append(source)

        # If I didn't have this, I would have neeeded a seen set, or remove from the path...
        parents = {source: None}
        result = []

        while queue:
            node = queue.popleft()

            if node == dest:
                while node is not None:  # Do "is not None" instead of just while node, because node could be zero...
                    result.append(node)
                    node = parents[node]
                break
                
            for neighbor in graph[node]:
                if neighbor not in parents:
                    queue.append(neighbor)
                    parents[neighbor] = node

        return result[::-1]

# Given the following list of directed edges, print the shortest path from A to D.
# undirected edges
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
print(Solution().bfs(edges, "A", "D"))






























        # graph = defaultdict(list)
        # for start, end in edges:
        #     graph[start].append(end)

        # queue = deque([source])

        # # If I didn't have this, I would have neeeded a seen set, or remove from the path...
        # parent = {}
        # parent[source] = None

        # while queue:
        #     node = queue.popleft()

        #     if node == dest:
        #         path = []
        #         while node is not None: # Do "is not None" instead of just while node, because node could be zero...
        #             path.append(node)
        #             node = parent[node]
        #         return path[::-1]
            
        #     for neighbor in graph[node]:
        #         if neighbor not in parent:
        #             queue.append(neighbor)
        #             parent[neighbor] = node

        # return []




