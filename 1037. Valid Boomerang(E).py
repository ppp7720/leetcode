points = [[1,1],[2,3],[3,5]]

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        y1 = points[1][1]-points[0][1]
        x1 = points[1][0]-points[0][0]
        y2 = points[2][1]-points[0][1]
        x2 = points[2][0]-points[0][0]

        if x1 and x2: return y1/x1 != y2/x2
        elif x1 == 0 and x2 == 0: return False
        elif x1 == 0 and y1 == 0: return False
        elif x2 == 0 and y2 == 0: return False
        else: return True