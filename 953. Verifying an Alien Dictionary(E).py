words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = dict()
        for i,c in enumerate(order): h[c] = i
        def keys(s): return [h[i] for i in s]
        return words == sorted(words, key=keys)