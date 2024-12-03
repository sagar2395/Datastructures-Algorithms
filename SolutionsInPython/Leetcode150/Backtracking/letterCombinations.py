# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        path = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i):
            if len(path) == len(digits):
                result.append("".join(path))
                return

            for char in digitToChar[digits[i]]:
                path.append(char)
                backtrack(i + 1)
                path.pop()
        if len(digits) > 0:
            backtrack(0)
        return result
    
    # Similar approach. Just for understanding
    def letterCombinations(self, digits: str) -> List[str]:
        
        results = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                results.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return results
    
    # Solving without backtracking using for loop
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        path = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        result = [""]
        for digit in digits:
            temp = []
            for res in result:
                for j in digitToChar[digit]:
                    temp.append(res + j)
            result = temp

        return result