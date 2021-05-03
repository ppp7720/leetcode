matrix = [[1,2,3],[4,5,6]]

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newmat = []
        for c in range(len(matrix[0])):
            newmat.append([])
            for r in range(len(matrix)):
                newmat[c].append(matrix[r][c])
        return newmat

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
