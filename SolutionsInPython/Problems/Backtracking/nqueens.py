# 51. N-Queens
# https://leetcode.com/problems/n-queens/description/?envType=problem-list-v2&envId=backtracking

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board= [["."] * n for i in range(n)]

        def backtrack(r):
            print("backtrack({0})".format(r))
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                print(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                print("before col: {0}".format(col))
                print("before posDiag: {0}".format(posDiag))
                print("before negDiag: {0}".format(negDiag))
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                print("after col: {0}".format(col))
                print("after posDiag: {0}".format(posDiag))
                print("after negDiag: {0}".format(negDiag))
                
            print("Board result from backtrack({0}): {1}".format(r, board))

        backtrack(0)
        print("result: {0}".format(res))
        return res

a = Solution()
print(a.solveNQueens(4))