class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        res = 0

        n = len(nums)

        while left < n and right < n:
            while right < n and (nums[right] or k):
                if nums[right] == 0:
                    k -= 1
                right += 1
            
            res = max(res, right-left)
            
            while left < n and k == 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        res = max(res, right-left)
        return res