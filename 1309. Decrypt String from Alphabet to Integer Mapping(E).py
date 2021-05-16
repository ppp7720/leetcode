import re


s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"


class Solution:

    def freqAlphabets(self, s: str) -> str:
        res = ''

        s = re.findall('[0-9]{2}#|[0-9]',s)

        for c in s: res += chr(96+int(c.replace('#','')))
        
        return res


    def freqAlphabets(self, s: str) -> str:
        dic = {  '1': 'a',   '2': 'b',   '3': 'c',   '4': 'd',   '5': 'e',   '6': 'f',   '7': 'g',   '8': 'h',   '9': 'i',
               '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r',
               '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}

        s = re.findall('[0-9]{2}#|[0-9]',s)

        res = ''
        for c in s:
            res += dic[c]
        
        return res

    def freqAlphabets(self, s: str) -> str:
        res = ''
        s = s[::-1]
        i = 0
        while i < len(s):
            if s[i] == '#':
                res += chr(96+int(s[i+2]+s[i+1]))
                i += 3
            else:
                res += chr(96+int(s[i]))
                i += 1
        return res[::-1]        