# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

from typing import List

class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        indexArray = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indexArray.append([i,j])
                    
        
        for index in indexArray:
            for k in range(len(matrix)):
                matrix[k][index[1]] = 0
                    
            for k in range(len(matrix[0])):
                matrix[index[0]][k] = 0
                        
                        
                        
                     
                