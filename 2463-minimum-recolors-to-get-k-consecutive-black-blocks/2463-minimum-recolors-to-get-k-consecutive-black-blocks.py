class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        mini = float('inf')
        if n==k:
            return blocks.count('W')
        for i in range(n-k+1):
            l = blocks[i:i+k].count('W')
            if l<mini:
                mini = l
        return mini