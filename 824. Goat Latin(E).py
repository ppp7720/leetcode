S = "The quick brown fox jumped over the lazy dog"

class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join([w + 'ma' + 'a' * (i + 1) if w[0] in "aeiouAEIOU" else w[1:] + w[0] + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split())])
