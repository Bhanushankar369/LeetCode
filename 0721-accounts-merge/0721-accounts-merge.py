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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet(len(accounts))
        map = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in map:
                    ds.unionByRank(map[accounts[i][j]], i)
                else:
                    map[accounts[i][j]] = i

        ans = defaultdict(list)
        for lst, key in map.items():
            ans[ds.findPar(key)].append(lst)

        result = []
        for i in range(len(accounts)):
            if len(ans[i]) > 0:
                result.append([accounts[i][0]] + sorted(ans[i]))

        return result