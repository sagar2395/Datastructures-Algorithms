# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0

from typing import List
class Solution:
    
    # memoization technique of dynamic programming - Top down
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} 

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
                
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2
    
    # Dynamic Programming - Bottom up approach
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        maxValue = 0
        
        for r in range(ROWS -1, -1, -1):
            for c in range(COLS -1, -1, -1):
                down = cache[r + 1][c]
                right = cache[r][c+1]
                diag = cache[r+1][c+1]
                
                if matrix[r][c] == "1":
                    cache[r][c] = 1 + min(down, right, diag)
                    maxValue = max(maxValue, cache[r][c])
                    
        return maxValue ** 2