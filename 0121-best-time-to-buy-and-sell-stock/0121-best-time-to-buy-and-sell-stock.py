class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy_price = nums[0]
        profit = 0
        for i in range(1, len(nums)):
            if nums[i] < buy_price:
                buy_price = nums[i]

            profit = max(profit, nums[i]-buy_price)
        
        return profit