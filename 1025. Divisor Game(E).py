n = 5

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2 == 0


def game(n,w):
    if n == 1: return w
    else:
        if w == 'A': w = 'B'
        else: w = 'A'
        res = [1]
        for i in range(2,int(n**0.5)+1):
            if not n%i:
                res.append(n//i)
                if n//i != i: res.append(i)
        for i in res:
            game(n-i,w)
