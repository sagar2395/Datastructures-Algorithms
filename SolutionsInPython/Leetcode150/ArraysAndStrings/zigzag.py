# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        res = ""
        increment = (numRows-1)*2
        strLength = len(s)

        for i in range(numRows):
            for j in range(i, strLength, increment):
                res += s[j]
                resIndex = j + increment - 2*i
                if (i > 0 and i < numRows - 1) and resIndex < strLength:
                    res += s[resIndex]

        return res