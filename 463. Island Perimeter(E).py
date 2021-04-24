grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ag = 0
        x = 0
        for i in range(len(grid)):
            ag += sum(grid[i])
            for j in range(1,len(grid[i])): x += grid[i][j-1]&grid[i][j]
            if i > 0 : x += sum([a&b for a,b in zip(grid[i-1],grid[i])])
        return ag*4 - x*2

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    p += 4
                    if i and grid[i-1][j]: p -= 2
                    if j and grid[i][j-1]: p -= 2
        return p