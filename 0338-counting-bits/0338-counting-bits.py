class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            count =0
            while num!=0:
                count += num%2
                num //= 2
            return count
        lst = []
        for i in range(n+1):
            lst.append(count(i))
        return lst