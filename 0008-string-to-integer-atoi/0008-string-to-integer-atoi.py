class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        i = 0
        sign = 1

        if s[0] == '-':
            sign = -1
            i += 1

        if s[0] == '+':
            i += 1

        result = 0

        while i<len(s) and s[i].isdigit():
            result = result*10 + int(s[i])
            i+=1
            if result > 2**31 - 1 and sign == 1: return 2**31 - 1
            if result > 2**31 and sign == -1: return -2**31

        return sign * result


#  s = s.strip()
#   if not s: return 0
#   sign = 1
#   i = 0
#   if s[0] == '-':
#     sign = -1
#     i += 1
#   elif s[0] == '+':
#     i += 1
#   result = 0
#   while i < len(s) and s[i].isdigit():
#     result = result * 10 + int(s[i])
#     i += 1
#     if result > 2**31 - 1 and sign == 1: return 2**31 - 1
#     if result > 2**31 and sign == -1: return -2**31
#   return sign * result