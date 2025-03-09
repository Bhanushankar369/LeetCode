class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k>=n:
            return sum(cardPoints)
        lsum, rsum, score = 0, 0, 0
        for i in range(k):
            lsum += cardPoints[i]
        score = lsum
        rind = n-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rind]
            rind -= 1

            score = max(score, lsum+rsum)
        return score