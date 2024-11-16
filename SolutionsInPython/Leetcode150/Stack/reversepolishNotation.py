# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isnumeric():
                token = int(token)
                stack.append(token)
            elif token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                sum = num1 + num2
                stack.append(sum)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                mul = num1 * num2
                stack.append(mul)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                div = int(num2 / num1)
                stack.append(div)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                sub = num2 - num1
                stack.append(sub) 
                
        return stack.pop()
    
a = Solution()
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

print(int(6//-132))