L, R = 6, 10

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        p = {2,3,5,7,11,13,17,19}
        return sum(bin(i).count('1') in p for i in range(L,R+1))