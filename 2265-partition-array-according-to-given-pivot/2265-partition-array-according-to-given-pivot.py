class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ind = nums.index(pivot)
        count = 0
        left = []
        right = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                right.append(nums[i])
            elif nums[i] < pivot:
                left.append(nums[i])
            if nums[i] == pivot:
                count += 1
        ans = [*left, *[pivot]*count,*right]
        return ans