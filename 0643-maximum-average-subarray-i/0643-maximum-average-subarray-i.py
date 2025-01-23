class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_avg = curr_sum
        l = 0
        r = k
        while r<len(nums):
            curr_sum += nums[r]
            curr_sum -= nums[r-k]
            max_avg = max(max_avg, curr_sum)
            r+=1
        return max_avg/k