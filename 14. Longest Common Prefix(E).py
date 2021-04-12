strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort(key=len)
        if strs == []:
            return ""
        for j in range(len(strs[0]),0,-1):
            pre = strs[0][:j]
            r = []
            for i in strs:
                if i[:j] == pre:
                    r.append(i[:j])
            if len(r) == len(strs):
                return pre
        return ""

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        out = ""
        if len(strs) == 0:
            return ""
        pref = strs[0]
        n = len(strs)
        for i in range(1,n):
            while strs[i].find(pref) != 0:
                pref = pref[:len(pref)-1]
        return pref        

