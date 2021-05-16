from typing import List
import itertools

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = ((m*n)+k)%(m*n)
        res = []

        grid = list(itertools.chain(*grid))

        grid = grid[-k:]+grid[:-k]

        for i in range(0,m*n,n):
            res.append(grid[i:i+n])

        return res
    
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = ((m*n)+k)%(m*n)

        grid2 = []
        for r in grid:
            grid2 += r

        grid2 = grid2[-k:]+grid2[:-k]

        res = []
        for i in range(0,m*n,n):
            res.append(grid2[i:i+n])
        
        return res