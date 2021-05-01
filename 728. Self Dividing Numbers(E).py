left = 1
right = 22

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            n = str(i)
            r = ''
            for j in n:
                if j != '0' and i%int(j) == 0:
                    r += j
            if n == r:
                res.append(i)
        return res

def self_divided(n):
    for i in str(n):
        if i == '0' or n%int(i) > 0:
            return False
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            if self_divided(i): res.append(i)
        return res