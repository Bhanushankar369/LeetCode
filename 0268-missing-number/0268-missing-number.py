class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n*(n+1))//2
        s -= sum(nums)
        return s