class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, (n//2)+1):
            curr = s[:i]
            check = len(s[i:])//len(curr)
            
            if s[i:] == curr*check:
                return True
        
        return False