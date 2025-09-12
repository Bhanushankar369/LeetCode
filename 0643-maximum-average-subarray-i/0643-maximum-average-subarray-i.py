class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        ind = k
        while ind < len(nums):
            curr_sum += nums[ind]
            curr_sum -= nums[ind-k]

            max_sum = max(max_sum, curr_sum)
            ind += 1
        
        return max_sum/k