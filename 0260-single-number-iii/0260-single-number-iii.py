class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]

        right_most = (num & num-1) ^ num

        b1 = 0
        b2 = 0

        for i in range(len(nums)):
            if nums[i] & right_most:
                b1 ^= nums[i]
            else:
                b2 ^= nums[i]

        return [b1, b2]
