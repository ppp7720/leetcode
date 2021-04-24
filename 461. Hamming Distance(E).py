x = 1
y = 4


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        a = 0
        b = x^y
        while b:
            a += b & 1
            b >>= 1
        return a