class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def recurs(ind, nums, dp):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + recurs(ind-2, nums, dp)
            not_pick = recurs(ind-1, nums, dp)
            dp[ind] = max(pick, not_pick)
            return dp[ind]

        return recurs(len(nums)-1, nums, dp)