class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if (x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] != '1'):
                return
            
            grid[x][y] = '*'

            dfs(grid, x-1, y)
            dfs(grid, x+1, y)
            dfs(grid, x, y-1)
            dfs(grid, x, y+1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans