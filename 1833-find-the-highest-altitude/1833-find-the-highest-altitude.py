class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        m = 0
        for i in gain:
            x = i+prev
            if x>m:
                m = x
            prev = x
        return m