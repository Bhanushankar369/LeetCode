class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        first = s[:len(s)//2]
        second = s[len(s)//2:]
        c = 0
        for i in range(len(first)):
            if first[i] in vowels:
                c += 1
            if second[i]  in vowels:
                c -= 1
        return c==0