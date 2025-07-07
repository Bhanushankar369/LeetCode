class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)

        for u, v in prerequisites:
            edges[u].append(v)

        visiting = set()
        processed = set()
        
        def dfs(node):
            if node in visiting:
                return False
            if node in processed:
                return True
            visiting.add(node)
            for nei in edges[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            processed.add(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True