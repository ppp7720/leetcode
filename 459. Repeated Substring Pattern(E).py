s = "abcabcabcabc"


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if len(s)%(i+1) == 0 and s == s[:i+1]*(len(s)//(i+1)): return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s+s)[1:-1]


'''
If there is such pattern, the original string could be represented as following:
    origin_str = pattern + pattern + ... + pattern =  m * pattern; 

With doubling:
    origin_str + origin_str = 2 * m * pattern;

After removing head and rear:
    new_str = pattern_wo_head + (2m-2) * pattern + pattern_wo_rear 
'''