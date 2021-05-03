s = "abcdddeeeeaabbbcd"

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                if i - start > 1: res.append([start,i])
                start = i + 1
        return res