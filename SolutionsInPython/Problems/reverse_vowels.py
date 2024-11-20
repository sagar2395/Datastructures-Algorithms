# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=problem-list-v2&envId=two-pointers&status=TO_DO&difficulty=EASY

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0 
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)

        while i < j:
            cur1 = s[i].lower()
            cur2 = s[j].lower() 

            if cur1 in vowels and cur2 in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif cur1 in vowels:
                j -= 1
            elif cur2 in vowels:
                i += 1
            else:
                i += 1
                j -= 1

        return "".join(s)