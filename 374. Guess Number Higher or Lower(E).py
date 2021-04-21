n = 100
p = 21

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1

        r = n

        while l <= r:

            m = (r+l)//2

            if guess(m) == 0: return m

            elif guess(m) == 1: l = m+1

            else: r = m-1

    def guessNumber2(self, n: int) -> int:
        
        l = 1
        r = n
        
        while l <= r:
            
            m1 = l+(r-l)//3
            
            m2 = r-(r-l)//3
            
            if guess(m1) == 0: return m1
            
            elif guess(m2) == 0: return m2
            
            elif guess(m2) == 1: l = m2 - 1
            
            elif guess(m1) == -1: r = m1 + 1
            
            else:
                l = m1 + 1
                r = m2 - 1