mat = [[1,2],[3,4]]
r = 1
c = 4

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat2 = []
        temp = []
        res = []
        for i in mat:
            for j in i:
                mat2.append(j)
        if len(mat2) == r*c:
            for i in mat2:
                temp.append(i)
                if len(temp) == c:
                    res.append(temp)
                    temp = []
            return res
        else: return mat