class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0]*len(nums)
        i = 0
        j = len(nums)-1
        ind = len(nums)-1

        while i <= j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                squares[ind] = nums[j]*nums[j]
                j-=1
            else:
                squares[ind] = nums[i]*nums[i]
                i+=1
            ind -= 1
        
        return squares