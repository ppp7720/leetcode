A = [3,-1,0,2]
K = 2

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        
        for i in range(len(A)):
            if K > 0 and A[i] < 0:
                A[i] *= -1
                K -= 1
        
        if 0 in A or K%2 == 0: return sum(A)
       
        else: return sum(A) - min(A)*2