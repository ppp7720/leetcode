A = [2]
B = [1,3]

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        s = (sum(A) - sum(B))//2
        A = set(A)
        B = set(B)
        for i in B:
            if i + s in A:
                return [i+s,i]