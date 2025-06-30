class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = nums[1]

        m = dp[0]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + m
            if dp[i-1] > m:
                m = dp[i-1]
        
        return max(dp)