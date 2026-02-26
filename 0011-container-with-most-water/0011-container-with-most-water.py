class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        maxi = float('-inf')

        while (left < right):
            water = abs(left-right) * min(nums[left], nums[right])
            maxi = max(water, maxi)

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        
        return maxi
        