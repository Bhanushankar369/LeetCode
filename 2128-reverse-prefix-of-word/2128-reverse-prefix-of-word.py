class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                break
        if i == len(word)-1:
            if word[i] == ch:
                return word[::-1]
            return word
        return word[:i+1][::-1] + word[i+1:]