class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))

        while start <= end:
            val = (start*start) + (end*end)
            if c == val:
                return True
            elif c > val:
                start += 1
            else:
                end -= 1
            
            print(val)
        
        return False