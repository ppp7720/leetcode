m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = [m]
        y = [n]
        for i in ops:
            x.append(i[0])
            y.append(i[1])
        return min(x)*min(y)

