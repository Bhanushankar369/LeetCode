class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)

        for u, v in prerequisites:
            edges[u].append(v)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if not edges[node]:
                return True
            visited.add(node)
            for nei in edges[node]:
                if not dfs(nei):
                    return False
            visited.discard(node)
            edges[node] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True