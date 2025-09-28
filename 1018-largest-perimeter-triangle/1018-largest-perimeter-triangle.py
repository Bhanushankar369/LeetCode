class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()

        def is_valid(a, b, c):
            if a+b > c and b+c > a and c+a > b:
                return True
            return False

        ans = 0
        for point in range(len(nums)-1, 1, -1):
            i = point-2
            j = point-1

            while i >= 0:
                if is_valid(nums[i], nums[j], nums[point]):
                    return nums[i]+nums[j]+nums[point]
                i-=1

        return ans