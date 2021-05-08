S = "(()())(())"


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        t = 0
        res = ""
        
        for c in S:
            if c == ")": t -= 1
            if t > 0: res += c
            if c == "(": t += 1

        return res

    def removeOuterParentheses(self, S: str) -> str:
        p = 0
        t = 0
        res = ""
        for i, c in enumerate(S):
            if c == "(":
                t += 1
            else:
                t -= 1
            if t == 0:
                res += S[p+1:i]
                p = i+1

        return res