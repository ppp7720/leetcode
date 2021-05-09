a = 2
b = 4
c = 1

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        
        return [0 if c - a == 2
                else 1 if c - b < 3 or b - a < 3
                else 2,
                c - a - 2]

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        line = sorted([a,b,c])
        
        MAX = line[2] - line[0] - 2
        
        if line[2] - line[0] == 2: MIN = 0
        elif line[2] - line[1] < 3 or line[1]-line[0] < 3: MIN = 1
        else: MIN = 2
        
        return [MIN,MAX]