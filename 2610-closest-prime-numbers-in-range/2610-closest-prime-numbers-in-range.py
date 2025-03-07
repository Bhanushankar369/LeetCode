class Solution:
    def closestPrimes(self, leftee: int, rightee: int) -> List[int]:
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        min_dis = 99999
        left=-1
        right=-1
        primes = []
        for i in range(leftee, rightee+1):
            if isPrime(i):
                primes.append(i)
        for i in range(len(primes)-1):
            diff = primes[i+1]-primes[i]
            if min_dis > diff:
                min_dis = diff
                left = primes[i]
                right = primes[i+1]
        return [left, right]
