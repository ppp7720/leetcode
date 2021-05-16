from typing import List

points = [[3,2],[-2,2]]

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for a, b in zip(points,points[1:]):
            res += max(abs(b[0] - a[0]),abs(b[1] - a[1]))
        return res