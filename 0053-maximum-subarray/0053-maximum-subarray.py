class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxi = 0
        if max(nums)<0:
            return max(nums)

        for i in range(len(nums)):
            curr += nums[i]
            if curr < 0:
                curr = 0
            
            maxi = max(curr, maxi)
        
        return max(maxi, curr)