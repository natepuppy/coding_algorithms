import heapq 

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


def minimumSpanningTree(edges, n):
    minHeap = []
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, [weight, n1, n2])

    uf = UnionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)
        if uf.union(n1, n2):
            mst.append((n1, n2))

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
