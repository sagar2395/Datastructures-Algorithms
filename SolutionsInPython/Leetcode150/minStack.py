class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val) :
        self.data.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.data:
            popped = self.data.pop()
            if self.min_stack and popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.data:
            return self.data[-1]
        return -1

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1