num = 16**2

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == 1 or int(num**0.5)*int(num**0.5) == num