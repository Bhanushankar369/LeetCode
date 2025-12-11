class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)

        map = {}
        for i in range(len(sortedNums)):
            if sortedNums[i] not in map:
                map[sortedNums[i]] = i

        ans = [0]*len(nums)

        for i in range(len(nums)):
            ans[i] = map[nums[i]]
        
        return ans