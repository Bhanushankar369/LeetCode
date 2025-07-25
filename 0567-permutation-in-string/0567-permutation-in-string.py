class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        window = len(s1)
        s = collections.Counter(s1)
        for i in range(len(s2) - window + 1):
            if s == collections.Counter(s2[i:i+window]):
                return True
        return False