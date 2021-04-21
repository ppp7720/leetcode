from math import log10

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467%n == 0

    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and log10(n)/log10(3)%1 == 0