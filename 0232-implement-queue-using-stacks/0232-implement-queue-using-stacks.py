class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        val = self.stack[0]
        temp = self.stack[1:]
        self.stack = temp
        
        return val

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not len(self.stack) > 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()