class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        prev_start, prev_end = intervals[0]
        ans = []

        for start, end in intervals[1:]:
            if start <= prev_end:
                prev_end = max(end, prev_end)
            
            else:
                ans.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        ans.append([prev_start, prev_end])
        return ans