class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = collections.Counter(nums)
        max_freq = max(map.values())

        total = 0

        for _, val in map.items():
            if val == max_freq:
                total += val
            
        return total