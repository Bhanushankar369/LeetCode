class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # ans = []
        # def takeNotTake(self, nums, ind, lst, ans):
        #     if ind == len(nums):
        #         ans.append(lst[:])
        #         return
        #     lst.append(nums[ind])
        #     takeNotTake(self, nums, ind+1, lst, ans)
        #     lst.remove(nums[ind])
        #     takeNotTake(self, nums, ind+1, lst, ans)
        # takeNotTake(self, nums, 0, [], ans)
        # x = 0
        # for i in range(len(ans)):
        #     for j in range(1, len(ans[i])):
        #         ans[i][0] ^= ans[i][j]
        #     if ans[i]:
        #         x += ans[i][0]
        # return x

        for i in range(1, len(nums)):
            nums[0] |= nums[i]
        return nums[0]*(2**(len(nums)-1))