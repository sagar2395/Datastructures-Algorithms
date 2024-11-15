# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

from typing import List

class Solution:
    
    # This solution is passing test cases but this is not getting successful in submission 
    # due to time complexity.
    # This solution is doing dfs search of path which is doing repetitive calculation.
    # Dynamic Programming should be used for this problem.
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        minSum = float("inf")

        def dfs(r, c, sum):
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                nonlocal minSum
                minSum =  min(minSum, sum)

            if r < len(grid) - 1:
                dfs(r + 1, c, sum + grid[r][c])
            if c < len(grid[0]) - 1:
                dfs(r, c + 1, sum + grid[r][c])

        dfs(0, 0, 0)
        return minSum + grid[len(grid) - 1][len(grid[0]) -1]
    
    
    # This is dynamic programming.
    # Space complexity - O(m.n) or O(n2)
    # Time complexity - O(n)
    # Space complexity can be further improved by using 1-D array instead of 2-D array.
    def minPathSum1(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        res[ROWS - 1][COLS] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        return res[0][0]
    
    
    # My own solution using 1-D array
    def minPathSum2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [float("inf")] * (COLS)
        res.append(0)
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1:
                    res[c] = grid[r][c] + res[c + 1]
                    
                else:
                    right = min(res[c], res[c+1])
                    res[c] = grid[r][c] + right
            if r == ROWS - 1:
                res[-1] = float("inf")

        print(res)

        return res[0] 
    
    # More optimized solution (code wise) making it more concise
    def minPathSum3(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [float("inf")] * (COLS + 1)
        res[-2] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[c] = grid[r][c] + min(res[c], res[c+1])

        return res[0] 



