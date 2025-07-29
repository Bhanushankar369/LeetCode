class DisjointSet:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]
    
    def findPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulu_u = self.findPar(u)
        ulu_v = self.findPar(v)
        
        if ulu_u == ulu_v: return 
        if self.size[ulu_u] < self.size[ulu_v]:
            self.parent[ulu_u] = ulu_v
            self.size[ulu_v] += self.size[ulu_u]
        else:
            self.parent[ulu_v] = ulu_u
            self.size[ulu_u] += self.size[ulu_v]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n*n)
        directions = [(-1,0),(0,1),(0,-1),(1,0)]

        def bfs(r, c):
            node = r*n+c
            for u, v in directions:
                nr = r+u
                nc = c+v

                if (nr < 0 or nr >= n or nc < 0 or nc >= n
                    or grid[nr][nc] != 1):
                    continue

                adj_node = nr*n+nc
                ds.unionBySize(node, adj_node)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)

        # Making 0 to 1
        maxi = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1: continue
                components = set()
                for u, v in directions:
                    nr = u+r
                    nc = v+c

                    if (nr < 0 or nr >= n or nc < 0 or nc >= n
                    or grid[nr][nc] != 1):
                        continue

                    components.add(ds.findPar(nr*n+nc))

                # Calculating after every 0 to 1 conversion
                total = 0
                for val in components:
                    total += ds.size[val]
                maxi = max(total+1, maxi) # +1 is for the coverted 0 itself

        for i in range(n*n):
            maxi = max(maxi, ds.size[ds.findPar(i)])

        return maxi