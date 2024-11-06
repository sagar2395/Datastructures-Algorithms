# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            
            ret += (matrix.pop(0))
            
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
                    
            if matrix:
                ret +=(matrix.pop()[::-1])
                
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
                    
        return ret 