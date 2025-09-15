class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        res = 0
        prev = 0
        i = 0

        curr_op = '+'

        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i+=1
                
                i-=1 # This brings back the pointer to its digit position. removes from symbol pos..

                if curr_op == '+':
                    prev = curr
                    res += curr

                elif curr_op == '-':
                    prev = -curr # -curr is because, we just add when we came back
                    res -= curr

                elif curr_op == '*':
                    res -= prev
                    res += prev*curr

                    prev = curr*prev

                else:
                    res -= prev
                    res += int(prev/curr)

                    prev = int(prev/curr)

            elif s[i] != " ":
                curr_op = s[i]

            curr = 0

            i+= 1

        return res