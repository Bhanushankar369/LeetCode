class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        for i in gain:
            lst.append(i+lst[-1])
        return max(lst)