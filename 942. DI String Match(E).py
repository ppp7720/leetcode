s = "III"

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        q = list(range(len(s)+1))
        res = []

        for i in s:
            if i == 'I': res.append(q.pop(0))
            else: res.append(q.pop())
        return res+q

    def diStringMatch(self, s: str) -> List[int]:
        D = 0
        U = len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(D)
                D += 1
            else:
                res.append(U)
                U -= 1

        return res+[D]