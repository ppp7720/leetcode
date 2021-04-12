s = "))"


class Solution:
    def isValid(self, s: str) -> bool:
        o = {'(':')','[':']','{':'}'}
        t = []
        s = list(s)

        while s:
            
            f = s.pop(0)
            
            if f in o:
                t.append(f)
                
            elif t == [] or o[t[-1]] != f:
                return False

            else:
                t.pop()

        return True if t == [] else False

print(Solution(s))