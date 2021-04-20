n = 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1
    
    def isPowerOfTwo2(self, n: int) -> bool:
        return n != 0 and not n&(n-1)