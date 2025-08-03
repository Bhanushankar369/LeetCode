class Solution:
    def findContentChildren(self, greed: List[int], cookie: List[int]) -> int:
        greed.sort()
        cookie.sort()
        i = 0
        j = 0
        count = 0
        
        while i < len(greed) and j < len(cookie):
            if greed[i] <= cookie[j]:
                count += 1
                i += 1
            j += 1
                
        return count