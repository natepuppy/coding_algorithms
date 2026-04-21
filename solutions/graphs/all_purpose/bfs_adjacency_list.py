# Used for shortest path when NOT weighted
from collections import defaultdict
from collections import deque
class Solution:
    def bfs(self, edges, source, dest):
        adj_list = defaultdict(list)

        for start, end in edges:
            adj_list[start].append(end)

        queue = deque([source])

        # If I didn't have this, I would have neeeded a seen set, or remove from the path...
        parent = {}
        parent[source] = None

        while queue:
            node = queue.popleft()

            if node == dest:
                path = []
                while node is not None: # Do is not None instead of just while node, because node could be zero...
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            
            for neighbor in adj_list[node]:
                if neighbor not in parent:
                    queue.append(neighbor)
                    parent[neighbor] = node

        return []

# Given the following list of directed edges, print the shortest path from A to D.
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
print(Solution().bfs(edges, "A", "D"))

