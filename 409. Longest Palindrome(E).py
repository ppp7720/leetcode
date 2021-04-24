import collections
s = "abcabcc"

class Solution:
    def longestPalindrome(self, s: str) -> int:
        r = 0
        t = 0
        for i in range(65,123):
            m = s.count(chr(i))
            r += m // 2 * 2
        return r

# print(Solution().longestPalindrome(s))

r = 0
for i in collections.Counter(s).values():
    r += i // 2 * 2
    if r % 2 == 0 and i % 2 == 1: r += 1

print(r)