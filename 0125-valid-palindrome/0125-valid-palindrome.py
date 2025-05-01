class Solution:
    def isPalindrome(self, s: str) -> bool:
        def palin(s, start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return palin(s, start+1, end-1)
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch
        return palin(new.lower(), 0, len(new)-1)            