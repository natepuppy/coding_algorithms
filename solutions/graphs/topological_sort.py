def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    visit = set()
    for i in range(1, n + 1):
        dfs(i, adj, visit, topSort)

    topSort.reverse()
    return topSort


def dfs(src, adj, visit, topSort):
    if src in visit:
        return
    visit.add(src)
    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)


# -------- RUN IT --------

edges = [
    (1, 2),
    (1, 3),
    (3, 4),
    (2, 4)
]

print(topologicalSort(edges, 4))
# Output: [1, 3, 2, 4]
