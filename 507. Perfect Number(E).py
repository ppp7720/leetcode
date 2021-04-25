num = 496

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 3: return False
        d = []
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                d.append(i)
        
        return sum(d)*d[-1] == num

d = []
for i in range(1,int(num**0.5)+1):
    if num%i == 0:
        d.append(i)

print(d)