class Solution:
    def possibleStringCount(self, word: str) -> int:
        repeat = 0
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                repeat += 1
            
        return repeat+1