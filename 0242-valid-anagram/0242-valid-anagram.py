class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = [0]*26
        for ind in range(len(s)):
            alpha[ord(s[ind])-ord('a')] += 1
            alpha[ord(t[ind])-ord('a')] -= 1

        for n in alpha:
            if n!= 0:
                return False
        
        return True
         