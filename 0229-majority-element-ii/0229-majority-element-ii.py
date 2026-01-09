class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = collections.Counter(nums)

        arr = []

        for k, v in dic.items():
            if v > len(nums)//3:
                arr.append(k)

        return arr