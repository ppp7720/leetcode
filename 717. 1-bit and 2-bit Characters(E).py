bits = [1,1,1,0]


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while len(bits) > 1:
            if bits[0:2] == [1,0] or bits[0:2] == [1,1]: bits = bits[2:]
            else: bits = bits[1:]
        return bits

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits)-1:
            i += bits[i] + 1
        return bits[i:]