class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        map = defaultdict(list)
        for u, v in edges:
            map[v].append(u)

        dp = {}

        def dfs(node):
            if node in dp:
                return dp[node]
            
            ancestor = set()
            for nei in map[node]:
                ancestor.add(nei)
                ancestor.update(dfs(nei))
                # Update is used to add group of elements without repetition

            dp[node] = sorted(ancestor)
            return dp[node]

        result = []
        for i in range(n):
            result.append(dfs(i))

        return result