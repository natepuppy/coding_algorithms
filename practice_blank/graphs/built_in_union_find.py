try:
    from disjoint_set import DisjointSet
except ImportError:
    class DisjointSet:
        def __init__(self):
            # Code will be implemented here
            pass

        def find(self, x):
            # Code will be implemented here
            pass

        def union(self, a, b):
            # Code will be implemented here
            pass

        def connected(self, a, b):
            # Code will be implemented here
            pass

ds = DisjointSet()

# It creates elements on the fly as you use them
ds.union(1, 2)
ds.union(2, 3)

# Check connectivity
print(ds.connected(1, 3)) # Output: True
print(ds.connected(1, 4)) # Output: False

# Find the root
print(ds.find(1))
