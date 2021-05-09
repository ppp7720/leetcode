R = 3
C = 3
r0 = 0
c0 = 2

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        def distance(cell):
            return abs(r0-cell[0]) + abs(c0-cell[1])
        
        return sorted([[r,c] for r in range(R) for c in range(C)], key=distance)


    def allCellsDistOrder2(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        M = [[r,c] for r in range(R) for c in range(C)]

        M.sort(key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))

        return M

    def allCellsDistOrder3(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        M = []
        
        for r in range(R):
            for c in range(C):
                M.append([abs(r0-r)+abs(c0-c),[r,c]])
        
        M.sort()
        
        return [i[1] for i in M]