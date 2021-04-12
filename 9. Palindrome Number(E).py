x = 121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

A = Solution()
print(A.isPalindrome(x))
        