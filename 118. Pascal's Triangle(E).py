numRows = 5

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(numRows-1):
            rows.append([a+b for a,b in zip(rows[-1]+[0], [0]+rows[-1])])
        return rows