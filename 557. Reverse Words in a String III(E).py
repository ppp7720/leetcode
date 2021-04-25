s = "Let's take LeetCode contest"
rs = ""

class Solution:
    def reverseWords(self, s: str) -> str:
        rs = ""
        for i in s.split(): rs += i[::-1]+' '
        return rs.rstrip()

    def reverseWords2(self, s: str) -> str:
        rs = []
        for i in s.split():
            rs.append(i[::-1])
        return ' '.join(rs)