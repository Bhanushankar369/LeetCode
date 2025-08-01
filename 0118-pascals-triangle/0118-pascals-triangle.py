class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            level = [1]
            for j in range(1, i):
                level.append(ans[i-1][j-1] + ans[i-1][j])
                print(ans[i-1][j-1])
            level.append(1)
            ans.append(level)
        return ans
