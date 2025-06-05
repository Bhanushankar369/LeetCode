class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        k=0
        for i in range(zero):
            nums[k] = 0
            k+=1
        for i in range(one):
            nums[k] = 1
            k+=1
        for i in range(two):
            nums[k] = 2
            k+=1