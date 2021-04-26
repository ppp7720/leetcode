moves = "LDRRLRUULR"

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = moves.count('U')-moves.count('D')
        y = moves.count('L')-moves.count('R')
        return True if x == 0 and y == 0 else False