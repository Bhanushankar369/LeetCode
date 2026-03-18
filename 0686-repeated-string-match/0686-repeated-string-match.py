class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        import math
        if not b:
            return 0
        
        if not a:
            return -1
            
        rem = math.ceil((len(b)/len(a)))

        temp = rem*a

        if b in temp:
            return rem
        
        if b in temp+a:
            return rem+1
        
        return -1