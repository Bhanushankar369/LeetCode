class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"

        map = Counter(text)
        count = 0

        while True:
            for char in s:
                if char not in map or map[char] < 1:
                    return count
                
                map[char] -= 1
        
            count += 1
        return count