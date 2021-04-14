haystack = "hello"
needle = "ll"


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i <= len(haystack):
            if haystack[i:i+len(needle)] == needle: return i
            else: i += 1
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)