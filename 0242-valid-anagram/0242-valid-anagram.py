class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = collections.Counter(s)
        map_t = collections.Counter(t)

        for char in set(s):
            if map_s[char] != map_t[char]:
                return False
        
        return True