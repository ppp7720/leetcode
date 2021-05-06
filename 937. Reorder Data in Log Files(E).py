# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# print(["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])

# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
# print(["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])


logs = ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(["let3 art zero","let1 art zero can","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for i in logs:
            if i.split()[1][0].isdigit(): digits.append(i)
            else: letters.append(i)

        letters.sort(key=lambda x: [x.split()[1:],x.split()[0]])
        
        return letters + digits

    def reorderLogFiles2(self, logs: List[str]) -> List[str]:
        def st(log):
            ID, Log = log.split(' ', maxsplit=1)
            return [1] if Log[0].isdigit() else [0,Log,ID]

        return sorted(logs, key=st)