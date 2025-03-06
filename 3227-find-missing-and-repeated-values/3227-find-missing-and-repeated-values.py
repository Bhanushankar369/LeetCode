class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        def cyclicSort(nums):
            i=0
            while i<len(nums):
                correct = nums[i]-1
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i+=1
            for i in range(len(nums)):
                if nums[i]!=i+1:
                    return [nums[i], i+1]
            return [len(nums), len(nums)]
        lst = []
        for i in range(len(grid)):
            lst.extend(grid[i])
        return cyclicSort(lst)