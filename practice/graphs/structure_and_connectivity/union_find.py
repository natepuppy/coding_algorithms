# You are given a connected undirected graph with n nodes labeled from 1 to n. 
# Initially, it contained no cycles and consisted of n-1 edges.
# We have now added one additional edge to the graph.
# Return an edge that can be removed so that the graph is still a connected non-cyclical graph.
# Example:
# Input: edges = [[1,2],[1,3],[3,4],[2,4]]
# Output: [2,4]

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i + 1] = i + 1
            self.rank[i + 1] = 0

    # Find - finds the root parent
    def find(self, n):
        if self.parent[n] == n:
            return n

        # PATH COMPRESSION (The Optimal Part)
        # Recurse up until you hit the parent, then as you recuse back down, 
        # set the highest found parent as the parent for all of them
        self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    # union - takes two nodes - If they have the same root parent, return False 
    # else, union them together and return True
    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        if root1 == root2:
            return False
        
        # Notice how I don't restrucure the two trees, I just make one the 
        # parent of the other, then do lazy path compression in the find() function
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True

n = 4
edges = [[1,2],[1,3],[3,4],[2,4]]
union_find = UnionFind(n)
edge_to_remove = None

for n1, n2 in edges:
    if not union_find.union(n1, n2):
        edge_to_remove = [n1, n2]

print(edge_to_remove)









# Built IN!!!!!!!!!!!!!!!!!!!!
        

from disjoint_set import DisjointSet

ds = DisjointSet()

# It creates elements on the fly as you use them
ds.union(1, 2)
ds.union(2, 3)

# Check connectivity
print(ds.connected(1, 3)) # Output: True
print(ds.connected(1, 4)) # Output: False

# Find the root
print(ds.find(1))







