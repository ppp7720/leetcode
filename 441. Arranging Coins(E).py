n = 6

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n:
            if n > i:
                i += 1
                n -= i
            else: break
        return i

a = (-1 + (1+8*n)**0.5) // 2
print(a)