class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        arr.sort()
        if not arr:
            return 0
        curr = 1
        max_len = 1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                continue
            elif arr[i] == 1+arr[i-1]:
                curr += 1
            else:
                max_len = max(max_len, curr)
                curr = 1
        return max(max_len, curr)