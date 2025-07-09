class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph)-1
        def dfs(root, lst):
            if root == target:
                result.append(lst[:]+[target])
                return
            lst.append(root)
            for nei in graph[root]:
                dfs(nei, lst)
            lst.remove(root)
        dfs(0, [])
        return result
