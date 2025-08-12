class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        left = nums[0]
        right = 0
        res = []


        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                right = nums[i-1]

                if right == left:
                    res.append(str(right))
                else:
                    arrow = str(left) + '->' + str(right)
                    res.append(arrow)

                left = nums[i]

        if left == nums[-1]:
            res.append(str(left))
        else:
            res.append(str(left) + '->' + str(nums[-1]))

        return res