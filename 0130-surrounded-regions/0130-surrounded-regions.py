class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m = len(board)
        n = len(board[0])

        def dfs(row, col):
            if( row<0 or row>=m or col<0 or col>=n
                or board[row][col] == 'X' or (row, col) in visited):
                return 
            
            board[row][col] = 'T'
            visited.add((row, col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        
        for r in range(n):
            if board[0][r] == 'O':
                board[0][r] = 'T'
            
            if board[m-1][r] == 'O':
                board[m-1][r] = 'T'

        for c in range(m):
            if board[c][0] == 'O':
                board[c][0] = 'T'
            
            if board[c][n-1] == 'O':
                board[c][n-1] = 'T'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            
