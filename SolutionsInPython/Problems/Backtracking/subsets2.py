# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()

        def backtrack(n):
            if n >= len(nums):
                result.append(path[:])
                return

            path.append(nums[n])
            backtrack(n + 1)
            path.pop()
            while n + 1 < len(nums) and nums[n] == nums[n + 1]:
                n += 1
            backtrack(n + 1)

        backtrack(0)
        return result