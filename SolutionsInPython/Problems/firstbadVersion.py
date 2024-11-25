# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(n: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n

        while l <= r:
            m = (l + r) //2

            if isBadVersion(m):
                r = m - 1
                if not isBadVersion(m - 1) or m == 1:
                    return m
            else:
                l = m + 1