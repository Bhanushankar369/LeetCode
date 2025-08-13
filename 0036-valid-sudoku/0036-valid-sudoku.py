class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(i//3, j//3)]:
                    return False

                row[i].append(board[i][j])
                col[j].append(board[i][j])
                box[(i//3, j//3)].append(board[i][j])

        return True
        