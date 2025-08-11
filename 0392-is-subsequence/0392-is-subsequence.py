class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        ind = 0
        curr = s[0]
        for i in range(len(t)):
            if t[i] == curr:
                ind += 1
                if ind >= len(s):
                    return True
                curr = s[ind]

        return ind == len(s)