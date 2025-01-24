class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        ind = 0
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        return int("".join(s))