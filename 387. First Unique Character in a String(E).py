s = "loveleetcode"


class Solution:

    def firstUniqChar(self, s: str) -> int:
        
        h = dict()

        for i in s:
            h[i] = h.get(i,0) + 1


        for i in h:
            if h[i] == 1: return s.index(i)
        
        return -1

    def firstUniqChar2(self, s: str) -> int:
        
        h = dict()

        for i in s:
            h[i] = h.get(i,0) + 1


        for i, a in enumerate(s):
            if h[a] == 1: return i
        
        return -1

    def firstUniqChar_(self, s: str) -> int:

        a = "abcdefghijklmnopqrstuvwxyz"
        
        r = [s.index(i) for i in a if s.count(i) == 1]
        
        return min(r) if r else -1