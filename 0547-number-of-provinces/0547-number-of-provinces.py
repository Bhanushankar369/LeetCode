class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n)
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(i+1, n):  # Only Upper Triangle
                if isConnected[i][j] == 1:
                    ds.unionByRank(i, j)

        components = set()
        for i in range(n):
            components.add(ds.findPar(i))

        return len(components)