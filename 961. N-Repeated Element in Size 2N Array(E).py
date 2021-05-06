A = [5,1,5,2,5,3,5,4]


from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        r = []
        for i in A:
            if i in r: return i
            else: r.append(i)


    def repeatedNTimes(self, A: List[int]) -> int:
        for n, i in Counter(A).items():
            if i == len(A)//2: return n