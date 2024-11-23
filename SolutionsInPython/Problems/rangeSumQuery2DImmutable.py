# Solution incomplete . Not passing all test cases. Prefix Sum method should be used.

from typing import List 

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                sum += self.matrix[row][col]

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)