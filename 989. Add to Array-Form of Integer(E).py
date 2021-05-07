num = [1,2,3,4]
k = 233

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1,-1,-1):
            if k: k, num[i] = divmod(num[i]+k,10)
            else: break
        while k:
            k, a = divmod(k,10)
            num = [a] + num
        return num

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        Sn = 0
        for i, n in enumerate(num[::-1]): Sn += n * 10**i
        Sn += k
        return [int(n) for n in str(Sn)]