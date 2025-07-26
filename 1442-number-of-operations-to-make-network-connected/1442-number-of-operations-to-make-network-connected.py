class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def findPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulu_u = self.findPar(u)
        ulu_v = self.findPar(v)

        if ulu_u == ulu_v: return
        if self.rank[ulu_u] < self.rank[ulu_v]:
            self.parent[ulu_u] = ulu_v
        elif self.rank[ulu_u] > self.rank[ulu_v]:
            self.parent[ulu_v] = ulu_u
        else:
            self.parent[ulu_v] = ulu_u
            self.rank[ulu_u] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        count = 0
        for u, v in connections:
            if ds.findPar(u) == ds.findPar(v):
                count += 1
            else:
                ds.unionByRank(u, v)

        components = 0
        for i in range(n):
            if i == ds.parent[i]:
                components += 1

        if count >= components-1:
            return components-1

        return -1