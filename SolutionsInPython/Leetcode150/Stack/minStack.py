# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

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