class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        count=0
        check=0
        i=1
        j=n-1
        for i in range(n-1):
            check += nums[i]
            if(check >= s-check):
                count+=1
        return count