g = [1,2,3]
s = [1,2]

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r = 0
        for i in s[::-1]:
            while g:
                c = g.pop()
                if c <= i:
                    r += 1
                    break
        return r