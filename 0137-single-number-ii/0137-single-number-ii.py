class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = Counter(nums)
        for key, val in map.items():
            if val == 1:
                return key
        
        return -1