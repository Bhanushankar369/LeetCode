class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(ir, ic):
            dq = deque([(ir, ic)])
            
            while dq:
                nr, nc = dq.popleft()
                for r, c in directions:
                    row = nr+r
                    col = nc+c

                    if (row < 0 or row >= m or col < 0 or col >= n
                        or (row, col) in visited or grid[row][col] != "1"):
                        continue

                    dq.append((row, col))
                    visited.add((row, col))

                    grid[row][col] = "-1"

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count

                    