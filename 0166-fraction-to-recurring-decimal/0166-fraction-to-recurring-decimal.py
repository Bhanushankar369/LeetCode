class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0) != (denominator < 0):
            print(numerator < 0)
            print(denominator < 0)
            print(denominator<0 != numerator<0)
            res.append('-')

        n = abs(numerator)
        d = abs(denominator)

        res.append(str(n//d))
        rem = n%d

        if rem == 0:
            return "".join(res)

        res.append(".")
        rem_map = {}

        while rem != 0:
            if rem in rem_map:
                pos = rem_map[rem]
                res.insert(pos, "(")
                res.append(")")
                return "".join(res)
            
            rem_map[rem] = len(res)
            rem *= 10
            res.append(str(rem//d))
            rem %= d
    
        return "".join(res)