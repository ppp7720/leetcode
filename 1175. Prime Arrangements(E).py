n = 100

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [0,0]+[1]*(n-1)
        for i in range(2,int(n**0.5)+1):
            if primes[i] == 1:
                for j in range(i*i,n+1,i):
                    primes[j] = 0
        p = sum(primes)

        res = 1

        for i in range(2,p+1): res *= i
        for i in range(2,n-p+1): res *= i

        return res%1000000007
        
    def numPrimeArrangements(self, n: int) -> int:
        p = 0
        for i in range(2,n+1):
            for j in range(2,int(i**0.5)+1):
                if i%j == 0: break
            else: p += 1

        res = 1
        for i in range(2,p+1): res *= i
        for i in range(2,n-p+1): res *= i

        return res%1000000007

    def numPrimeArrangements(self, n: int) -> int:
        res = []

        primes = [0,0]+[1]*(n-1)
        for i in range(5+1):
            if primes[i] == 1:
                for j in range(i*i,n+1,i):
                    primes[j] = 0

        def per(l,r):
            if r:
                for i in range(len(r)):
                    per(l+[r[i]], r[:i]+r[i+1:])
            else:
                for n in l:
                    if primes[n] == 1 and primes[l.index(n)+1] == 0:
                        return
                else: res.append(1)

        per([],list(range(1,n+1)))
        
        return sum(res)