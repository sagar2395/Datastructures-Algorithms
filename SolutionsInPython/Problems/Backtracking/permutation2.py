# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        v = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            visited = set()
            for i in range(len(nums)):
                if not v[i] and nums[i] not in visited:
                    v[i] = True
                    visited.add(nums[i])
                    path.append(nums[i])
                    backtrack()
                    v[i] = False
                    path.pop()

            
        backtrack()
        return result