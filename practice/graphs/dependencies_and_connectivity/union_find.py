# You are given a connected undirected graph with n nodes labeled from 0 to n - 1. 
# Initially, it contained no cycles and consisted of n-1 edges.
# We have now added one additional edge to the graph.
# Return an edge that can be removed so that the graph is still a connected non-cyclical graph.
# Example:
# Input: edges = [[0,1],[0,2],[2,3],[1,3]]
# Output: [1,3]

# Do this one!!!!!

# When to use: You need to rapidly group nodes into distinct sets, 
# merge those sets together, or check if two nodes belong to the 
# same group. It is incredibly efficient for detecting cycles in 
# undirected graphs


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(0, n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        return True

n = 4
edges = [[0,1],[0,2],[2,3],[1,3]]
union_find = UnionFind(n)

for n1, n2 in edges:
    if not union_find.union(n1, n2):
        return [n1, n2]
return []

