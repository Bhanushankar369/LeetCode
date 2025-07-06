class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        lst = collections.defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and isConnected[j][i] == 1:
                    lst[i+1].append(j+1)
        
        valid = [True] * n
        count = 0

        def dfs(node):
            if not valid[node-1]:
                return 
            valid[node-1] = False
            for nei in lst[node]:
                dfs(nei)


        for i in range(1, n+1):
            if valid[i-1]:
                count += 1
                dfs(i)

        return count