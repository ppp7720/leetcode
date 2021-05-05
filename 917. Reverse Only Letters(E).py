S = "a-bC-dEf-ghIj"

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        i = 0
        j = len(S)-1

        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
        return ''.join(s)