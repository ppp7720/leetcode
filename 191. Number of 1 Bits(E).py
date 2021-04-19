n = 0b00000001000000000000000010000000

class Solution:
    
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            r += n & 1
            n >>= 1
        return r

    def hammingWeight2(self, n: int) -> int:
        r = 0
        while n:
            n &= n - 1
            r += 1
        return r

print(Solution().hammingWeight2(n))