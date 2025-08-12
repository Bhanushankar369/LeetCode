class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = collections.Counter(s)
        map_t = collections.Counter(t)

        if len(map_s) != len(map_t):
            return False

        for key, val in map_s.items():
            if val != map_t[key]:
                return False
        
        return True