A = "this apple is sweet"
B = "this apple is sour"

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        S = A.split() + B.split()
        h = dict()
        for i in S: h[i] = h.get(i,0) + 1
        return [s for s,c in h.items() if c == 1]
