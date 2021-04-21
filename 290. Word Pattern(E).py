pattern = "aba"
s = "dog cat cat"

class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(' ')
        h = dict()
        
        if len(pattern) != len(s): return False
        
        for i in range(len(pattern)):
        
            if pattern[i] not in h and s[i] not in h.values(): h[pattern[i]] = s[i]

            elif pattern[i] in h and s[i] in h.values() and h[pattern[i]] == s[i]: continue

            else: return False
        
        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        
        p = pattern
        s = s.split(' ')
        h = dict()

        if len(p) != len(s): return False

        for i in range(len(p)):
            pk = 'p_{}'.format(p[i])
            sk = 's_{}'.format(s[i])
            if pk not in h: h[pk] = i
            if sk not in h: h[sk] = i
            if h[pk] != h[sk]: return False
        
        return True

    def wordPattern3(self, pattern: str, s: str) -> bool:
        
        p = pattern
        s = s.split(' ')
                
        return list(map(p.index,p)) == list(map(s.index,s))
