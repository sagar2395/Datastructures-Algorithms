# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=TO_DO

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(M - 1, N - 1): 1}

        def dfs(r, c):
            if r == M or c == N or obstacleGrid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)
    
    # Solution using 2-D array as dp
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS - 1][COLS - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[float("inf")] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[ROWS - 1][COLS - 1] = 1
        def dfs(r, c):
            if r > ROWS - 1 or c > COLS - 1 or obstacleGrid[r][c] == 1:
                return 0
            if dp[r][c] != float("inf"):
                return dp[r][c]
            dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[r][c]
        
        dfs(0,0)
        return dp[0][0]