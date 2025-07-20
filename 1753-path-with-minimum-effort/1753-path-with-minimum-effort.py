import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        heap = []
        heapq.heappush(heap, (0,0,0))

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while heap:
            effort, row, col = heapq.heappop(heap)
            if row == m-1 and col == n-1:
                return effort
            for u, v in directions:
                nr = row + u
                nc = col + v

                if (nr < 0 or nr >= m or nc < 0 or nc >= n):
                    continue

                newEffort = max(effort, abs(grid[nr][nc] - grid[row][col]))
                if dist[nr][nc] > newEffort:
                    dist[nr][nc] = newEffort
                    heapq.heappush(heap, (newEffort, nr, nc))        
        return -1