class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = set()

        for ind in range(len(nums)-2):
            i = ind+1
            j = len(nums)-1

            while i<j:
                if nums[ind] + nums[i] + nums[j] > 0:
                    j-=1
                elif nums[ind] + nums[i] + nums[j] < 0:
                    i+=1
                else:
                    ans.add((nums[ind], nums[i], nums[j]))
                    i+=1
                    j-=1

        return list(ans)