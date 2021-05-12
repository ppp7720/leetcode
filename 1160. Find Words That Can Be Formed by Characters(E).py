words = ["hello","world","leetcode"]
chars = "welldonehoneyr"


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:

        def count(word):
            for c in word:
                if word.count(c) > chars.count(c): return 0
            return len(word)

        return sum(count(i) for i in words)

    def countCharacters2(self, words: List[str], chars: str) -> int:

        res = 0

        for w in words:
            
            for c in w:
                if chars.count(c) < w.count(c):
                    break
            else:
                res += len(w)

        return res