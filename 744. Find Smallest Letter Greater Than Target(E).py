letters = ["e","e","e","e","e","e","n","n","n","n"]
target = "e"

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        l = l[l.index(target)+1:]
        for i in l:
            if i in letters: return i

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in letters:
            if i > target:
                return i
        return letters[0]
