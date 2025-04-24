class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if buy>nums[i]:
                buy = nums[i]
            
            ans = max(ans, nums[i]-buy)
        return ans