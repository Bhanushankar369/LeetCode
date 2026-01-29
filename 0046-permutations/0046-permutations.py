class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ds = []
        def recurs(ind, ds, nums):
            if ind == len(nums):
                ds.append(nums[:])
                return

            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                recurs(ind+1, ds, nums)
                nums[i], nums[ind] = nums[ind], nums[i] # To get previous arr state
        
        recurs(0, ds, nums)
        return ds