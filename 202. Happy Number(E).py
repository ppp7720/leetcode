n = 123321

class Solution:
    def isHappy(self, n: int) -> bool:
        r = 0
        while n > 9 :
            r = 0
            for i in str(n): r += int(i)**2
            n = r
        return True if n == 1 or n == 7 else False
    
    def isHappy2(self, n: int) -> bool:
        nums = []
        while 1:
            r = 0
            for i in str(n): r += int(i)**2
            if r == 1: return 1
            elif r in nums: return 0
            else:
                nums.append(r)
                n = r

print(Solution().isHappy(n))