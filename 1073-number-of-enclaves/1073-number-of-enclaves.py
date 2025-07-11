class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dq = deque([])

        for i in range(m):
            if grid[i][0] == 1:
                dq.append((i, 0))
            if grid[i][n-1] == 1:
                dq.append((i, n-1))

        for j in range(n):
            if grid[0][j] == 1:
                dq.append((0, j))
            if grid[m-1][j] == 1:
                dq.append((m-1, j))

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while dq:
            nr, nc = dq.popleft()
            grid[nr][nc] = -1
            for r, c in directions:
                row = nr+r
                col = nc+c

                if (row < 0 or row >= m or col < 0 or col >= n
                     or grid[row][col] != 1):
                    continue
                
                dq.append((row, col))
                grid[row][col] = -1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count