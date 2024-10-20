def spiral_matrix(matrix):
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
                       
    
    
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(arr))