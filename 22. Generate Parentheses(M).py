n = 3

from itertools import combinations

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        r = list(combinations(range((n-1)*2),n-1))
        a = []

        for j in r:
            t, r = 1, 0
            q = '('
            for i in range((n-1)*2):
                if i in j:
                    t += -1
                    q += ')'
                else:
                    t += 1
                    q += '('
                if t < 0:
                    r = 1
                    break
            if r == 0: a.append(q+')')
        
        return a

    def generateParenthesis2(self, n: int) -> List[str]:
        res = []
            
        def btParenth(prefix, l, r):
            #print('lcount = ' , lCount, 'rcount = ' , rCount)
            if len(prefix) == n*2-1:
                prefix = prefix + ')'
                res.append(prefix)
                return
            else:
                if l < n:
                    btParenth(prefix+'(', l+1, r)
                if l > r:
                    btParenth(prefix+')', l, r+1)
                    
        
        btParenth('', 0, 0)
        return set(res)