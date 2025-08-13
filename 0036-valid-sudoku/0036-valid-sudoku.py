class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                    
                r = i - (i%3)
                c = j - (j%3)

                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(r, c)]:
                    return False

                row[i].append(board[i][j])
                col[j].append(board[i][j])
                box[(r, c)].append(board[i][j])

        return True
        