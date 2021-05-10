n = 31


class Solution:
    def tribonacci(self, n: int) -> int:
        
        h = {0:0, 1:1, 2:1}
        
        def t(n):
            if n in h:
                return h[n]
            else:
                res = t(n-3) + t(n-2) + t(n-1)
                h[n] = res
            return res
        
x        return t(n)

    def tribonacci(self, n: int) -> int:
        
        if n == 0: return 0
        
        a = 0
        b = 1
        c = 1

        for _ in range(n-2):
            temp = a + b + c
            a = b
            b = c
            c = temp
        
        return c