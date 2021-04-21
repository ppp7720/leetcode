s = "leetcode"

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        v = ['a','e','i','o','u','A','E','I','O','U']
        while i < j:
            if s[i] in v and s[j] in v:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in v: i += 1
            elif s[j] not in v: j -= 1
            
        return ''.join(s)