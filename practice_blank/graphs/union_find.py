class UnionFind:
    def __init__(self, n):
        # Code will be implemented here
        pass
    
    # Find parent of n, with path compression.
    def find(self, n):
        # Code will be implemented here
        pass

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        # Code will be implemented here
        pass

# Create a UnionFind structure with 7 elements (1 through 7)
uf = UnionFind(7)

# Connect some nodes
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

# Check which set a node belongs to
print(uf.find(1))  # same as uf.find(2) and uf.find(3)
print(uf.find(3))
print(uf.find(5))  # same as uf.find(4)

# Check if two nodes are connected
def connected(a, b):
    return uf.find(a) == uf.find(b)

print(connected(1, 3))  # True
print(connected(1, 4))  # False

# Connect the two groups
uf.union(3, 4)

print(connected(1, 5))  # True
