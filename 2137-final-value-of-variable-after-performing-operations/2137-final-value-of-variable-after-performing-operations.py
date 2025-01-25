class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                num += 1
            else:
                num -= 1
        return num