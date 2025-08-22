class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = math.sqrt(num)
        return int(x) == x