class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[False for _ in range(n)] for _ in range(n)]
        for u, v in prerequisites:
            dist[u][v] = True

        for i in range(n):
            dist[i][i] = True

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] or (dist[i][via] and dist[via][j]):
                        dist[i][j] = True

        result = []
        for x, y in queries:
            result.append(dist[x][y])

        return result