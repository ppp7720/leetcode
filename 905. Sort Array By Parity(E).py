A = [3,1,2,4]

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in A:
            if i%2 == 0: even.append(i)
            else: odd.append(i)
        return even+odd

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        return sorted(A, key = lambda x: x % 2)