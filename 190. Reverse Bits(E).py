n = 0b1011111111

class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        p = 31

        while n:
            r += (n & 1) << p
            n = n >> 1
            p -= 1

        return r