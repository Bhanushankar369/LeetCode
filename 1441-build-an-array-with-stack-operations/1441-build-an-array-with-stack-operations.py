class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        check = []

        for i in range(1, n+1):
            check.append(i)

        ti, ci = 0, 0

        ans = []
        x = 0

        while ti< len(target) and ci< len(check):
            if target[ti] == check[ci]:
                ans.extend(["Pop"]*x)
                ans.append("Push")
                x = 0
                ti+= 1
                ci+= 1
            else:
                ans.append("Push")
                x += 1
                ci += 1
        
        return ans