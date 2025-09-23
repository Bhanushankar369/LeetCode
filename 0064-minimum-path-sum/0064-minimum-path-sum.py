class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = []

        for _ in range(m):
            matrix.append([0]*n)

        matrix[0][0] = grid[0][0]

        for i in range(1, n):
            matrix[0][i] = matrix[0][i-1] + grid[0][i]

        for j in range(1, m):
            matrix[j][0] = matrix[j-1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]

        return matrix[m-1][n-1]