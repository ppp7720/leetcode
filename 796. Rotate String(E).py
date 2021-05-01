A = 'abcde'
B = 'cdeab'

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B: return True
        for _ in A:
            A = A[1:]+A[0]
            if A == B: return True
        return False

    def rotateString2(self, A: str, B: str) -> bool:
        return len(A) == len(B) and A in B*2