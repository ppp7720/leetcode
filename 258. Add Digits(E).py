num = 123456

class Solution:
    def addDigits(self, num: int) -> int:
        r = num
        while r > 9:
            num = r
            r = 0
            while num > 0:
                r += num%10
                num = num // 10
        return r
    
    def addDigits2(self, num: int) -> int:
        return 1+(num-1)%9 if num else 0

print(Solution().addDigits2(num))