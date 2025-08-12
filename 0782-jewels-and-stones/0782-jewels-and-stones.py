class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map = collections.Counter(stones)

        count = 0
        for char in jewels:
            if char in map:
                count += map[char]

        return count