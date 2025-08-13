class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = Counter(text)
        return min(map['b'], map['a'], map['l']//2, map['o']//2, map['n'])