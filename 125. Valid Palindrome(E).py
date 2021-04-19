s = "A man, a plan, a canal: Panama"

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+','',s).lower()
        return s == s[::-1]

print(Solution().isPalindrome(s))