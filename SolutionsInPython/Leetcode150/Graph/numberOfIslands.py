# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0 

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1 ,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == "1") and ((r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    numIslands += 1
                    dfs(r, c)
        return numIslands