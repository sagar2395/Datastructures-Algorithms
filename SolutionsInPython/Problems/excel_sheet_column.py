# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/description/

# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
            
        return "".join(result[::-1])