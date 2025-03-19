class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds = []
        ans = []
        def recur(ind, nums, ds, ans):
            if ind == len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[ind])
            recur(ind+1, nums, ds, ans)
            ds.remove(nums[ind])
            recur(ind+1, nums, ds, ans)
        recur(0, nums, ds, ans)
        return ans