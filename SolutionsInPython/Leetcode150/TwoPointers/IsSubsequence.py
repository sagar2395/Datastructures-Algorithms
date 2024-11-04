# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
         
        while i < len(s):
            if j == len(t):
                return False
            else:
                if s[i] == t[j]:
                    i += 1
                j+= 1
                    
        return True