from typing import List


n = 1

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1,n//2+1):
            res.append(-i)
            res.append(i)
        return res if n%2 == 0 else res + [0]