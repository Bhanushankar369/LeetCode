class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for point in range(len(nums)-1, 1, -1):
            i = 0
            j = point-1

            while i < j:
                if nums[i]+nums[j] > nums[point]:
                    count += (j-i) # All pairs btw them are eligible to be a triangle
                    j-=1
                else:
                    i+=1
        
        return count