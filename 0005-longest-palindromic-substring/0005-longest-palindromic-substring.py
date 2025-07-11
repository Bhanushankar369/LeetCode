class Solution:
    def longestPalindrome(self, s: str) -> str:
        new = ""
        newLen = 0
        for i in range(len(s)):
            # for odd length
            left, right = i, i
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > newLen:
                    new = s[left:right+1]
                    newLen = right-left+1
                left -= 1
                right += 1

            # for Even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > newLen:
                    new = s[left:right+1]
                    newLen = right-left+1
                left -= 1
                right += 1
        return new