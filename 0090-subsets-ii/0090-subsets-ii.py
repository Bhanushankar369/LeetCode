class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        check = [[]]

        nums.sort()

        def sets(ind, arr, temp, nums):
            arr.append(temp[:])

            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue

                temp.append(nums[i])
                sets(i+1, arr, temp, nums)
                temp.pop()

        sets(0, ans, [], nums)
        return ans
            