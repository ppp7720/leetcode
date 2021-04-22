s = "abc"
t = "ahbgd"

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0: return True
        for j in t:
            if j == s[i]: i += 1
            if i == len(s): return True
        return False


    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            
            c = t.find(i)
            
            if c >= 0: t = t[c+1:]
 
            else: return False

        return True