# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
class Solution:
    #  My solution
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            tempResult = ""
            for j in range(min(len(strs[i]), len(prefix))):
                if strs[i][j] == prefix[j]:
                   tempResult += strs[i][j]
    
                else:
                    break

            prefix = tempResult
            print(prefix)

        return prefix
    
    # leetcode discussion solution. Organized code 
    
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref
