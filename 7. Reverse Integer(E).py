x = -12314314321423143214321342
class Solution:
    def reverse(self, x: int) -> int:
        s = int(str(abs(x))[::-1])
        if s > 2**31 or s < -2**31:
            return 0
        return s if x >= 0 else s * -1

A = Solution()

print(A.reverse(x))