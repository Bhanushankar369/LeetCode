class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        for i in nums:
            if i==0:
                continue
            elif i<0:
                neg+=1
            else:
                pos+=1
        return max(neg, pos)