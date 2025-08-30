class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dest = 2**len(nums)
        res = []

        for i in range(dest):
            lst = []
            ind = 0
            while i != 0:
                if (i%2):
                    lst.append(nums[ind])
                
                ind += 1
                i //= 2

            res.append(lst)
        
        return res