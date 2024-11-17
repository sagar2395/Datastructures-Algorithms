#  289. Game of Life
# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        tempBoard = []
        for row in range(len(board)):
            cur = []

            for col in range(len(board[row])):
                liveCount = 0

                if col > 0:
                    if board[row][col-1] == 1:
                        liveCount += 1
                    
                    if row > 0:
                        if board[row-1][col-1] == 1:
                            liveCount += 1
                    
                    if row < len(board) - 1:
                        if board[row+1][col-1]:
                            liveCount += 1
                
                if col < len(board[row]) - 1:
                    if board[row][col + 1] == 1:
                        liveCount += 1

                    if row > 0:
                        if board[row-1][col+1] == 1:
                            liveCount += 1

                    if row < len(board) - 1:
                        if board[row+1][col+1] == 1:
                            liveCount += 1

                if row > 0:
                    if board[row-1][col] == 1:
                        liveCount += 1
                    
                if row < len(board) - 1:
                    if board[row+1][col] == 1:
                        liveCount += 1

                if board[row][col] == 1:
                    if liveCount < 2 or liveCount > 3:
                        cur.append(0)
                    else:
                        cur.append(1)
                else:
                    if liveCount == 3:
                        cur.append(1)
                    else:
                        cur.append(0)
            tempBoard.append(cur)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = tempBoard[i][j]