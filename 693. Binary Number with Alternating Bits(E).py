n = 4
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return '0' not in bin(n ^ n>>1)[2:]

    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ n>>1
        return n & n+1 == 0