class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        time = [float('inf')]*(n*n)
        visit = set()
        heap = []

        heapq.heappush(heap, (grid[0][0], (0, 0)))
        time[0] = grid[0][0]

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(n):
                while heap:
                    dist, (r, c) = heapq.heappop(heap)

                    for row, col in directions:
                        nr = row+r
                        nc = col+c

                        if (nr < 0 or nr >= n or
                            nc < 0 or nc >= n or
                            (nr, nc) in visit):
                            continue
                        
                        visit.add((nr, nc))
                        ind = nr*n + nc

                        if time[ind] > max(dist, grid[nr][nc]):
                            time[ind] = max(dist, grid[nr][nc])
                            heapq.heappush(heap, (max(dist, grid[nr][nc]), (nr, nc)))

        return time[-1]
