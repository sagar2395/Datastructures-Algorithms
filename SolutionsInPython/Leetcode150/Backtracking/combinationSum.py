# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM&status=TO_DO

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        def backtrack(i, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target or i >= len(candidates):
                return

            comb.append(candidates[i])
            backtrack(i, comb, total + candidates[i])
            comb.pop()
            backtrack(i + 1, comb, total)

            return res

        return backtrack(0, [], 0)