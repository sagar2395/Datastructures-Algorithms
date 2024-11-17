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
        i = 0

        cur = prev = res = 0
        cur_operation = "+"

        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1 

                i -= 1

                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    mul = prev * cur
                    res += mul
                    prev = mul
                else:
                    res -= prev
                    div = int(prev/cur)
                    res += div
                    prev = div

                cur = 0

            elif cur_char != " ":
                cur_operation = cur_char  

            i += 1
        return res