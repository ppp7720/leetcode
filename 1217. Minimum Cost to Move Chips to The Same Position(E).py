from typing import List

position = [1,1000000000]

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = 0
        b = 0

        for n in position:
            if n%2 == 0: b += 1
            else: a += 1

        return min(a,b)