from collections import deque
from collections import defaultdict

def solution(edges):
    adj_list = defaultdict(list)
    for start, end in edges:
        adj_list[start].append(end)
    
    if "A" not in adj_list:
        return []

    queue = deque()
    queue.append("A")

    parent = {}
    parent["A"] = None

    while queue:
        element = queue.popleft()

        if element == "D":
            result = [element]

            while parent[element] != None:
                result.append(parent[element])
                element = parent[element]
            return result[::-1]

        for neighbor in adj_list[element]:
            if neighbor not in parent:
                parent[neighbor] = element
                queue.append(neighbor)
    
    return []

# Given the following list of directed edges, print the shortest path from A to D.
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
print(solution(edges))

# print(bfs("A", "D", adjList))
