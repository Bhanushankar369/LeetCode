class MinStack:

    def __init__(self):
        self.stack = []
        self.st = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.st:
            self.st.append(min(val, self.st[-1]))
        else:
            self.st.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.st.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()