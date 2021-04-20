s = "anagram"
t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for i in s:
            if i in h1: h1[i] += 1
            else: h1[i] = 1
        for i in t:
            if i in h2: h2[i] += 1
            else: h2[i] = 1
        return h1 == h2

print(Solution().isAnagram2(s,t))