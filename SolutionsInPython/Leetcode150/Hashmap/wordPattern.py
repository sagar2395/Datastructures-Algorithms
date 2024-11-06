# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False
        
        dict = {}
        for i in range(len(words)):
            if words[i] not in dict:
                dict[words[i]] = pattern[i]
            elif dict[words[i]] != pattern[i]:
                return False
        
        dict2 = {}
        for i in range(len(words)):
            if pattern[i] not in dict2:
                dict2[pattern[i]] = words[i]
            elif dict2[pattern[i]] != words[i]:
                return False
            
        return True
        
        
        
a = Solution()

print(a.wordPattern("abba", "dog cat cat dog"))