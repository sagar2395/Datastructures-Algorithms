# 78. Subsets
# https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(n):
            if n == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[n])
            backtrack(n + 1)

            path.pop()
            backtrack(n + 1)

        backtrack(0)
        return result