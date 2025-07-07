class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for i, j in prerequisites:
            edges[i].append(j)
        
        visited = set()
        def dfs(pre):
            if pre in visited:
                return False
            if not edges[pre]:
                return True
            visited.add(pre)
            for i in edges[pre]:
                if not dfs(i):
                    return False
            
            visited.discard(pre)
            edges[pre] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True