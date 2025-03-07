class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        sieve = [True]*(right+1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(right**0.5)+1):
            if sieve[i]:
                for j in range(i*i, right+1, i):
                    sieve[j] = False
        for i in range(left, right+1):
            if sieve[i]:
                primes.append(i)
        if len(primes)<2:
            return [-1, -1]
        min_dis = 99999
        left=-1
        right=-1
        for i in range(len(primes)-1):
            diff = primes[i+1]-primes[i]
            if min_dis > diff:
                min_dis = diff
                left = primes[i]
                right = primes[i+1]
        return [left, right]
