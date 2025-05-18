class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
                or grid[row][col] != 1):
                return 0

            else:
                grid[row][col] = 0
                return 1+dfs(row-1, col)+dfs(row+1, col)+dfs(row, col-1)+dfs(row, col+1)

        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_count = max(dfs(i, j), max_count)
        return max_count