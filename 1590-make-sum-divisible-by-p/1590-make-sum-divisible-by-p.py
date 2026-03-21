class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total%p
    
        if rem == 0:
            return 0

        res = len(nums)
        curr = 0

        map = {0:-1}

        for i, n in enumerate(nums):
            curr = (curr + n) % p
            prefix = (curr - rem + p) % p # +p is useful for negative results

            if prefix in map:
                length = i - map[prefix]
                res = min(res, length)
            
            map[curr] = i
        
        return -1 if res == len(nums) else res