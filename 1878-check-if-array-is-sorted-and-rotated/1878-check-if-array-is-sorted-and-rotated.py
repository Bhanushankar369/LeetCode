class Solution:
    def check(self, nums: List[int]) -> bool:
        first = sorted(nums)
        l = len(nums)
        nums += nums
        for i in range(len(nums)-l):
            if nums[i:i+l] == first:
                return True
        return False