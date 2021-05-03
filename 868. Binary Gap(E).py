n = 5

class Solution:
    def binaryGap(self, n: int) -> int:
        c = 0
        mc = 0
        while n:
            if c and n & 1 == 0:
                c += 1
            elif n & 1 == 1:
                mc = max(c,mc)
                c = 1
            n >>= 1
        return mc