class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1

        divi = abs(dividend)
        divs = abs(divisor)

        if divi == divs:
            return sign*1

        ans = 0

        while divi >= divs:
            count = 0

            while divi >= (divs<<(count+1)): # This equals to divs*(2**(count+1))
                count += 1
            
            ans += (1 << count)
            divi -= (divs * (1 << count)) # (1<<count) is equivalent to 2**count

        if ans>=2**31-1 and sign == 1:
            return 2**31-1
        elif ans>=2**31 and sign == -1:
            return -2**31
        
        return ans*sign