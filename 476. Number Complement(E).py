num = 5

class Solution:
    def findComplement(self, num: int) -> int:
        r = 1
        while num >= r: r <<= 1
        return num^(r-1)

    def findComplement2(self, num: int) -> int:
        n = num
        c = 1
        while n:
            num ^= c
            c <<= 1
            n >>= 1
        return num