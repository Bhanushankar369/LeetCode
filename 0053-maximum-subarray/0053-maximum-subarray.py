class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = max(nums)
        if x < 0:
            return x

        arr = [0] * (len(nums)+1)

        for i in range(len(nums)):
            if arr[i-1]+nums[i]<0:
                continue
            arr[i] = arr[i-1] + nums[i]

        return max(max(arr), x)
