class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        x = len(pref)
        for word in words:
            if word[:x] == pref:
                count+=1
        return count