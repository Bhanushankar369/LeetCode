class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n>1:
            if n%2 == 0:
                ans += n/2
                n/=2
            else:
                ans += (n//2)+1
                n//=2
        return int(ans)
