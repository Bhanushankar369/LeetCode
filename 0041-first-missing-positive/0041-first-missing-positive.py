class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        map = {}
        for i in range(1, len(nums)+1):
            map[i] = 0
        
        for i in range(len(nums)):
            map[nums[i]] = 1
        
        for k, v in map.items():
            if v == 0:
                return k
        
        return len(nums)+1