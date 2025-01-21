class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = float('-inf')
        prev = m
        for i in range(len(nums)):
            if nums[i]<=m and nums[i]>prev:
                prev = nums[i]
            if nums[i]>m:
                prev = m
                m = nums[i]
        return (m-1)*(prev-1)