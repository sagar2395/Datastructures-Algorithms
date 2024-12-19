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
        magMap = {}

        for i in range(len(magazine)):
            magMap[magazine[i]] = 1 + magMap.get(magazine[i], 0)

        for i in range(len(ransomNote)):
            if magMap.get(ransomNote[i], 0) <= 0:
                return False
            else:
                magMap[ransomNote[i]] -= 1

        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for letter in magazine:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
                
        for letter in ransomNote:
            if letter not in dict:
                return False
            elif dict[letter] == 0:
                return False
            else:
                dict[letter] -= 1
            
        return True
        
        
ransom = Solution()

ransom.canConstruct("aa", "aab")