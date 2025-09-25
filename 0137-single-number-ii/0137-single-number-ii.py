class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for bitIndex in range(32):
            count = 0
            for n in nums:
                if (n & (1 << bitIndex)): # Check if bitIndex bit is set or not
                    count += 1

            if count%3 == 1:
                ans = ans | (1 << bitIndex) # Set the bitIndex bit

        # To handle negative integers
        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans