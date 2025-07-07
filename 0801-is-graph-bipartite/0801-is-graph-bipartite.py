class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        def dfs(curr, col):
            colors[curr] = col

            for node in graph[curr]:
                if colors[node] == -1:
                    if not dfs(node, 1-col):
                        return False

                elif colors[node] == col:
                    return False
            return True
            


        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True