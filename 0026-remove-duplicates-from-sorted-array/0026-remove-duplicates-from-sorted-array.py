class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return []

        ind = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            nums[ind] = nums[i]
            ind += 1
        
        return ind