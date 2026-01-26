def topologicalSort(edges, n):
    # Code will be implemented here
    pass


def dfs(src, adj, visit, topSort):
    # Code will be implemented here
    pass


# -------- RUN IT --------

edges = [
    (1, 2),
    (1, 3),
    (3, 4),
    (2, 4)
]

print(topologicalSort(edges, 4))
# Output: [1, 3, 2, 4]
