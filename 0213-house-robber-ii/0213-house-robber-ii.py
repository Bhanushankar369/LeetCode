class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp1 = [0]*n
        dp1[1] = nums[1]
        for i in range(2, n):
            dp1[i] = nums[i] + max(dp1[:i-1])

        dp2 = [0]*n
        dp2[0] = nums[0]
        dp2[1] = nums[1]
        for i in range(2, n-1):
            dp2[i] = nums[i] + max(dp2[:i-1])
        
        temp1 = max(dp1)
        temp2 = max(dp2)
        return max(temp1, temp2)