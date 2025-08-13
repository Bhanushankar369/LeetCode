class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            req = target-nums[i]
            if req in map:
                return [i, map[req]]
            
            map[nums[i]] = i

        return [-1, -1]