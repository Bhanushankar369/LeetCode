from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        dq = deque([])

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i, j, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while dq:
            nr, nc, dist = dq.popleft()
            for r, c in directions:
                newr = nr+r
                newc = nc+c

                if (newr<0 or newr>=m or newc<0 or newc>=n
                    or (newr, newc) in visited):
                    continue
                    
                visited.add((newr, newc))

                if mat[newr][newc] == 1:
                    mat[newr][newc] = dist+1
                    dq.append((newr, newc, mat[newr][newc]))
        return mat