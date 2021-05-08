A = ["bella","label","roller"]

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        S = set(A[0])
        res = ""
        for c in S:
            count = A[0].count(c)
            for i in range(1,len(A)):
                if c in A[i]:
                    count = min(A[i].count(c), count)
                else:
                    count = 0
                    break
            res += c*count
        return list(res)