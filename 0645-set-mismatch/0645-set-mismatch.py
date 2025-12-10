class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map = {}

        for i in range(len(nums)):
            map[i+1] = 0

        for i in range(len(nums)):
            map[nums[i]] += 1
        
        dup, missing = -1, -1

        for key, val in map.items():
            if val == 2:
                dup = key
            if val == 0:
                missing = key
        
        return [dup, missing]
        
