class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        maxi = 0
        for i in range(len(gain)):
            curr += gain[i]
            maxi = max(maxi, curr)
        
        return maxi