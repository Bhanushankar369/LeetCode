class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurs(ind, nums, dp):
            if ind == 0:
                return nums[ind]
            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + recurs(ind-2, nums, dp)
            not_pick = recurs(ind-1, nums, dp)

            dp[ind] = max(pick, not_pick)
            return dp[ind]
        if len(nums) <= 3:
            return max(nums)
        n = len(nums)
        dp1 = [-1]*n
        first = recurs(n-2, nums[:n-1], dp1)
        dp2 = [-1]*n
        last = recurs(n-2, nums[1:], dp2)

        return max(first, last)