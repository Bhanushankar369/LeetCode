class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                count += len(nums)-i
        
        return count