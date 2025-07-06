class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == 0 or len(piles)==0:
            return 0
        if len(piles) ==1:
            if piles[0] > h:
                return math.ceil(piles[0]/h)
            return 1
        if h == len(piles):
            return max(piles)

        def isSatisfies(x):
            total = 0
            for pile in piles:
                total += math.ceil(pile/x)
                if total > h:
                    return False
            return True

        left = 0
        right = max(piles)
        result = 0
        while left <= right:
            mid = (left+right)//2
            if mid and isSatisfies(mid):
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result
        