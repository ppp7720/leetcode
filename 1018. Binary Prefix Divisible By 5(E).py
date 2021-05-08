A = [1,1,1,0,1]

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = [True]*len(A)
        s = 0
        for i, n in enumerate(A):
            s <<= 1
            s += n
            s %= 5
            if s: res[i] = False
        return res

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        s = 0
        for n in A:
            s <<= 1
            s += n
            s %= 5
            if s: res.append(False)
            else: res.append(True)
        return res