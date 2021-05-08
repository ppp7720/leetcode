N = 5

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        return N ^ 2**N.bit_length()-1

    def bitwiseComplement(self, N: int) -> int:
        return N ^ 2**(len(bin(N))-2)-1

    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        
        l = N
        p = 0
        
        while l:
            l >>= 1
            p += 1
        
        return N ^ 2**p-1