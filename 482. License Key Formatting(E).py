s = "5F3Z-2e-9"
k = 4

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        f = (len(s)-1)%k+1
        r = s[:f]
        for i in range(f,len(s),k): r += '-' + s[i:i+k]
        return r.upper()

    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()[::-1]
        return '-'.join([s[i:i+k] for i in range(0,len(s),k)])[::-1]