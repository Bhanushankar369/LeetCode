class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buyPrice = nums[0]
        profit = 0

        for i in range(1, len(nums)):
            if nums[i] < buyPrice:
                buyPrice = nums[i]

            profit = max(profit, nums[i]-buyPrice)

        return profit