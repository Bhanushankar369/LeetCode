class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        count = 0
        ans=[]
        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            else:
                ans.append(nums[j])
        ans.extend([0]*count)
        return ans