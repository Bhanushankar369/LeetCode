# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            t_or_f = isBadVersion(mid)
            if t_or_f:
                right = mid
            else:
                left = mid+1
        return left