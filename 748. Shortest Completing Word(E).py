licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = []
        for i in words:
            temp = re.findall('[a-zA-Z]',licensePlate.lower())
            for j in i:
                if j in temp:
                    temp.remove(j)
            if not temp: res.append(i)
        res.sort(key=len)
        return res[0]