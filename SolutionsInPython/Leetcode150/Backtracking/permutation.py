# 46. Permutations
# https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if(len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result
    
    # Backtracking approach
    def permute1(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        v = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not v[i]:
                    v[i] = True
                    path.append(nums[i])
                    backtrack()
                    v[i] = False
                    path.pop()

            
        backtrack()
        return result