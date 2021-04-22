s = "abcd"
t = "abcde"

class Solution:

    def findTheDifference(self, s: str, t: str) -> str:

        s = sorted(list(s))
        t = sorted(list(t))

        for i in range(len(t)-1):
            if s[i] != t[i]: return t[i]
        
        return t[-1]

    def findTheDifference(self, s: str, t: str) -> str:
        
        string = s+t
        
        r = 0
        
        for i in string: r ^= ord(i)

        return chr(r)