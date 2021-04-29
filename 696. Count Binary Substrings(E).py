s = "00110"

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        g = [1]
        r = 0

        for i in range(1,len(s)):
            if s[i-1] == s[i]: g[-1] += 1
            else: g.append(1)

        for i in range(1,len(g)):
            r += min(g[i],g[i-1])
            
        return r