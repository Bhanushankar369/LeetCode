class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    return False
            return True
        sum_a = 0
        sum_b = 0
        for i in range(len(nums)):
            if isPrime(i):
                sum_a += nums[i]
            else:
                sum_b += nums[i]

        return abs(sum_a-sum_b)