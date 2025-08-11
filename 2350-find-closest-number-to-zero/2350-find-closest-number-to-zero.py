class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = float('inf')
        diff = float('inf')

        for num in nums:
            if abs(num) < diff:
                val = num
                diff = abs(num)
            elif abs(num) == diff:
                val = max(val, num)

        return val