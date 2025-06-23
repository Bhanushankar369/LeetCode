class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        lst = []
        for i in range(0, len(s), k):
            x = s[i:i+k]
            if len(x)<k:
                x += fill * (k-len(x))
            lst.append(x)
        return lst