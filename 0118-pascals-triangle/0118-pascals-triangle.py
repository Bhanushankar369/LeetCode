class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(i, j):
            res = 1
            for l in range(j):
                res *= (i-l)
                res /= (l+1)
            return int(res)
        ans = [[1]]
        for i in range(1, numRows):
            lst = []
            for j in range(i+1):
                if(j==0 or j==i):
                    lst.append(1)
                else:
                    lst.append(helper(i, j))
            ans.append(lst)
        return ans