class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)

        if m*k > len(bloomDay):
            return -1

        temp = [0]*len(bloomDay)
        ans = right

        while left <= right:
            boque = 0
            mid = (left+right)//2
            for i in range(len(temp)):
                temp[i] = bloomDay[i] - mid
            
            count = 0
            for i in range(len(temp)):
                if temp[i] <= 0:
                    count += 1
                    if count == k:
                        boque += 1
                        count = 0
                else:
                    count = 0
            
            if boque >= m:
                ans = min(ans, mid)
                right = mid-1
            else:
                left = mid+1
        
        return ans