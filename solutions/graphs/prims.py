import heapq

def minimumSpanningTree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    minHeap = []
    for neighbor, weight in adj[1]:
        heapq.heappush(minHeap, [weight, 1, neighbor])

    mst = []
    visit = {1}

    while len(visit) < n:
        weight, n1, n2 = heapq.heappop(minHeap)
        if n2 in visit:
            continue
        mst.append((n1, n2))
        visit.add(n2)
        for neighbor, weight in adj[n2]:
            if neighbor not in visit:
                heapq.heappush(minHeap, [weight, n2, neighbor])

    return mst


# -------- RUN IT --------

edges = [
    (1, 2, 3),
    (1, 3, 1),
    (2, 3, 7),
    (2, 4, 5),
    (3, 4, 2)
]

print(minimumSpanningTree(edges, 4))
# Output: [(1, 3), (3, 4), (1, 2)]
