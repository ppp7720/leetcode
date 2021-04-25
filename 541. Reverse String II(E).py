s = "abcd"
k = 2

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl = ''
        for i in range(0,len(s),k*2):
            sl += s[i:i+k][::-1] + s[i+k:i+k*2]
        return sl