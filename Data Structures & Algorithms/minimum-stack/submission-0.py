class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        minVal = min(val, self.minArr[-1]) if self.minArr else val
        self.minArr.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minArr.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        return self.minArr[-1]
