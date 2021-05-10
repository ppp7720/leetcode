text = "we will we will rock you"
first = "we"
second = "will"

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        res = []
        for i in range(len(text)-2):
            if text[i] + ' ' + text[i+1] == first + ' ' + second:
                res.append(text[i+2])
        return res