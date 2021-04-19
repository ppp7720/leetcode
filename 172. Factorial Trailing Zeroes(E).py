n = 625


class Solution:

    def trailingZeroes(self, n: int) -> int:
        i = 1
        r = 0
        while 5**i <= n:
            r += n//(5**i)
            i += 1
        return r

    def trailingZeroes2(self, n: int) -> int:
        r = 0
        while n > 0:
            n = n//5
            r += n
        return r

print(Solution().trailingZeroes2(n))