flowerbed = [1,0,0,0,1,0,0]
n = 2

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0]+flowerbed+[0]
        i = 1
        while i < len(f)-1 and n > 0:
            if f[i] == 0 and f[i-1] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
            i += 1
        return True if n == 0 else False