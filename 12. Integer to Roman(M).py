num = 1994
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
        up1 = {'IIII': 'IV', 'XXXX': 'XL', 'CCCC': 'CD'}
        up2 = {'VIV' : 'IX', 'LXL' : 'XC', 'DCD' : 'CM'}
        r = ''
        for i in roman:
            r += roman[i]*(num//i)
            num = num%i
        for i in up1: r = r.replace(i,up1[i])
        for i in up2: r = r.replace(i,up2[i])
        return r

    def intToRoman2(self, num: int) -> str:
    dic = { 1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90 : 'XC', 50 : 'L',
             40 : 'XL', 10 : 'X', 9  : 'IX', 5  : 'V', 4  : 'IV', 1  : 'I',}
    res = ''
    while(num > 0):
        for key in dic:
            if num >= key:
                res += dic[key]
                num -= key
                break
    return res