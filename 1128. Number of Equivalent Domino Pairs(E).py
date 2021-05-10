dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        h = dict()
        for a,b in dominoes:
            p = (max(a,b),min(a,b))
            h[p] = h.get(p,0) + 1

        res = 0
        for i in h.values():
            res += i*(i-1)/2
        return int(res)