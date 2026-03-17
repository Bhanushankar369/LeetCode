class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lst = []
        for i in range(len(s)):
            if s[i]!='-':
                if s[i].isalpha():
                    lst.append(s[i].upper())
                else:
                    lst.append(s[i])

        if len(s) < k:
            return "".join(lst)
        
        firstRem = len(lst)%k

        ans = "".join(lst[:firstRem])
        l = len(lst)//k

        temp = []

        while l:
            temp.append("".join(lst[firstRem: firstRem+k]))
            firstRem += k
            l -= 1
        
        if ans:
            ans += '-'

        return ans + "-".join(temp)