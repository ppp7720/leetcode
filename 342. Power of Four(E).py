n = 32

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n&n-1 == 0 and bin(n).count('0')%2 == 1 and n > 0

    def isPowerOfFour2(self, n: int) -> bool:
        return bin(n).count('0')%2 == 1 and bin(n).count('1') == 1 and n > 0