try:
    from disjoint_set import DisjointSet
except ImportError:
    class DisjointSet:
        def __init__(self):
            self.parent = {}

        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra != rb:
                self.parent[rb] = ra

        def connected(self, a, b):
            return self.find(a) == self.find(b)

ds = DisjointSet()

# It creates elements on the fly as you use them
ds.union(1, 2)
ds.union(2, 3)

# Check connectivity
print(ds.connected(1, 3)) # Output: True
print(ds.connected(1, 4)) # Output: False

# Find the root
print(ds.find(1))
