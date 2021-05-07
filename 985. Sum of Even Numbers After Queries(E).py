A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = sum(i for i in A if i%2 == 0)
        for a,b in queries:
            if A[b]%2 == 0: s -= A[b]
            A[b] += a
            if A[b]%2 == 0: s += A[b]
            res.append(s)
        return res

    def sumEvenAfterQueries2(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = sum(i for i in A if i%2 == 0)
        for a,b in queries:
            new = a+A[b]
            if A[b]%2 == 0:
                if new%2 == 0: s += a
                else: s -= A[b]
            elif new%2 == 0: s += new
            res.append(s)
            A[b] = new
        return res