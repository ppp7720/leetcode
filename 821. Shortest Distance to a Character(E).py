s = "loveleetcode"
c = "e"

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []

        d = float('inf')
        for i in s:
            if i == c: d = 0
            else: d += 1
            res.append(d)

        d = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i] == c: d = 0
            else: d += 1
            res[i] = min(res[i],d)

        return res

    def shortestToChar2(self, s: str, c: str) -> List[int]:
        res = []

        d = float('-inf')
        for i in range(len(s)):
            if s[i] == c: d = i
            res.append(i-d)

        d = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i] == c: d = i
            res[i] = min(res[i],d-i)

        return res