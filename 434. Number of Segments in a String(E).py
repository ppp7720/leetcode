import re

s = "love live! mu'sic forever"

class Solution:
    def countSegments(self, s: str) -> int:
        c = 0
        r = 0
        for i in s:
            if i != ' ' and c == 0:
                r += 1
                c += 1
            if i == ' ':
                c = 0
        return r

    def countSegments2(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ' :
                r += 1
        return r

    def countSegments3(self, s: str) -> int:
        return len(re.findall("\S+", s))