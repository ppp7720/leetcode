a = "aa"
b = "aa"

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if a == b:
            for i in set(a):
                if a.count(i) > 1: return True
            return False
        if len(a) == len(b):
            j = []
            for i, c in enumerate(a):        
                if c != b[i]: j.append([c,b[i]])
            if len(j) == 2 and j[0] == j[1][::-1]: return True
        return False