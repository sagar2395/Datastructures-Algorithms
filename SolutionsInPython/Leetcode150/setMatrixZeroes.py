class Solution(object):
    def setZeroes(self, matrix):
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
                        
                        
                        
                     
                