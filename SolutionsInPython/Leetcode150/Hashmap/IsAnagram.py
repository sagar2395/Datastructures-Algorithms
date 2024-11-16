# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        
        hm = {}
                
        for a in t:
            hm[a] = 1 + hm.get(a, 0)
                
        for a in s:
            if a not in hm or hm[a] == 0:
                return False
            else: 
                hm[a] -= 1
                
        return True