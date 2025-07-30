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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet(len(edges))

        x, y = 0, 0
        for u, v in edges:
            if ds.findPar(u-1) != ds.findPar(v-1):
                ds.unionByRank(u-1, v-1)
            else:
                x, y = u, v

        return [x, y]