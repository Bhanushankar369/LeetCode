class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        prev = 0

        even = 0
        odd = 0

        for i in range(len(nums)):
            if i%2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        
        count = 0
        
        for i in range(len(nums)):
            if i%2 == 0:
                even += prev
                even -= nums[i]
            else:
                odd += prev
                odd -= nums[i]
            
            if even == odd:
                count += 1
            
            prev = nums[i]

        return count

