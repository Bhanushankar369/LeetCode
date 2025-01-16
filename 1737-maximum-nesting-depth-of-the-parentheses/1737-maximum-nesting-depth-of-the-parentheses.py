class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0
        for i in s:
            if i == '(':
                stack.append('(')
            if i == ')':
                stack.pop()
            if s and result<len(stack):
                result = len(stack)
        return result