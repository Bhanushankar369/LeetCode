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
    def removeStones(self, stones: List[List[int]]) -> int:
        maxx = 0
        maxy = 0
        for u, v in stones:
            maxx = max(u, maxx)
            maxy = max(v, maxy)

        total = maxx+maxy+2

        ds = DisjointSet(total)

        used = set()
        for x, y in stones:
            ds.unionByRank(x, y+maxx+1)
            used.add(x)
            used.add(y+maxx+1)

        components = 0
        for i in range(total):
            if i in used and i == ds.parent[i]:
                components += 1

        return len(stones) - components

        