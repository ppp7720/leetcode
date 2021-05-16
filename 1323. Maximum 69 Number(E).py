num = 9996


class Solution:
    def maximum69Number (self, num: int) -> int:
        for i, n in enumerate(str(num)):
            if n == '6':
                return num + 10**(len(str(num))-i-1)*3
        else: return num

    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))