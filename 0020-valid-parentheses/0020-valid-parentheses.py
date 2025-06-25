class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "}":"{", "]":"["}
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if stack and map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0