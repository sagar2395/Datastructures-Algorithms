# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: left = 5, right = 7
# Output: 4

# Example 2:
# Input: left = 0, right = 0
# Output: 0

# Example 3:
# Input: left = 1, right = 2147483647
# Output: 0

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt