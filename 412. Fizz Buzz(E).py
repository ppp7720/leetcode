n = 15

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1,n+1):
            if i%15 == 0: r.append("FizzBuzz")
            elif i%5 == 0: r.append("Buzz")
            elif i%3 == 0: r.append("Fizz")
            else: r.append(str(i))
        return r

    def fizzBuzz2(self, n: int) -> List[str]:
        r = []
        for i in range(1,n+1):
            t = ""
            if i%3 == 0: t += "Fizz"
            if i%5 == 0: t += "Buzz"
            r.append(t or str(i))
        return r