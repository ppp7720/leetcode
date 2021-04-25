n = 5
class Solution:
    def fib(self, n: int) -> int:
        if n > 1: return self.fib(n-1) + self.fib(n-2)
        else: return n

    def fib2(self, n: int) -> int:
        if n > 1:
            n1 = 0
            n2 = 1
            for i in range(n-1):
                n = n2 + n1
                n1 = n2
                n2 = n
        return n