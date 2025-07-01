class Solution:
    def findLengthOfLCIS(self, arr: List[int]) -> int:
        dp = [1] * (len(arr))
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp[i] = 1+dp[i-1]
                
            else:
                dp[i] = 1
        return max(dp)