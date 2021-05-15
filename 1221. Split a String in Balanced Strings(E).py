s = "RLRRRLLRLL"

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        C,R = 0,0

        for c in s:
            if c == 'L': C += 1
            else: C -= 1

            if C == 0: R += 1

        return R