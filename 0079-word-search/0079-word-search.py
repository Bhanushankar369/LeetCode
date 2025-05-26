class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(r, c, ind):
            if ind == len(word):
                return True

            if(r<0 or c<0 or r>=len(board) or c>=len(board[0]) 
                or (r,c) in visited or word[ind] != board[r][c]):
                return False
            
            visited.add((r,c))

            res = (dfs(r-1, c, ind+1) or
                    dfs(r+1, c, ind+1) or
                    dfs(r, c-1, ind+1) or
                    dfs(r, c+1, ind+1))
                    
            visited.remove((r,c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False