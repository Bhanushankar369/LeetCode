class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        m = len(image)
        n = len(image[0])
        def dfs(row, col):
            if (row < 0 or row >= m or col < 0 or col >= n or (row, col) in visited or image[row][col]!=check_color):
                return

            image[row][col] = color
            visited.add((row,col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        check_color = image[sr][sc]
        dfs(sr, sc)
        return image