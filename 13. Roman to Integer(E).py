s = "MCMXCIV"

class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        answer = 0
        c = 0
        for i, a in enumerate(s):
            if r[a] <= c:
                answer += r[a]
            else:
                answer += r[a]
                answer -= c*2
            c = r[a]
        return answer

a = Solution()
print(a.romanToInt(s))