# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for letter in magazine:
            if letter not in dict:
                dict[letter] = True
        print(dict)
                
        for letter in ransomNote:
            if letter not in dict:
                return False
            
        return True
        
        
ransom = Solution()

ransom.canConstruct("aa", "aab")