class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        map = {}
        def backtrack(s, ind):
            if (s, ind) in map:
                return map[(s, ind)]
            if ind == len(nums):
                if s == target:
                    return 1
                return 0
            pos = backtrack(s+nums[ind], ind+1)
            neg = backtrack(s-nums[ind], ind+1)

            map[(s, ind)] = pos+neg

            return map[(s, ind)]
        return backtrack(0, 0)