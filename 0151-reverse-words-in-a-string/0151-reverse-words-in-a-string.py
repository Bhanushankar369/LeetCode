class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        new = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new += s[i]
            elif s[i] == " " and new:
                lst.append(new)
                new = ""
            else:
                continue
        if new:
            lst.append(new)
        ans = ""
        for i in range(len(lst)-1, 0, -1):
            ans += lst[i] + " "
        return ans + lst[0]