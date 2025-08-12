class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = collections.Counter(nums)

        for _, val in map.items():
            if val > 1:
                return True
        return False