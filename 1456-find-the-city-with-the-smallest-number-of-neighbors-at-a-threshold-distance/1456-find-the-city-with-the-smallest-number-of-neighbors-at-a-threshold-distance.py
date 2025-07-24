class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != float('inf') and dist[via][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][via]+dist[via][j])

        city = -1
        city_neis = float('inf')

        for i in range(n):
            val = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    val += 1

            if city_neis >= val:
                city_neis = val
                city = i
        
        return city