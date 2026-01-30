class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def chess(ind, board, ans):
            if ind == n:
                ans.append(["".join(row) for row in board])
                return

            for i in range(n):
                if isSafe(board, i, ind):
                    board[i][ind] = 'Q'
                    chess(ind+1, board, ans)
                    board[i][ind] = '.'
        
        def isSafe(board, row, col):
            dummyRow = row
            dummyCol = col

            while row>=0 and col>=0:
                if board[row][col] == 'Q':
                    return False
                
                row -= 1
                col -= 1
            
            coll = dummyCol
            while coll >= 0:
                if board[dummyRow][coll] == 'Q':
                    return False
                
                coll -= 1


            while dummyRow < n and dummyCol >= 0:
                if board[dummyRow][dummyCol] == 'Q':
                    return False

                dummyRow += 1
                dummyCol -= 1

            return True
        
        chess(0, board, ans)
        
        return ans