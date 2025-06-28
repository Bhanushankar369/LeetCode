class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        s = 0
        for no in nums:
            s += no
            if s > maxi:
                maxi = s
            if s < 0:
                s = 0

        if maxi < 0:
            return max(nums)
        return maxi