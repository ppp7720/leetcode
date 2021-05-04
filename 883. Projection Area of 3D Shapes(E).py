grid = [[1,2],[3,4]]

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        for Y in grid:
            temp = 0
            for X in Y:
                if X > 0: res += 1
                temp = max(temp, X)
            res += temp


        for X in range(len(grid[0])):
            temp = 0
            for Y in range(len(grid)):
                temp = max(temp, grid[Y][X])
            res += temp
        
        return res

class Solution:
    def projectionArea2(self, grid: List[List[int]]) -> int:
        XY = 0
        ZY = []
        ZX = []
        for Y in grid:
            temp = 0
            for X in Y:
                if X > 0: XY += 1
                temp = max(temp, X)
            ZY.append(temp)


        for X in range(len(grid[0])):
            temp = 0
            for Y in range(len(grid)):
                temp = max(temp, grid[Y][X])
            ZX.append(temp)
        
        return XY + sum(ZY) +sum(ZX)