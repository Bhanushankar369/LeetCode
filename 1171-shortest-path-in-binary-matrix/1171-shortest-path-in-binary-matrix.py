class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        maxGrid = [[float('inf') for _ in range(n)] for _ in range(n)]
        maxGrid[0][0] = 1
        dq = deque([(1, (0, 0))])
        #Check same question in gfg you will find why we used Just Queue
        #Instead of Priority Queue(heap)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [(-1,0),(1,0),(1,1),(-1,1),(0,-1),(0,1),(-1,-1),(1,-1)]

        while dq:
            depth, (row, col) = dq.popleft()
            for u, v in directions:
                nr = row + u
                nc = col + v

                if (nr < 0 or nr >= n or nc < 0 or nc >= n
                    or grid[nr][nc] != 0):
                    continue

                if maxGrid[nr][nc] > depth+1:
                    maxGrid[nr][nc] = depth+1
                    dq.append((depth+1, (nr, nc)))

        return maxGrid[n-1][n-1] if maxGrid[n-1][n-1] != float('inf') else -1