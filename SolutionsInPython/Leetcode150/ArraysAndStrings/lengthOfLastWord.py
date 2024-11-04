# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution(object):
    #  Implementation 1
    def lengthOfLastWord(self, s: str) -> int:

        s = s.rstrip()
        count = 0
        i = len(s) - 1
        
        while s[i] != " " and i >= 0:
            count += 1
            i -= 1

        return count
    
    #  Implementation 2
    def lengthOfLastWord1(self, s: str) -> int:
        count = 0
        startCounting = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                startCounting = True
                count += 1

            if startCounting and s[i] == " ":
                break

        return count
            