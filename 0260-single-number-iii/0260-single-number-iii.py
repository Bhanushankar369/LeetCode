class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        map = Counter(nums)
        lst = []

        for k, v in map.items():
            if v == 1:
                lst.append(k)

        return lst