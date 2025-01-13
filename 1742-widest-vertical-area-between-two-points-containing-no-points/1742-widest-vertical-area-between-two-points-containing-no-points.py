class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lst = []
        for i, j in points:
            lst.append(i)
        lst.sort()
        m = 0
        for i in range(1, len(lst)):
            m = max(m, lst[i]-lst[i-1])
        return m