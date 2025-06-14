class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        dq = deque()
        fresh = 0
        time = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    dq.append([r, c])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while dq and fresh > 0:
            for i in range(len(dq)):
                rr, rc = dq.popleft()

                for row, col in directions:
                    dr, dc = row+rr, col+rc

                    if (dr<0 or dr>=rows or dc<0 or dc>=cols
                        or grid[dr][dc] != 1):
                        continue 

                    dq.append([dr, dc])
                    grid[dr][dc] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1