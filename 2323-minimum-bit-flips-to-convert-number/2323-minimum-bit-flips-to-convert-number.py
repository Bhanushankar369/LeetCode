class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        count = 0

        # Counting number of 1's in the result
        # while n!=0:
        #     n = n&(n-1)
        #     count += 1

        # Another way of counting 1's
        while n>1:
            count += n&1
            n = n>>1
        
        if n==1: count += 1

        return count