class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0)+1
            if map[num] > len(nums)//2:
                return num
        return -1