class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if val != []: self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)