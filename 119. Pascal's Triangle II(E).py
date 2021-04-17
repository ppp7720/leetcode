rowIndex = 6

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1]]
        for i in range(rowIndex):
            rows.append([a+b for a,b in zip(rows[-1]+[0], [0]+rows[-1])])
        return rows[-1]