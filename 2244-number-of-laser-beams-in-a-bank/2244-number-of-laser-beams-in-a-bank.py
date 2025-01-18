class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            lasers = row.count('1')
            if lasers > 0:
                ans += lasers*prev
                prev = lasers
        return ans