class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack = []
        s = 0

        for i in range(len(op)):
            if op[i] == '+':
                num = stack[-1] + stack[-2]
                stack.append(num)
                s += num
            elif op[i] == 'C':
                num = stack.pop()
                s -= num
            elif op[i] == 'D':
                num = stack[-1]*2
                stack.append(num)
                s += num
            else:
                num = int(op[i])
                stack.append(num)
                s += num

        return s