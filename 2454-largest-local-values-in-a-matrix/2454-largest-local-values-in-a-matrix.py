class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def ma(subgrid):
            m = float('-inf')
            for i in range(len(subgrid)):
                if m < max(subgrid[i]):
                    m = max(subgrid[i])
            return m
        ans = []
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                ans.append(ma(subgrid))
        lst = []
        for i in range(len(grid)-2):
            lst.append([0]*(len(grid)-2))
        k=0
        for i in range(len(lst)):
            for j in range(len(lst)):
                lst[i][j] = ans[k]
                k+=1
        return lst