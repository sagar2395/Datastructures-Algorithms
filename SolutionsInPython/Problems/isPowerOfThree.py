# 326. Power of Three
# https://leetcode.com/problems/power-of-three/description/

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

class Solution:
    def isPowerOfThree(self, n: int) -> bool: 
        if n < 1:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3

        return True