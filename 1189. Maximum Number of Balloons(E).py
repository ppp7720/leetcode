text = "leetcode"

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = {'b' : 1, 'a' : 1, 'l' : 2, 'o' : 2, 'n' : 1}
        res = float('inf')
        for c in s:
            res = min(res,text.count(c)//s[c])
        return res