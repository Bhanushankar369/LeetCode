class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        m = float('-inf')
        while(i < j):
            water = abs(j-i)*(min(nums[i], nums[j]))
            m = max(m, water)

            if nums[i] < nums[j]:
                i+=1
            else:
                j-=1
        return m
        