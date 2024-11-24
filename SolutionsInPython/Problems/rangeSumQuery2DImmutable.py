# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

# Example 1:
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                top = self.prefixSum[row - 1][col] if row > 0 else 0
                left = self.prefixSum[row][col - 1] if col > 0 else 0
                topLeft = self.prefixSum[row - 1][col - 1] if row > 0 and col > 0 else 0
                self.prefixSum[row][col] = matrix[row][col] + top + left - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefixSum[row2][col1 - 1] if col1 > 0 else 0
        top = self.prefixSum[row1 - 1][col2] if row1 > 0 else 0
        topLeft = self.prefixSum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return self.prefixSum[row2][col2] - left - top + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)