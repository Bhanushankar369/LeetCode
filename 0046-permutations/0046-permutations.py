class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = 0

        def recurs(nums, ds, temp, map):
            if len(temp) == len(nums):
                ds.append(temp[:])
                return

            for i in range(len(nums)):
                if not map[nums[i]]:
                    map[nums[i]] = 1
                    temp.append(nums[i])

                    recurs(nums, ds, temp, map)

                    temp.pop()
                    map[nums[i]] = 0
            
        recurs(nums, ans, [], map)
        return ans