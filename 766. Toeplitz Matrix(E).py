matrix = [[1,2],[2,2]]

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R, C = len(matrix), len(matrix[0])
        i = 0
        while i < R-1:
            if matrix[i][:C-1] != matrix[i+1][1:]: return False
            i += 1
        return True