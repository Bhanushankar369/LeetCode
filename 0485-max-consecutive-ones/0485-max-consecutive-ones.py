class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                ans = max(count, ans)
                count = 0
        return max(count, ans)