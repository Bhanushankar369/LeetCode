class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = collections.Counter(magazine)

        for char in ransomNote:
            if char not in map or map[char] < 1:
                return False
            
            map[char] -= 1

        return True