class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visit = [0]*n
        path = [0]*n
        check = [0]*n

        def dfs(node):
            visit[node] = 1
            path[node] = 1

            for nei in graph[node]:
                if not visit[nei]:
                    if dfs(nei):
                        return True

                elif path[nei]:
                    return True

            check[node] = 1
            path[node] = 0
            return False


        for i in range(n):
            if not visit[i]:
                dfs(i)
        
        ans = []
        for i in range(n):
            if check[i]:
                ans.append(i)

        return ans