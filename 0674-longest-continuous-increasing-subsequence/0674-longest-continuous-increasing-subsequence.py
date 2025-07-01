class Solution:
    def findLengthOfLCIS(self, arr: List[int]) -> int:
        dp = 1
        m = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp += 1
                
            else:
                m = max(dp, m)
                dp = 1
        return max(dp, m)