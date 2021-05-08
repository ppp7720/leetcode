arr = [3,3,6,5,-2,2,5,1,-9,4]

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        if sum(arr)%3: return False

        p = sum(arr)//3
        s = 0
        c = 0

        for i in arr:
            s += i
            if s == p:
                c += 1
                s = 0
            if c == 3:
                return True
        
        return False