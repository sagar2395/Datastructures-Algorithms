# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/description/

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in ['+', '-']:
                res  += sign * cur
                sign = 1 if char == '+' else -1
                cur = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif char == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0

        return res + sign * cur 