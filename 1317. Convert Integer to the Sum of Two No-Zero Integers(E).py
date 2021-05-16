from typing import List


n = 1010

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while a < n:
            if '0' not in str(n-a) and '0' not in str(a): return [n-a, a]
            a += 1
