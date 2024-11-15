#  120. Triangle
# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10


from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        result = float("inf")
        path = []
        def backtrack(r, c, sumN):
            if r == len(triangle):
                nonlocal result
                result =  min(result, sumN)
                return

            backtrack(r + 1, c, sumN + triangle[r][c])
            backtrack(r + 1, c + 1, sumN + triangle[r][c])

        backtrack(0, 0, 0)
        return result
    
    # Tried to implement top bottom approach (Memoization)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        result = float("inf")
        cache = []
        
        for r in range(len(triangle)):
            cache.append([float("inf")] * len(triangle[r]))

        def dfs(r, c):
            if r == len(triangle):
                return 0
            if cache[r][c] == float("inf"):
                cache[r][c] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
            return cache[r][c]

        dfs(0, 0)
        return cache[0][0]
    
    # Bottom Up approach of Dynamic Programming
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        result = float("inf")
        cache = []
        
        for r in range(len(triangle)):
            cache.append([float("inf")] * len(triangle[r]))

        cache.append([float("inf")] * (len(triangle[-1]) + 1))

        for i in range(len(triangle) -1, -1, -1):
            for j in range(len(triangle[i]) -1, -1, -1):
                if cache[i+1][j] == float("inf") and cache[i+1][j+1] == float("inf"):
                    cache[i][j] = triangle[i][j]
                else:
                    cache[i][j] = triangle[i][j] + min(cache[i+1][j], cache[i+1][j+1])

        return cache[0][0]

        