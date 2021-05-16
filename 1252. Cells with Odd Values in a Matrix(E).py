from typing import List

m = 28
n = 38
indices = [[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]]

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        RI = dict()
        CI = dict()
        
        for r,c in indices:
            RI[r] = RI.get(r,0) + 1
            CI[c] = CI.get(c,0) + 1

        res = 0
        for r in range(m):
            for c in range(n):
                if (RI.get(r,0) + CI.get(c,0))%2 == 1: res += 1

        return res

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        res = 0
        row = [0]*m
        col = [0]*n
        
        for r,c in indices:
            row[r] += 1
            col[c] += 1

        for i in row:
            for j in col:
                if (i+j)%2 == 1:
                    res += 1
        
        return res