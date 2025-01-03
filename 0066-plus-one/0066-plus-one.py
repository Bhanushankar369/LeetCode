class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i in range(len(digits)):
            s = s*10 + digits[i]
        s+=1
        ans = []
        for i in range(len(str(s))):
            ans.append(s%10)
            s//=10
        return ans[::-1]