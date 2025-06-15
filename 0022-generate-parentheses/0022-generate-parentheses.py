class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append("(")
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        result = []

        def backtrack(s):
            if len(s) == 2 * n:
                result.append(s)
                return
            backtrack(s + "(")
            backtrack(s + ")")

        backtrack("")

        res = []
        for com in result:
            if valid(com):
                res.append(com)

        return res

