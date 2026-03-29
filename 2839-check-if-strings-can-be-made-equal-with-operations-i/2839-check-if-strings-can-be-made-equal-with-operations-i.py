class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if s1 == s2[2] + s2[1] + s2[0] + s2[3]:
            return True

        if s1 == s2[0] + s2[3] + s2[2] + s2[1]:
            return True
        
        if s1 == s2[2] + s2[3] + s2[0] + s2[1]:
            return True

        return False