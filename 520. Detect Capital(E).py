word = "Fla"

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.lower(), word.capitalize())

    def detectCapitalUse2(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)