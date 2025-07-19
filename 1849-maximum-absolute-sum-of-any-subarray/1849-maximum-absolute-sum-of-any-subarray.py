class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def maxSubarraySum(arr):
            res = arr[0]
            maxEnding = arr[0]

            for i in range(1, len(arr)):
                maxEnding = max(maxEnding + arr[i], arr[i])
                res = max(res, maxEnding)
            
            return res

        positive = maxSubarraySum(nums)
        for i in range(len(nums)):
            nums[i] *= -1

        negative = maxSubarraySum(nums)
        return max(positive, negative)