class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums2[i-1] != nums1[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = 1 + dp[i-1][j-1]
        
        return dp[n][m]
