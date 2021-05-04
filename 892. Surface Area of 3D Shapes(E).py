grid = [[2,2,2],[2,1,2],[2,2,2]]

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0
        for r in range(R):
            for c in range(C):
                v = grid[r][c]
                if v:
                    res += v*4 + 2
                    if r: res -= min(v, grid[r-1][c]) * 2
                    if c: res -= min(v, grid[r][c-1]) * 2
        return res

    def surfaceArea2(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0
        for r in range(R):
            for c in range(C):
                v = grid[r][c]
                if v: res += 2
                if r != 0: res += max(grid[r-1][c] - v, 0)
                else: res += v
                if r != R-1: res += max(grid[r+1][c] - v, 0)
                else: res += v
                if c != 0: res += max(grid[r][c-1] - v, 0)
                else: res += v
                if c != C-1: res += max(grid[r][c+1] - v, 0)
                else: res += v
        return res