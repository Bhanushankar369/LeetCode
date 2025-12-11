class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            map[i+1] = 0
        
        for i in range(len(nums)):
            map[nums[i]] += 1
        
        ans = []
        for k, v in map.items():
            if v == 0:
                ans.append(k)

        return ans