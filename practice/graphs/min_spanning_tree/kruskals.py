from disjoint_set import DisjointSet


# Use for Sparse Graphs
# Use these when you want to connect all nodes together with the absolute minimum total edge weight
def minimumSpanningTree(edges, n):
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet()
    mst = []

    for u, v, w in edges:
        if not ds.connected(u, v):
            # If not connected, union them and add to MST
            ds.union(u, v)
            mst.append((u, v, w))
            
            # 4. Optimization: A tree with n nodes always has n-1 edges
            if len(mst) == n - 1:
                break
    
    return mst

edges = [
    (1, 2, 3),
    (1, 3, 1),
    (2, 3, 7),
    (2, 4, 5),
    (3, 4, 2)
]

print(minimumSpanningTree(edges, 4))
# Output: [(1, 3, 1), (3, 4, 2), (1, 2, 3)]