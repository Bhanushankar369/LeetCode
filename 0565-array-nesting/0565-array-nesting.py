class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        m = 0
        count = 0
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            nonlocal count
            count += 1
            dfs(nums[node])

        for i in range(len(nums)):
            dfs(nums[i])
            m = max(m, count)
            count = 0
        
        return m