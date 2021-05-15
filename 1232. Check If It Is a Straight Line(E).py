from typing import List


coordinates = [[0,0],[0,1],[0,-1]]

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0]:
            a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for (x1,y1),(x2,y2) in zip(coordinates,coordinates[1:]):
                if y2-y1 != a*(x2-x1): return False

        else:
            for (x1,y1),(x2,y2) in zip(coordinates,coordinates[1:]):
                if x2 != x1: return False
        
        return True