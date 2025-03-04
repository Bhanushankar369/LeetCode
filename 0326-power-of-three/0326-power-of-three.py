class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1: return True
        while n>0:
            if n==1: return True
            n/=3.0
        return False