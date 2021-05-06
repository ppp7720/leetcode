strs = ["cba","daf","ghi"]

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for s in zip(*strs):
            if list(s) != sorted(s):
                res += 1
        return res

    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for c in range(len(strs[0])):
            t = ""
            for r in strs:
                t += r[c]
            res += 1 if list(t) != sorted(t) else 0
        return res