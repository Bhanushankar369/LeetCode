class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isSafe(row, col, target):
            if board[row][col] == '.':
                return True

            # Check the same row
            for i in range(len(board)):
                if i != col and board[row][i] == target:
                    return False
            
            # Check the same col
            for j in range(len(board)):
                if j != row and board[j][col] == target:
                    return False

            # Check the same cell i.e, 3x3 grid
            r = row - (row%3)
            c = col - (col%3)

            for x in range(r, r+3):
                for y in range(c, c+3):
                    if (x != row or y != col) and board[x][y] == target:
                        return False
                
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not isSafe(i, j, board[i][j]):
                    return False

        return True
        