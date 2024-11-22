# 258. Add Digits
# https://leetcode.com/problems/add-digits/description/

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            curNum = 0
            while num > 0:
                curNum += num % 10
                num = num // 10
            num = curNum
        return num
    